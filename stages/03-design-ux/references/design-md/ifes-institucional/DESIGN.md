---
name: Portal Institucional Ifes
source_url: https://www.ifes.edu.br/
extracted: 2026-07-06
stack: [Joomla, Bootstrap 2.x, template padraogoverno01, Open Sans, Poppins, Oswald, FontAwesome 3.2.1]
archetype: "polaris-friendly (detector 100%)"
note: "Referência de MARCA institucional para a nova Vitrine. Cor-âncora = verde Ifes."
colors:
  primary: "#147a02"        # from tema (verde institucional Ifes, hex_usage 11×)
  secondary: "#066017"      # from tema (verde escuro, hex_usage 14×)
  tertiary: "#195128"       # from tema (verde profundo, hex_usage 8×)
  neutral: "#555555"        # from body text muted (hex_usage 27×)
  surface: "#ffffff"        # from body background (222×)
  text: "#333333"           # from body color (hex_usage 41× como #333)
  text-muted: "#777777"     # from secondary text
  border: "#dddddd"         # from divisores (hex_usage 56× como #ddd)
  error: "#bd362f"          # from Bootstrap 2 danger
  success: "#51a351"        # from Bootstrap 2 success (verde)
  info: "#2f96b4"           # from Bootstrap 2 info
  warning: "#f89406"        # from Bootstrap 2 warning (laranja, 16×)
  link: "#0088cc"           # from Bootstrap 2 link (azul, 22×)
  green-material: "#4caf50" # from acento verde material
  green-deep: "#036355"     # from rgba(3,99,85,1) — verde-petróleo de apoio
typography:
  display-hero:
    fontFamily: "Oswald, Open Sans, sans-serif"    # from títulos condensados
    fontSize: "60px"        # from h1 hero
    fontWeight: "700"
    lineHeight: "1.1"
    letterSpacing: "0em"
  display-large:
    fontFamily: "Oswald, Open Sans, sans-serif"
    fontSize: "38.5px"      # from h1 (2.75em)
    fontWeight: "700"
    lineHeight: "1.2"
    letterSpacing: "0em"
  section-heading:
    fontFamily: "Poppins, Open Sans, sans-serif"   # from headings de destaque
    fontSize: "31.5px"      # from h2 (2.25em)
    fontWeight: "600"
    lineHeight: "1.2"
    letterSpacing: "0em"
  subheading-large:
    fontFamily: "Poppins, Open Sans, sans-serif"
    fontSize: "24.5px"      # from h3 (1.75em)
    fontWeight: "600"
    lineHeight: "1.3"
    letterSpacing: "0em"
  subheading:
    fontFamily: "Open Sans, sans-serif"
    fontSize: "17.5px"      # from h4 (1.25em)
    fontWeight: "700"
    lineHeight: "1.3"
    letterSpacing: "0em"
  body-large:
    fontFamily: "Open Sans, sans-serif"
    fontSize: "18px"        # from .lead
    fontWeight: "400"
    lineHeight: "1.5"
    letterSpacing: "0em"
  body:
    fontFamily: "Open Sans, sans-serif"             # from @font-face + body
    fontSize: "14px"        # from body base
    fontWeight: "400"
    lineHeight: "20px"
    letterSpacing: "0em"
  body-small:
    fontFamily: "Open Sans, sans-serif"
    fontSize: "12px"        # from small
    fontWeight: "400"
    lineHeight: "18px"
    letterSpacing: "0em"
  button:
    fontFamily: "Open Sans, sans-serif"
    fontSize: "14px"        # from .btn
    fontWeight: "600"
    lineHeight: "20px"
    letterSpacing: "0em"
  link:
    fontFamily: "Open Sans, sans-serif"
    fontSize: "14px"        # from a
    fontWeight: "400"
    lineHeight: "20px"
    letterSpacing: "0em"
  caption:
    fontFamily: "Open Sans, sans-serif"
    fontSize: "11px"        # from caption / labels
    fontWeight: "400"
    lineHeight: "14px"
    letterSpacing: "0em"
  overline:
    fontFamily: "Oswald, sans-serif"                # from tags/kickers condensados
    fontSize: "13px"
    fontWeight: "500"
    lineHeight: "1.25"
    letterSpacing: "0.05em"
  mono:
    fontFamily: "Menlo, Monaco, Consolas, Courier New, monospace"
    fontSize: "13px"
    fontWeight: "400"
    lineHeight: "1.4"
    letterSpacing: "0em"
rounded:
  none: "0px"
  sm: "3px"                 # from botões/inputs
  md: "4px"                 # from cards/botões (mais comum)
  lg: "6px"                 # from painéis
  xl: "14px"                # from botões pill assimétricos / destaques
  full: "500px"             # from .btn-round / avatares
spacing:
  xs: "4px"
  sm: "8px"
  md: "15px"                # base comum do template
  lg: "20px"
  xl: "60px"                # from seções hero
preview_tokens:
  button_primary_bg: "#147a02"
  button_primary_text: "#ffffff"
  button_primary_border: "#147a02"
  button_secondary_bg: "transparent"
  button_secondary_text: "#147a02"
  button_secondary_border: "#147a02"
  button_tertiary_text: "#0088cc"
  surface_bg: "#ffffff"
  card_bg: "#ffffff"
  text: "#333333"
  text_muted: "#777777"
  border: "#dddddd"
  accent: "#f89406"
  button_radius: "4px"
  card_radius: "6px"
  input_radius: "4px"
components:
  button-primary:
    bg: "#147a02"
    text: "#ffffff"
    border: "#147a02"
    radius: "4px"
    padding: "8px 14px"
    font: "14px Open Sans weight 600"
    hover_bg: "#066017"
  button-secondary:
    bg: "transparent"
    text: "#147a02"
    border: "#147a02"
    radius: "4px"
    padding: "8px 14px"
    font: "14px Open Sans weight 600"
    hover_bg: "#dff0d8"
  button-search:
    bg: "#147a02"
    text: "#ffffff"
    border: "transparent"
    radius: "0px 14px 14px 0px"
    padding: "8px 14px"
  card:
    bg: "#ffffff"
    border: "#dddddd"
    radius: "6px"
    shadow: "0 1px 3px rgba(0,0,0,0.1)"
    padding: "20px"
  input-text:
    bg: "#ffffff"
    text: "#333333"
    border: "#cccccc"
    radius: "4px"
    padding: "8px 14px"
    focus_border: "#147a02"
  badge-default:
    bg: "#147a02"
    text: "#ffffff"
    border: "transparent"
    radius: "3px"
    padding: "2px 10px"
    font: "11px Open Sans weight 600"
  nav-header:
    bg: "#ffffff"
    text: "#333333"
    border_bottom: "#dddddd"
    height: "60px"
---

# Portal Institucional Ifes — Design System (referência de marca)

> **Documento de referência de MARCA** para a nova Vitrine MOOC. A âncora de identidade do
> Ifes é o **verde institucional**. A tipografia institucional é **Open Sans + Poppins + Oswald**.
> Nota: o portal roda numa base legada (Joomla + Bootstrap 2 + template governo), então o
> vocabulário de cor está poluído por defaults de framework — extraia a INTENÇÃO de marca,
> não cada hex legado.

## 1. Visual Theme & Atmosphere

O portal do Ifes é um **site institucional de governo** construído em Joomla com o template `padraogoverno01` sobre Bootstrap 2.x. A identidade é ancorada no **verde institucional do Ifes** — detectado em múltiplos tons de verde (`#147a02`, `#066017`, `#195128`, `#117a45`, `#036355`) usados em cabeçalhos, botões primários, links de navegação e faixas de marca. O verde é a assinatura visual da instituição e deve ser o ponto de partida cromático da nova Vitrine.

A tipografia é o ativo de marca mais forte e transferível: **três famílias carregadas via `@font-face`** — **Open Sans** (corpo, pesos 400/600/700/800), **Poppins** (títulos de destaque, geométrica e amigável) e **Oswald** (condensada, para kickers/hero de alto impacto). Essa combinação é característica de portais educacionais brasileiros e alinha-se ao legado do padrão gov.br (que historicamente usa Open Sans). Ícones vêm de FontAwesome 3.2.1 + simple-line-icons.

Visualmente é **denso, informativo e conservador** — arquétipo *polaris-friendly* (100%), coerente com o objetivo de serviço público: muita informação, hierarquia clara, superfícies claras (branco dominante), acentos de cor funcionais. Há um **débito importante herdado**: por rodar sobre Bootstrap 2, o CSS acumulou centenas de cores legadas (azuis `#0088cc`, laranjas `#f89406`, vermelhos `#bd362f` de fábrica) que **não fazem parte da marca** e devem ser ignoradas na destilação.

**Key Characteristics:**
- Verde institucional `#147a02`/`#066017` como assinatura de marca.
- Tipografia de marca: **Open Sans** (corpo) + **Poppins** (destaque) + **Oswald** (condensada).
- Superfície branca dominante, estética de serviço público.
- Denso e informativo (arquétipo *polaris-friendly*).
- Acentos funcionais: laranja `#f89406` (avisos), azul `#0088cc` (links legados).
- Radius moderado (4–6px), alguns botões com cantos assimétricos (busca: `0 14px 14px 0`).
- Ícones FontAwesome 3.2.1 + simple-line-icons.
- **Débito:** vocabulário de cor poluído por defaults de Bootstrap 2 (extrair só a marca).
- Base legada Joomla — sem design tokens (CSS vars = 0).

## 2. Color Palette & Roles

### Primary (verde institucional Ifes)
- **Verde Ifes** (`#147a02`): cor de marca — botões primários, cabeçalhos, navegação ativa. Uso 11×.
- **Verde Escuro** (`#066017`): variante de hover/faixas de marca. Uso 14×.
- **Verde Profundo** (`#195128`): fundos de marca imersivos, rodapé. Uso 8×.
- **Verde-petróleo** (`#036355`, de `rgba(3,99,85,1)`): apoio.
- **Verde Material** (`#4caf50`): acento verde mais claro/vivo, estados de sucesso.

### Neutral Scale
- **Texto** (`#333333`): corpo (41× como `#333`). **Muted** (`#777777`/`#999999`): secundário.
- Cinzas: `#555`, `#666`, `#999`, `#ccc`, `#ddd`, `#eee`, `#f2f2f2`, `#fafafa`.

### Surface & Borders
- **Surface** (`#ffffff`): fundo (branco domina — 222+98 usos). **Border** (`#dddddd`): divisor padrão (56×).
- Fundos alternados: `#eeeff2` (24×), `#fafafa` (24×), `#f5f5f5` (14×).

### Interactive / Semantic (Bootstrap 2 legado — usar com parcimônia)
- **Link** `#0088cc` (azul legado, 22×) · **Success** `#51a351` (verde) · **Info** `#2f96b4` · **Warning** `#f89406` (laranja, 16×) · **Error** `#bd362f`.

### Color Philosophy
A identidade real do Ifes é **verde sobre branco** — sóbria, institucional, legível. O ruído de cor (dezenas de azuis/laranjas/vermelhos) é **entulho técnico do Bootstrap 2**, não decisão de marca. A destilação para a nova Vitrine deve: (1) fixar o verde `#147a02`/`#066017` como primária; (2) manter neutros limpos; (3) reservar acentos (laranja/azul) para papéis semânticos específicos, não para cor de marca.

## 3. Typography Rules

### Font Family
- **Corpo/UI:** **Open Sans** (`@font-face`, pesos 400/600/700/800 + itálico) — a fonte de leitura institucional.
- **Títulos de destaque:** **Poppins** (geométrica, carregada de `images/font/poppins.ttf`).
- **Kickers/Hero condensado:** **Oswald** (condensada, `images/font/oswald.ttf`).
- **Ícones:** FontAwesome 3.2.1 + simple-line-icons.

### Hierarchy

| Role | Font | Size | Weight | Line Height | Notes |
|------|------|------|--------|-------------|-------|
| display-hero | Oswald | 60px | 700 | 1.1 | hero condensado |
| display-large | Oswald | 38.5px | 700 | 1.2 | h1 (2.75em) |
| section-heading | Poppins | 31.5px | 600 | 1.2 | h2 |
| subheading-large | Poppins | 24.5px | 600 | 1.3 | h3 |
| subheading | Open Sans | 17.5px | 700 | 1.3 | h4 |
| body-large | Open Sans | 18px | 400 | 1.5 | `.lead` |
| body | Open Sans | 14px | 400 | 20px | base |
| body-small | Open Sans | 12px | 400 | 18px | `small` |
| button | Open Sans | 14px | 600 | 20px | `.btn` |
| link | Open Sans | 14px | 400 | 20px | `a` |
| caption | Open Sans | 11px | 400 | 14px | labels |
| overline | Oswald | 13px | 500 | 1.25 | kicker/tags (tracking +0.05em) |
| mono | Menlo/monospace | 13px | 400 | 1.4 | código |

### Principles
- **Open Sans** é a base de leitura — corpo a 14px, generoso em pesos.
- **Poppins** para títulos de seção — dá calor e modernidade sem perder formalidade.
- **Oswald** para hero/kickers de impacto — condensada, comunica "campanha institucional".
- Base tipográfica menor (14px corpo) — típica de portais densos; a nova Vitrine deve **subir o corpo para 16px** para leitura de descoberta pública.

## 4. Components

### Buttons
**Primary Verde** (`button-primary`)
- Background: `#147a02` · Text: `#ffffff` · Border: `#147a02`
- Padding: 8px 14px · Radius: 4px · Font: 14px Open Sans weight 600 · Hover: `#066017`
- Uso: ação institucional primária.

**Secondary Outline** (`button-secondary`) — transparent, text `#147a02`, border `#147a02`, hover bg `#dff0d8` (verde claro).

**Search** (`button-search`) — verde `#147a02`, **radius assimétrico `0 14px 14px 0`** (encaixa no campo de busca à esquerda). Padrão característico do template.

### Cards & Containers
**Card** (`card`) — bg `#ffffff`, border `#dddddd`, radius 6px, shadow `0 1px 3px rgba(0,0,0,0.1)`, padding 20px.

### Inputs & Forms
**Input** (`input-text`) — bg `#ffffff`, text `#333333`, border `#cccccc`, radius 4px, padding 8px 14px, **focus border verde `#147a02`**.

### Badges / Tags / Pills
**Badge** (`badge-default`) — bg verde `#147a02`, text branco, radius 3px, padding 2px 10px, font 11px Open Sans weight 600.

### Navigation
**Header** (`nav-header`) — bg `#ffffff`, border-bottom `#dddddd`, altura ~60px, com logo do Ifes à esquerda e barra de acessibilidade (padrão governo) no topo.

### Decorative Elements
- Faixas verdes de marca em cabeçalhos de seção.
- Barra de acessibilidade governamental (contraste, tamanho de fonte) no topo.

## 5. Layout Principles

### Spacing System
Base irregular herdada de Bootstrap 2 (`15px` container gutter comum). Escala prática: 4, 8, 15, 20, 60px. A nova Vitrine deve **normalizar para uma escala de 8px**.

### Grid & Container
Grid Bootstrap 2 de 12 colunas (`.row`/`.span*`), container ~940–1170px. Layout multi-coluna denso com sidebars.

### Whitespace Philosophy
Conservador e denso — prioriza densidade informacional (serviço público). A nova Vitrine, voltada à descoberta pública, deve ser mais generosa em respiro.

### Border Radius Scale
- `0` · `3px` · `4px` (padrão) · `6px` (painéis) · `14px`/assimétricos (busca) · `500px` (round/avatares).

## 6. Depth & Elevation

| Level | Treatment | Use |
|-------|-----------|-----|
| Flat | sem sombra | superfícies, faixas de marca |
| Standard | `0 1px 3px rgba(0,0,0,0.1)` | cards, dropdowns |
| Ambient | `0 0 8px rgba(0,0,0,0.15)` | modais, menus |
| Ring (focus) | `rgba(0,105,214,0.25)` (legado) | inputs em foco |

### Shadow Philosophy
Elevação baixa e funcional — sombras leves para separar cards e menus do fundo branco, sem dramatização. Coerente com a sobriedade institucional. A nova Vitrine deve **substituir o ring de foco azul legado por verde** para alinhar à marca.

## 7. Do's and Don'ts

**Do's**
- ✅ Use verde `#147a02`/`#066017` como cor de marca — é a identidade do Ifes.
- ✅ Use **Open Sans** para corpo, **Poppins** para títulos de seção, **Oswald** para hero/kickers.
- ✅ Mantenha superfície branca dominante e neutros limpos.
- ✅ Pinte o foco de formulário de verde `#147a02` (não o azul legado).

**Don'ts**
- ❌ Não trate os azuis `#0088cc`/laranjas `#f89406`/vermelhos `#bd362f` como cores de marca — são defaults de Bootstrap 2 (entulho legado).
- ❌ Não use corpo a 14px na nova Vitrine — suba para 16px para leitura de descoberta pública.
- ❌ Não replique o vocabulário de cor poluído — destile só o verde + neutros + acentos semânticos.
- ❌ Não misture Poppins e Oswald no mesmo bloco de título — Oswald é para kicker/hero, Poppins para seções.

## 8. Responsive Behavior

### Breakpoints

| Name | Width | Key Changes |
|------|-------|-------------|
| phone | <768px | 1 coluna, menu colapsado, barra de acessibilidade compacta |
| tablet | ≥768px | 2 colunas, sidebar abaixo do conteúdo |
| desktop | ≥980px | layout multi-coluna com sidebar |
| wide | ≥1200px | container largo |

### Touch Targets
Botões ~34px (14px + padding 8px) — abaixo de 44px; a nova Vitrine deve ampliar.

### Collapsing Strategy
Menu → dropdown/accordion em mobile. Barra de acessibilidade governamental permanece.

### Image Behavior
Banners e cards de notícia em proporção fixa; imagens fluidas dentro do grid Bootstrap.

## 9. Agent Prompt Guide

### Quick Color Reference
- Marca (primária): Verde Ifes (`#147a02`)
- Marca (hover/escuro): Verde Escuro (`#066017`)
- Marca (profundo): Verde `#195128`
- Texto: Cinza-escuro (`#333333`)
- Texto muted: Cinza (`#777777`)
- Superfície: Branco (`#ffffff`)
- Borda: Cinza-claro (`#dddddd`)
- Acento (aviso): Laranja (`#f89406`)
- Link (legado): Azul (`#0088cc`)

### Example Component Prompts
> "Header institucional Ifes: fundo branco, logo do Ifes à esquerda, navegação em Open Sans 14px weight 600, item ativo em verde `#147a02`, borda inferior `#dddddd`, barra de acessibilidade no topo."

> "Botão primário: fundo verde `#147a02`, texto branco, Open Sans 14px weight 600, padding 8px 14px, radius 4px, hover `#066017`."

> "Título de seção em Poppins 31.5px weight 600, cor `#333333`; kicker acima em Oswald 13px weight 500 uppercase, tracking +0.05em, cor verde `#147a02`."

### Iteration Guide
1. Verde `#147a02`/`#066017` é a espinha cromática — toda decisão de marca parte dele.
2. Tipografia: Open Sans (corpo), Poppins (seções), Oswald (hero/kicker) — não improvise fontes.
3. Ignore o entulho de Bootstrap 2 (azuis/laranjas/vermelhos legados) — não é marca.
4. Foco de formulário em verde, não azul.
5. Suba o corpo de 14px → 16px e normalize spacing para escala de 8px na nova Vitrine.
6. Superfície branca dominante + neutros limpos + verde como âncora = identidade Ifes.
