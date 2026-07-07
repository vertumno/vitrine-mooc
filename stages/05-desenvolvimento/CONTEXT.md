# Estagio 05: Desenvolvimento

Construir o tema, os templates e o modelo de dados do catalogo no WordPress 7.

## Inputs

| Fonte | Arquivo/Local | Escopo | Por que |
|-------|---------------|--------|---------|
| Design | `../03-design-ux/output/` | Arquivos completos | Spec de design e mapa de paginas |
| Ambiente | `../04-setup-ambiente/output/` | Arquivo completo | Estado do ambiente e estrutura do repo |
| Catalogo | `../02-catalogo/output/` | Arquivos completos | Taxonomia e metadados a modelar |
| Modelo de origem | `../01-descoberta/output/modelo-dados-vitrine-atual.md` | Arquivo completo | Schema atual (CPT `curso` + ACF) de onde os dados migram |
| Design system | `../../design-system/palette.md`, `../../design-system/typography.md` | Arquivos completos | Tokens de cor e tipografia |
| Skill | `../../skills/README.md` | Indice, depois regras | WordPress e frontend-design |

## Process

1. Construa a base do tema a partir do design-spec e do design-system.
2. Implemente os templates de pagina: home, listagem/busca, pagina do curso, categoria.
3. Modele os dados do catalogo (custom post type e campos) a partir da taxonomia do estagio 02.
4. Implemente busca e filtros por categoria e status.
5. Popule com os dados do catalogo (`../02-catalogo/output/`).
6. **[Checkpoint]** Revise as paginas-chave renderizadas localmente.
7. Rode os checks de Audit. Se algum falhar, corrija antes de registrar.
8. Faca commit na branch de trabalho e registre as notas em `output/`.

## Checkpoints

| Apos passo | Agente apresenta | Humano decide |
|------------|------------------|---------------|
| 5 | Home, listagem e pagina de curso renderizadas com dados reais | Se atende a spec e segue para QA |

## Audit

| Check | Condicao de aprovacao |
|-------|------------------------|
| Fidelidade | Paginas seguem `design-spec.md` e o design-system |
| Dados | Cursos do catalogo aparecem com os metadados corretos |
| Funcional | Busca e filtros funcionam por categoria e status |
| Git | Trabalho em branch de dev; nenhum push direto para a Master |

## Outputs

| Artefato | Local | Formato |
|----------|-------|---------|
| Codigo | Tema/templates no repositorio | Codigo WordPress (PHP/CSS/JS) |
| Notas | `output/notas-desenvolvimento.md` | Markdown: o que foi feito, pendencias, decisoes |
