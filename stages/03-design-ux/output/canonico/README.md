# Protótipo canônico — Cursos Abertos do Ifes

> **Estágio:** 03 — Design/UX · **Última atualização:** 09/07/2026
> **Direção visual:** azul/teal (Moodle/OpenLearning) — ver `../plano-atualizacao.md`.
> Este é o **protótipo vivo** da Vitrine. As specs de apoio ficam em
> `../design-spec.md` (componentes/tokens) e `../mapa-paginas.md` (páginas/dados).

## Arquivos

| Arquivo | Papel |
|---------|-------|
| `index.html` | Home (pt-BR) |
| `cursos.html` | Catálogo/busca (pt-BR) |
| `index-en.html` | Home (English) |
| `cursos-en.html` | Catálogo/busca (English) |
| `estilos.css` | Folha de estilo única, compartilhada por todas as páginas |
| `index-v3.html` | Home com **refino tipográfico** — mesmo HTML, mesma estrutura (ver abaixo) |
| `cursos-v3.html` | Catálogo com o mesmo refino |
| `projeto-v3.html` | **Página de projeto parceiro** (UnAC e Rio Doce Escolar) — proposta, ver abaixo |
| `licenca-v3.html` | **Planejador de Licença para Capacitação** (rota prevista `/qualificacao/`) — ver abaixo |
| `estilos-v3.css` | Camada de refino carregada **depois** de `estilos.css`, só nas páginas v3 |
| `projeto-v3.css` | Camada da página de projeto, carregada depois das outras duas |
| `licenca-v3.css` | Componentes `.plc-*` do planejador + folha de impressão do plano |
| `cursos-dados.js` | Dados dos 165 cursos + facetas (fonte única, em pt-BR) — **gerado, não editar à mão** |
| `gerar-dados.mjs` | Gera `cursos-dados.js` (ver abaixo) |
| `curadoria.json` | Séries, projetos, idiomas adicionais e cursos obsoletos — curadoria do CEFOR |
| `assets/` | Imagens do hero, ribbon de Libras e ícones |

## Como regerar os dados

```bash
node gerar-dados.mjs
```

Lê duas entradas e escreve `cursos-dados.js`:

1. `stages/02-catalogo/output/catalogo-cursos-completo.json` — a extração da vitrine atual.
2. `curadoria.json` — o que **não existe** na fonte e é decisão do CEFOR: quais cursos formam cada
   série, quais pertencem a cada projeto parceiro, idiomas adicionais e cursos substituídos por
   versão mais recente.

O gerador também normaliza o texto livre da extração, que vinha bagunçado: carga horária (25+
grafias → `NNh`), idioma (13 grafias de "Português" → códigos `pt`/`en`/`es`/`pom`) e nível. A saída
é determinística — rodar duas vezes produz o mesmo arquivo.

> **Para alterar séries, projetos ou marcar um curso como obsoleto:** edite `curadoria.json` e rode
> o gerador. Não edite `cursos-dados.js`.

Quando o dump do WordPress chegar (estágio 04), a fonte muda mas a curadoria e as regras de
normalização continuam valendo.

## Funcionalidades implementadas

### 1. Seletor de idioma (topo do header)
- Dropdown acessível no canto superior direito (`.lang-switch`), antes do CTA "Acessar ambiente".
- Idiomas: **Português (padrão)**, **English**, **Français**, **Español** — cada um com bandeira e nome nativo.
- Acessibilidade: `role="menu"`/`menuitemradio`, `aria-expanded`/`aria-checked`, fecha ao clicar fora e com **Esc** (devolvendo foco ao botão), `:focus-visible`.
- Navegação real **PT ⇄ EN** (os links apontam para o par traduzido). **FR/ES** ainda são placeholder: só atualizam o estado visual (a tradução real virá no estágio 05).

### 2. Versões em inglês
- `index-en.html` e `cursos-en.html` traduzem **toda a interface** (header, hero, seções, FAQ com as 34 perguntas, rodapé, filtros e microcopy dinâmica do catálogo).
- **Decisão:** os **títulos oficiais dos cursos permanecem em português** (nomes reais do Ifes, sem versão oficial em inglês). A taxonomia/categorias, rótulos de filtro (`Up to 10h`, `Basic`…) e números (`22,390 enrollments`) são traduzidos via mapas no próprio script, sem duplicar `cursos-dados.js`.

### 3. Busca no hero da Home → catálogo
- A Home tem uma barra de busca (`.hero-search`) que é um `<form method="get">` apontando para o catálogo.
- Ao enviar, o navegador monta `cursos.html?q=<termo>` (ou `cursos-en.html?q=…`) e o catálogo **pré-preenche o campo e aplica o filtro** ao carregar (via `applyInitialParams` → `params.get("q")`).
- Funciona **sem JavaScript** (submit nativo), com `role="search"` e label acessível.

### 4. Hero do catálogo (`.catalog-hero`)
- Faixa de abertura do catálogo redesenhada para o acabamento do restante do canônico: **kicker em pill** ("Catálogo completo" com ponto dourado), **título** "Catálogo de cursos" (trecho destacado em `teal-soft`) e dois **stat cards em glass** (cursos publicados + áreas temáticas) com ícone, filete dourado e elevação no hover.
- **Fundo em camadas:** gradiente diagonal teal→teal-deep→teal-dark + halos radiais + textura de pontos que esmaece na base (`mask`).
- Altura **compacta** (`padding` vertical `clamp(32px,4.5vw,50px)`); colapsa para 1 coluna no mobile. Espelhada em `cursos.html` (PT) e `cursos-en.html` (EN). CSS: `.catalog-hero`, `.catalog-hero-decor`, `.summary-box`, `.summary-icon`, `.summary-label`.

## Refino tipográfico da Home (`index-v3.html`) — 21/07/2026

Abra lado a lado com `index.html`. **O layout não mudou:** mesmas seções, mesma ordem, mesmo
conteúdo, mesma paleta, mesmo HTML. Mudam apenas tamanho de fonte, peso, tracking, entrelinha,
espaçamento e margem. Tudo isola em `estilos-v3.css`, que é uma camada de override — para
descartar a proposta, basta remover o segundo `<link>`.

**Diagnóstico.** O canônico tinha uma alavanca só para criar hierarquia: aumentar a fonte. Como
toda seção precisava de destaque, toda seção cresceu. O resultado é escala sem hierarquia, com
`h2` de seção maior que o `h1` de muitos sites e pesos 700/800 em quase todo texto.

**Direção.** Hierarquia por **peso, cor e espaço**. O tamanho que sobrou virou tracking negativo e
entrelinha fechada — é isso que faz um display parecer desenhado em vez de esticado.

| Elemento | Canônico (máx.) | v3 | Observação |
|---|---|---|---|
| `h1` do hero | 56,8px / 800 | **44px** / 800 | `letter-spacing -.022em`; 2ª linha cai para peso 500 |
| `h2` "O que é MOOC?" | 61,6px | **37,6px** | continua o maior `h2`, mas agora abaixo do `h1` |
| `h2` de seção | 37,6px **e** 40px | **30px** | eram dois valores para o mesmo papel |
| `h2` licença capacitação | 50,4px | **36px** | |
| `60%` (prova social) | 72,8px | **52px** | |
| `30 dias` / `129h` (painel) | 48px / 33,6px | **36px / 28px** | |
| Marca d'água "MOOC" | **272px** | **152px** | era a maior massa tipográfica da página; some no mobile |
| Marca d'água "licença" | 192px | **136px** | idem |
| Rank `01`–`08` | 41,6px | **32px** | |
| Numeração dos passos | 48px | **34px** | |
| `h3` de card | 16,3px / 700 | **16px** / 700 | |
| Categoria do card | 12,2px teal | **11px caixa alta, cinza** | etiqueta deixa de disputar com o título |
| Rótulo de indicador | 13px / **700** | 13px / **500** | rótulo não precisa gritar |
| Corpo | 16px / 1.55 | 16px / **1.6** | |
| Descrição de seção | 16px | **15px** | |
| Metadados de card | 12,5px | **13px** | subiu: dado precisa ser legível |

**Outros ajustes**

- **Ritmo vertical:** `section` era fixo em 64px em qualquer tela; virou `clamp(52px, 5vw, 80px)` —
  mais ar no desktop, menos aperto no celular.
- **Eyebrows** (`kicker`, categoria do card) viraram 11px em caixa alta com `letter-spacing .09em`,
  em vez de 12–13px em caixa normal competindo com o texto ao lado.
- **Números tabulares** (`font-variant-numeric: tabular-nums`) em toda medida — carga horária,
  matrículas, ranks, percentuais. Os dígitos param de "dançar" entre cards.
- **Medida de linha** em `ch` (45–75 caracteres) no lugar de `max-width` em px.
- **Separador `·`** entre metadados do card: "60h · Básico" em vez de "60h  Básico".
- **`footer h4`** não estava no reset `h1,h2,h3 { margin: 0 }` e carregava a margem padrão do
  navegador (~21px), desalinhando as colunas do rodapé. Corrigido.
- `text-wrap: balance` nos títulos e `pretty` nos parágrafos.

**Não verificado em navegador** — esta sessão não tem browser disponível. A validação foi
estrutural: sintaxe do CSS, ordem dos `<link>`, e conferência de que os 131 seletores do refino
existem em `estilos.css` e são usados no HTML — 129 sobrescrevem uma regra existente, 2 são novos
(`::placeholder` do campo de busca e o separador `·` dos metadados) e nenhum é regra morta.
Falta o olho.

### Em teste: máscara teal no hero da home — 22/07/2026

O hero claro do canônico está com uma máscara teal escura, para comparação. Vive no **último
bloco** do `estilos-v3.css`, sob um cabeçalho `TESTE`: apagar dali até o fim do arquivo devolve o
hero claro. Só afeta a home (o catálogo usa `.catalog-hero`).

**Calibrada para a foto de pessoas** (`assets/hero-ifes-desktop.png`, mosaico de 7 painéis sobre
fundo de estúdio claro). Três fatos dessa imagem definiram a máscara:

1. **A foto é clara.** Véu translúcido sobre branco vira leitoso — a máscara precisa de densidade,
   não de transparência.
2. **Os rostos ficam na mesma faixa vertical do texto**, e as divisórias dos painéis criam um
   padrão agitado atrás da leitura.
3. A primeira tentativa usava **vinheta clássica** — centro claro (`.28`), bordas escuras (`.84`).
   Errado para esta foto: jogava o texto na área menos protegida e mais ocupada da imagem.

Agora é o inverso: um borrão escuro e muito difuso atrás do texto, com as pessoas aparecendo nas
bordas. São **duas camadas**, para poder controlar tom e legibilidade separadamente:

| Camada | Onde | Papel |
|---|---|---|
| `.hero::after` (z −2) | sobre a foto | tom: rampa `135deg` teal → teal-deep → teal-dark, a mesma da `.catalog-hero`. Faixa superior sai do `#008080` exato do header, para a emenda sumir. Densidade .52–.70 |
| `.hero::before` (z −1) | sobre o tom | o borrão de leitura: radial de **sete paradas**, para a transição não formar anel visível |

Cobertura resultante: **~90% no centro** (texto legível sobre qualquer rosto) e **~53% nas bordas**
(pessoas claramente visíveis). A foto ganhou `saturate(.72)`, que acalma a mostarda e o laranja das
roupas — brigavam com o teal — e `object-position: center 32%`, que sobe o enquadramento para os
rostos.

Junto vieram as inversões que a máscara exige: título e lead em branco, segunda linha do `h1` em
branco a 72% (era `--teal`, invisível sobre teal), ponto do eyebrow em dourado (o vermelho embarra)
e o botão "Como funciona" virou fantasma. A busca continua sendo a pílula branca do canônico —
sobre fundo escuro ela ganha ainda mais destaque.

> **Pendência: o mobile carrega outra imagem.** O `<picture>` do hero serve
> `assets/hero-ifes-mobile.png` abaixo de 760px, que é uma **ilustração clara em verde-menta**
> (mulher com notebook, cards de UI, campus), desenhada para o hero claro e com área vazia no topo
> reservada ao texto. A máscara escura vai embarrar essa arte. Antes de aprovar o teste, decidir:
> gerar um recorte vertical da foto de pessoas, ou aliviar a máscara abaixo de 760px.

### Catálogo (`cursos-v3.html`)

Os cards do catálogo são montados por JS com as **mesmas classes** da home (`.course-card`,
`.course-cat`, `.course-meta`), então todo o refino de card já valia sem uma linha a mais. O que
foi tratado é o que só existe no catálogo:

| Elemento | Canônico (máx.) | v3 | Observação |
|---|---|---|---|
| `h1` "Catálogo de cursos" | 48px | **38px** | fica abaixo do `h1` da home (44px) — a home apresenta, o catálogo rotula |
| `h2` "Todos os cursos" | 28,8px | **26px** | |
| Números do resumo | 37,6px / 800 | **32px / 700** | mesmo valor do indicador da home: é o mesmo papel |
| Título de faceta | 14,7px / 700 | **12px caixa alta** | sete grupos em negrito competiam com os títulos dos cards ao lado |
| Rótulo de faceta | 14px | **14px** | entrelinha 1.4 para caber contagem na mesma linha |
| Contagem, chips, ordenação | 12,5–13,4px | **12–13px** | contagens com dígito tabular |

**Navegação:** as duas páginas v3 apontam uma para a outra (`index-v3` ⇄ `cursos-v3`), inclusive
a busca do hero e os links "ver todos". Assim dá para percorrer o protótipo inteiro sem cair no
canônico no meio do caminho. O seletor de idioma continua apontando para `cursos-en.html` e
`index-en.html` do canônico — não há versão EN da v3.

**Dados:** `cursos-v3.html` carrega o mesmo `cursos-dados.js`. Nada foi duplicado; rodar
`node gerar-dados.mjs` atualiza as duas versões ao mesmo tempo.

**Pendências se a proposta for aprovada:** aplicar a mesma camada em `index-en.html` e
`cursos-en.html`, e então fundir `estilos-v3.css` dentro de `estilos.css`.

## Proposta: página de projeto parceiro (`projeto-v3.html`) — 22/07/2026

Até aqui os dois projetos parceiros eram só cards na home com `href="#"`. Agora têm página, e os
cards da home apontam para ela.

**Um template, dois projetos.** O projeto vem da URL:

| Endereço | Projeto | Cursos |
|---|---|---|
| `projeto-v3.html?p=unac` | UnAC — Universidade Aberta Capixaba | 33 |
| `projeto-v3.html?p=rio-doce-escolar` | Rio Doce Escolar | 31 |

Sem parâmetro, abre a UnAC. `?p=riodoce` e `?p=rio-doce` são aceitos como apelido, para o link não
quebrar por causa do formato. **No WordPress isso vira o template de arquivo da taxonomia
`projeto`** — uma página, N projetos. Adicionar um terceiro projeto é acrescentar uma entrada em
`curadoria.json` e um objeto em `PROJETOS`, sem página nova.

**Esta página substitui o hub atual** (`mooc.cefor.ifes.edu.br/v/unac/` e `/v/riodoce/`) — decisão
de 22/07/2026. Por isso não há link para "página atual do projeto".

**A página tem:**

1. **Faixa de abertura** com a marca do projeto na mesma placa branca do card da home e o **mesmo
   gradiente do card** — teal para a UnAC, verde para o Rio Doce. Quem clica no card não troca de
   identidade no meio do caminho. Os números do projeto vêm em **uma linha de texto**
   ("33 cursos · 1.440 horas · 12 áreas temáticas · 8 com Libras"), calculada dos dados.
2. **Lista de cursos com a anatomia do catálogo:** barra de filtros, cabeçalho de resultados
   (contagem + título + ordenação) e *chips* de filtro ativo que removem o próprio filtro — os
   mesmos componentes `.results-head`, `.toolbar`, `.sorter` e `.chip`.
3. **Todos os cursos, sem paginação, em grade de 4 por linha** — as duas diferenças em relação ao
   catálogo, que carrega de 24 em 24 e usa 3 colunas por causa da barra lateral de facetas. Sem
   barra lateral, cabe uma coluna a mais: 4 → 3 (≤1120px) → 2 (≤900px) → 1 (≤620px).
4. **Saída:** o outro projeto parceiro e o catálogo completo.

**Números conferidos com os dados** (`node gerar-dados.mjs` não precisa rodar de novo):

| | UnAC | Rio Doce Escolar |
|---|---|---|
| Cursos | 33 | 31 |
| Horas somadas | 1.440 (1 curso sem carga informada) | 645 |
| Áreas temáticas | 12 | 1 (Ambiente e Saúde) |
| Com Libras | 8 | 0 |

**O que os dados obrigaram a tratar.** O Rio Doce Escolar tem **uma área só** e **nenhum curso em
Libras** — filtro que não filtra nada é ruído, então as duas linhas de *pills* somem e a linha de
metadados omite o item de Libras e usa "1 área temática" no singular. O total de horas da UnAC
ignora 1 curso sem carga informada, e a própria linha diz isso em vez de fingir que é o total.

**Textos.** A apresentação da UnAC é a **descrição oficial do programa**
(`../../02-catalogo/output/projetos-especiais.md`). O Rio Doce Escolar **não tem texto oficial** —
a página usa a frase provisória que já estava no card da home e exibe, na própria faixa, um aviso
de que a apresentação precisa ser confirmada com o Cefor. A **vinculação dos cursos** aos projetos
vem das `data-tag` da vitrine atual e também está sinalizada como pendente de confirmação, ao pé
da lista.

**CSS:** `projeto-v3.css`, carregado depois de `estilos.css` e `estilos-v3.css`. Reaproveita
`.results-head` / `.toolbar` / `.sorter` / `.chip` / `.course-grid.four` (catálogo) e `.projeto` /
`.projeto-logo` (cards da home); só traz o que não existia — a faixa do projeto, a barra de *pills*
e as notas. Se aprovado, funde em `estilos.css`.

**Não verificado em navegador** — como no refino tipográfico, esta sessão não tem browser. A
validação foi estrutural e automatizada: sintaxe do script inline, hooks `data-*` e IDs usados pelo
JS presentes na marcação, ausência de IDs duplicados, chaves do CSS balanceadas, nenhuma regra
morta em `projeto-v3.css` e todos os caminhos de arquivo resolvendo em disco. Os números da linha
de metadados foram conferidos rodando a mesma lógica sobre `cursos-dados.js`. **Falta o olho.**

**Sem versão EN.** Todos os idiomas além do português aparecem como "em breve" no seletor.

## Planejador de Licença para Capacitação (`licenca-v3.html`) — 22/07/2026

A home prometia um planejador desde o começo, mas o botão "Planejar Licença para Capacitação" caía
no catálogo. Agora ele abre a ferramenta. **Rota prevista: `/qualificacao/`** (página 7 do
`../mapa-paginas.md`).

**Escopo — instrucional, por decisão da comissão (09/07/2026, §4 do `../../../../shared/resumo-reuniao-2026-07-09.md`).**
Ele soma carga horária, monta o cronograma, reúne os links e imprime o plano. Não inscreve, não
emite declaração e não abre processo — isso vive no Moodle e na DGP, envolve bloqueio de curso e
exige autenticação.

**A conta.** Uma regra só, a do Cefor (pergunta 17 do FAQ): **30 horas de curso por semana de
licença**. Daí sai tudo:

```
carga horária mínima = ceil(dias ÷ 7 × 30h)     →  30 dias = 129h
```

129h é exatamente o número que a chamada da home já exibia.

### Uma tela, quatro blocos

A primeira versão tinha três passos em cartões, seis cartões de orientação, três blocos de aviso e
cinco perguntas de FAQ. Virou página de leitura, não ferramenta. Refeita em **uma tela só**:

| Bloco | O que faz | Requisito |
|---|---|---|
| **Barra de controles** (fixa no topo) | dias em *chips* (15/30/45/60/90/outro), data de início e, à direita, o quanto você precisa somar | PLC-01, PLC-02 |
| **Medidor** | número grande do que já foi somado, barra e selo de estado — dourado enquanto falta, verde quando fecha | PLC-04 |
| **Cursos do plano** | lista com o fundo preenchido na proporção da carga horária, título clicável e ×; abaixo, "Escolher cursos" e "Montar para mim" | PLC-03 |
| **Linha do tempo** | *gantt* simples com régua de datas e dois modos: **Juntos** ou **Em sequência** | FAQ 18 |

**Nenhum parágrafo solto.** Cada orientação virou uma linha presa ao controle a que se refere —
"mínimo de 30h de curso por semana" sob os dias, "o acesso ao curso só abre nesta data" sob a data,
"em todos os dias da licença você precisa estar cursando algo" sob a linha do tempo, e o aviso de
que a inscrição não é feita aqui ao lado do botão de imprimir.

### Como se inscrever — a parte que faltava

A inscrição para licença **não acontece aqui**: acontece dentro de cada curso, na atividade
*Licença para capacitação*, onde o servidor informa as datas e emite a declaração do processo. Sem
isso o plano não vira nada. A página ganhou uma seção com **os seis prints reais do ambiente**,
baixados da página oficial do Cefor (https://mooc.cefor.ifes.edu.br/v/licenca-capacitacao/) para
`assets/licenca/` — a explicação é a imagem, não o parágrafo; clicar abre em tamanho real. A fonte
integral, com o que cada print mostra, está em
`../../references/licenca-capacitacao-pagina-oficial.md`.

Abaixo dos prints, cinco regras que mudam decisão: salvar a declaração **no mesmo dia** (o curso é
desabilitado no dia seguinte), as datas saem **na declaração e no certificado**, a oferta é
**anual**, o certificado só sai **na data de fim**, e quem não vai usar o curso para licença **não
deve preencher as datas**.

**A regra da oferta anual virou validação:** se o período informado atravessa a virada do ano, o
medidor exibe um aviso — nenhum curso pode começar em um ano e terminar no seguinte.

**Escolher cursos é um `<dialog>`**, não uma lista embutida: busca, fita de áreas roláveis e os 155
cursos com "+"/"✓". A tela principal fica com o plano, não com o catálogo. O rodapé do diálogo
mostra o total somado enquanto a pessoa marca, então dá para fechar a meta sem sair dele.

**"Montar para mim"** é guloso: pega os maiores primeiro para fechar com poucos cursos e escolhe,
para a última vaga, o menor curso que ainda resolve o que falta — o excesso fica no mínimo (para 30
dias fecha em 130h com 3 cursos, 1h acima da meta). Respeita o filtro de área ativo e tudo pode ser
trocado na mão depois.

**Os dois ritmos vêm do FAQ 18**, não foram inventados: ou a mesma data em todos os cursos, ou um
após o outro. No sequencial o período é dividido na proporção da carga horária, e nenhuma data sai
do período declarado — nem no caso extremo de haver mais cursos do que dias.

**O plano impresso (PLC-05)** é um bloco separado, montado por JS e escondido na tela: só aparece no
`@media print`, em preto, numa página. Ele é o que a pessoa leva para o processo, então carrega o
que a tela não precisa mostrar:

- **tabela com uma caixa para marcar por curso**, o **endereço da sala** em texto (no papel ninguém
  clica) e **as datas exatas a informar naquele curso**;
- os **sete passos da inscrição**, na ordem das telas do ambiente;
- as regras de "Atenção" — declaração no mesmo dia, datas na declaração e no certificado, oferta
  anual, não preencher datas em curso que não é para licença, e procurar a gestão de pessoas;
- o endereço da página oficial do Cefor, para o passo a passo completo.

**Dados.** O mesmo `cursos-dados.js`. Entram os **155 cursos** com carga horária conhecida e não
obsoletos — dos 165, ficam de fora 9 sem carga informada (não dá para somar o que não se sabe) e 1
marcado como obsoleto. Sem back-end e sem login (PLC-08); o plano fica no `localStorage` e a página
funciona igual se ele estiver bloqueado (é o caso ao abrir por `file://`).

### Consertos que apareceram no caminho

- **O header quebrava entre 861px e ~1150px, em todas as páginas v3.** A `.main-nav` tem
  `min-width: 0` com `justify-self: end`: quando os links não cabem, o excedente vaza para a
  esquerda e passa **por cima do nome da marca**. O menu vira hambúrguer a partir de **1200px** (era
  860px) e, abaixo de 640px, o nome da marca sai e fica só o símbolo. Em `estilos-v3.css`, valendo
  para home, catálogo, projeto e planejador. Conferido em 12 larguras, de 390px a 1920px.
- **Títulos com caracteres invisíveis.** "Acessibilidade em Processos Seletivos Discentes" carregava
  três `U+FFFC` da extração e exibia quadradinhos. `gerar-dados.mjs` agora limpa `U+FFFC`,
  zero-width e BOM do título. Regerado: o diff em `cursos-dados.js` é de 2 linhas, só desse curso.
- **Coerência de navegação.** "Licença capacitação" no menu e no rodapé de `index-v3`, `cursos-v3` e
  `projeto-v3` aponta para cá (antes ia para a âncora da home, que no catálogo nem existia); o
  exemplo na chamada da home passou de 126h para 130h (Canva 6h → Classroom 10h), porque exemplo que
  não fecha a meta de 129h ao lado do número 129h confunde.

**Verificado em navegador** (Chromium headless): render em 390px, 900px e 1360px, medidor, os dois
ritmos da linha do tempo, o diálogo de cursos e a folha de impressão. Além disso, uma bateria em
jsdom cobre o comportamento — 30 dias = 129h, 45 = 193h, 22 = 95h, sugestão fechando a meta,
cronograma dentro do período, filtro por área e por busca, documento montado. Falta o teste com
gente de verdade.

**Pendências:** PLC-09 (matrículas como prova social) ficou de fora — `cursos-dados.js` não tem esse
campo; entra quando o dump do WordPress chegar. O texto sobre o que é a licença e a base legal
**saiu da tela** nesta versão: se a comissão quiser essa explicação na página, ela volta como bloco
curto — e aí precisa ser validada com a DGP/Cefor. Sem versão EN.

## Limitações conhecidas / próximos passos
- **FR/ES** sem página própria — desde 20/07/2026 aparecem **desabilitados**, com selo "em breve", em vez de trocar só o rótulo (o que parecia bug). Integrar i18n de verdade no estágio 05 (WordPress/tema).
- Catálogo em EN mantém títulos de curso em pt-BR (decisão acima).
- Troca de idioma é por **página irmã** (sufixo `-en`), não por parâmetro/rota. No tema WordPress isso deve virar rota/locale.
- **Versão em inglês desatualizada** — trabalho em inglês pausado a pedido do cliente em 20/07/2026. Falta, em relação ao PT:
  - `index-en.html`: retirar o curso "Moodle para Educadores" dos mais cursados (renumerando os ranks e incluindo "Introdução à Libras") e aplicar o novo texto do planejador de licença.
  - `cursos-en.html`: desabilitar FR/ES no seletor de idioma (`data-soon` + `aria-disabled`), como já está nas outras três páginas.
- **Carrosséis da Home são estáticos** — "Em destaque", "Mais cursados" e "Recentes" estão fixos no HTML. A comissão pediu (09/07) que venham de consulta ao banco com janela temporal configurável; é requisito do estágio 05. As ordenações "Mais cursados"/"Recentes" do catálogo também não funcionam de fato: dependem de campos (`demanda`, `recente`) que não existem em `cursos-dados.js`.
