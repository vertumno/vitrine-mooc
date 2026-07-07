# Mapa de Páginas — Vitrine MOOC Ifes

> **Estágio:** 03 — Design/UX · **Versão:** 1.0 · **Data:** 06/07/2026
> **Base:** `stages/02-catalogo/output/arquitetura-informacao.md` v4.1 (navegação/URLs) ·
> `design-spec.md` (componentes) · `design-system/` (tokens).
> **Protótipos:** `stages/03-design-ux/output/prototipo-vitrine-mooc/` (HTML navegável).

Cada página lista: **propósito**, **seções** (ordem de leitura), **dados exibidos** (com a fonte),
e **indexável?** (SEO). Metadados do curso seguem o **Art. 14 da Resolução CS 72/2020** e o
`catalogo-cursos-completo.csv`.

---

## Inventário de páginas

| # | Página | URL | Indexável | Protótipo existente |
|---|--------|-----|:---------:|---------------------|
| 1 | Home | `/` | ✅ | `proposta-home-vitrine.html` |
| 2 | Catálogo / Busca | `/cursos/` | ✅ | `cursos.html` |
| 3 | Página do curso | `/cursos/{slug}/` | ✅ | `curso-como-criar-mooc.html` |
| 4 | Área (categoria) | `/areas/{slug}/` | ✅ | `area-educacao.html` |
| 5 | Para quem (público) | `/publicos/{slug}/` | ✅ | `publico-professores.html` |
| 6 | Série | `/series/{slug}/` | ✅ | — |
| 7 | Projeto parceiro | `/v/{slug}/` (Rio Doce, UnAC) | ✅ | — |
| 8 | Licença Capacitação + Planejador | `/qualificacao/` | ✅ | `qualificacao.html` |
| 9 | Certificação | `/certificacao/` | ✅ | — |
| 10 | Sobre | `/sobre/` | ✅ | `sobre.html` |
| 11 | Perguntas frequentes | `/faq/` | ✅ | `perguntas-frequentes.html` |

Combinações de faceta (`/cursos/?categoria=…&carga=…`) = **não indexáveis** (`noindex`/canonical).

---

## 1. Home — `/`

**Propósito:** apresentar a Vitrine, orientar a descoberta e expor a demanda real. Público leigo, nacional, de descoberta.

**Seções (ordem):**
1. **Hero** — título/proposta de valor ("Cursos gratuitos e abertos do Ifes, com certificado"), busca proeminente, CTA.
2. **Atalhos "Para quem"** — 3–4 cards de público (professores/educadores · comunidade/começar do zero · trabalho e carreira · servidores/setor público). *Atalhos, nunca rota única.*
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

**Propósito:** encontrar cursos por busca + facetas combináveis.

**Seções:**
1. Barra de busca (título + tags, tolerante a acento).
2. Facetas (sidebar desktop / bottom-sheet mobile): Categoria (15) · Para quem · Carga horária (≤10/10–20/20–40/40–60h) · Acessibilidade (Libras/AD) · Idioma.
3. Chips de filtros ativos + "Limpar".
4. Ordenação: Relevância · Mais cursados · Recentes · A–Z.
5. Grade de cards (paginação/scroll com fallback rastreável).
6. Estado vazio (microcopy + sugestões).

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

## 5. Para quem (público) — `/publicos/{slug}/`

**Propósito:** atalho de autoidentificação (professores, comunidade, trabalho/carreira, servidores). Indexável ("cursos para professores" é busca-alvo).

**Seções:** título voltado ao público · texto curto · grade de cursos com aquele público-alvo · CTA (para servidores → liga à Licença Capacitação).

**Dados:** cards filtrados por `público-alvo`. *Atalho, não rota única (107/165 cursos têm 2+ públicos).*

---

## 6. Série — `/series/{slug}/`

**Propósito:** contar a história de uma coleção de marca/produção.

**Séries:** Atendente e Vendedor (3, com níveis) · Educador Maker (4) · Lovelace (6) · Embrace (3) · Lesson Study (PT/EN = mesmo curso, dois selos de idioma).

**Seções:** identidade da série · sequência sugerida de cursos · grade.

---

## 7. Projeto parceiro — `/v/{slug}/`

**Propósito:** hub de projeto com identidade institucional.

**Projetos:** **Rio Doce Escolar** (`/v/riodoce/`, 31 cursos) · **UnAC** (`/v/unac/`, 33 cursos — Universidade Aberta Capixaba, parceria Ifes/CEFOR × Governo do ES; ver `projetos-especiais.md`).

**Seções:** descrição oficial do projeto/parceria · logo · grade de cursos associados.

---

## 8. Licença Capacitação + Planejador — `/qualificacao/`

**Propósito:** serviço para servidores públicos (não é filtro de conteúdo).

**Seções:** o que é a Licença · quem tem direito · legislação · **Planejador** (monta combinação de cursos somando `carga_horaria` até a meta de horas) · CTA.

**Dados:** `carga_horaria` (já populada) por curso; meta de horas informada pelo usuário.

---

## 9. Certificação — `/certificacao/`

**Propósito:** explicar como funciona o certificado (aproveitamento ≥60%, autoinstrucional, sem tutoria). Página indexável (busca "curso gratuito com certificado").

---

## 10. Sobre — `/sobre/`

**Propósito:** o que é a Vitrine MOOC, o CEFOR/Ifes, o objetivo (Resolução CS 72/2020 — democratização/inclusão), como participar.

---

## 11. Perguntas frequentes — `/faq/`

**Propósito:** dúvidas comuns (como me inscrevo, certificado, gratuidade, pré-requisitos, Libras). Formato acordeão. Schema `FAQPage` para AEO.

---

## Dados do card de curso (referência única)

Usado em toda grade (home, catálogo, área, público, série, projeto):

`imagem` · `selos[]` (Libras/AD/Idioma) · `badge_novo?` · `categorias[]` (chips) · `titulo` ·
`carga_horaria` · `serie/projeto?` · `link → /cursos/{slug}/`.

Fonte: `stages/02-catalogo/output/catalogo-cursos-completo.csv`.

---

## Rastreabilidade

- **Cobertura:** as 11 páginas cobrem toda a navegação da arquitetura v4.1 (Categorias, Para quem, Séries, Projetos, Licença, Certificação, Sobre, FAQ).
- **Protótipos:** 7 das 11 já têm HTML em `prototipo-vitrine-mooc/`; faltam Série, Projeto e Certificação (derivam de padrões já definidos).
- **Escopo:** 165 cursos publicados (os 65 "em produção" ficam fora — ver `arquitetura-informacao.md` v4.1).
