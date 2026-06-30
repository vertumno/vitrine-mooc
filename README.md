# Vitrine MOOC Ifes

Workspace de planejamento e desenvolvimento da nova Vitrine dos cursos abertos (MOOC) do Ifes, estruturado pela metodologia ICM (Interpretable Context Methodology).

Vitrine atual: https://mooc.cefor.ifes.edu.br/

## Como usar

1. Abra este diretorio no Claude Code.
2. Digite `setup` para configurar branches, ambiente, repo modelo e design (uma vez so).
3. Avance pelos estagios `01` a `06`, revisando o `output/` de cada um antes de seguir.
4. Digite `status` a qualquer momento para ver a completude do pipeline.

O roteamento completo esta em [CLAUDE.md](CLAUDE.md) e [CONTEXT.md](CONTEXT.md).

## Pipeline

| Estagio | Faz |
|---------|-----|
| [01-descoberta](stages/01-descoberta/CONTEXT.md) | Requisitos + analise da Vitrine atual + modelo da Base |
| [02-catalogo](stages/02-catalogo/CONTEXT.md) | Inventario e taxonomia dos cursos (165 + 65) |
| [03-design-ux](stages/03-design-ux/CONTEXT.md) | Interfaces do AI/UX Studio + templates de pagina |
| [04-setup-ambiente](stages/04-setup-ambiente/CONTEXT.md) | WordPress 7 local + repo + dump + fluxo Git |
| [05-desenvolvimento](stages/05-desenvolvimento/CONTEXT.md) | Tema, blocos e templates (codigo WordPress) |
| [06-qa-entrega](stages/06-qa-entrega/CONTEXT.md) | QA + PR para branch de teste + migracao |

## Metodologia

Estrutura de pastas como arquitetura de agente: estagios numerados, contratos `CONTEXT.md` (Inputs, Process, Outputs), handoff via pastas `output/` e carregamento de contexto em camadas. Referencia: `C:\Users\elton\mmos\icm`.
