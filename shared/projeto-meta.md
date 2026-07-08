# Meta do Projeto - Vitrine MOOC Ifes

Fatos estaveis do projeto. Fonte canonica para os estagios. Atualize aqui quando algo mudar, nunca duplique em outros arquivos.

## Identidade

| Campo | Valor |
|-------|-------|
| Produto | Vitrine dos cursos abertos (MOOC) do Ifes |
| Organizacao | Ifes - CEFOR (Centro de Referencia em Formacao e em Educacao a Distancia) |
| URL atual | https://mooc.cefor.ifes.edu.br/ |
| Setores envolvidos | CGTI (infraestrutura) e CGTE (desenvolvimento) |
| Equipe de desenvolvimento | Elton Vinicius e Marcos Forecchi Accioly (CGTE) |
| Infraestrutura | Eduardo "Dudu" Moura da Silva (CGTI) |

## Tecnologia

| Campo | Valor |
|-------|-------|
| Plataforma | WordPress |
| Versao alvo | 7.0 (a Vitrine atual roda 5.9) |
| Tema atual | `vitrinemooctheme` (Bootstrap 4.2.1, Font Awesome 4.7) |
| Ambiente de trabalho | Local (WP7) e depois ambiente de teste dedicado (VM da CGTI) |
| Banco de dados | Dump da CGTI de 03/07/2026 em `stages/04-setup-ambiente/references/backup_vitrine_mooc.sql` (nÃ£o versionado â€” LGPD, ver `.gitignore`); anÃ¡lise em `stages/01-descoberta/output/modelo-dados-vitrine-atual.md` |
| Modelo de referencia | Estrutura de pastas do repositorio da Base de Conhecimento |

## Escopo do Catalogo

| Campo | Valor |
|-------|-------|
| Cursos publicados | 165 (ver `stages/02-catalogo/references/cursos-fonte.md`) |
| Cursos em producao | 65 (previstos ate 10/06/26) |

## Fontes Analiticas

| Fonte | Valor |
|-------|-------|
| Painel de Indicadores MOOC | `stages/02-catalogo/output/powerbi-mooc-ifes/` |
| Planilha extraida | `stages/02-catalogo/output/powerbi-mooc-ifes/painel-indicadores-mooc-ifes.xlsx` |
| Analise executiva | `stages/02-catalogo/output/powerbi-mooc-ifes/analise-insights-powerbi-mooc-ifes.md` |
| Dataset Power BI - ultimo refresh conhecido | 2026-06-29T11:15:54.177 |
| Data da extracao documentada | 2026-07-01 |

Use esses dados para decisoes sobre priorizacao, destaque, filtros, ordenacao e estrategia de catalogo. Nao use 2026 como ano fechado; a extracao atual foi feita em 2026-07-01.

## Itens a confirmar no `setup`

Os valores abaixo dependem da CGTI e do design final. Sao preenchidos no onboarding.

| Item | Placeholder |
|------|-------------|
| Branch de producao (Master) | {{BRANCH_PRODUCAO}} |
| Branch de teste / destino dos PRs | {{BRANCH_TESTE}} |
| URL do ambiente de teste | {{URL_TESTE}} |
| Repositorio modelo (Base de Conhecimento) | {{REPO_BASE_CONHECIMENTO}} |
| Estagio inicial padrao | {{ESTAGIO_INICIAL}} |

## Prazos

- Ambiente de teste da Vitrine: inicio previsto por volta de 06/07.
- Ate la, a equipe trabalha localmente.


