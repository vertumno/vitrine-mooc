# Skills - Vitrine MOOC

Conhecimento de dominio para os agentes que trabalham neste workspace. Skills dao aos agentes APIs, boas praticas e exemplos sem depender de instalacao global.

## Skills recomendadas

| Skill | Para que serve | Estagios |
|-------|----------------|----------|
| `frontend-design` | Filosofia de design, estetica, evitar o "look generico de IA" | 03-design-ux, 05-desenvolvimento |
| WordPress (tema/blocos) | Estrutura de tema, templates, custom post types, blocos | 05-desenvolvimento |

## Como bundlar

As skills ainda nao foram copiadas para ca. Para tornar o workspace autocontido, copie a skill desejada para `skills/[nome]/` (com seu `SKILL.md`) durante o `setup` ou quando o estagio que a usa for iniciado.

- `frontend-design` esta disponivel como skill global do Claude Code (`frontend-design`).
- Para WordPress, avaliar uma skill de dominio ou um arquivo de convencoes proprio em `stages/05-desenvolvimento/references/`.

Referencie a skill no `CONTEXT.md` do estagio na tabela de Inputs, por exemplo:

```
| Skill | `../../skills/frontend-design/SKILL.md` | Indice, depois regras conforme necessario | Direcao de design |
```
