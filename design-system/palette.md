# Paleta de Cores — Vitrine MOOC

Cores oficiais da nova Vitrine. Fonte canônica para tema e templates.

> **Origem (06/07/2026):** destilada com a skill `design-md` a partir de duas fontes reais —
> o portal institucional do Ifes (`https://www.ifes.edu.br/`, marca) e a Vitrine MOOC atual
> (`https://mooc.cefor.ifes.edu.br/`, herança). Evidência em
> `stages/03-design-ux/references/design-md/*/DESIGN.md` (+ `tokens.json`).
> **Decisão:** marca = **verde institucional do Ifes**; apoio = **teal** (herança da Vitrine);
> acento de ação = **dourado** (herança da Vitrine). Todos os pares texto/fundo abaixo miram **WCAG AA**.

## Cores Primárias (marca — verde Ifes)

| Token | Uso | Valor | Origem |
|-------|-----|-------|--------|
| `--cor-primaria` | Verde Ifes — cor institucional primária (botões, header ativo, links de marca) | `#147a02` | Ifes (uso 11×) |
| `--cor-primaria-escura` | Hover/pressed, faixas de marca | `#066017` | Ifes (uso 14×) |
| `--cor-primaria-profunda` | Rodapé, seções de marca imersivas | `#195128` | Ifes (uso 8×) |

## Cores de Apoio e Acento

| Token | Uso | Valor | Origem |
|-------|-----|-------|--------|
| `--cor-secundaria` | Teal — apoio, categorias, elementos de destaque | `#008080` | Vitrine atual (herança) |
| `--cor-secundaria-escura` | Hover do teal | `#0c797a` | Vitrine atual |
| `--cor-acento` | Dourado — CTA de ação/destaque (usar **texto escuro** por cima) | `#ffbc00` | Vitrine atual |

> **Acessibilidade do acento:** dourado `#ffbc00` **não** atinge AA com texto branco. Em botões/badges dourados, use texto `#212529`.

## Neutros

| Token | Uso | Valor | Origem |
|-------|-----|-------|--------|
| `--cor-texto` | Corpo de texto, títulos | `#212529` | comum (Ifes `#333` / Vitrine `#212529`) |
| `--cor-texto-suave` | Texto secundário, metadados | `#6c757d` | comum |
| `--cor-fundo` | Fundo das páginas | `#ffffff` | comum |
| `--cor-fundo-alt` | Fundo alternado de seção, cards sutis | `#f8f9fa` | comum |
| `--cor-borda` | Divisores e bordas de card | `#dee2e6` | comum |

## Estados

| Token | Uso | Valor | Origem |
|-------|-----|-------|--------|
| `--cor-sucesso` | Confirmações (distinto do verde de marca) | `#2e9e4f` | derivado (evita colidir com `--cor-primaria`) |
| `--cor-alerta` | Avisos | `#f0a000` | Ifes (laranja `#f89406`) ajustado |
| `--cor-erro` | Erros | `#dc3545` | comum (Bootstrap danger) |
| `--cor-info` | Informação/links auxiliares | `#0d6efd` | derivado (azul de UI) |

## Notas de uso

- **Verde é a marca.** Toda decisão cromática parte de `--cor-primaria`. Foco de formulário = verde, não azul.
- **Teal ≠ verde.** O teal `#008080` é apoio/categoria; não use como cor de marca principal (evitar competir com o verde Ifes).
- **Dourado é ação/destaque pontual.** Não pinte grandes áreas de dourado; reserve para CTAs e selos, sempre com texto escuro.
- **Superfície branca dominante** + neutros limpos = leitura de descoberta pública (o público MOOC é leigo, nacional).
- Cores legadas de framework (azuis `#007bff`/`#0088cc`, etc.) **não** são marca — ver a seção "Don'ts" nos `DESIGN.md` de referência.
