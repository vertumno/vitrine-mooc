# Especificação de Design — Vitrine MOOC Ifes

> **Estágio:** 03 — Design/UX · **Versão:** 1.0 · **Data:** 06/07/2026
> **Base:** `design-system/palette.md` + `design-system/typography.md` (destilados via skill `design-md`)
> · `stages/02-catalogo/output/arquitetura-informacao.md` v4.1 (taxonomia/navegação)
> · `stages/02-catalogo/output/powerbi-mooc-ifes/analise-insights-powerbi-mooc-ifes.md` (demanda)
> **Companheiro:** `mapa-paginas.md` (páginas, seções e dados exibidos).
> **Protótipos de referência:** `stages/03-design-ux/output/prototipo-vitrine-mooc/` (HTML navegável).

Este documento especifica os **tokens**, **componentes**, **estados** e **regras** da nova Vitrine.
Objetivo (Resolução CS 72/2020): plataforma de **cursos abertos à comunidade** — público **leigo,
nacional, de descoberta**. A UI fala a língua do cidadão comum e favorece **achar + concluir + ser
indexável** (SEO/GEO/AEO).

---

## 1. Tokens (resumo canônico)

Fonte da verdade: `design-system/`. Reproduzidos aqui para uso direto no tema.

### Cores

| Token | Valor | Papel |
|-------|-------|-------|
| `--cor-primaria` | `#147a02` | Verde Ifes — marca, botões, header ativo, foco |
| `--cor-primaria-escura` | `#066017` | Hover/pressed, faixas |
| `--cor-primaria-profunda` | `#195128` | Rodapé, seções imersivas |
| `--cor-secundaria` | `#008080` | Teal — apoio, chips de categoria |
| `--cor-acento` | `#ffbc00` | Dourado — CTA/destaque (texto escuro por cima) |
| `--cor-texto` | `#212529` | Corpo e títulos |
| `--cor-texto-suave` | `#6c757d` | Metadados, secundário |
| `--cor-fundo` | `#ffffff` | Superfície |
| `--cor-fundo-alt` | `#f8f9fa` | Seção alternada, card sutil |
| `--cor-borda` | `#dee2e6` | Divisores, borda de card |
| `--cor-sucesso` / `--cor-alerta` / `--cor-erro` / `--cor-info` | `#2e9e4f` / `#f0a000` / `#dc3545` / `#0d6efd` | Estados |

### Tipografia

- **Títulos:** Poppins (600). **Corpo:** Open Sans (400/600/700). **Hero/kicker:** Oswald (500/700, uppercase).
- Escala: hero 48 · h1 40 · h2 32 · h3 24 · h4 20 · lead 18 · **corpo 16** · corpo-peq 14 · legenda 12 (px).
- `line-height`: 1.5 corpo, 1.2 títulos.

### Espaçamento e raio

- **Spacing (base 8px):** 4 · 8 · 16 · 24 · 32 · 48 · 64.
- **Radius:** `--raio-sm` 4px · `--raio-md` 8px · `--raio-lg` 12px · `--raio-pill` 9999px.
- **Elevação:** `--sombra-card` `0 1px 3px rgba(0,0,0,.1)` · `--sombra-hover` `0 6px 16px rgba(0,0,0,.12)` · foco = anel **dourado** `0 0 0 3px rgba(255,188,0,.6)` (`--cor-acento`, alto contraste universal — padrão gov.br; verde não contrastaria sobre botões verdes).

---

## 2. Componentes

Para cada componente: anatomia, tokens, estados. Hex sempre literal.

### 2.1 Card de curso (componente central)

O card é a unidade de descoberta. Exibe o metadado mínimo do curso (ver `mapa-paginas.md §dados`).

**Anatomia (topo → base):**
1. **Imagem** (16:9) com `object-fit: cover`; fallback = bloco `--cor-fundo-alt` com ícone.
2. **Faixa de selos** (canto superior): `Libras`, `Audiodescrição`, `Idioma` quando aplicável.
3. **Badge "Novo"** (dourado) quando publicado < 3 meses.
4. **Categoria(s)** — chip(s) teal pequenos.
5. **Título** (Poppins 20px/600, máx. 2 linhas, `ellipsis`).
6. **Meta**: carga horária (`⏱ 20h`) · série/projeto quando houver.
7. **CTA**: "Acessar curso" (botão primário) — o card inteiro é clicável para `/cursos/{slug}/`.

**Tokens:** bg `#ffffff` · borda `#dee2e6` · raio 8px · sombra `--sombra-card` · padding 16px.

**Estados:**
| Estado | Tratamento |
|--------|-----------|
| default | sombra-card, borda `#dee2e6` |
| hover | eleva (`--sombra-hover`), título vira `--cor-primaria`, translate-y -2px |
| focus (teclado) | anel dourado 3px (`--cor-acento`), `outline: none` visual próprio |
| loading | skeleton (blocos `--cor-fundo-alt` pulsando) |
| sem imagem | placeholder com ícone da categoria |

### 2.2 Botões

| Variante | bg | texto | borda | raio | uso |
|----------|----|-------|-------|------|-----|
| `btn-primario` | `#147a02` | `#ffffff` | `#147a02` | 8px | CTA principal (Acessar, Buscar) · hover `#066017` |
| `btn-secundario` | transparent | `#147a02` | `#147a02` | 8px | ação secundária · hover bg `#eaf5e6` |
| `btn-acento` | `#ffbc00` | `#212529` | `#ffbc00` | 8px | destaque/conversão (ex.: "Montar meu plano") |
| `btn-ghost` | transparent | `#212529` | transparent | 8px | ações terciárias, toolbar |

Padding padrão `12px 20px`; **altura mínima 44px** (toque). Estado `:disabled` = opacidade 0.5, sem hover. Foco = anel dourado.

### 2.3 Busca + Facetas

- **Campo de busca** (topo de `/cursos/`): input 16px, ícone de lupa, `btn-primario` "Buscar" acoplado à direita (raio `0 8px 8px 0`). Busca sobre título + tags (tolerante a acento — herdar `diacritic` do legado).
- **Facetas** (sidebar em desktop, bottom-sheet em mobile) — combináveis, refletidas na URL como querystring (`noindex`):
  - **Categoria** (15, checkbox múltiplo)
  - **Para quem** (público)
  - **Carga horária** (faixas: ≤10h, 10–20h, 20–40h, 40–60h)
  - **Acessibilidade** (Libras, Audiodescrição)
  - **Idioma**
- Chips ativos removíveis acima da grade; botão "Limpar filtros".
- Regra: faceta com **0 resultados** aparece desabilitada (nunca some), com contagem `(0)`.

### 2.4 Seções curadas (home e categorias)

| Seção | Regra de ordenação | Fonte |
|-------|--------------------|-------|
| **Em destaque** | curadoria manual (1 dono editorial) | CEFOR |
| **Mais cursados** | nº de matrículas desc | Power BI / Moodle |
| **Recentes** | data de publicação desc | metadado (absorve levas trimestrais automaticamente) |

### 2.5 Chips e selos

- **Chip de categoria:** teal `#008080` sobre `#e6f2f2`, texto 12px, raio pill, clicável → `/areas/{slug}/`.
- **Selo de acessibilidade:** ícone + label curto; `Libras` (mãos), `Audiodescrição` (AD), `Idioma` (bandeira/BR/EN). `aria-label` descritivo.
- **Badge "Novo":** dourado `#ffbc00` + texto `#212529`.

### 2.6 Header

- bg `#ffffff`, borda inferior `#dee2e6`, altura 64px, sticky.
- Logo Ifes/Vitrine à esquerda → home. Navegação: **Cursos · Áreas · Para quem · Licença Capacitação · Sobre**. Item ativo em `--cor-primaria`.
- Busca acessível (ícone que expande). Barra de acessibilidade governamental no topo (contraste, A- A+), padrão gov.

### 2.7 Footer

- bg `--cor-primaria-profunda` `#195128`, texto branco. Colunas: institucional (Ifes/CEFOR), navegação, acessibilidade/Libras, contato. Créditos + logos de parceiros (Rio Doce, UnAC).

### 2.8 Página de curso (bloco principal)

- **Hero:** título (Poppins 40px), categoria(s), selos, carga horária, idioma, botão primário "Acessar no Moodle".
- **Corpo:** descrição, objetivos de aprendizagem, conteúdo programático, metodologia, avaliação, certificação (Art. 14 da resolução).
- **Sidebar:** ficha (carga horária, nível, idioma, provedor/projeto, certificação), CTA, selo Licença Capacitação quando elegível.
- **Rodapé do curso:** cursos relacionados (mesma categoria/série).

### 2.9 Wizard "Não sei o que quero" (3 perguntas)

- 3 passos: (1) o que busca (Para quem) · (2) tema (categoria) · (3) tempo disponível (carga horária). Progresso visível. Resultado = grade filtrada. Só consome metadados já existentes.

### 2.10 Planejador de Licença Capacitação

- Página `/qualificacao/`: explicação (o que é, quem tem direito, legislação) + montador que soma carga horária de cursos escolhidos até a meta de horas. Usa `carga_horaria` (já populada em `catalogo-cursos-completo.csv`).

---

## 3. Regras transversais

### 3.1 Acessibilidade (WCAG 2.1 AA)
- Contraste AA em todo par texto/fundo. Verde `#147a02` sobre branco e branco sobre verde: OK. **Dourado exige texto escuro** `#212529`.
- Foco sempre visível (anel dourado 3px, `--cor-acento`). Navegação por teclado completa. `alt` em toda imagem de curso. `aria-label` nos selos e ícones. Suporte a acentuação PT-BR garantido pelas fontes.
- Respeitar `prefers-reduced-motion` (desliga hover-elevações/animações).

### 3.2 Responsividade (mobile-first, base 8px)

| Breakpoint | Largura | Grade de cursos | Navegação |
|-----------|---------|-----------------|-----------|
| mobile | <576px | 1 coluna | hamburger + busca full-width; facetas em bottom-sheet |
| sm | ≥576px | 2 colunas | idem |
| md | ≥768px | 2–3 colunas | menu horizontal |
| lg | ≥992px | 3 colunas | menu + busca inline; facetas em sidebar |
| xl | ≥1200px | 4 colunas | container 1140px |

### 3.3 SEO/GEO/AEO
- 1 URL canônica por curso (`/cursos/{slug}/`). Páginas indexáveis: `/cursos/`, `/areas/{cat}/`, `/publicos/{pub}/`, `/certificacao/`, `/qualificacao/`. Combinações de faceta = `noindex`/canonical.
- Schema.org: `Course` + `ItemList` + `BreadcrumbList` + `Organization` + `inLanguage`/`accessibilityFeature`. Conteúdo principal no HTML (evitar "carregar mais" sem fallback rastreável).

### 3.4 Consistência com o design-system
- **Apenas** tokens de `design-system/` (nada de hex avulso). Verde = marca; teal = apoio; dourado = ação pontual. Azuis de framework **não** são marca (débito do legado — ver `references/design-md/*/DESIGN.md §7`).
- Ícones: definir um set único (sugestão: Lucide/Font Awesome 6 self-hosted) — **não** herdar FontAwesome 4.7 legado.
- Fontes self-hosted no tema (performance + LGPD; evitar chamada runtime ao Google Fonts).

### 3.5 Dados que orientam destaque/ordenação (Power BI)
- **Descompasso oferta × demanda:** catálogo dominado por educação/ambiental, mas a demanda real concentra-se em **prático** — Inglês (22.390), Moodle p/ Educadores (11.392), Canva (8.589), Google Drive (8.007). → "Mais cursados" e "Em destaque" devem **expor a demanda real**, não só o volume de oferta.
- **65% das matrículas vêm de fora do ES** → SEO/páginas de tema bem nomeadas são canal de aquisição primário; o design prioriza páginas de categoria indexáveis.

---

## 4. Estados globais e microcopy

| Situação | Tratamento |
|----------|-----------|
| Busca sem resultados | Ilustração + "Nenhum curso encontrado. Tente outra palavra ou remova filtros." + sugestões (Mais cursados) |
| Erro de carregamento | Mensagem amigável + botão "Tentar de novo" |
| Lista vazia de categoria | Explica que a categoria ainda não tem cursos + link para catálogo completo |
| Carregando | Skeletons de card (nunca spinner isolado em tela cheia) |

Microcopy: direta, acolhedora, sem jargão acadêmico ("cursos gratuitos com certificado", "comece do zero"). Verbos de ação nos CTAs.

---

## 5. Rastreabilidade (Audit)

| Check (CONTEXT §Audit) | Como esta spec atende |
|------------------------|------------------------|
| Cobertura de páginas | Todas as páginas em `mapa-paginas.md` têm componentes definidos aqui |
| Consistência | §3.4 — apenas tokens do design-system; hex literais rastreados aos `DESIGN.md` |
| Acessibilidade | §3.1 — AA, foco visível, acentuação, `prefers-reduced-motion` |
| Responsividade | §3.2 — comportamento mobile→desktop por breakpoint |
| Dados reais | §3.5 — destaque/ordenação ancorados no Power BI |
