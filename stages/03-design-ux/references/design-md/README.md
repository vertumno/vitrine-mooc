# Extrações design-md — referências de design da Vitrine

Destilação de design system (spec Google `DESIGN.md`) das fontes reais de referência, feita com a
skill `skills/design-md` em **06/07/2026**.

## Fontes extraídas

| Pasta | URL | Papel |
|-------|-----|-------|
| `vitrine-mooc-atual/` | `https://mooc.cefor.ifes.edu.br/` | Baseline legado (Bootstrap 4.2.1 + tema; teal `#008080` + dourado `#ffbc00`) |
| `ifes-institucional/` | `https://www.ifes.edu.br/` | Referência de marca (verde `#147a02` + Open Sans/Poppins/Oswald) |

Cada pasta contém:
- `DESIGN.md` — spec Google (frontmatter YAML + 9 seções narrativas).
- `tokens.json` — frontmatter parseado (cores, tipografia, componentes, spacing, radius).
- `inputs/` — evidência estática detectada: `css-vars-detected.json`, `tokens-detected.json`, `font-faces.json`, `component-properties.json`, `page.md`, etc.
- `style-fingerprint.json`, `crash-context.json`.

A **síntese** dessas duas fontes para a nova Vitrine vive em `design-system/palette.md` e
`design-system/typography.md`.

## Como foi gerado (rastreabilidade)

O pipeline da skill tem 8 fases. As **fases 1–5 (detecção estática)** rodaram normalmente via
`node skills/design-md/run.cjs --url <url> --out <pasta>` e produziram todos os `inputs/` +
`prompt.txt`. A **fase 6 (cognição LLM)** não pôde ser executada pelo pipeline neste ambiente:

1. **Bug de portabilidade (Windows):** a skill (feita no macOS) invoca `spawnSync("claude", …)`
   sem `shell:true`; no Windows isso resulta em `ENOENT` (o wrapper `.cmd` do npm não é resolvido).
2. **Política de segurança do harness:** a skill invoca `claude -p --dangerously-skip-permissions`,
   que o Claude Code bloqueia como "unsafe agent loop" sem autorização explícita.

Como a fase 6 é puramente cognitiva (transformar os tokens detectados no `DESIGN.md` conforme o
`inputs/prompt.txt`), ela foi **completada nativamente** pelo mesmo modelo (Opus) que a skill
invocaria — sem spawnar um agente aninhado. Os `DESIGN.md` seguem fielmente o `prompt.txt` e os
`inputs/` detectados; `tokens.json` foi gerado por parse do frontmatter (`js-yaml`).

> **Para reproduzir a fase 6 automaticamente** (fora deste ambiente): rodar em macOS/Linux, ou
> corrigir `skills/design-md/lib/providers/claude-cli.cjs` para chamar o CLI via
> `node <cli.js>` (sem shell) e autorizar `claude -p` no ambiente. As fases 7–8 (lint,
> quality-score, `preview.html`) dependem da 6 e não foram executadas — não são bloqueantes para
> o uso dos tokens.
