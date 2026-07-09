---
version: "alpha"
name: "Cursos Abertos do Ifes"
description: "Design system canonico da vitrine de cursos abertos do Ifes, consolidando a paleta institucional sobria #008080 e as decisoes ja aplicadas em index.html e cursos.html."
colors:
  primary: "#008080"
  primary-dark: "#005F5F"
  primary-deep: "#003F3F"
  primary-light: "#33A6A6"
  primary-soft: "#D9F2F2"
  navy: "#1D3557"
  sky: "#A8DADC"
  sage: "#7A9E7E"
  olive-soft: "#CDE7B0"
  action: "#A85B50"
  action-hover: "#87483F"
  terracotta: "#C96C4A"
  amber: "#F2B84B"
  sand: "#F4EFE6"
  lavender: "#6C63FF"
  plum: "#8E5572"
  rose-soft: "#F7D6E0"
  background: "#F7FAFA"
  background-alt: "#EEF6F6"
  surface: "#FFFFFF"
  text: "#172424"
  text-muted: "#5F7474"
  border: "#D8E6E6"
  ifes-green: "#147A02"
  success-deep: "#195128"
  danger: "#D43B35"
  on-primary: "#FFFFFF"
  on-action: "#FFFFFF"
  on-amber: "#172424"
typography:
  display-hero:
    fontFamily: "Nunito Sans, Open Sans, Arial, sans-serif"
    fontSize: "clamp(2.45rem, 5vw, 4.35rem)"
    fontWeight: 800
    lineHeight: 1.1
    letterSpacing: "0"
  display-section:
    fontFamily: "Nunito Sans, Open Sans, Arial, sans-serif"
    fontSize: "clamp(1.6rem, 3vw, 2.35rem)"
    fontWeight: 800
    lineHeight: 1.1
    letterSpacing: "0"
  heading-card:
    fontFamily: "Nunito Sans, Open Sans, Arial, sans-serif"
    fontSize: "1.02rem"
    fontWeight: 700
    lineHeight: 1.28
    letterSpacing: "0"
  body:
    fontFamily: "Open Sans, Arial, sans-serif"
    fontSize: "1rem"
    fontWeight: 400
    lineHeight: 1.55
    letterSpacing: "0"
  lead:
    fontFamily: "Open Sans, Arial, sans-serif"
    fontSize: "clamp(1rem, 1.35vw, 1.22rem)"
    fontWeight: 400
    lineHeight: 1.55
    letterSpacing: "0"
  ui-action:
    fontFamily: "Open Sans, Arial, sans-serif"
    fontSize: ".95rem"
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: "0"
  ui-strong:
    fontFamily: "Open Sans, Arial, sans-serif"
    fontSize: ".86rem"
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: "0"
  badge:
    fontFamily: "Open Sans, Arial, sans-serif"
    fontSize: ".65rem"
    fontWeight: 700
    lineHeight: 1
    letterSpacing: "0"
rounded:
  xs: "4px"
  sm: "6px"
  md: "8px"
  lg: "18px"
  xl: "28px"
  pill: "999px"
spacing:
  xs: "6px"
  sm: "8px"
  md: "16px"
  lg: "24px"
  xl: "32px"
  section: "64px"
  container: "1180px"
components:
  button-primary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.ui-action}"
    rounded: "{rounded.md}"
    height: "44px"
    padding: "0 18px"
  button-action:
    backgroundColor: "{colors.action}"
    textColor: "{colors.on-action}"
    typography: "{typography.ui-action}"
    rounded: "{rounded.md}"
    height: "44px"
    padding: "0 18px"
  button-outline:
    backgroundColor: "rgba(255, 255, 255, .76)"
    textColor: "{colors.primary-deep}"
    typography: "{typography.ui-action}"
    rounded: "{rounded.md}"
    height: "44px"
    padding: "0 18px"
  button-amber:
    backgroundColor: "{colors.amber}"
    textColor: "{colors.on-amber}"
    typography: "{typography.ui-action}"
    rounded: "{rounded.md}"
    height: "44px"
    padding: "0 18px"
  card-course:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.text}"
    typography: "{typography.body}"
    rounded: "{rounded.md}"
    padding: "18px"
  area-pill:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.primary-deep}"
    typography: "{typography.ui-action}"
    rounded: "{rounded.md}"
    height: "42px"
    padding: "0 16px"
  chip:
    backgroundColor: "{colors.primary-soft}"
    textColor: "{colors.primary-deep}"
    typography: "{typography.ui-action}"
    rounded: "{rounded.md}"
    padding: "7px 10px"
  catalog-hero:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.lead}"
    rounded: "0"
    padding: "44px 0 38px"
  input:
    backgroundColor: "{colors.background}"
    textColor: "{colors.text}"
    typography: "{typography.body}"
    rounded: "{rounded.md}"
    padding: "11px 12px"
---

## Overview

Este arquivo e a fonte canonica para novas telas da plataforma **Cursos Abertos do Ifes**. Ele consolida tres origens: a paleta `paleta_site_008080_institucional_sobria.html`, as decisoes ja implementadas em `stages/03-design-ux/output/canonico/index.html` e as necessidades do catalogo em `stages/03-design-ux/output/canonico/cursos.html`.

A atmosfera deve ser institucional, clara e acolhedora. A interface precisa parecer de um portal publico confiavel, mas sem rigidez pesada: muito espaco de leitura, cards objetivos, filtros eficientes, chamadas de acao serenas e tipografia com peso moderado. O teal `#008080` sustenta a identidade; o cobre `#A85B50` e o acento de conversao; o verde Ifes aparece como marca institucional, nao como cor dominante da interface.

As paginas oficiais do prototipo sao `index.html` e `cursos.html`. Nao manter pagina singular `curso.html` neste pacote canonico.

## Colors

Use o teal como eixo de marca:

- **Teal principal** `#008080`: links importantes, botoes primarios, indicadores ativos, elementos de identidade.
- **Teal escuro** `#005F5F`: hover de botoes primarios, estados ativos, menus em superficies claras.
- **Teal profundo** `#003F3F`: footer, hero escuro, titulos institucionais quando houver muito contraste.
- **Teal claro** `#33A6A6`: icones, detalhes, linhas editoriais e pequenos destaques.
- **Teal suave** `#D9F2F2`: chips, fundos informativos, estados neutros e areas de apoio.

Use acentos com parcimonia:

- **Cobre sobrio** `#A85B50`: CTA de descoberta, especialmente "Explorar cursos"; tambem pode marcar a acao principal em secoes editoriais.
- **Cobre profundo** `#87483F`: hover do cobre. Deve escurecer sem virar vermelho vivo.
- **Terracota** `#C96C4A`: apoio quente para ilustracoes, graficos e pequenos detalhes, nao para competir com CTA.
- **Ambar** `#F2B84B`: avisos, selos "novo", pontos de atencao e botoes secundarios especiais.

Use cores de apoio por funcao:

- **Azul-noite** `#1D3557`: autoridade, dados, areas escuras alternativas e graficos.
- **Salvia** `#7A9E7E` e **verde suave** `#CDE7B0`: conteudo humano, saude, natureza e sucesso.
- **Areia** `#F4EFE6`: respiro editorial quando a pagina precisar fugir do branco frio.
- **Lavanda** `#6C63FF`, **ameixa** `#8E5572` e **rosa suave** `#F7D6E0`: tecnologia, diversidade visual e graficos. Nao usar lavanda como CTA principal.

Neutros oficiais:

- **Fundo principal** `#F7FAFA`
- **Fundo alternativo** `#EEF6F6`
- **Superficie** `#FFFFFF`
- **Texto principal** `#172424`
- **Texto secundario** `#5F7474`
- **Borda** `#D8E6E6`

## Typography

A tipografia oficial do prototipo e **Nunito Sans** para display e **Open Sans** para texto, navegacao, formularios e botoes.

Use pesos mais leves do que a primeira versao do prototipo:

- Titulos hero: `Nunito Sans`, peso `800`, escala `clamp(2.45rem, 5vw, 4.35rem)`, linha `1.1`.
- Titulos de secao: `Nunito Sans`, peso `800`, escala `clamp(1.6rem, 3vw, 2.35rem)`.
- Titulos de cards: `Nunito Sans`, peso `700`, corpo aproximado de `1.02rem`.
- Corpo de texto: `Open Sans`, peso `400`, `16px`, linha `1.55`.
- Texto de apoio e metadados: `Open Sans`, pesos `400` ou `600`, nunca ultra-bold.
- Botoes, filtros, chips e pills: `Open Sans`, peso `600`. Reserve `700` para links editoriais, selos pequenos e informacoes de maior hierarquia.

Nao usar pesos `900` ou fontes condensadas no produto. A sensacao desejada e legivel, leve e publica, nao promocional ou agressiva.

## Layout

O container base e `min(1180px, calc(100% - 40px))`. Em mobile, reduza para `calc(100% - 28px)`.

As paginas usam uma arquitetura simples:

- `index.html`: topbar, header sticky, hero com imagem real, faixa de indicadores, cards de cursos, ranking, recentes, publicos, nuvem de areas, faixa de licenca-capacitacao, explicacao do fluxo, FAQ e footer.
- `cursos.html`: hero compacto de catalogo em teal principal `#008080`, resumo numerico, painel de filtros, busca, ordenacao, chips ativos, grid de resultados, estado vazio e botao de carregar mais.

O catalogo deve priorizar eficiencia: filtros legiveis, area de resultados ampla e cards consistentes. Em desktop, use coluna lateral para filtros; abaixo de `1060px`, filtros deixam de ser sticky e ocupam largura total.

Em telas menores que `640px`, todas as grids viram uma coluna. Botoes principais no hero podem ocupar largura total limitada a `330px`.

## Elevation & Depth

Use sombras apenas para separar superficies funcionais. A sombra principal e `0 22px 60px rgba(0, 63, 63, .12)` quando houver destaque real. Para cards comuns, use sombra mais baixa, proxima de `0 10px 28px rgba(0, 63, 63, .08)`.

Nao usar brilho neon, sombra colorida saturada ou profundidade decorativa sem funcao. O relevo deve parecer institucional e calmo.

## Shapes

O raio canonico para a interface operacional e `8px`. Ele aparece em botoes, cards de curso, filtros, chips, pills, accordions e paineis.

Use raios maiores apenas quando a composicao pedir:

- `18px`: blocos de demonstracao, previews e paineis mais editoriais.
- `28px`: pecas de apresentacao da paleta ou artefatos de design system, nao como regra geral do site.
- `999px`: apenas para elementos explicitamente circulares ou pills muito pequenas.

Cards nao devem ser colocados dentro de outros cards. Secoes de pagina sao bandas ou layouts abertos; cards sao reservados para itens repetidos, filtros, paineis e conteudo enquadrado.

## Components

**Header**

Topbar escura em teal profundo, seguida por header sticky com fundo translúcido claro e borda inferior sutil. A marca usa o verde Ifes `#147A02` no marcador institucional, mantendo o resto da navegacao no teal.

**Buttons**

Botoes tem altura minima de `44px`, raio `8px`, peso `600` e feedback de `translateY(-1px)` no hover. O texto deve caber sem quebrar de forma estranha.

- Primario: teal `#008080`, hover `#005F5F`.
- Acao principal de descoberta: cobre `#A85B50`, hover `#87483F`.
- Outline: superficie branca translúcida, texto teal profundo, borda teal suave.
- Ambar: apenas para acoes editoriais especiais, como planejamento ou destaque.

**Hero Home**

Hero com imagem real em full-bleed de fundo, overlay claro e conteudo centralizado. O CTA "Explorar cursos" usa cobre. "Como funciona" usa outline. A nota flutuante lateral pode existir em desktop, mas desaparece no mobile para preservar leitura.

**Stats Strip**

Faixa de indicadores em teal medio/escuro, texto branco, numeros em `Nunito Sans` grande. Deve funcionar como transicao entre hero e conteudo, nao como bloco solto.

**Catalog Hero**

Cabecalho da pagina `cursos.html` usa a cor principal da marca: teal `#008080`, com gradiente discreto para o teal escuro `#005F5F`. Textos devem ficar brancos ou em teal muito claro para manter contraste. Os cards de resumo dentro do cabecalho usam superficie branca translucida, borda teal leve e sombra baixa.

**Course Card**

Card branco, raio `8px`, imagem em proporcao fixa, categoria em teal, titulo escuro, metadados pequenos e botao compacto "Acessar curso". Hover levanta no maximo `3px`. A imagem so recebe o ribbon de Libras no canto superior direito. Os demais selos ficam no rodape do card, ao lado do botao: `NOVO`, projeto, serie (`Série`) e idioma (bandeira da Gra-Bretanha para ingles, bandeira da Espanha para espanhol). Portugues e padrao implicito e nao recebe selo. Selos de projeto e serie usam fundo neutro esverdeado, texto teal e borda sutil; nao usar vermelho nesses selos. O selo `NOVO` usa ambar claro discreto (`#fbefdc`), texto marrom suave (`#7a5416`) e borda baixa (`#ecd3a8`).

**Area Pill**

Pill retangular leve com raio `8px`, fundo branco, borda teal suave, texto `Open Sans 600`. O numero da area usa texto secundario e peso `600`, para nao ficar bruto.

**Catalog Filters**

Painel branco com sombra suave, busca e selects em fundo `#F7FAFA`. Labels de grupos usam `Open Sans 700` pequeno. Checkboxes usam `accent-color: #008080`.

**Active Chips**

Chips em teal suave, texto teal profundo, peso `600`. Eles sao ferramentas de remocao de filtro, entao devem parecer clicaveis sem virar CTA.

**FAQ**

`details/summary` com fundo branco, raio `8px`, sombra suave e titulo teal profundo. Conteudo interno em texto secundario.

**Footer**

Fundo teal profundo, texto branco ou teal muito claro. Links sublinham apenas no hover.

## Do's and Don'ts

Do:

- Usar `design-system/design.md` como fonte de verdade antes de criar ou alterar telas.
- Manter `index.html` e `cursos.html` visualmente irmaos: mesmos tokens, pesos, radius e comportamento responsivo.
- Preservar acentuacao correta em portugues brasileiro.
- Usar imagens reais de cursos ou do contexto institucional sempre que o usuario precisar reconhecer o conteudo.
- Priorizar leitura, busca e tomada de decisao rapida.
- Manter o padrao canonico de selos: Libras na imagem; demais selos no rodape do card, ao lado do botao.

Don't:

- Nao recriar `curso.html` neste prototipo canonico.
- Nao usar vermelho vivo como CTA principal de descoberta.
- Nao usar amarelo saturado `#ffbc00` como botao principal; o ambar oficial e `#F2B84B` e deve ser secundario.
- Nao usar pesos tipograficos muito brutos em botoes, pills, filtros ou cards.
- Nao transformar o site em landing page generica com excesso de cards, gradientes, blobs ou textos promocionais.
- Nao usar roxo/lavanda como linguagem dominante da plataforma; ele e apoio para tecnologia e graficos.
- Nao usar `Inter` como fonte principal do prototipo, mesmo que esteja presente na pagina de estudo de paleta.
- Nao colocar selos de projeto, serie, novidade ou idioma sobre a imagem do curso.
