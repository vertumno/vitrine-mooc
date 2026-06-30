# Estagio 01: Descoberta

Levantar requisitos da nova Vitrine, analisar a Vitrine atual e o modelo da Base de Conhecimento.

## Inputs

| Fonte | Arquivo/Local | Escopo | Por que |
|-------|---------------|--------|---------|
| Meta | `../../shared/projeto-meta.md` | Arquivo completo | Contexto, tecnologia e partes envolvidas |
| Reuniao | `../../shared/resumo-reuniao.md` | Arquivo completo | Decisoes e restricoes do kickoff |
| Vitrine atual | `references/html-vitrine-atual.md` | Arquivo completo | Estrutura, secoes e recursos a manter/melhorar |
| Convencoes | `../../shared/convencoes-git-deploy.md` | "Estrutura do Repositorio" | Modelo da Base de Conhecimento |
| Usuario | (conversa) | Requisitos | Objetivos da nova Vitrine |

## Process

1. Colete e confirme com o usuario os requisitos da nova Vitrine: objetivos, publico-alvo, o que muda em relacao a atual.
2. Analise a Vitrine atual (`html-vitrine-atual.md`): secoes, navegacao, recursos (busca, categorias), o que manter e o que melhorar.
3. Revise o modelo de estrutura de repositorio da Base de Conhecimento a ser replicado.
4. Liste restricoes conhecidas: WordPress 7, ambiente de teste, dump do banco, fluxo Git, prazos.
5. **[Checkpoint]** Apresente a sintese de requisitos e a analise da Vitrine atual para validacao.
6. Rode os checks de Audit. Se algum falhar, revise antes de salvar.
7. Salve os artefatos em `output/`.

## Checkpoints

| Apos passo | Agente apresenta | Humano decide |
|------------|------------------|---------------|
| 4 | Requisitos consolidados + analise da Vitrine atual | Se esta completo, correto e prioridades certas |

## Audit

| Check | Condicao de aprovacao |
|-------|------------------------|
| Cobertura | Todo requisito do usuario aparece no documento |
| Rastreabilidade | Cada decisao referencia reuniao, Vitrine atual ou usuario |
| Restricoes | WP7, ambiente, dump, Git e prazos estao registrados |

## Outputs

| Artefato | Local | Formato |
|----------|-------|---------|
| Requisitos | `output/requisitos-descoberta.md` | Markdown com requisitos e restricoes |
| Analise da Vitrine atual | `output/analise-vitrine-atual.md` | Markdown: o que manter, mudar, descartar |
