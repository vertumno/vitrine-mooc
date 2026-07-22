# Proposta de refino — Home dos Cursos Abertos

> **Estágio:** 03 — Design/UX · **Criado em:** 21/07/2026
> **Status:** proposta em teste, para comparar com `../canonico/index.html`. Não substitui o canônico.

Abra lado a lado:

| Página | Canônico | Refino |
|---|---|---|
| Home | `../canonico/index.html` | `index.html` |
| Catálogo | `../canonico/cursos.html` | `cursos.html` |

**Dados:** `cursos.html` carrega `../canonico/cursos-dados.js` — a mesma fonte gerada que o
canônico usa. Nada foi duplicado. Regerar com `node gerar-dados.mjs` no canônico atualiza as
duas propostas ao mesmo tempo.

A versão EN não foi refeita; o seletor de idioma aponta para as páginas EN do canônico.

---

## O problema

A home canônica pede escala em vez de hierarquia. O diagnóstico:

- `h1` chega a **57px**; há um número decorativo em `clamp(7rem, 18vw, 17rem)` — **até 272px** de altura de fonte.
- Uma família só (Inter) faz título, corpo e dados. Sem contraste de forma, a única forma de
  destacar algo é aumentar o tamanho — e foi o que aconteceu em cada seção.
- **Cinco** famílias de acento no mesmo scroll (teal, dourado, verde, vermelho, terracota).
- Ruído de fundo acumulado: grid de pontos fixo em `body::before` + halos radiais + glass +
  sombra de `0 22px 60px`.

## A direção

Hierarquia por **peso, cor e espaço** — não por tamanho. A página é um catálogo, então ela
assume a linguagem de um catálogo bem impresso.

### Tipografia: superfamília IBM Plex, três larguras

> **Atualizado em 21/07/2026:** dois pedidos do CEFOR foram aplicados — títulos **sem serifa**
> (eram IBM Plex Serif) e camada de dados **sem monoespaçada** (era IBM Plex Mono, que ficou
> com cara de máquina de escrever). Ver as duas notas de execução abaixo.

Dois cortes da mesma família, e nenhuma monoespaçada:

| Papel | Fonte | Onde |
|---|---|---|
| Display | **IBM Plex Sans Condensed** 600 | h1, h2, h3, marca, números do índice |
| Texto | **IBM Plex Sans** 400/500/600 | corpo, navegação, botões, passos |
| Dados | **IBM Plex Sans** 300, 12px, tabular | carga horária, matrículas, ranks, eyebrows, rótulos técnicos |
| Código | monoespaçada do sistema | só o `<code>` do FAQ (senha de exemplo) |

A **camada de dados** continua sendo a ideia central da proposta: toda medida (`60h`,
`22.390 matrículas`, `01`, `31 cursos`) pertence a um registro visual próprio, separado do
texto corrido. O que mudou é **como** essa separação é feita — ver abaixo.

O Plex tem lastro institucional: foi desenhado para uma empresa de engenharia. Serve a um
instituto federal de ciência e tecnologia melhor que uma grotesca neutra.

#### Como a camada de dados funciona sem monoespaçada

Trocar `--mono` por uma sans e parar aí apagaria a camada: dado e texto virariam a mesma
coisa. A separação foi redistribuída em quatro sinais que agem juntos:

| Sinal | Como |
|---|---|
| **Numeral tabular** | `font-variant-numeric: tabular-nums` — todo dígito ocupa a mesma largura, então colunas de números continuam alinhadas (contagens das facetas, cargas horárias, ranks) |
| **Corpo menor** | 12px contra 15px do texto |
| **Peso leve** | **300** contra 400 do corpo — o dado *recua* em vez de avançar |
| **Tracking** | `+.02em` nos dados; `+.09em` a `+.14em` com caixa alta nos rótulos |

O numeral tabular é o que mais importa: era o único ganho *funcional* da monoespaçada, e foi
mantido sem ela.

> **Peso 300 exige carregamento.** A URL do Google Fonts pede `IBM+Plex+Sans:wght@300;400;500;600`.
> Se o `300` sair dali, o navegador cai em 400 e a diferença some **sem nenhum aviso** — nas
> duas páginas ao mesmo tempo.

A monoespaçada sobrou em um lugar só: o `<code>` que mostra `Cursos@123` no FAQ. Ali largura
fixa por caractere é informação, não estilo. Usa a fonte do sistema, sem download.

#### Como a troca de serifa para sem serifa foi feita

Trocar `--display` por uma sans qualquer resolveria o pedido, mas custaria caro: título e
corpo passariam a ser a **mesma fonte**, e a hierarquia voltaria a depender só de tamanho —
que é exatamente o problema do canônico. Então o eixo de contraste mudou de **forma** para
**largura**:

| | Antes | Agora |
|---|---|---|
| Fonte de título | IBM Plex Serif | IBM Plex Sans **Condensed** |
| Contraste com o corpo | serifa × sem serifa | condensada × normal |
| Peso do display | 500 (serifa segura o peso) | **600** (sans do mesmo corpo lê mais leve) |
| Tracking dos títulos | `-.014em` | `-.01em` (a condensada já é estreita) |

Os tamanhos **não mudaram** — a compensação foi só de peso e largura. Onze regras de
`font-weight` foram ajustadas: h1–h4, hero, marca, ficha técnica, índices, planejador,
rodapé, cards e estado vazio.

Uma exceção deliberada: a segunda linha do `h1` do hero (`Cursos Abertos do Ifes` /
*estudo aberto, no seu ritmo*) segue em **400**, contra 600 da primeira. Sem a serifa, esse
contraste interno passou a fazer mais trabalho do que fazia antes.

### Escala reduzida

| Elemento | Canônico | Refino |
|---|---|---|
| `h1` do hero | 35 → **57px** | 32 → **46px** |
| `h2` de seção | 26 → **38px** | 24 → **30px** |
| `h3` de card | ~19px | **17px** |
| Corpo | 16px | **15px** |
| Metadados | 14px | **12px** peso 500, tabular |
| Eyebrow | 13px | **11px** caixa alta, `letter-spacing .14em` |
| Número decorativo | até **272px** | removido |

### Espaçamento

Escala única de 4px (`--s1` a `--s8`) e **um só token de ritmo vertical**: `--section-y:
clamp(3.5rem, 5.5vw, 5.5rem)`. Toda seção usa `.section`. Não há override de padding por
seção — que era a origem dos saltos de ritmo no canônico.

### Cor

De cinco acentos para **dois**: teal (marca) e âmbar `#c98a16` (sinal). O âmbar aparece em
três lugares apenas — o filete do eyebrow, o marcador de passo e o botão da licença.
Fundo `#f6f8f8`, papel frio e levemente esverdeado, sem textura.

#### Correções de contraste (21/07/2026)

Ao baixar a camada de dados para o peso 300, auditei o contraste de todos os pares
cor/fundo dela. **Quatro reprovavam no AA da WCAG** (mínimo 4.5:1 para texto pequeno) — e as
falhas *já existiam antes* do peso 300; o texto fino só tornou o problema mais visível. Numa
vitrine pública federal, com categoria de Inclusão e Acessibilidade e cursos em Libras, isso
não podia ficar.

| Onde | Antes | Depois |
|---|---|---|
| `--ink-faint` (contagens, "31 cursos", "48") | `#8a9c9b` — **2.87:1** | `#687a79` — **4.52:1** |
| `.eyebrow` sobre papel | `--teal` — **4.48:1** | `--teal-deep` — **6.94:1** |
| `.load-row .data` ("faltam 12") | `--ink-faint` sobre papel — **4.24:1** | `--ink-soft` — **5.07:1** |

A **marca não mudou**: `--teal` (`#00807f`) continua igual. O que mudou foi o tom de um
rótulo, que sobre o fundo papel ficava um fio abaixo do mínimo.

Os 10 pares auditados passam em AA. O mais apertado é `.data-faint` a 4.52:1 — se alguém
clarear `--ink-faint` de novo, ele reprova.

### Forma

Raio de 6px, filete de 1px como estrutura principal, sombra quase inexistente
(`0 8px 24px rgba(...,.05)`). O peso visual vem da linha, não do blur.

### Cabeçalho: o lockup da marca e o ponto de quebra

O nome do produto subiu de 13px para **18px**, ao lado do logo de 34px (2509×700, então
122px de largura). Os dois passam a ler como um par — instituição + produto — em vez de
marca com legenda.

Isso obrigou a rever a conta de largura do cabeçalho:

| Peça | Largura |
|---|---|
| Marca (logo + filete + nome 18px) | 258px |
| Menu, 6 itens com gap de 24px | 538px |
| Ações (idioma + CTA + gaps) | 206px |
| Gaps do grid | 64px |
| **Total** | **1066px** |

Como a `.wrap` é `min(1140px, 100vw − 40)`, o menu horizontal só cabe a partir de **1141px**
de viewport. **O hambúrguer entrava em 900px** — ou seja, entre 900 e 1100 o menu
transbordava sem nenhum aviso. Esse defeito já existia (o limite real era 1075px antes do
lockup); o nome maior apenas alargou a faixa.

O ponto de quebra do menu foi movido de 900px para **1140px**, amarrado ao `--maxw`. O CTA
"Acessar ambiente" continua saindo só em 900px — com o menu já recolhido, sobra espaço.

O lockup também encolhe: 28px/16px abaixo de 680px, e abaixo de **520px** o filete e o nome
somem, deixando só a marca do Ifes (o `h1` da página já diz "Cursos Abertos do Ifes").

---

## Mudanças de estrutura

| Onde | Antes | Agora | Por quê |
|---|---|---|---|
| Header | Barra teal sólida, 68px | Transparente sobre o hero, vira sólido no scroll, 60px | Devolve o hero inteiro à imagem; menos massa de cor |
| Marca | Logo 22px + nome 13px | **Lockup**: logo 34px + filete + nome **18px** | A 13px o nome do produto lia como legenda do logo. Agora instituição e produto têm peso comparável |
| Indicadores | 3 cards com ícone e sombra | **Linha de índice** em hairline no rodapé do hero | Número não precisa de caixa. Ganhou uma 4ª entrada: `Custo — R$ 0,00` |
| Hero | 2 botões grandes + busca | Busca em destaque + 2 links de texto | Uma ação primária só. A busca é o caminho real |
| Setas do carrossel | Flutuando sobre os cards | No cabeçalho da seção, com estado desabilitado nas pontas | Não cobrem conteúdo; indicam onde você está no trilho |
| Ranking | Badge numérico no corpo do card | `01`–`08` sobre a imagem, em chip escuro | O rank é dado, não decoração |
| "O que é MOOC" | Bloco com `60%` gigante + 4 cartões de fato | **Ficha técnica** em `<dl>`: formato, duração, turmas, ingresso, aprovação, certificado, custo | Sete fatos consultáveis no lugar de um número decorativo |
| FAQ | 34 accordions na home | **8** mais consultadas + link para a Base de Conhecimento | 34 accordions numa home é arquivo, não navegação |
| Passos | Círculos grandes `01`–`04` | Rótulos pequenos com filete vertical | Aqui a numeração é legítima: é sequência real |

---

## Imagem da seção MOOC

A "Ficha do formato" foi removida em 21/07/2026 e deu lugar a uma imagem.

**Onde salvar:** `assets/mooc-estudo.jpg` — **1600 × 1600 px (1:1)**, JPG de qualidade alta.
O CSS aplica `aspect-ratio: 1/1` com `object-fit: cover`, então **gerar em quadrado evita
qualquer corte**. Em outro formato, a imagem é cortada pelo centro.

Enquanto o arquivo não existir, o espaço aparece como um bloco teal claro com filete — não
como ícone de imagem quebrada.

**Os fatos da ficha não se perderam.** Os que já estavam no texto ficaram lá; os que não
estavam viraram a legenda sob a imagem: *Até 60h · Turmas anuais · 60% de aproveitamento
para certificar · Gratuito, inclusive o certificado*.

### Prompt (colar em gerador de imagem)

Escrito em inglês porque os modelos de imagem respondem melhor assim.

```text
A candid documentary-style photograph, square 1:1 composition.

SUBJECT: a Brazilian woman in her late thirties, brown skin, natural curly hair
loosely tied back, wearing a plain sage-green knit sweater. She is alone,
seated at a simple wooden table in a modest sunlit apartment, studying from an
open laptop. One hand rests on a spiral notebook she has been writing in, a pen
between her fingers. Her expression is calm and absorbed — quietly focused,
with a trace of satisfaction. She looks at the screen, never at the camera.

SETTING: an ordinary Brazilian home, lived-in rather than styled. A ceramic mug
of coffee, a small potted plant, a phone lying face-down. Plain off-white wall
behind her. Late-morning daylight from a window to her left, soft and diffused,
no harsh shadows.

LIGHT AND COLOUR: bright and airy, cool-neutral base. Muted teal and soft sage
in the wardrobe and background, with one warm accent — the wood of the table
and the amber of the coffee — to keep it human. Low overall saturation, gentle
contrast, subtle film grain.

CAMERA: 50mm lens at eye level, shallow depth of field around f/2.2; subject
sharp, background gently soft. Medium shot from the waist up. Place her
slightly right of centre, leaving calm empty space in the upper-left of the
square.

MOOD: autonomy and quiet progress. Someone learning on her own terms, at her
own pace, in her own time. Dignified, ordinary, real.

AVOID: stock-photo artificiality, looking at camera, thumbs-up, forced smiles,
groups of people, classroom, teacher, whiteboard, graduation cap, floating UI
or holograms, any text, letters, numbers, logos or watermarks, heavy vignette,
oversaturated colour, orange-and-teal blockbuster grading, plastic retouched
skin, malformed hands.

OUTPUT: 1600 x 1600 px, photographic realism.
```

### Por que essa cena

| Decisão | Motivo |
|---|---|
| **Uma pessoa só** | A seção explica que o MOOC é **sem tutoria** e no seu ritmo. Sala de aula ou grupo contradiz o texto. O hero já tem cena coletiva — aqui o contraste reforça a autonomia |
| **Casa comum, não estúdio** | "De onde você estiver" só é crível num lugar real. Fundo branco de estúdio venderia "curso corporativo" |
| **Olhando para a tela, não para a câmera** | Olhar para a câmera transforma a pessoa em modelo. Olhar para a tela mantém a cena como observação |
| **Teal e sage na roupa e no fundo** | Amarra a foto à paleta da página sem filtro por cima. O acento quente (madeira, café) evita que fique fria demais |
| **Espaço vazio no topo-esquerdo** | Dá respiro ao lado do texto e evita que a foto pese mais que a coluna de prosa |
| **Sem texto na imagem** | Modelos de imagem escrevem palavras erradas, e texto em imagem não é acessível nem traduzível |

### Variações, se a primeira não servir

Troque só o bloco `SUBJECT`, mantendo o resto:

- **Alcance etário** — *a Brazilian man in his sixties, grey hair and beard, reading glasses,
  wearing a simple checked shirt, studying from a tablet propped on a kitchen table.*
  Reforça "aberto a qualquer pessoa, sem processo seletivo".
- **Estudo no intervalo** — *a young Black Brazilian man in his twenties, in a plain work polo
  shirt, sitting on a bench during a break, studying from his phone, backpack beside him.*
  Reforça "no seu tempo, de onde estiver".
- **Servidor público** — *a Brazilian woman in her forties at a tidy desk in a public-service
  office after hours, studying from a laptop.* Conversa direto com a seção de licença
  capacitação.

> **Acessibilidade:** ao trocar a imagem, ajuste o `alt` no `index.html`. Ele descreve a cena
> para quem usa leitor de tela — hoje diz "Pessoa estudando sozinha pelo notebook, em casa, no
> seu próprio ritmo".

---

## Projetos parceiros — dimensionamento das marcas

Ajustado em 21/07/2026. A estrutura do card **não mudou** (logo + contagem na linha de topo,
depois `<h3>`, descrição e link). Só as marcas cresceram — e cada uma com a sua altura.

### Por que alturas diferentes

Os dois PNGs foram medidos, não estimados. A caixa de tinta real de cada um:

| | Rio Doce Escolar | UnAC |
|---|---|---|
| Canvas | 511 × 511 | 690 × 486 |
| Tinta real | 445 × 377 | 520 × 225 |
| Ocupação do canvas | 87% × **74%** | 75% × **46%** |
| Formato | selo quase quadrado | wordmark horizontal |
| Transparência | sim (RGBA) | **não** (RGB) |

O arquivo do UnAC carrega quase o dobro de margem vazia. Com os dois na **mesma altura CSS**
— que era o caso antes, ambos em 34px — o UnAC aparecia com apenas **77% da área de tinta**
do Rio Doce.

| Marca | Altura | Tinta visível | Área relativa |
|---|---|---|---|
| Rio Doce (`data-logo="quadrado"`) | 34 → **48px** | 42 × 35 | 100% |
| UnAC (`data-logo="horizontal"`) | 34 → **54px** | 58 × 25 | **98%** |

Os 6px a mais no UnAC não são capricho: compensam a margem embutida no arquivo. A área de
tinta do Rio Doce dobrou em relação ao estado anterior.

### Pendência de arquivo

> **Pedir ao pessoal do UnAC um PNG com fundo transparente.** O arquivo atual é RGB sem canal
> alfa, ou seja, tem um fundo branco chapado embutido. Hoje isso não aparece, porque o card é
> branco — mas qualquer fundo colorido atrás dele revelaria um retângulo branco.

### Títulos e `alt`

Os `<h3>` continuam **visíveis** — são sinal de SEO/GEO e âncora de leitura. O `alt` das
imagens traz o nome da marca com um qualificador ("Marca do projeto Rio Doce Escolar"), para
somar em busca por imagem sem repetir o `<h3>` palavra por palavra logo acima.

---

## Catálogo (`cursos.html`)

O catálogo é **ferramenta**, não vitrine. Ele foi tratado com a mesma gramática da home, mas
com prioridade diferente: a lista precisa aparecer cedo.

| Onde | Antes | Agora | Por quê |
|---|---|---|---|
| Header | Faixa teal com gradiente diagonal, halos radiais e 2 cards em glass | Faixa **clara** com hairline, altura compacta | A abertura anterior empurrava a lista para baixo. Aqui o header já nasce sólido, porque não há foto atrás dele |
| Busca | Dentro da barra lateral, junto das facetas | No **topo da faixa**, larga | É a ação principal da página. Estava competindo com 7 grupos de checkbox |
| Indicadores | 2 cards com ícone e sombra | Linha de índice — cursos, áreas, **Libras**, custo | Mesma linguagem da home. "Disponíveis em Libras: 20" é informação de acessibilidade, não decoração |
| Facetas | Blocos com fundo e borda | Grupos separados por hairline, título em caixa alta, checkbox custom 15px, contagem tabular | Densidade sem caixas. A barra é sticky com scroll próprio |
| Contagem | "Mostrando 24 de 165 cursos" | `24` de `165` cursos, com os números em destaque | Números são dado — mesma camada de dados |
| Chips | Retângulos | Pills com `×` e hover invertido | Fica claro que são removíveis |
| Grid | Largura fixa | `auto-fill minmax(220px, 1fr)` — 2 col. no celular | Aproveita a largura real da tela |
| Selos | Ribbon PNG + badges de bandeira | Tags, **no máximo 2 por card** | Um curso pode gerar 4 selos (Libras + projeto + série + idioma); 4 quebravam o alinhamento do grid |
| Vazio | Frase solta | Bloco com título, direção e botão de limpar | Tela vazia é convite para agir |
| Mobile | Barra lateral empilhada acima da lista | Botão `Filtrar cursos (n)` que abre o painel | 7 grupos de facetas antes da lista inviabilizavam a página no celular |

### Navegação home → catálogo

A home aponta para o catálogo desta proposta (não mais para o do canônico), e os cards de
**projeto** e **série** abrem o catálogo **já filtrado**:

| Card da home | Destino |
|---|---|
| Rio Doce Escolar | `cursos.html?projeto=rio-doce-escolar` — 31 cursos |
| UnAC | `cursos.html?projeto=unac` — 33 cursos |
| Série Lovelace | `cursos.html?serie=lovelace` — 6 cursos |
| Série Educador Maker | `cursos.html?serie=educador-maker` — 4 cursos |
| Série Atendente e Vendedor | `cursos.html?serie=atendente-e-vendedor` — 3 cursos |
| Série Embrace | `cursos.html?serie=embrace` — 3 cursos |
| Série Lesson Study | `cursos.html?q=Lesson%20Study` — 3 cursos |
| Busca do hero | `cursos.html?q=<termo>` (submit nativo, funciona sem JS) |
| Mais cursados / Recentes | `cursos.html?ordem=…` |

Para isso o catálogo passou a ler **qualquer faceta pela URL**, e não só `categoria`:
`?categoria=`, `?carga=`, `?nivel=`, `?idioma=`, `?projeto=`, `?serie=` e `?libras=1`. Cada
grupo aceita vários valores separados por vírgula (`?serie=lovelace,embrace`). Sem isso, os
links acima seriam ignorados em silêncio — o catálogo abriria sem filtro nenhum.

> **Lesson Study** não é uma série em `curadoria.json`, por isso cai na busca por termo em vez
> de faceta. Se virar série de verdade, troque o link por `?serie=lesson-study`.

### Verificação

A lógica foi executada contra os 165 cursos reais (não só inspecionada):

- 165 cursos carregados, **0** sem categoria, thumb ou link
- **0 facetas com contagem zero** — nenhuma opção morta na barra lateral
- 20 cursos com Libras; 1 obsoleto, com a nota preservada
- Maiores áreas: Educação (48), Ambiente e Saúde (44), Tecnologias e Informática (18)
- HTML balanceado, 0 classe sem CSS, 0 id referenciado pelo script e ausente do HTML
- **15 links da home para o catálogo, 0 quebrado** — cada slug de projeto/série foi conferido
  contra os dados, e as contagens exibidas nos cards (31, 33, 6, 4, 3, 3) batem com o número
  real de cursos que o filtro retorna
- 9 caminhos locais (imagens, logos, páginas irmãs) existem no disco

---

## Decisões que precisam do seu aval

1. ~~**Serif nos títulos.**~~ **Resolvido em 21/07/2026:** o CEFOR pediu sem serifa. Ficou
   IBM Plex Sans Condensed 600 — o contraste com o corpo agora vem da largura. Se ainda
   parecer estreito demais, a alternativa é usar IBM Plex Sans normal em 600 no display, mas
   aí título e corpo viram a mesma fonte e só o peso separa os dois.
2. **Ribbon de Libras substituído por tag.** O PNG `ribbon_mooc_libras.png` sobre a imagem
   virou uma tag `Libras` em âmbar na linha de metadados. Fica consistente com a camada de
   dados e legível em card pequeno — mas é a remoção de um asset que vocês já usam. Reversível.
3. **FAQ reduzida a 8.** Depende de existir destino para as outras 26 (Base de Conhecimento
   ou página `/duvidas`). Se não existir, mantemos as 34 aqui.
4. **`R$ 0,00` no índice do hero.** Gratuidade é o argumento mais forte e estava só no
   eyebrow. Se soar comercial demais para uma instituição pública, volta a ser texto.

## O que não mudou

Conteúdo, links, ordem das seções, dados dos cursos e o ranking de matrículas
(fonte: `powerbi-mooc-ifes/indicadores-por-curso.csv`, com "Moodle para Educadores" já
retirado conforme a reunião de 09/07). A proposta é de forma, não de escopo.

## Pendências herdadas do canônico

Não foram resolvidas aqui porque são de dado, não de design — continuam para o estágio 05:

- **Carrosséis da home são estáticos.** "Em destaque", "Mais cursados" e "Recentes" estão fixos
  no HTML. A comissão pediu (09/07) que venham de consulta ao banco com janela temporal
  configurável.
- **"Mais cursados" e "Recentes" no catálogo ainda são placeholder.** `demanda` só conhece os
  4 primeiros colocados (tabela `DEMAND_RANK`) e `recente` usa a ordem do catálogo, não a data
  de publicação. Mantive as duas opções no seletor para paridade de teste — mas elas não
  ordenam de verdade até existirem os campos.
- **FR/ES** seguem desabilitados, com selo "em breve".
- **Versão EN** não foi refeita nesta proposta.
