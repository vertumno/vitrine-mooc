# Power BI MOOC Ifes - extração e análise

Esta pasta registra a extração do Painel de Indicadores dos MOOC do Ifes e os artefatos analíticos gerados para apoiar decisões de catálogo, UX e priorização da nova Vitrine.

## Fonte

- Painel público: https://app.powerbi.com/view?r=eyJrIjoiMWMyN2UxZTktY2FiMi00ZDI1LWE5NTctOGZiZjUzOTdhMjUyIiwidCI6IjQ0ZTllMTcyLWZmYTUtNDNmMy1iMjJjLTM3MWNmY2QyNzJlZCJ9&pageName=ReportSection
- Resource key Power BI: `1c27e1e9-cab2-4d25-a957-8fbf5397a252`
- Dataset `LastRefreshTime`: `2026-06-29T11:15:54.177`
- Extração feita em: `2026-07-01`

## Arquivos principais

| Arquivo | Uso |
|---|---|
| `painel-indicadores-mooc-ifes.xlsx` | Planilha consolidada com abas extraídas do painel |
| `indicadores-por-curso.csv` | Tabela principal por curso: unidade, carga horária, tipo, matrículas, certificados, taxa e tempo |
| `analise-insights-powerbi-mooc-ifes.md` | Relatório executivo com achados, riscos, oportunidades e recomendações |
| `manifest.json` | Manifesto da extração: abas, linhas, colunas, erros e metadados |
| `powerbi-modelsAndExploration.json` | Metadados técnicos do relatório Power BI |
| `powerbi-conceptualschema.json` | Esquema semântico retornado pelo Power BI |

## CSVs auxiliares

| Arquivo | Conteúdo |
|---|---|
| `dados-por-uf.csv` | Matrículas por UF |
| `dados-por-pais.csv` | Matrículas por país |
| `matriculas-por-ano.csv` | Série anual/mensal de matrículas extraída do visual de matrículas |
| `certificados-por-ano.csv` | Série anual/mensal de certificados |
| `crescimento-matriculas.csv` | Matrículas válidas e crescimento YoY |
| `crescimento-certificados.csv` | Certificados válidos e crescimento YoY |
| `cursos-por-unidade.csv` | Quantidade de cursos por unidade |
| `top-cursos-matriculas.csv` | Top 5 cursos com mais matrículas |

## Como reproduzir

Rode a partir da raiz do projeto:

```powershell
python stages\02-catalogo\scripts\extrair_powerbi_mooc.py
```

O script baixa os metadados públicos do Power BI, executa as consultas semânticas disponíveis, decodifica o formato compactado `ValueDicts`, gera CSVs e monta o XLSX consolidado.

## Limitações conhecidas

- Algumas visualizações do Power BI não retornaram `DS` pela API pública no momento da extração: `Top cursos certificados` e `Top cursos populares`.
- A resposta compactada do Power BI trouxe algumas linhas incompletas/anômalas na tabela principal; a análise executiva excluiu 7 linhas dos cálculos quantitativos e documentou isso.
- O ano de 2026 é parcial, pois a extração ocorreu em 2026-07-01; não comparar 2026 como ano fechado.

## Uso no projeto

- Estágio 02: enriquecer catálogo e priorização por dados reais de demanda/conclusão.
- Estágio 03: orientar UX da Vitrine, pesos de ordenação, filtros, destaques e recomendações.
- Estágio 05: apoiar campos e métricas derivadas no modelo de dados, se a Vitrine for exibir indicadores.

