# Vitrine MOOC Ifes

Workspace de planejamento e desenvolvimento da nova Vitrine dos cursos abertos (MOOC) do Ifes, estruturado pela metodologia ICM. Rode `setup` uma vez para configurar identidade, design e convencoes. Depois avance pelos estagios 01 a 06, revisando o `output/` de cada um antes de seguir.

## Mapa de Pastas

```
vitrine-mooc/
├── AGENTS.md              (voce esta aqui - roteamento)
├── CONTEXT.md            (comece aqui para rotear tarefas)
├── setup/
│   └── questionnaire.md  (onboarding unico - identidade, design, convencoes)
├── shared/               (contexto estavel do projeto)
│   ├── projeto-meta.md   (fatos do projeto: ambiente, WP7, prazos)
│   ├── convencoes-git-deploy.md (fluxo Git, branches, migracao)
│   ├── glossario.md      (termos: MOOC, Vitrine, CGTI, CGTE, CEFOR)
│   ├── resumo-reuniao.md (sintese da reuniao de kickoff)
│   └── transcricao-reuniao-cgti-cgte.txt (fonte bruta)
├── design-system/        (cores e tipografia da Vitrine)
│   ├── CONTEXT.md
│   ├── palette.md
│   └── typography.md
├── skills/               (conhecimento de dominio para os agentes)
│   └── README.md
└── stages/
    ├── 01-descoberta/      requisitos + analise da Vitrine atual + modelo Base
    ├── 02-catalogo/        inventario + taxonomia + indicadores dos cursos (165+65)
    ├── 03-design-ux/       interfaces AI/UX Studio + templates de pagina
    ├── 04-setup-ambiente/  WP7 local + estrutura do repo + dump + fluxo Git
    ├── 05-desenvolvimento/ tema / blocos / templates (codigo WordPress)
    └── 06-qa-entrega/      QA + PR para branch de teste + migracao
```

## Triggers

| Keyword | Acao |
|---------|------|
| `setup` | Roda o onboarding unico - configura identidade, design e convencoes |
| `status` | Mostra a completude do pipeline nos seis estagios |

### Como `status` funciona

Varra as pastas `stages/*/output/`. Para cada estagio, se houver arquivos alem de `.gitkeep`, ele esta COMPLETO; caso contrario, PENDENTE. Renderize:

```
Pipeline: vitrine-mooc

  [01-descoberta] -> [02-catalogo] -> [03-design-ux] -> [04-setup-ambiente] -> [05-desenvolvimento] -> [06-qa-entrega]
      STATUS            STATUS            STATUS             STATUS                  STATUS                  STATUS
```

## Roteamento

| Tarefa | Ir para |
|--------|---------|
| Levantar requisitos e analisar a Vitrine atual | `stages/01-descoberta/CONTEXT.md` |
| Inventariar, classificar ou priorizar os cursos | `stages/02-catalogo/CONTEXT.md` |
| Definir design e templates de pagina | `stages/03-design-ux/CONTEXT.md` |
| Preparar ambiente WP7 local e repo | `stages/04-setup-ambiente/CONTEXT.md` |
| Desenvolver tema, blocos e templates | `stages/05-desenvolvimento/CONTEXT.md` |
| Rodar QA e migrar para teste/producao | `stages/06-qa-entrega/CONTEXT.md` |

## O que carregar

| Tarefa | Carregar | NAO carregar |
|--------|----------|--------------|
| Descoberta | `stages/01-descoberta/references/*`, `shared/projeto-meta.md`, `shared/resumo-reuniao.md` | `design-system/`, `skills/`, estagios 03 a 06 |
| Catalogo | `stages/01-descoberta/output/`, `stages/02-catalogo/references/cursos-fonte.md`, `stages/02-catalogo/output/powerbi-mooc-ifes/` quando houver priorizacao/indicadores | `design-system/`, `skills/`, estagios 03 a 06 |
| Design/UX | `stages/02-catalogo/output/`, `stages/02-catalogo/output/powerbi-mooc-ifes/analise-insights-powerbi-mooc-ifes.md`, `stages/03-design-ux/references/*`, `design-system/*`, `skills/` (frontend) | estagios 04 a 06, transcricao |
| Setup ambiente | `stages/01-descoberta/output/`, `shared/convencoes-git-deploy.md`, `stages/04-setup-ambiente/references/*` | `design-system/`, `stages/02-catalogo/` |
| Desenvolvimento | `stages/03-design-ux/output/`, `stages/04-setup-ambiente/output/`, `design-system/*`, `skills/` | estagios 01 e 02 (brutos), transcricao |
| QA e entrega | `stages/05-desenvolvimento/output/`, `shared/convencoes-git-deploy.md`, `stages/06-qa-entrega/references/*` | estagios 01 a 03 |

## Handoff entre estagios

Cada estagio escreve seu artefato na propria pasta `output/`. O proximo estagio le de la. Se voce editar um arquivo de output entre estagios, o proximo estagio usa a sua versao editada. O fluxo tipico e sequencial (01 a 06), mas voce pode entrar em qualquer estagio conforme o que ja tem pronto.
