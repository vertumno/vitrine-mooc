# Vitrine MOOC Ifes

Planejamento e desenvolvimento da nova Vitrine dos cursos abertos (MOOC) do Ifes. Configure uma vez com `setup`, depois avance pelos estagios.

## Roteamento de Tarefas

| Tipo de Tarefa | Ir para | Descricao |
|----------------|---------|-----------|
| Descoberta | `stages/01-descoberta/CONTEXT.md` | Requisitos, analise da Vitrine atual e do modelo da Base de Conhecimento |
| Catalogo | `stages/02-catalogo/CONTEXT.md` | Inventario, taxonomia, metadados e indicadores dos cursos (165 publicados + 65 em producao) |
| Design/UX | `stages/03-design-ux/CONTEXT.md` | Organizar interfaces do AI/UX Studio e definir templates de pagina |
| Setup de ambiente | `stages/04-setup-ambiente/CONTEXT.md` | WordPress 7 local, estrutura do repo, dump do banco e fluxo Git |
| Desenvolvimento | `stages/05-desenvolvimento/CONTEXT.md` | Construir tema, blocos e templates do WordPress |
| QA e entrega | `stages/06-qa-entrega/CONTEXT.md` | QA visual e funcional, PR para a branch de teste e migracao |

## Recursos Compartilhados

| Recurso | Local | Conteudo |
|---------|-------|----------|
| Meta do projeto | `shared/projeto-meta.md` | Ambiente, versao WP, prazos, partes envolvidas |
| Convencoes Git e deploy | `shared/convencoes-git-deploy.md` | Fluxo de branches, regra de PR, migracao teste/producao |
| Glossario | `shared/glossario.md` | Termos do dominio (MOOC, Vitrine, CGTI, CGTE, CEFOR) |
| Resumo da reuniao | `shared/resumo-reuniao.md` | Sintese do kickoff (decisoes e proximos passos) |
| SEO/GEO/AEO | `shared/seo-geo-aeo.md` | Guia transversal de encontrabilidade em busca tradicional, IA generativa e mecanismos de resposta |
| Design system | `design-system/CONTEXT.md` | Paleta de cores e tipografia da Vitrine |
| Skills | `skills/README.md` | Conhecimento de dominio bundled para os agentes |
| Indicadores MOOC | `stages/02-catalogo/output/powerbi-mooc-ifes/` | Extracao do Power BI, planilha, CSVs e insights para decisao |
| Modelo de dados da Vitrine atual | `stages/01-descoberta/output/modelo-dados-vitrine-atual.md` | CPT `curso` + ACF, taxonomia vigente, plugins ativos, dump da CGTI |

## Dados Analiticos Disponiveis

O estagio 02 possui uma extracao do Painel de Indicadores dos MOOC do Ifes em `stages/02-catalogo/output/powerbi-mooc-ifes/`.

Use essa fonte quando a tarefa envolver priorizacao, destaques, ordenacao de cursos, estrategia de catalogo, alcance geografico, conclusao/certificacao ou UX baseada em dados reais.
