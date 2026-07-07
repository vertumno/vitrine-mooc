---
name: Vitrine MOOC Ifes (atual)
source_url: https://mooc.cefor.ifes.edu.br/
extracted: 2026-07-06
stack: [WordPress 5.9, Bootstrap 4.2.1, FontAwesome 4.7, jQuery, Cloudflare]
archetype: "bootstrap-flat (detector: apple-glass 90% — ver nota de correção em secao 1)"
note: "Baseline do sistema LEGADO que está sendo redesenhado. Não é a referência-alvo."
colors:
  primary: "#008080"        # from tema custom (teal, hex_usage 15×) — cor de marca da Vitrine
  secondary: "#0c797a"      # from tema custom (teal escuro, hex_usage 10×)
  tertiary: "#ffbc00"       # from tema custom (dourado, destaque)
  neutral: "#6c757d"        # from --gray / --secondary (Bootstrap)
  surface: "#ffffff"        # from body background (Bootstrap)
  text: "#212529"           # from --gray-dark / body color (Bootstrap)
  text-muted: "#6c757d"     # from --gray (Bootstrap)
  border: "#dee2e6"         # from Bootstrap border-color (hex_usage 26×)
  error: "#dc3545"          # from --danger (Bootstrap)
  success: "#28a745"        # from --success (Bootstrap)
  info: "#17a2b8"           # from --info (Bootstrap)
  warning: "#ffc107"        # from --warning (Bootstrap)
  bootstrap-blue: "#007bff" # from --primary (Bootstrap default — chassi de UI, NÃO é a marca)
typography:
  display-hero:
    fontFamily: "-apple-system, BlinkMacSystemFont, Segoe UI, Roboto, Helvetica Neue, Arial, sans-serif"  # from --font-family-sans-serif
    fontSize: "4.5rem"      # from h1 display / .display-3 declaration
    fontWeight: "300"       # from .display-* (Bootstrap light display)
    lineHeight: "1.2"
    letterSpacing: "0em"
  display-large:
    fontFamily: "-apple-system, BlinkMacSystemFont, Segoe UI, Roboto, sans-serif"
    fontSize: "3.5rem"      # from .display-4
    fontWeight: "300"
    lineHeight: "1.2"
    letterSpacing: "0em"
  section-heading:
    fontFamily: "-apple-system, BlinkMacSystemFont, Segoe UI, Roboto, sans-serif"
    fontSize: "2.5rem"      # from h1
    fontWeight: "500"
    lineHeight: "1.2"
    letterSpacing: "0em"
  subheading-large:
    fontFamily: "-apple-system, BlinkMacSystemFont, Segoe UI, Roboto, sans-serif"
    fontSize: "2rem"        # from h2
    fontWeight: "500"
    lineHeight: "1.2"
    letterSpacing: "0em"
  subheading:
    fontFamily: "-apple-system, BlinkMacSystemFont, Segoe UI, Roboto, sans-serif"
    fontSize: "1.75rem"     # from h3
    fontWeight: "500"
    lineHeight: "1.2"
    letterSpacing: "0em"
  body-large:
    fontFamily: "-apple-system, BlinkMacSystemFont, Segoe UI, Roboto, sans-serif"
    fontSize: "1.25rem"     # from .lead
    fontWeight: "300"
    lineHeight: "1.5"
    letterSpacing: "0em"
  body:
    fontFamily: "-apple-system, BlinkMacSystemFont, Segoe UI, Roboto, sans-serif"
    fontSize: "1rem"        # from body (Bootstrap base 16px)
    fontWeight: "400"
    lineHeight: "1.5"
    letterSpacing: "0em"
  body-small:
    fontFamily: "-apple-system, BlinkMacSystemFont, Segoe UI, Roboto, sans-serif"
    fontSize: "0.875rem"    # from small / .small
    fontWeight: "400"
    lineHeight: "1.5"
    letterSpacing: "0em"
  button:
    fontFamily: "-apple-system, BlinkMacSystemFont, Segoe UI, Roboto, sans-serif"
    fontSize: "1rem"        # from .btn
    fontWeight: "400"       # from .btn font-weight
    lineHeight: "1.5"
    letterSpacing: "0em"
  link:
    fontFamily: "-apple-system, BlinkMacSystemFont, Segoe UI, Roboto, sans-serif"
    fontSize: "1rem"        # from a
    fontWeight: "400"
    lineHeight: "1.5"
    letterSpacing: "0em"
  caption:
    fontFamily: "-apple-system, BlinkMacSystemFont, Segoe UI, Roboto, sans-serif"
    fontSize: "0.75rem"     # from .badge / small
    fontWeight: "400"
    lineHeight: "1.5"
    letterSpacing: "0em"
  mono:
    fontFamily: "SFMono-Regular, Menlo, Monaco, Consolas, Liberation Mono, Courier New, monospace"  # from --font-family-monospace
    fontSize: "0.875rem"
    fontWeight: "400"
    lineHeight: "1.5"
    letterSpacing: "0em"
rounded:
  none: "0px"               # from .btn square variant (most_common on some buttons)
  sm: "3.2px"               # from .2rem
  md: "4px"                 # from .25rem (Bootstrap default radius)
  lg: "4.8px"               # from .3rem
  xl: "16px"                # from 1rem (cards)
  full: "9999px"            # from 50rem (.rounded-pill / badge-pill)
spacing:
  xs: "4px"                 # from .25rem
  sm: "8px"                 # from .5rem
  md: "16px"                # from 1rem (Bootstrap base spacer)
  lg: "24px"                # from 1.5rem
  xl: "48px"                # from 3rem
preview_tokens:
  button_primary_bg: "#008080"
  button_primary_text: "#ffffff"
  button_primary_border: "#008080"
  button_secondary_bg: "transparent"
  button_secondary_text: "#0c797a"
  button_secondary_border: "#0c797a"
  button_tertiary_text: "#007bff"
  surface_bg: "#ffffff"
  card_bg: "#ffffff"
  text: "#212529"
  text_muted: "#6c757d"
  border: "#dee2e6"
  accent: "#ffbc00"
  button_radius: "4px"
  card_radius: "4px"
  input_radius: "4px"
components:
  button-primary:
    bg: "#008080"
    text: "#ffffff"
    border: "#008080"
    radius: "4px"
    padding: "10px 25px"
    font: "16px system-ui weight 400"
    hover_bg: "#0c797a"
  button-secondary:
    bg: "transparent"
    text: "#0c797a"
    border: "#0c797a"
    radius: "4px"
    padding: "10px 25px"
    font: "16px system-ui weight 400"
    hover_bg: "#0c797a"
  button-ghost:
    bg: "transparent"
    text: "#212529"
    border: "transparent"
    radius: "4px"
    padding: "8px 16px"
  card:
    bg: "#ffffff"
    border: "#dee2e6"
    radius: "4px"
    shadow: "0 0.125rem 0.25rem rgba(0,0,0,0.075)"
    padding: "20px"
  input-text:
    bg: "#ffffff"
    text: "#495057"
    border: "#ced4da"
    radius: "4px"
    padding: "6px 12px"
    focus_border: "#80bdff"
  badge-default:
    bg: "#008080"
    text: "#ffffff"
    border: "transparent"
    radius: "9999px"
    padding: "4px 8px"
    font: "12px system-ui weight 700"
  nav-header:
    bg: "#ffffff"
    text: "#212529"
    border_bottom: "#dee2e6"
    height: "56px"
---

# Vitrine MOOC Ifes — Design System ATUAL (baseline legado)

> **Este documento descreve o sistema que está sendo substituído.** Serve como inventário do
> ponto de partida — o que existe hoje, o que herdar e o que descartar na nova Vitrine. A
> referência-alvo de marca é o portal institucional do Ifes (ver `ifes-institucional/DESIGN.md`).

## 1. Visual Theme & Atmosphere

A Vitrine MOOC atual é um **tema WordPress construído sobre Bootstrap 4.2.1 quase sem customização estrutural**. O chassi de UI — grid, botões, cards, badges, formulários — é o Bootstrap de fábrica, com a paleta padrão (azul `#007bff`, cinzas neutros). A camada de marca própria é fina e aplicada por cima via CSS hardcoded do tema `vitrinemooctheme`: um **teal `#008080`/`#0c797a`** que aparece em destaques, títulos de seção e alguns CTAs, e um **dourado `#ffbc00`** usado pontualmente como acento.

O detector automático classificou o arquétipo como *apple-glass* (90%), mas isso é um **falso positivo**: a pontuação vem de overlays com `linear-gradient` sobre as imagens dos cards e de sombras suaves, não de glassmorphism real. Na prática o sistema é **flat, denso e utilitário** — a estética típica de um tema Bootstrap institucional de 2019. Não há `backdrop-filter`, não há escala de elevação intencional (as únicas `box-shadow` são os *focus rings* padrão do Bootstrap), e a tipografia usa a *system font stack* nativa (sem nenhuma fonte de marca carregada).

A página é **single-page**: toda a navegação acontece por âncoras (`#cursos`, `#como-funciona`, `#perguntas-frequentes`) dentro de um único documento. Os ícones vêm do FontAwesome 4.7 via CDN.

**Key Characteristics:**
- Chassi 100% Bootstrap 4.2.1 — grid, botões, cards e badges de fábrica.
- Cor de marca teal `#008080`/`#0c797a` aplicada por cima do azul Bootstrap.
- Dourado `#ffbc00` como acento pontual.
- Tipografia = *system font stack* (nenhuma fonte de marca carregada).
- Ícones via FontAwesome 4.7 (CDN).
- Design flat: sem elevação real, só *focus rings*.
- Radius padrão de 4px (`.25rem`); alguns botões quadrados (`0`).
- Cards com overlay `linear-gradient` escuro sobre a imagem.
- Arquitetura single-page com navegação por âncoras.
- Sem dark mode.

## 2. Color Palette & Roles

### Primary (marca)
- **Teal** (`#008080`): cor de identidade da Vitrine — títulos de seção, CTAs de marca, badges. Aparece 15× no CSS do tema.
- **Teal Escuro** (`#0c797a`): variante de hover/pressed e texto sobre fundo claro. Aparece 10×.

### Accent
- **Dourado** (`#ffbc00`): acento decorativo (selos, destaques). Família de amarelos claros de apoio: `#ffdf7e`, `#ffe8a1`, `#ffffdb`.

### UI / Interactive (chassi Bootstrap)
- **Azul Bootstrap** (`#007bff`): `--primary` de fábrica. É a cor default de links e de vários componentes — **é UI-affordance, não marca**. `#0069d9` (hover), `#0056b3` (active).
- Focus ring: `rgba(0,123,255,.25)` em `0 0 0 .2rem`.

### Neutral Scale
- **Texto** (`#212529`): `--gray-dark`, corpo. **Muted** (`#6c757d`): `--gray`, texto secundário.
- Cinzas de apoio: `#495057`, `#adb5bd`, `#ced4da`, `#dee2e6`, `#e9ecef`, `#f8f9fa`.

### Surface & Borders
- **Surface** (`#ffffff`): fundo padrão (usado 131× como `#fff`). **Border** (`#dee2e6`): divisor padrão (26×).
- Fundo alternado de seção: `#f8f9fa` (`--light`, 18×).

### Semantic
- **Success** `#28a745` · **Danger** `#dc3545` · **Warning** `#ffc107` · **Info** `#17a2b8` — todos Bootstrap de fábrica.

### Color Philosophy
A paleta é **Bootstrap de fábrica com uma fina camada de marca por cima**. O problema herdado: o azul `#007bff` domina a UI (links, componentes) por ser o default do framework, enquanto o teal da marca aparece de forma inconsistente. Na nova Vitrine, a cor de identidade deve ser **decidida deliberadamente** (alinhada ao verde institucional do Ifes) em vez de emergir do default do framework.

## 3. Typography Rules

### Font Family
- **Corpo/UI:** *system font stack* — `-apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif` (`--font-family-sans-serif`, Bootstrap default). **Nenhuma fonte de marca é carregada.**
- **Mono:** `SFMono-Regular, Menlo, Monaco, Consolas, monospace`.
- **Ícones:** FontAwesome 4.7 (`@font-face` único detectado).

### Hierarchy

| Role | Font | Size | Weight | Line Height | Notes |
|------|------|------|--------|-------------|-------|
| display-hero | system | 4.5rem (72px) | 300 | 1.2 | `.display-3` |
| display-large | system | 3.5rem (56px) | 300 | 1.2 | `.display-4` |
| section-heading | system | 2.5rem (40px) | 500 | 1.2 | h1 |
| subheading-large | system | 2rem (32px) | 500 | 1.2 | h2 |
| subheading | system | 1.75rem (28px) | 500 | 1.2 | h3 |
| body-large | system | 1.25rem (20px) | 300 | 1.5 | `.lead` |
| body | system | 1rem (16px) | 400 | 1.5 | base |
| body-small | system | 0.875rem (14px) | 400 | 1.5 | `small` |
| button | system | 1rem (16px) | 400 | 1.5 | `.btn` |
| link | system | 1rem (16px) | 400 | 1.5 | `a` |
| caption | system | 0.75rem (12px) | 400 | 1.5 | `.badge` |
| mono | SFMono | 0.875rem (14px) | 400 | 1.5 | `code` |

### Principles
- Escala tipográfica = Bootstrap 4 de fábrica (base 16px, `rem`-based).
- Display usa weight 300 (light) — herança do `.display-*` do Bootstrap.
- Não há OpenType features nem tracking customizado.
- **Débito:** ausência de fonte de marca torna o texto genérico; a nova Vitrine deve adotar a tipografia institucional do Ifes (Open Sans/Poppins/Oswald).

## 4. Components

### Buttons
**Primary Teal** (`button-primary`)
- Background: `#008080` · Text: `#ffffff` · Border: `#008080`
- Padding: 10px 25px · Radius: 4px · Font: 16px system weight 400 · Hover: `#0c797a`
- Uso: CTA principal ("Acessar curso", "Ver mais").

**Secondary Outline** (`button-secondary`)
- Background: transparent · Text: `#0c797a` · Border: `#0c797a` · Radius: 4px

**Ghost** (`button-ghost`) — texto puro `#212529`, sem borda. Alguns botões do tema são **quadrados** (`border-radius: 0`).

### Cards & Containers
**Card** (`card`) — bg `#ffffff`, border `#dee2e6`, radius 4px, shadow `0 0.125rem 0.25rem rgba(0,0,0,0.075)`, padding 20px. Cards de curso aplicam **overlay `linear-gradient(0deg, rgba(0,0,0,.7), rgba(0,0,0,.3) 70%, transparent)`** sobre a imagem para legibilidade do título.

### Inputs & Forms
**Input** (`input-text`) — bg `#ffffff`, text `#495057`, border `#ced4da`, radius 4px, padding 6px 12px, focus border `#80bdff` + ring `rgba(0,123,255,.25)`. (Bootstrap `.form-control` de fábrica.)

### Badges / Tags / Pills
**Badge** (`badge-default`) — bg `#008080`, text `#ffffff`, radius pill (`50rem`), padding 4px 8px, font 12px weight 700. Usado para categoria/Libras nos cards.

### Navigation
**Header** (`nav-header`) — bg `#ffffff`, border-bottom `#dee2e6`, altura ~56px, navbar Bootstrap com brand-logo à esquerda.

### Decorative Elements
- Overlay gradiente escuro nos cards de curso.
- Stripe pattern (`linear-gradient(45deg, ...)`) apenas nos progress bars do Bootstrap.

## 5. Layout Principles

### Spacing System
Base **Bootstrap spacer = 1rem (16px)**. Escala: 4, 8, 16, 24, 48px (`.25/.5/1/1.5/3 rem`). Utilitários `m-*`/`p-*` de fábrica.

### Grid & Container
Grid de 12 colunas do Bootstrap, `.container` com max-widths por breakpoint (540/720/960/1140px). Cursos exibidos em grade de cards responsiva.

### Whitespace Philosophy
Denso e utilitário — pouco respiro entre seções. Reflete a origem "tema institucional", priorizando densidade de informação sobre generosidade visual.

### Border Radius Scale
- `0` (botões quadrados) · `.2rem` (3.2px) · `.25rem` (4px, padrão) · `.3rem` (4.8px) · `1rem` (16px, cards especiais) · `50rem` (pills/badges).

## 6. Depth & Elevation

| Level | Treatment | Use |
|-------|-----------|-----|
| Flat | sem sombra | superfícies padrão, seções |
| Standard | `0 .125rem .25rem rgba(0,0,0,.075)` | cards |
| Ring (focus) | `0 0 0 .2rem rgba(0,123,255,.25)` | inputs/botões em foco |

### Shadow Philosophy
O sistema é **intencionalmente flat** (herança Bootstrap). Praticamente todas as `box-shadow` detectadas são *focus rings* de acessibilidade, não elevação. Profundidade é comunicada por borda + contraste de superfície. **Não adicionar** camadas de sombra ao replicar o legado.

## 7. Do's and Don'ts

**Do's**
- ✅ Use teal `#008080`/`#0c797a` para elementos de marca — é o que distingue a Vitrine do Bootstrap cru.
- ✅ Mantenha radius de 4px (`.25rem`) — é o padrão consistente do tema.
- ✅ Use badges pill para categoria e selo de Libras nos cards.

**Don'ts**
- ❌ Não trate o azul `#007bff` como cor de marca — é o default do Bootstrap (UI-affordance), não identidade.
- ❌ Não confie no arquétipo *apple-glass* detectado — não há glassmorphism real; o sistema é flat.
- ❌ Não adote a *system font stack* na nova Vitrine — a ausência de fonte de marca é um débito, não uma escolha.
- ❌ Não perpetue os botões quadrados (`border-radius: 0`) inconsistentes — padronize em 4px+.

## 8. Responsive Behavior

### Breakpoints

| Name | Width | Key Changes |
|------|-------|-------------|
| xs | <576px | 1 coluna, nav colapsada (hamburger) |
| sm | ≥576px | container 540px |
| md | ≥768px | grade de cards 2 col, container 720px |
| lg | ≥992px | grade 3 col, container 960px |
| xl | ≥1200px | grade 4 col, container 1140px |

### Touch Targets
Botões Bootstrap ~38px de altura (`.btn` padding `.375rem .75rem`) — abaixo do ideal de 44px para toque.

### Collapsing Strategy
Navbar → hamburger em <992px. Grade de cursos reduz colunas progressivamente. Tipografia não tem downscale explícito (usa `rem` fixo).

### Image Behavior
Imagens de curso em proporção fixa dentro do card, com overlay gradiente para o título.

## 9. Agent Prompt Guide

### Quick Color Reference
- Marca (primária): Teal (`#008080`)
- Marca (hover/escuro): Teal Escuro (`#0c797a`)
- Acento: Dourado (`#ffbc00`)
- UI/links (Bootstrap): Azul (`#007bff`)
- Texto: Cinza-escuro (`#212529`)
- Texto muted: Cinza (`#6c757d`)
- Superfície: Branco (`#ffffff`)
- Borda: Cinza-claro (`#dee2e6`)

### Example Component Prompts
> "Card de curso Bootstrap 4: imagem no topo com overlay `linear-gradient(0deg, rgba(0,0,0,.7), rgba(0,0,0,.3) 70%, transparent)`, título branco sobre a imagem, badge teal `#008080` pill para a categoria, corpo branco `#ffffff` com borda `#dee2e6`, radius 4px."

> "Botão primário: fundo `#008080`, texto branco, padding 10px 25px, radius 4px, hover `#0c797a`."

### Iteration Guide
1. Este é o sistema LEGADO — replique apenas para paridade/migração, não como alvo de design.
2. A cor de marca é teal `#008080`, não o azul Bootstrap.
3. Radius padrão é 4px; elimine os botões quadrados inconsistentes.
4. Não há fonte de marca — a nova Vitrine deve trazer Open Sans/Poppins do Ifes.
5. Mantenha o design flat; não invente elevação que o legado não tem.
