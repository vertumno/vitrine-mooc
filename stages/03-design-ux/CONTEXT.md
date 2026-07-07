# Estagio 03: Design e UX

Organizar as interfaces do AI/UX Studio, fechar o design system e especificar os templates de pagina.

## Inputs

| Fonte | Arquivo/Local | Escopo | Por que |
|-------|---------------|--------|---------|
| Estagio anterior | `../02-catalogo/output/` | Arquivos completos | Taxonomia e metadados que a UI exibe |
| Indicadores | `../02-catalogo/output/powerbi-mooc-ifes/analise-insights-powerbi-mooc-ifes.md` | Arquivo completo | Prioridades, destaques, filtros e ordenacao baseados em demanda/conclusao |
| Assets de UX | `references/` (interfaces do AI/UX Studio) | Arquivos completos | Direcao visual ja produzida |
| Extrações design-md | `references/design-md/{ifes-institucional,vitrine-mooc-atual}/DESIGN.md` + `tokens.json` | Arquivos completos | Tokens reais destilados da marca Ifes e da Vitrine atual |
| Design system | `../../design-system/palette.md`, `../../design-system/typography.md` | Arquivos completos | Tokens ja consolidados (marca Ifes + heranças) |
| Skill | `../../skills/design-md/SKILL.md` | Indice | Pipeline URL → DESIGN.md (destilação de design system) |

## Process

1. Reuna e organize os assets do AI/UX Studio em `references/`.
2. Mapeie as paginas: home, listagem/busca de cursos, pagina do curso, pagina de categoria, sobre.
3. Leia os insights do Power BI quando a tarefa envolver priorizacao, destaques, ordenacao, filtros ou metricas.
4. Extraia os tokens de design com a skill `design-md` (URL → DESIGN.md) das fontes de referência e consolide em `design-system/palette.md` e `typography.md`. **[Feito 06/07 — ver `references/design-md/`]**
5. Especifique os componentes: card de curso, busca, filtros por categoria/status, header e footer.
6. **[Checkpoint]** Apresente o mapa de paginas e os componentes para validacao.
7. Rode os checks de Audit. Se algum falhar, revise antes de salvar.
8. Salve a especificacao de design em `output/`.

## Checkpoints

| Apos passo | Agente apresenta | Humano decide |
|------------|------------------|---------------|
| 4 | Mapa de paginas + lista de componentes + tokens extraidos | Se a estrutura e o visual atendem ao publico |

## Audit

| Check | Condicao de aprovacao |
|-------|------------------------|
| Cobertura de paginas | Toda pagina necessaria tem layout definido |
| Consistencia | Componentes usam apenas tokens do design-system |
| Acessibilidade | Contraste e tamanhos atendem boas praticas; suporte a acentuacao |
| Responsividade | Cada template define comportamento mobile e desktop |
| Dados reais | Decisoes de destaque, ordenacao e filtros consideram os insights do Painel de Indicadores quando aplicavel |

## Outputs

| Artefato | Local | Formato |
|----------|-------|---------|
| Spec de design | `output/design-spec.md` | Markdown: componentes, estados, regras |
| Mapa de paginas | `output/mapa-paginas.md` | Markdown: paginas, secoes e dados exibidos |
