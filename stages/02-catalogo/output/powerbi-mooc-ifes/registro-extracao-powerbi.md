# Registro da extração do Painel de Indicadores

## Objetivo

Extrair dados tabulares do Painel de Indicadores dos MOOC do Ifes para apoiar decisões da nova Vitrine, principalmente:

- demanda por curso;
- certificação/conclusão;
- distribuição por unidade;
- distribuição geográfica;
- tendência anual;
- oportunidades de melhoria de catálogo e UX.

## Procedimento executado

1. Acessado o HTML público do Power BI a partir do link do painel.
2. Identificado o `resourceKey` público e o cluster regional usado pelo relatório.
3. Baixados os endpoints públicos:
   - `modelsAndExploration`;
   - `conceptualschema`.
4. Lidos os visuais, páginas, `prototypeQuery`, filtros e comandos semânticos.
5. Executadas consultas no endpoint público `querydata?synchronous=true`, usando `SemanticQueryDataShapeCommands`.
6. Decodificado o formato de retorno do Power BI:
   - `DS`;
   - `PH`;
   - `DM0`;
   - `ValueDicts`;
   - flags de repetição `R`.
7. Gerados CSVs por visual extraído.
8. Gerado XLSX consolidado.
9. Gerada análise executiva em Markdown com achados e recomendações.

## Script

Arquivo: `stages/02-catalogo/scripts/extrair_powerbi_mooc.py`

Saída principal: `stages/02-catalogo/output/powerbi-mooc-ifes/`

## Resultado da extração

| Artefato | Resultado |
|---|---:|
| Tabela `Indicadores por curso` | 171 linhas extraídas |
| Linhas válidas para análise quantitativa | 164 |
| Planilhas no XLSX | 10 |
| CSVs tabulares gerados | 9 |
| Metadados técnicos preservados | 2 JSONs |

## Abas extraídas

| Aba | Linhas | Observação |
|---|---:|---|
| Indicadores por curso | 171 | Base principal |
| Dados por UF | 29 | Distribuição geográfica nacional |
| Dados por país | 58 | Distribuição internacional |
| Matrículas por ano | 12 | Série extraída do visual de matrículas |
| Top cursos matrículas | 5 | Ranking de procura |
| Certificados por ano | 87 | Série mensal/anual de certificados |
| Cursos por unidade | 18 | Distribuição institucional |
| Crescimento matrículas | 7 | Série YoY |
| Crescimento certificados | 7 | Série YoY |
| Fonte | 4 | Metadados da extração |

## Visualizações não extraídas

| Visual | Motivo |
|---|---|
| Top 5 - Cursos com mais certificados | A consulta pública retornou resposta sem `DS` |
| Top 5 - Cursos mais populares | A consulta pública retornou resposta sem `DS` |

## Principais achados incorporados

- 50 cursos concentram 74,0% das matrículas e 75,2% dos certificados.
- A taxa global de certificação é 33,3%.
- Cursos de alta demanda e baixa conversão têm potencial estimado de +7.281 certificados se alcançarem a mediana de certificação.
- O Campus Vila Velha aparece como referência de eficiência, com 42,6% de conversão entre unidades com volume relevante.
- O Campus Linhares tem grande escala, mas baixa conversão agregada, puxada principalmente por `Inglês Comunicativo`.
- A Vitrine tem alcance nacional: 65,1% das matrículas por UF vêm de fora do Espírito Santo.
- Internacionalização ainda é residual: 0,5% das matrículas por país vêm de fora do Brasil.

## Decisões derivadas para próximos estágios

- UX deve favorecer descoberta por tema, objetivo e carga horária, não apenas listagem alfabética.
- Ordenação da Vitrine deve considerar popularidade e conversão, evitando destacar só cursos com mais cliques/matrículas.
- Cursos de alta demanda e baixa conversão devem virar fila de revisão pedagógica/UX.
- Cursos com alta conversão e baixa escala devem ser candidatos a destaque editorial e campanhas.
- O modelo de dados pode prever campos analíticos opcionais: matrículas, certificados, taxa de certificação, tempo médio de conclusão, horas de formação e classificação de popularidade.

