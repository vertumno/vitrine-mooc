# Estagio 06: QA e Entrega

Validar a Vitrine, abrir o PR para a branch de teste e planejar a migracao para producao.

## Inputs

| Fonte | Arquivo/Local | Escopo | Por que |
|-------|---------------|--------|---------|
| Desenvolvimento | `../05-desenvolvimento/output/` | Arquivo completo | O que foi construido e pendencias |
| Convencoes | `../../shared/convencoes-git-deploy.md` | Arquivo completo | Fluxo de PR e migracao |
| Design | `../03-design-ux/output/design-spec.md` | Arquivo completo | Referencia para o QA visual |

## Process

1. QA visual: compare as paginas com o `design-spec.md`.
2. QA funcional: teste busca, filtros, links, responsividade e acessibilidade.
3. Valide os dados do catalogo (cursos publicados vs em producao, links corretos).
4. Liste e corrija os problemas encontrados (volte ao estagio 05 se necessario).
5. **[Checkpoint]** Aprove para abertura de PR.
6. Abra o PR para {{BRANCH_TESTE}} (delegue ao `@devops`). Nunca para a Master.
7. Apos validacao no ambiente de teste, planeje a migracao: refazer o dump na hora e migrar.
8. Rode os checks de Audit e registre o relatorio em `output/`.

## Checkpoints

| Apos passo | Agente apresenta | Humano decide |
|------------|------------------|---------------|
| 4 | Lista de problemas e correcoes aplicadas | Se a Vitrine esta pronta para PR |

## Audit

| Check | Condicao de aprovacao |
|-------|------------------------|
| Visual | Paginas batem com a spec de design |
| Funcional | Busca, filtros, links e responsividade ok |
| Dados | Catalogo correto e completo |
| Destino do PR | PR aberto para {{BRANCH_TESTE}}, nunca a Master |

## Outputs

| Artefato | Local | Formato |
|----------|-------|---------|
| Relatorio de QA | `output/relatorio-qa.md` | Markdown: checks, problemas, status |
| Plano de migracao | `output/plano-migracao.md` | Markdown: passos de dump e migracao para producao |
