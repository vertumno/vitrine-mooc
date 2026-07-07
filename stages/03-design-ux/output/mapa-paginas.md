# Mapa de Páginas — Vitrine MOOC Ifes

> **Estágio:** 03 — Design/UX · **Versão:** 1.2 · **Data:** 07/07/2026
> **Base:** `stages/02-catalogo/output/arquitetura-informacao.md` v4.1 (navegação/URLs) ·
> `design-system/design-system-oficial.md` (tokens, componentes e regras — canônico).
> **Protótipos oficiais:** `stages/03-design-ux/output/prototipo-cursos-abertos/` (Home + Catálogo).
> Protótipos anteriores arquivados em `_arquivo/` (ver README de lá).
> **Nome público da plataforma: "Cursos Abertos do Ifes"** — "Vitrine" é só codinome interno.

Cada página lista: **propósito**, **seções** (ordem de leitura), **dados exibidos** (com a fonte),
e **indexável?** (SEO). Metadados do curso seguem o **Art. 14 da Resolução CS 72/2020** e o
`catalogo-cursos-completo.csv`.

---

## Inventário de páginas

| # | Página | URL | Indexável | Protótipo oficial (`prototipo-cursos-abertos/`) |
|---|--------|-----|:---------:|---------------------|
| 1 | Home | `/` | ✅ | `index.html` |
| 2 | Catálogo / Busca | `/cursos/` | ✅ | `cursos.html` |
| 3 | Página do curso | `/cursos/{slug}/` | ✅ | — (arquivado: `_arquivo/prototipo-vitrine-mooc/curso-como-criar-mooc.html`) |
| 4 | Área (categoria) | `/areas/{slug}/` | ✅ | — (arquivado: `_arquivo/prototipo-vitrine-mooc/area-educacao.html`) |
| 5 | Série | `/series/{slug}/` | ✅ | — |
| 6 | Projeto parceiro | `/v/{slug}/` (Rio Doce, UnAC) | ✅ | — |
| 7 | Licença Capacitação + Planejador | `/qualificacao/` | ✅ | — (arquivado: `_arquivo/prototipo-vitrine-mooc/qualificacao.html`) |
| 8 | Certificação | `/certificacao/` | ✅ | — |
| 9 | Sobre | `/sobre/` | ✅ | — (arquivado: `_arquivo/prototipo-vitrine-mooc/sobre.html`) |
| 10 | Perguntas frequentes | `/faq/` | ✅ | — (arquivado: `_arquivo/prototipo-vitrine-mooc/perguntas-frequentes.html`) |

Combinações de faceta (`/cursos/?categoria=…&carga=…&publico=…`) = **não indexáveis** (`noindex`/canonical).

> **Removido (v1.2):** as páginas `/publicos/{slug}/` ("Para quem") foram eliminadas como páginas dedicadas. A navegação por público funciona apenas como **atalhos na Home** que apontam para o catálogo pré-filtrado (`/cursos/?publico=professores`). Justificativa: 107/165 cursos declaram 2+ públicos — páginas por audiência geram repetição e auto-exclusão falsa (ver `decisao-taxonomia-cenarios.md` §2b).

---

## 1. Home — `/`

**Propósito:** apresentar a Vitrine, orientar a descoberta e expor a demanda real. Público leigo, nacional, de descoberta.

**Seções (ordem):**
1. **Hero** — título/proposta de valor ("Cursos gratuitos e abertos do Ifes, com certificado"), busca proeminente, CTA.
2. **Atalhos "Para quem"** — 3–4 cards de público (professores/educadores · comunidade/começar do zero · trabalho e carreira · servidores/setor público). *Atalhos na Home que linkam para `/cursos/?publico=…` (catálogo pré-filtrado). Sem página própria.*
3. **Em destaque** — curadoria manual (CEFOR).
4. **Mais cursados** — ordenado por matrículas (Power BI). Expõe demanda: Inglês, Moodle p/ Educadores, Canva, Google Drive.
5. **Recentes** — últimos publicados (absorve levas trimestrais automaticamente).
6. **Navegar por área** — grade das 15 Categorias com contagem.
7. **Projetos parceiros** — Rio Doce Escolar, UnAC (hubs).
8. **Licença Capacitação** — chamada para servidores + Planejador.
9. **Faixa institucional / rodapé.**

**Dados exibidos:** cards de curso (§dados abaixo) · nomes+contagem de categorias · nº de matrículas (Power BI, "Mais cursados").

---

## 2. Catálogo / Busca — `/cursos/`

**Propósito:** encontrar cursos por busca + facetas combináveis. Estrutura de referência: página de catálogo da DeepLearning.AI (destaques em carrossel no topo + grade com filtros laterais).

**Seções:**
1. **Cursos em destaque** — carrossel com card grande (imagem + título + descrição + chips + carga/nível + CTAs "Saber mais"/"Começar agora"), curadoria CEFOR, indicadores de navegação (dots).
2. Facetas em **sidebar** com checkboxes e contagem por faceta (desktop; bottom-sheet mobile): Categoria (15) · Para quem · Carga horária (≤10/10–20/20–40/40–60h) · Nível · Acessibilidade (Libras/AD) · Idioma. Busca (título + tags, tolerante a acento) no topo da sidebar + "Limpar filtros".
3. **"Mostrando N cursos"** + título "Todos os cursos" + Ordenação: Relevância · Mais cursados · Recentes · A–Z.
4. Grade de cards com CTA por card (paginação/scroll com fallback rastreável).
5. Estado vazio (microcopy + sugestões).

**Dados:** cards de curso; contagem por faceta; total de resultados.

---

## 3. Página do curso — `/cursos/{slug}/`

**Propósito:** apresentar o curso e levar à matrícula no Moodle. **1 URL canônica por curso.**

**Seções:**
1. **Hero:** título, categoria(s), selos (Libras/AD/Idioma), carga horária, nível, botão primário "Acessar no Moodle".
2. **Sobre o curso:** descrição, objetivos de aprendizagem.
3. **Conteúdo programático** · **Metodologia** · **Processo de avaliação** · **Certificação** (≥60%).
4. **Ficha (sidebar):** carga horária · nível · idioma · provedor/projeto · certificação · elegível p/ Licença Capacitação.
5. **Cursos relacionados** (mesma categoria/série).

**Dados exibidos (fonte `catalogo-cursos-completo.csv` + Art. 14):**

| Campo | Fonte | Obrigatório |
|-------|-------|:---:|
| título, descrição, conteúdos, metodologia, avaliação | CSV / WP | ✅ |
| categorias[] (15) | taxonomia v4.1 | ✅ |
| carga_horaria | CSV (`carga_horaria`) | ✅ |
| idioma, nível | CSV / Art. 14 | ✅ |
| público-alvo | CSV | ✅ |
| professores/instrutores | CSV | ➖ |
| selos: libras, audiodescrição | CSV/metadado | ➖ |
| link_curso (Moodle) | CSV | ✅ |
| imagem/thumb | CSV | ✅ |
| série / projeto | editorial | ➖ |
| badge "Novo" (< 3 meses) | derivado da data | ➖ |
| Área CNPq, Eixo Tecnológico | metadado oficial (registro) | ✅ (não navegação) |

---

## 4. Área (categoria) — `/areas/{slug}/`

**Propósito:** página editorial indexável por tema (SEO — 65% das matrículas vêm de fora do ES).

**Seções:** título + texto introdutório da área · grade de cursos da categoria · facetas locais (carga/idioma/acessibilidade) · áreas relacionadas.

**Dados:** cards da categoria; contagem; texto editorial por área. **Slug:** uma das 15 categorias (`ambiente-e-saude`, `educacao`, `tecnologias-e-informatica`, …).

---

---

> **Nota (v1.2):** a página dedicada "Para quem (público)" (`/publicos/{slug}/`) foi **removida**. A autoidentificação por público agora funciona exclusivamente como **atalhos na Home** (seção 1, item 2) que direcionam para o catálogo pré-filtrado (`/cursos/?publico=professores`). O filtro "Para quem" continua disponível como **faceta** na sidebar do catálogo (página 2).

## 5. Série — `/series/{slug}/`

**Propósito:** contar a história de uma coleção de marca/produção.

**Séries:** Atendente e Vendedor (3, com níveis) · Educador Maker (4) · Lovelace (6) · Embrace (3) · Lesson Study (PT/EN = mesmo curso, dois selos de idioma).

**Seções:** identidade da série · sequência sugerida de cursos · grade.

---

## 6. Projeto parceiro — `/v/{slug}/`

**Propósito:** hub de projeto com identidade institucional.

**Projetos:** **Rio Doce Escolar** (`/v/riodoce/`, 31 cursos) · **UnAC** (`/v/unac/`, 33 cursos — Universidade Aberta Capixaba, parceria Ifes/CEFOR × Governo do ES; ver `projetos-especiais.md`).

**Seções:** descrição oficial do projeto/parceria · logo · grade de cursos associados.

---

## 7. Licença Capacitação + Planejador — `/qualificacao/`

**Propósito:** serviço para servidores públicos (não é filtro de conteúdo).

**Seções:** o que é a Licença · quem tem direito · legislação · **Planejador** (monta combinação de cursos somando `carga_horaria` até a meta de horas) · CTA.

**Dados:** `carga_horaria` (já populada) por curso; meta de horas informada pelo usuário.

---

## 8. Certificação — `/certificacao/`

**Propósito:** explicar como funciona o certificado (aproveitamento ≥60%, autoinstrucional, sem tutoria). Página indexável (busca "curso gratuito com certificado").

---

## 9. Sobre — `/sobre/`

**Propósito:** o que é a Vitrine MOOC, o CEFOR/Ifes, o objetivo (Resolução CS 72/2020 — democratização/inclusão), como participar.

---

## 10. Perguntas frequentes — `/faq/`

**Propósito:** dúvidas comuns (como me inscrevo, certificado, gratuidade, pré-requisitos, Libras). Formato acordeão. Schema `FAQPage` para AEO.

---

## Dados do card de curso (referência única)

Usado em toda grade (home, catálogo, área, público, série, projeto):

`imagem` · `selos[]` (Libras/AD/Idioma) · `badge_novo?` · `categorias[]` (chips) · `titulo` ·
`carga_horaria` · `serie/projeto?` · `link → /cursos/{slug}/`.

Fonte: `stages/02-catalogo/output/catalogo-cursos-completo.csv`.

---

## Rastreabilidade

- **Cobertura:** as 10 páginas cobrem toda a navegação da arquitetura v4.2 (Categorias, Séries, Projetos, Licença, Certificação, Sobre, FAQ). "Para quem" funciona como atalho na Home + faceta no catálogo (sem página própria).
- **Protótipos oficiais:** Home e Catálogo prontos em `prototipo-cursos-abertos/` (design system oficial). As demais páginas serão recriadas lá gradualmente; as versões antigas estão em `_arquivo/prototipo-vitrine-mooc/` apenas como consulta.
- **Escopo:** 165 cursos publicados (os 65 "em produção" ficam fora — ver `arquitetura-informacao.md` v4.2).
