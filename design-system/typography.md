# Tipografia — Vitrine MOOC

Famílias, escala e pesos da nova Vitrine. Fonte canônica para tema e templates.

> **Origem (06/07/2026):** destilada com a skill `design-md` a partir do portal institucional
> do Ifes (`https://www.ifes.edu.br/`), onde três famílias são carregadas via `@font-face`:
> **Open Sans**, **Poppins** e **Oswald**. Evidência em
> `stages/03-design-ux/references/design-md/ifes-institucional/DESIGN.md`.
> **Decisão:** herdar a tipografia institucional do Ifes; corpo subido de 14px → **16px** para
> leitura de descoberta pública. Todas são Google Fonts com suporte completo a acentuação PT-BR.

## Famílias

| Token | Uso | Valor | Origem |
|-------|-----|-------|--------|
| `--fonte-titulo` | Headings (h1–h3), seções | **Poppins** | Ifes (`@font-face`) |
| `--fonte-corpo` | Texto corrido, descrições, UI | **Open Sans** | Ifes (`@font-face`) |
| `--fonte-destaque` | Hero e kickers/overlines condensados (uppercase) | **Oswald** | Ifes (`@font-face`) |

## Escala (base 16px, leitura pública)

| Token | Papel | Tamanho | Fonte | Peso |
|-------|-------|---------|-------|------|
| `--fs-hero` | Hero / display | 48px | Oswald ou Poppins | 700 |
| `--fs-h1` | Título de página | 40px | Poppins | 600 |
| `--fs-h2` | Título de seção | 32px | Poppins | 600 |
| `--fs-h3` | Subtítulo | 24px | Poppins | 600 |
| `--fs-h4` | Rótulo de bloco | 20px | Open Sans | 700 |
| `--fs-lead` | Subtítulo/lead de corpo | 18px | Open Sans | 400 |
| `--fs-corpo` | Corpo padrão | 16px | Open Sans | 400 |
| `--fs-corpo-peq` | Metadados, apoio | 14px | Open Sans | 400 |
| `--fs-legenda` | Legendas, selos | 12px | Open Sans | 400 |
| `--fs-overline` | Kicker/tag (uppercase, tracking +0.05em) | 13px | Oswald | 500 |

## Pesos

| Token | Peso | Uso |
|-------|------|-----|
| Regular | 400 | corpo, lead |
| SemiBold | 600 | títulos (Poppins), botões |
| Bold | 700 | h4, ênfase, hero |
| ExtraBold | 800 | reservado para hero de campanha (Open Sans/Oswald) |

## Notas de uso

- **Poppins** dá calor e modernidade aos títulos sem perder a formalidade institucional.
- **Open Sans** é a base de leitura — corpo a **16px** (não 14px do portal legado) para o público leigo de descoberta.
- **Oswald** apenas para hero/kicker de impacto e overlines em uppercase; **não** misture Oswald e Poppins no mesmo título.
- `line-height` de leitura ≈ 1.5 no corpo, ≈ 1.2 nos títulos.
- Todas as três são Google Fonts com glyphs completos para português (á, ã, ç, õ, é…). Preferir carregamento self-hosted no tema WP para performance/LGPD (evitar chamada ao Google Fonts em runtime).
