"""
Extrai dados tabulares do Painel de Indicadores MOOC Ifes no Power BI publico.

Saidas:
- stages/02-catalogo/output/powerbi-mooc-ifes/*.csv
- stages/02-catalogo/output/powerbi-mooc-ifes/painel-indicadores-mooc-ifes.xlsx
- stages/02-catalogo/output/powerbi-mooc-ifes/manifest.json
- JSONs tecnicos do Power BI para auditoria/reprocessamento.

Uso:
    python stages\\02-catalogo\\scripts\\extrair_powerbi_mooc.py

Notas:
- O script usa somente biblioteca padrao do Python.
- Algumas visualizacoes do Power BI publico podem nao retornar `DS`; nesses casos,
  o erro e registrado no manifesto e a extracao segue com as demais abas.
"""

import copy
import csv
import gzip
import html
import json
import re
import sys
import urllib.error
import urllib.request
import uuid
import zipfile
from datetime import datetime, timezone
from pathlib import Path
from xml.sax.saxutils import escape


ROOT = Path(__file__).resolve().parents[3]
OUT_DIR = ROOT / "stages" / "02-catalogo" / "output" / "powerbi-mooc-ifes"
RESOURCE_KEY = "1c27e1e9-cab2-4d25-a957-8fbf5397a252"
BASE_API = f"https://wabi-brazil-south-api.analysis.windows.net/public/reports/{RESOURCE_KEY}"
QUERY_URL = "https://wabi-brazil-south-api.analysis.windows.net/public/reports/querydata?synchronous=true"
REPORT_URL = (
    "https://app.powerbi.com/view?"
    "r=eyJrIjoiMWMyN2UxZTktY2FiMi00ZDI1LWE5NTctOGZiZjUzOTdhMjUyIiwidCI6IjQ0ZTllMTcyLWZmYTUtNDNmMy1iMjJjLTM3MWNmY2QyNzJlZCJ9"
    "&pageName=ReportSection"
)


SHEETS = [
    ("Indicadores por curso", "Indicadores por curso", "tableEx", None),
    ("Dados por UF", "Tabelas Localidade", "tableEx", "Dados por UF"),
    ("Dados por pais", "Tabelas Localidade", "tableEx", "Dados por país"),
    ("Matriculas por ano", "Matrículas", "stackedAreaChart", "Matrículas por ano"),
    ("Top cursos matriculas", "Matrículas", "donutChart", "Top 5 - Cursos com mais matrículas"),
    ("Certificados por ano", "Certificados", "stackedAreaChart", "Certificados por ano"),
    ("Top cursos certificados", "Certificados", "donutChart", "Top 5 - Cursos com mais certificados"),
    ("Cursos por unidade", "Cursos", "columnChart", "Quantidade de Cursos"),
    ("Crescimento matriculas", "Indicadores de Escala e Crescimento", "lineClusteredColumnComboChart", "Crescimento Anual de Matrículas"),
    ("Crescimento certificados", "Indicadores de Escala e Crescimento", "lineClusteredColumnComboChart", "Crescimento Anual de Certificados"),
    ("Top cursos populares", "Indicadores de Escala e Crescimento", "donutChart", "Top 5 - Cursos mais populares"),
]


def fetch_json(url):
    headers = {
        "Accept": "application/json",
        "ActivityId": str(uuid.uuid4()),
        "RequestId": str(uuid.uuid4()),
        "X-PowerBI-ResourceKey": RESOURCE_KEY,
    }
    req = urllib.request.Request(url, headers=headers, method="GET")
    with urllib.request.urlopen(req, timeout=60) as resp:
        body = resp.read()
        if body[:2] == b"\x1f\x8b":
            body = gzip.decompress(body)
        return json.loads(body.decode("utf-8"))


def post_query(command, model_id):
    payload = {
        "version": "1.0.0",
        "SemanticQueryDataShapeCommands": [command],
        "modelId": model_id,
    }
    data = json.dumps(payload, ensure_ascii=False).encode("utf-8")
    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json",
        "ActivityId": str(uuid.uuid4()),
        "RequestId": str(uuid.uuid4()),
        "X-PowerBI-ResourceKey": RESOURCE_KEY,
    }
    req = urllib.request.Request(QUERY_URL, data=data, headers=headers, method="POST")
    try:
        with urllib.request.urlopen(req, timeout=90) as resp:
            return json.loads(resp.read().decode("utf-8"))
    except urllib.error.HTTPError as exc:
        body = exc.read().decode("utf-8", "replace")
        raise RuntimeError(f"Power BI query failed: HTTP {exc.code}: {body[:800]}") from exc


def visual_title(single_visual):
    for source in ("vcObjects", "objects"):
        title = single_visual.get(source, {}).get("title")
        if not title:
            continue
        props = title[0].get("properties", {}) if isinstance(title, list) else {}
        text = props.get("text", {}).get("expr", {}).get("Literal", {}).get("Value")
        if text:
            return text.strip("'")
    return ""


def iter_visuals(models):
    for section in models["exploration"]["sections"]:
        page = section.get("displayName") or section.get("name")
        for visual in section.get("visualContainers", []):
            config = json.loads(visual.get("config", "{}")) if isinstance(visual.get("config"), str) else {}
            single = config.get("singleVisual", {})
            yield page, visual, single, visual_title(single)


def find_visual(models, page_name, visual_type, title):
    candidates = []
    for page, visual, single, found_title in iter_visuals(models):
        if page != page_name or single.get("visualType") != visual_type:
            continue
        if title is None or found_title == title:
            candidates.append((visual, single, found_title))
    if not candidates:
        raise LookupError(f"Visual not found: {page_name} / {visual_type} / {title}")
    return candidates[0]


def remap_sources(obj, alias_map):
    if isinstance(obj, dict):
        source_ref = obj.get("SourceRef")
        if isinstance(source_ref, dict) and "Source" in source_ref:
            source_ref["Source"] = alias_map.get(source_ref["Source"], source_ref["Source"])
        for value in obj.values():
            remap_sources(value, alias_map)
    elif isinstance(obj, list):
        for value in obj:
            remap_sources(value, alias_map)


def query_from_visual(visual, single):
    if visual.get("query"):
        command = json.loads(visual["query"])["Commands"][0]["SemanticQueryDataShapeCommand"]
        return copy.deepcopy(command)

    query = copy.deepcopy(single.get("prototypeQuery"))
    if not query:
        raise LookupError("Visual has no query or prototypeQuery")

    main_alias_by_entity = {
        item.get("Entity"): item.get("Name")
        for item in query.get("From", [])
        if item.get("Entity") and item.get("Name")
    }

    for item in json.loads(visual.get("filters") or "[]"):
        filter_query = item.get("filter")
        if not filter_query or not filter_query.get("Where"):
            continue
        alias_map = {
            source.get("Name"): main_alias_by_entity.get(source.get("Entity"), source.get("Name"))
            for source in filter_query.get("From", [])
            if source.get("Name")
        }
        where = copy.deepcopy(filter_query["Where"])
        remap_sources(where, alias_map)
        query.setdefault("Where", []).extend(where)

    select_names = [item["Name"] for item in query.get("Select", [])]
    projections = []
    for role_items in single.get("projections", {}).values():
        for item in role_items:
            ref = item.get("queryRef")
            if ref in select_names:
                index = select_names.index(ref)
                if index not in projections:
                    projections.append(index)
    if not projections:
        projections = list(range(len(select_names)))

    return {
        "Query": query,
        "Binding": {
            "Primary": {"Groupings": [{"Projections": projections}]},
            "DataReduction": {"DataVolume": 4, "Primary": {"Window": {"Count": 5000}}},
            "Version": 1,
        },
        "ExecutionMetricsKind": 1,
    }


def decode_cell(value, descriptor):
    dict_name = descriptor.get("DN")
    if dict_name:
        if value is None:
            return None
        if not isinstance(value, int) and not (isinstance(value, str) and re.fullmatch(r"\d+", value)):
            return value
        return ("DICT", dict_name, value)
    if isinstance(value, str):
        try:
            if re.fullmatch(r"-?\d+(\.\d+)?([eE]-?\d+)?", value):
                return float(value)
        except ValueError:
            return value
    return value


def decode_dsr(data):
    result_data = data["results"][0]["result"]["data"]
    ds = result_data["dsr"]["DS"][0]
    value_dicts = ds.get("ValueDicts", {})
    row_nodes = ds["PH"][0][next(iter(ds["PH"][0].keys()))]
    descriptors = row_nodes[0].get("S", [])
    select_by_value = {
        item.get("Value"): item.get("Name")
        for item in result_data["descriptor"].get("Select", [])
        if item.get("Value") and item.get("Name")
    }
    headers = [select_by_value.get(item.get("N"), item.get("N", "")) for item in descriptors]

    rows = []
    previous = [None] * len(descriptors)
    for node in row_nodes:
        if "S" in node:
            descriptors = node["S"]
            previous = [None] * len(descriptors)
        repeated = int(node.get("R", 0))
        raw_values = list(node.get("C", []))
        values = []
        cursor = 0
        for index, descriptor in enumerate(descriptors):
            if repeated & (1 << index):
                value = previous[index]
            else:
                value = raw_values[cursor] if cursor < len(raw_values) else None
                cursor += 1
                decoded = decode_cell(value, descriptor)
                if isinstance(decoded, tuple) and decoded[0] == "DICT":
                    _, dict_name, dict_index = decoded
                    dictionary = value_dicts.get(dict_name, [])
                    dict_index = int(dict_index)
                    value = dictionary[dict_index] if 0 <= dict_index < len(dictionary) else dict_index
                else:
                    value = decoded
            values.append(value)
        previous = values
        rows.append(values)
    return headers, rows


def friendly_headers(headers):
    replacements = {
        "campus.nome": "Unidade",
        "curso.nome": "Curso",
        "Sum(curso.carga_horaria)": "Carga horaria",
        "tipo_curso.descricao": "Tipo de curso",
        "Sum(mdl_role_assignments.id)": "Matriculas",
        "mdl_role_assignments.userid": "Matriculas",
        "mdl_simplecertificate_issues.% Certificados": "% certificados",
        "Sum(mdl_simplecertificate_issues.id)": "Certificados",
        "CountNonNull(mdl_simplecertificate_issues.certificateid)": "Certificados",
        "mdl_simplecertificate_issues.Tempo Médio de Conclusão (dias)": "Tempo medio conclusao dias",
        "mdl_simplecertificate_issues.Horas Formacao": "Horas formacao",
        "parametros_ciclos_sistec.Classificação Popularidade": "Classificacao popularidade",
        "mdl_user_info_data.data": "UF",
        "mdl_user.country": "Pais",
        "mdl_role_assignments.Ano": "Ano",
        "mdl_role_assignments.Matrículas Válidas": "Matriculas validas",
        "mdl_role_assignments.Crescimento Matrículas YoY %": "Crescimento matriculas YoY",
        "mdl_simplecertificate_issues.Ano": "Ano",
        "mdl_simplecertificate_issues.Certificados Válidos": "Certificados validos",
        "mdl_simplecertificate_issues.Crescimento Certificados YoY %": "Crescimento certificados YoY",
        "parametros_ciclos_sistec.Popularidade do Curso (Medida)": "Popularidade",
        "CountNonNull(parametros_ciclos_sistec.id_curso)": "Cursos",
    }
    return [replacements.get(header, header) for header in headers]


def write_csv(path, headers, rows):
    with path.open("w", encoding="utf-8-sig", newline="") as handle:
        writer = csv.writer(handle)
        writer.writerow(headers)
        writer.writerows(rows)


def col_name(index):
    name = ""
    index += 1
    while index:
        index, rem = divmod(index - 1, 26)
        name = chr(65 + rem) + name
    return name


def sheet_xml(headers, rows):
    out = ['<?xml version="1.0" encoding="UTF-8" standalone="yes"?>']
    out.append('<worksheet xmlns="http://schemas.openxmlformats.org/spreadsheetml/2006/main">')
    widths = []
    sample_rows = [headers] + rows[:200]
    for col in range(len(headers)):
        max_len = max((len(str(row[col])) if col < len(row) and row[col] is not None else 0) for row in sample_rows)
        widths.append(min(max(max_len + 2, 10), 45))
    out.append("<cols>")
    for i, width in enumerate(widths, 1):
        out.append(f'<col min="{i}" max="{i}" width="{width}" customWidth="1"/>')
    out.append("</cols>")
    out.append("<sheetData>")
    all_rows = [headers] + rows
    for r_idx, row in enumerate(all_rows, 1):
        out.append(f'<row r="{r_idx}">')
        for c_idx, value in enumerate(row, 1):
            ref = f"{col_name(c_idx - 1)}{r_idx}"
            style = ' s="1"' if r_idx == 1 else ""
            if value is None:
                out.append(f'<c r="{ref}"{style}/>')
            elif isinstance(value, (int, float)) and not isinstance(value, bool):
                out.append(f'<c r="{ref}"{style}><v>{value}</v></c>')
            else:
                text = escape(str(value))
                out.append(f'<c r="{ref}" t="inlineStr"{style}><is><t>{text}</t></is></c>')
        out.append("</row>")
    out.append("</sheetData>")
    if rows:
        last_ref = f"{col_name(len(headers) - 1)}{len(rows) + 1}"
        out.append(f'<autoFilter ref="A1:{last_ref}"/>')
    out.append("</worksheet>")
    return "".join(out)


def write_xlsx(path, sheets):
    safe_names = []
    used = set()
    for name, _, _ in sheets:
        clean = re.sub(r"[\[\]\:\*\?\/\\]", " ", name)[:31].strip() or "Sheet"
        base = clean
        counter = 2
        while clean.lower() in used:
            suffix = f" {counter}"
            clean = (base[: 31 - len(suffix)] + suffix).strip()
            counter += 1
        used.add(clean.lower())
        safe_names.append(clean)

    with zipfile.ZipFile(path, "w", zipfile.ZIP_DEFLATED) as zf:
        zf.writestr("[Content_Types].xml", """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Types xmlns="http://schemas.openxmlformats.org/package/2006/content-types">
<Default Extension="rels" ContentType="application/vnd.openxmlformats-package.relationships+xml"/>
<Default Extension="xml" ContentType="application/xml"/>
<Override PartName="/xl/workbook.xml" ContentType="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet.main+xml"/>
<Override PartName="/xl/styles.xml" ContentType="application/vnd.openxmlformats-officedocument.spreadsheetml.styles+xml"/>
""" + "".join(
            f'<Override PartName="/xl/worksheets/sheet{i}.xml" ContentType="application/vnd.openxmlformats-officedocument.spreadsheetml.worksheet+xml"/>'
            for i in range(1, len(sheets) + 1)
        ) + "</Types>")
        zf.writestr("_rels/.rels", """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">
<Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/officeDocument" Target="xl/workbook.xml"/>
</Relationships>""")
        zf.writestr("xl/_rels/workbook.xml.rels", """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">
""" + "".join(
            f'<Relationship Id="rId{i}" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/worksheet" Target="worksheets/sheet{i}.xml"/>'
            for i in range(1, len(sheets) + 1)
        ) + f'<Relationship Id="rId{len(sheets) + 1}" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/styles" Target="styles.xml"/>'
        + "</Relationships>")
        zf.writestr("xl/styles.xml", """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<styleSheet xmlns="http://schemas.openxmlformats.org/spreadsheetml/2006/main">
<fonts count="2"><font><sz val="11"/><name val="Calibri"/></font><font><b/><sz val="11"/><color rgb="FFFFFFFF"/><name val="Calibri"/></font></fonts>
<fills count="3"><fill><patternFill patternType="none"/></fill><fill><patternFill patternType="gray125"/></fill><fill><patternFill patternType="solid"><fgColor rgb="FF14532D"/><bgColor indexed="64"/></patternFill></fill></fills>
<borders count="1"><border><left/><right/><top/><bottom/><diagonal/></border></borders>
<cellStyleXfs count="1"><xf numFmtId="0" fontId="0" fillId="0" borderId="0"/></cellStyleXfs>
<cellXfs count="2"><xf numFmtId="0" fontId="0" fillId="0" borderId="0" xfId="0"/><xf numFmtId="0" fontId="1" fillId="2" borderId="0" xfId="0" applyFont="1" applyFill="1"/></cellXfs>
</styleSheet>""")
        workbook_sheets = []
        for i, name in enumerate(safe_names, 1):
            workbook_sheets.append(f'<sheet name="{escape(name)}" sheetId="{i}" r:id="rId{i}"/>')
        zf.writestr("xl/workbook.xml", """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<workbook xmlns="http://schemas.openxmlformats.org/spreadsheetml/2006/main" xmlns:r="http://schemas.openxmlformats.org/officeDocument/2006/relationships">
<sheets>""" + "".join(workbook_sheets) + "</sheets></workbook>")
        for i, (_, headers, rows) in enumerate(sheets, 1):
            zf.writestr(f"xl/worksheets/sheet{i}.xml", sheet_xml(headers, rows))


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    models = fetch_json(f"{BASE_API}/modelsAndExploration?preferReadOnlySession=true")
    schema = fetch_json(f"{BASE_API}/conceptualschema")
    model_id = models["models"][0]["id"]

    (OUT_DIR / "powerbi-modelsAndExploration.json").write_text(json.dumps(models, ensure_ascii=False, indent=2), encoding="utf-8")
    (OUT_DIR / "powerbi-conceptualschema.json").write_text(json.dumps(schema, ensure_ascii=False, indent=2), encoding="utf-8")

    extracted = []
    manifest = {
        "source_url": REPORT_URL,
        "resource_key": RESOURCE_KEY,
        "dataset_last_refresh": models["models"][0].get("LastRefreshTime"),
        "extracted_at_utc": datetime.now(timezone.utc).isoformat(),
        "sheets": [],
    }

    for sheet_name, page, visual_type, title in SHEETS:
        try:
            visual, single, found_title = find_visual(models, page, visual_type, title)
            command = query_from_visual(visual, single)
            data = post_query(command, model_id)
            headers, rows = decode_dsr(data)
            headers = friendly_headers(headers)
            if not rows:
                continue
            extracted.append((sheet_name, headers, rows))
            csv_name = re.sub(r"[^A-Za-z0-9_-]+", "-", sheet_name.lower()).strip("-") + ".csv"
            write_csv(OUT_DIR / csv_name, headers, rows)
            manifest["sheets"].append({
                "sheet": sheet_name,
                "page": page,
                "visual_type": visual_type,
                "title": found_title,
                "rows": len(rows),
                "columns": len(headers),
                "csv": csv_name,
            })
            print(f"ok {sheet_name}: {len(rows)} rows")
        except Exception as exc:
            manifest["sheets"].append({
                "sheet": sheet_name,
                "page": page,
                "visual_type": visual_type,
                "title": title,
                "error": str(exc),
            })
            print(f"skip {sheet_name}: {exc}")

    source_rows = [
        ["Campo", "Valor"],
        ["URL do painel", REPORT_URL],
        ["Resource key", RESOURCE_KEY],
        ["Dataset LastRefreshTime", models["models"][0].get("LastRefreshTime")],
        ["Extraído em UTC", manifest["extracted_at_utc"]],
    ]
    extracted.append(("Fonte", source_rows[0], source_rows[1:]))

    xlsx_path = OUT_DIR / "painel-indicadores-mooc-ifes.xlsx"
    write_xlsx(xlsx_path, extracted)
    (OUT_DIR / "manifest.json").write_text(json.dumps(manifest, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"xlsx {xlsx_path}")


if __name__ == "__main__":
    main()
