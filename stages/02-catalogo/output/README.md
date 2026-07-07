# Output do Estágio 02 - Catálogo

Esta pasta reúne os artefatos produzidos no estágio de catálogo da Vitrine MOOC Ifes.

> **Documento oficial:** `arquitetura-informacao.md` **v4.1** é o modelo definitivo de taxonomia e navegação. `taxonomia.md`, `decisao-taxonomia-cenarios.md` e `comparativo-taxonomias.md` são registro histórico (decisões já incorporadas na v4.1).

## Decisões travadas (06/07/2026)

| Decisão | Estado |
|---|---|
| **Escopo** | **165 cursos publicados**. Os 65 "em produção" ficam **fora deste projeto**. |
| **Navegação primária** | As **15 Categorias** do formulário de cadastro. |
| **Trilhas** | **Removidas** — só Séries + Projetos parceiros. |
| **Carga horária** | **Populada** em `catalogo-cursos-completo.csv` (coluna `carga_horaria`). |
| **UnAC** | **Definido** — Universidade Aberta Capixaba (programa do Governo do ES; parceria Ifes/CEFOR). Ver `projetos-especiais.md`. |
| **Tree test / card sorting** | **Não será feito** — rótulos por decisão editorial do CEFOR. |
| **Objetivo da plataforma** | Ancorado na Resolução CS 72/2020 ("abertos à comunidade"). |

## Artefatos de catálogo

| Arquivo | Descrição |
|---|---|
| `catalogo-cursos.md` | Catálogo inicial em Markdown |
| `catalogo-cursos.csv` | Catálogo inicial em CSV |
| `catalogo-cursos-completo.md` | Catálogo enriquecido com detalhes extraídos das páginas dos cursos |
| `catalogo-cursos-completo.csv` | Versão tabular do catálogo enriquecido |
| `catalogo-cursos-completo.json` | Versão estruturada do catálogo enriquecido |
| `taxonomia.md` | Taxonomia proposta, regras e campos |
| `taxonomia-cursos.csv` | Classificação tabular dos cursos na taxonomia |
| `projetos-especiais.md` | Cursos/projetos com tratamento específico |
| `relatorio-publicos-alvo-mooc-ifes.md` | Análise de públicos-alvo do catálogo |

## Artefatos analíticos

| Pasta/arquivo | Descrição |
|---|---|
| `powerbi-mooc-ifes/` | Extração e análise do Painel de Indicadores dos MOOC do Ifes |
| `powerbi-mooc-ifes/painel-indicadores-mooc-ifes.xlsx` | Workbook consolidado com dados extraídos do Power BI |
| `powerbi-mooc-ifes/analise-insights-powerbi-mooc-ifes.md` | Relatório executivo com insights e recomendações |
| `powerbi-mooc-ifes/registro-extracao-powerbi.md` | Registro técnico da extração, limitações e reprodutibilidade |
| `powerbi-mooc-ifes/manifest.json` | Manifesto das abas extraídas e metadados |

## Como usar nos próximos estágios

- **Design/UX:** usar taxonomia, público-alvo e insights do Power BI para definir filtros, ordenação, destaques e recomendações.
- **Desenvolvimento:** usar catálogo completo e taxonomia como base de dados; indicadores podem virar campos analíticos opcionais.
- **QA:** validar paridade do catálogo, links, metadados e consistência de qualquer métrica exibida.

## Cuidados

- O catálogo publicado e a extração do Power BI são fontes complementares; divergências devem ser registradas e reconciliadas.
- A extração atual do Power BI foi feita em 2026-07-01, com dataset atualizado em 2026-06-29.
- O ano de 2026 é parcial nos indicadores.

