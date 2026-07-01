#!/usr/bin/env python3
"""Extrai fichas publicas dos cursos MOOC do Ifes.

Fonte de entrada: output/catalogo-cursos.csv.
Saidas:
- output/catalogo-cursos-completo.json
- output/catalogo-cursos-completo.csv
- output/catalogo-cursos-completo.md
"""

from __future__ import annotations

import csv
import json
import re
import time
from http.cookiejar import CookieJar
from datetime import datetime
from html import escape
from html.parser import HTMLParser
from pathlib import Path
from typing import Iterable
from urllib.parse import parse_qs, urlencode, urljoin, urlparse
from urllib.request import HTTPCookieProcessor, Request, build_opener, urlopen


ROOT = Path(__file__).resolve().parents[3]
INPUT_CSV = ROOT / "stages" / "02-catalogo" / "output" / "catalogo-cursos.csv"
OUTPUT_DIR = ROOT / "stages" / "02-catalogo" / "output"
BASE = "https://mooc.cefor.ifes.edu.br/moodle/"
USER_AGENT = "Mozilla/5.0 (compatible; vitrine-mooc-catalogo/1.0)"
OPENER = build_opener(HTTPCookieProcessor(CookieJar()))
GUEST_SESSION_READY = False

FIELD_LABELS = {
    "nome_curso": "Nome do curso",
    "descricao_curso": "Descrição do curso",
    "carga_horaria": "Carga horária",
    "idioma": "Idioma",
    "nivel_dificuldade": "Nível de dificuldade",
    "professores_instrutores": "Professores/Instrutores",
    "publico_alvo": "Público-alvo",
    "requisitos_tecnicos": "Requisitos técnicos",
    "pre_requisitos": "Pré-requisitos para o curso",
    "conteudos": "Conteúdos",
    "metodologia": "Metodologia",
    "processo_avaliacao": "Processo de Avaliação",
}

FIELD_ALIASES = {
    "nome_curso": ["Nome do curso"],
    "descricao_curso": ["Descrição do curso", "Descrição"],
    "carga_horaria": ["Carga horária", "Carga Horária"],
    "idioma": ["Idioma"],
    "nivel_dificuldade": ["Nível de dificuldade", "Dificuldade"],
    "professores_instrutores": [
        "Professores/Instrutores",
        "Professores",
        "Professor",
        "Professor(a)",
        "Professoras",
        "Professora",
        "Instrutores",
        "Instrutor",
        "Docentes",
        "Docente",
    ],
    "publico_alvo": ["Público-alvo", "Público alvo"],
    "requisitos_tecnicos": ["Requisitos técnicos", "Requisitos técnico", "Requisitos"],
    "pre_requisitos": ["Pré-requisitos para o curso", "Pré-requisitos", "Pré-requisito"],
    "conteudos": ["Conteúdos", "Conteúdo"],
    "metodologia": ["Metodologia"],
    "processo_avaliacao": ["Processo de Avaliação", "Processo de avaliação", "Avaliação"],
}

LABEL_TO_KEY = {
    label.lower(): key
    for key, labels in FIELD_ALIASES.items()
    for label in labels
}
ALL_LABELS = sorted({label for labels in FIELD_ALIASES.values() for label in labels}, key=len, reverse=True)
LABEL_PATTERN = re.compile(
    r"(" + "|".join(re.escape(label) for label in ALL_LABELS) + r")\s*:",
    flags=re.IGNORECASE,
)


def normalize_space(value: str) -> str:
    value = value.replace("\xa0", " ")
    value = re.sub(r"[ \t\r\f\v]+", " ", value)
    value = re.sub(r"\n{3,}", "\n\n", value)
    return value.strip()


def slugify(value: str) -> str:
    table = str.maketrans(
        "áàâãäéèêëíìîïóòôõöúùûüçñÁÀÂÃÄÉÈÊËÍÌÎÏÓÒÔÕÖÚÙÛÜÇÑ",
        "aaaaaeeeeiiiiooooouuuucnAAAAAEEEEIIIIOOOOOUUUUCN",
    )
    value = value.translate(table).lower()
    value = re.sub(r"[^a-z0-9]+", "-", value)
    return value.strip("-")


def fetch(url: str, retries: int = 3) -> str:
    last_error: Exception | None = None
    for attempt in range(1, retries + 1):
        try:
            req = Request(url, headers={"User-Agent": USER_AGENT})
            with OPENER.open(req, timeout=30) as response:
                content_type = response.headers.get_content_charset() or "utf-8"
                return response.read().decode(content_type, "replace")
        except Exception as exc:  # pragma: no cover - diagnostic path
            last_error = exc
            time.sleep(attempt)
    raise RuntimeError(f"Falha ao baixar {url}: {last_error}")


def ensure_guest_session() -> None:
    global GUEST_SESSION_READY
    if GUEST_SESSION_READY:
        return
    login_url = urljoin(BASE, "login/index.php")
    html = fetch(login_url)
    token_match = re.search(r'name="logintoken"\s+value="([^"]+)"', html)
    if not token_match:
        raise RuntimeError("Token de login visitante nao encontrado")
    data = urlencode(
        {
            "logintoken": token_match.group(1),
            "username": "guest",
            "password": "guest",
        }
    ).encode("utf-8")
    req = Request(
        login_url,
        data=data,
        headers={
            "User-Agent": USER_AGENT,
            "Content-Type": "application/x-www-form-urlencoded",
        },
        method="POST",
    )
    with OPENER.open(req, timeout=30) as response:
        response.read()
    GUEST_SESSION_READY = True


class TextParser(HTMLParser):
    def __init__(self, capture_role_main: bool = True) -> None:
        super().__init__(convert_charrefs=True)
        self.capture_role_main = capture_role_main
        self.in_main = False
        self.depth = 0
        self.skip = 0
        self.parts: list[str] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        attrs_dict = {k: v for k, v in attrs}
        if tag in {"script", "style"}:
            self.skip += 1
        if self.capture_role_main and not self.in_main and attrs_dict.get("role") == "main":
            self.in_main = True
            self.depth = 1
            return
        if self.in_main:
            self.depth += 1
            if tag == "a":
                href = attrs_dict.get("href")
                if href:
                    self.parts.append(f"[[HREF:{href}]]")
            if tag in {"p", "div", "li", "br", "h1", "h2", "h3", "h4", "tr"}:
                self.parts.append("\n")

    def handle_endtag(self, tag: str) -> None:
        if self.skip and tag in {"script", "style"}:
            self.skip -= 1
            return
        if self.in_main:
            if tag == "a":
                self.parts.append("[[/HREF]]")
            if tag in {"p", "div", "li", "h1", "h2", "h3", "h4", "tr"}:
                self.parts.append("\n")
            self.depth -= 1
            if self.depth <= 0:
                self.in_main = False

    def handle_data(self, data: str) -> None:
        if self.in_main and not self.skip:
            text = " ".join(data.split())
            if text:
                self.parts.append(text)

    def text(self) -> str:
        raw = "".join(self.parts)
        raw = re.sub(r"\[\[HREF:([^\]]+)\]\]([^\[]+)\[\[/HREF\]\]", r"[\2](\1)", raw)
        raw = re.sub(r"\[\[/?HREF[^\]]*\]\]", "", raw)
        lines = [normalize_space(line) for line in raw.splitlines()]
        return "\n".join(line for line in lines if line)


def extract_main_text(html: str) -> str:
    parser = TextParser()
    parser.feed(html)
    text = parser.text()
    stop_markers = [
        "\nCriar Conta\n",
        "\nTurmas anteriores\n",
        "\nAcessibilidade\n",
        "\nVocê ainda não se identificou",
    ]
    for marker in stop_markers:
        index = text.find(marker)
        if index != -1:
            text = text[:index]
    return normalize_space(text)


def markdown_to_plain(value: str) -> str:
    value = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", value)
    value = re.sub(r" ?● ?", "\n- ", value)
    return normalize_space(value)


def split_fields(text: str) -> dict[str, str]:
    matches = list(LABEL_PATTERN.finditer(text))
    fields: dict[str, str] = {}
    if not matches:
        return fields
    for i, match in enumerate(matches):
        label = match.group(1)
        start = match.end()
        end = matches[i + 1].start() if i + 1 < len(matches) else len(text)
        key = LABEL_TO_KEY[label.lower()]
        fields[key] = normalize_space(text[start:end])
    return fields


def parse_course_id_from_url(url: str) -> str | None:
    query = parse_qs(urlparse(url).query)
    course_id = query.get("id", [None])[0]
    return course_id


def parse_course_id_from_html(html: str) -> str | None:
    patterns = [
        r'"courseId"\s*:\s*(\d+)',
        r"\bcourse-(\d+)\b",
        r"contextInstanceId\"?\s*:\s*(\d+)",
    ]
    for pattern in patterns:
        match = re.search(pattern, html)
        if match:
            return match.group(1)
    return None


def resolve_course_id(link: str) -> tuple[str | None, str | None]:
    course_id = parse_course_id_from_url(link)
    if course_id:
        return course_id, None
    ensure_guest_session()
    html = fetch(link)
    return parse_course_id_from_html(html), None


def read_catalog() -> list[dict[str, str]]:
    with INPUT_CSV.open("r", encoding="utf-8-sig", newline="") as handle:
        return list(csv.DictReader(handle))


def build_info_url(course_id: str) -> str:
    return urljoin(BASE, "course/info.php?" + urlencode({"id": course_id}))


def enrich(row: dict[str, str]) -> dict[str, object]:
    link = row["link_curso"]
    result: dict[str, object] = {
        "n": int(row["n"]),
        "titulo_catalogo": row["titulo"],
        "slug": slugify(row["titulo"]),
        "categorias_slugs": [item for item in row["categorias_slugs"].split(";") if item],
        "categorias_nomes": [item for item in row["categorias_nomes"].split(";") if item],
        "libras": row["libras"].lower() == "sim",
        "link_curso": link,
        "link_thumb": row["link_thumb"],
        "tags": [item for item in row["tags"].split(";") if item],
        "status": "publicado",
        "fonte": {},
        "campos": {},
        "erro_extracao": "",
    }
    try:
        course_id, _ = resolve_course_id(link)
        if not course_id:
            raise RuntimeError("ID do curso nao encontrado")
        info_url = build_info_url(course_id)
        html = fetch(info_url)
        main_text = extract_main_text(html)
        fields = split_fields(main_text)
        if not fields.get("nome_curso"):
            first_line = next((line.strip() for line in main_text.splitlines() if line.strip()), "")
            if first_line:
                fields["nome_curso"] = markdown_to_plain(first_line)
        result["id_moodle"] = int(course_id)
        result["link_info"] = info_url
        result["fonte"] = {
            "url": info_url,
            "capturado_em": datetime.now().isoformat(timespec="seconds"),
            "metodo": "course/info.php publico",
        }
        result["campos"] = fields
        result["texto_extraido"] = main_text
    except Exception as exc:
        result["erro_extracao"] = str(exc)
    return result


def rows_for_csv(courses: Iterable[dict[str, object]]) -> list[dict[str, object]]:
    rows: list[dict[str, object]] = []
    for course in courses:
        fields = course.get("campos") or {}
        assert isinstance(fields, dict)
        row: dict[str, object] = {
            "n": course["n"],
            "id_moodle": course.get("id_moodle", ""),
            "titulo_catalogo": course["titulo_catalogo"],
            "nome_curso": fields.get("nome_curso", ""),
            "carga_horaria": fields.get("carga_horaria", ""),
            "idioma": fields.get("idioma", ""),
            "nivel_dificuldade": fields.get("nivel_dificuldade", ""),
            "professores_instrutores": fields.get("professores_instrutores", ""),
            "publico_alvo": markdown_to_plain(str(fields.get("publico_alvo", ""))),
            "requisitos_tecnicos": markdown_to_plain(str(fields.get("requisitos_tecnicos", ""))),
            "pre_requisitos": markdown_to_plain(str(fields.get("pre_requisitos", ""))),
            "descricao_curso": markdown_to_plain(str(fields.get("descricao_curso", ""))),
            "conteudos": markdown_to_plain(str(fields.get("conteudos", ""))),
            "metodologia": markdown_to_plain(str(fields.get("metodologia", ""))),
            "processo_avaliacao": markdown_to_plain(str(fields.get("processo_avaliacao", ""))),
            "categorias_nomes": ";".join(course["categorias_nomes"]),  # type: ignore[arg-type]
            "tags": ";".join(course["tags"]),  # type: ignore[arg-type]
            "libras": "sim" if course["libras"] else "nao",
            "link_curso": course["link_curso"],
            "link_info": course.get("link_info", ""),
            "link_thumb": course["link_thumb"],
            "erro_extracao": course.get("erro_extracao", ""),
        }
        rows.append(row)
    return rows


def write_json(courses: list[dict[str, object]]) -> None:
    payload = {
        "gerado_em": datetime.now().isoformat(timespec="seconds"),
        "fonte_catalogo": str(INPUT_CSV.relative_to(ROOT)).replace("\\", "/"),
        "total": len(courses),
        "total_com_erro": sum(1 for course in courses if course.get("erro_extracao")),
        "campos_extraidos": FIELD_LABELS,
        "cursos": courses,
    }
    path = OUTPUT_DIR / "catalogo-cursos-completo.json"
    path.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")


def write_csv(courses: list[dict[str, object]]) -> None:
    rows = rows_for_csv(courses)
    path = OUTPUT_DIR / "catalogo-cursos-completo.csv"
    with path.open("w", encoding="utf-8-sig", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)


def write_markdown(courses: list[dict[str, object]]) -> None:
    lines = [
        "# Catálogo Completo de Cursos MOOC Ifes",
        "",
        f"> Gerado em {datetime.now().isoformat(timespec='seconds')}.",
        f"> Total de cursos: {len(courses)}. Erros de extração: {sum(1 for c in courses if c.get('erro_extracao'))}.",
        "",
        "Fonte pública principal: páginas `course/info.php?id=...` do Moodle.",
        "",
    ]
    for course in courses:
        fields = course.get("campos") or {}
        assert isinstance(fields, dict)
        title = fields.get("nome_curso") or course["titulo_catalogo"]
        lines.extend(
            [
                f"## {course['n']}. {title}",
                "",
                f"- ID Moodle: `{course.get('id_moodle', '')}`",
                f"- Status: {course['status']}",
                f"- Categorias: {', '.join(course['categorias_nomes'])}",  # type: ignore[arg-type]
                f"- Libras: {'sim' if course['libras'] else 'nao'}",
                f"- Link do curso: {course['link_curso']}",
                f"- Link da ficha pública: {course.get('link_info', '')}",
                f"- Thumbnail: {course['link_thumb']}",
                "",
            ]
        )
        if course.get("erro_extracao"):
            lines.extend([f"**Erro de extração:** {escape(str(course['erro_extracao']))}", ""])
            continue
        for key, label in FIELD_LABELS.items():
            value = fields.get(key)
            if value:
                lines.extend([f"**{label}:**", "", str(value), ""])
    path = OUTPUT_DIR / "catalogo-cursos-completo.md"
    path.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")


def main() -> None:
    rows = read_catalog()
    courses: list[dict[str, object]] = []
    for index, row in enumerate(rows, start=1):
        course = enrich(row)
        courses.append(course)
        title = course.get("titulo_catalogo", "")
        status = "erro" if course.get("erro_extracao") else "ok"
        print(f"[{index:03d}/{len(rows):03d}] {status} - {title}", flush=True)
        time.sleep(0.15)
    write_json(courses)
    write_csv(courses)
    write_markdown(courses)
    errors = [course for course in courses if course.get("erro_extracao")]
    print(f"Concluido: {len(courses)} cursos; {len(errors)} erros.")
    if errors:
        for course in errors[:20]:
            print(f"- {course['n']} {course['titulo_catalogo']}: {course['erro_extracao']}")


if __name__ == "__main__":
    main()
