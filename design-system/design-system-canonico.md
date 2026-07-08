# Design System Canonico - Cursos Abertos do Ifes

> Status: referencia derivada do prototipo `stages/03-design-ux/output/canonico/index.html`, validado para apresentacao em 08/07/2026.
> Fonte visual: `stages/03-design-ux/output/canonico/estilos.css`.
> Uso: orientar ajustes no prototipo canonico e a futura traducao para tema/blocos WordPress.

Este design system registra a direcao visual do prototipo Canonico. Ele nao substitui automaticamente o `design-system-oficial.md`; quando houver conflito entre os dois, trate este arquivo como a leitura fiel do prototipo `canonico` e use a decisao humana mais recente para consolidar a versao oficial.

---

## 1. Principio Visual

A interface deve parecer uma vitrine publica, clara e confiavel, com energia de plataforma educacional aberta. A marca institucional continua presente, mas a experiencia deixa de ser "portal governamental verde" e passa a ser uma descoberta mais leve: fundo aqua muito claro, hero com imagem realista/educacional, superficies brancas e teal como cor de navegacao.

Assinatura visual:

- hero centralizado com imagem de fundo e camada aqua translucida;
- grid sutil no fundo da pagina, lembrando organizacao/catalogo;
- cards brancos com sombra macia, imagem original do curso no topo e CTA textual;
- cobre profundo usado no CTA principal e em acoes de alta prioridade; dourado reservado para selo de novidade e apoios pontuais;
- linguagem direta, publica e sem jargao interno.

Nome publico da plataforma: **Cursos Abertos do Ifes**.

Nao usar "Vitrine" em textos visiveis da interface, exceto em documentos internos.

---

## 2. Tokens CSS

```css
:root {
  --paper: #eefaf7;
  --paper-soft: #f7fbf9;
  --surface: #ffffff;
  --ink: #16272d;
  --ink-soft: #5d6b70;
  --line: #d8e5e2;

  --teal: #008080;
  --teal-deep: #0d5d66;
  --teal-dark: #07394f;

  --green: #147a02;
  --green-deep: #195128;

  --gold: #ffbc00;
  --red: #d43b35;
  --accent-action: #a85a32;
  --accent-action-deep: #874527;
  --accent-action-soft: #fff1e8;

  --shadow: 0 18px 44px rgba(7, 57, 79, .14);
  --shadow-soft: 0 10px 28px rgba(7, 57, 79, .08);

  --radius: 8px;
  --maxw: 1180px;
  --stats-height: 196px;

  --display: "Nunito Sans", "Open Sans", Arial, sans-serif;
  --body: "Open Sans", Arial, sans-serif;
}
```

### Uso das cores

| Token | Uso principal | Observacao |
|-------|---------------|------------|
| `--paper` | Fundo do hero e areas aqua | Deve aparecer como atmosfera leve, nao como bloco pesado |
| `--paper-soft` | Fundo geral da pagina | Base de leitura da vitrine |
| `--surface` | Cards, filtros, paineis, FAQ | Usar com sombra suave ou borda leve |
| `--ink` | Texto principal | Mais frio que o neutro institucional anterior |
| `--ink-soft` | Metadados, descricoes, textos secundarios | Evita excesso de contraste nos cards |
| `--line` | Bordas de header, filtros e inputs | Linha clara, sempre discreta |
| `--teal` | CTA principal, categorias, bordas ativas | Cor central da experiencia canonica |
| `--teal-deep` | Hover, links e textos de acao | Mantem legibilidade sem escurecer demais |
| `--teal-dark` | Header textual, topbar, footer, hero interno | Cor estrutural mais forte |
| `--green` | Marca Ifes no selo/brand mark | Usar como ancora institucional, nao como cor dominante |
| `--gold` | Selo NOVO, bullets de servico e apoios pontuais | Sempre com texto escuro |
| `--red` | Ponto de destaque do kicker e alertas | Uso pontual |
| `--accent-action` | CTA principal e acoes de alta prioridade | Cobre profundo quente, harmonico com teal, sempre com texto branco |
| `--accent-action-deep` | Hover do CTA principal | Mantem contraste e profundidade no estado hover |
| `--accent-action-soft` | Fundo suave para estados, avisos editoriais ou badges quentes | Usar com texto escuro, nunca como CTA principal |

### Estudo do acento de acao

O amarelo original (`--gold`) funcionava como destaque alegre, mas competia com selos e elementos editoriais. O vermelho anterior (`#c7352f`) tinha contraste adequado, porem comunicava alerta/erro. Para uma cor que sera usada em varios lugares, o acento precisa ser quente, confiavel e reutilizavel.

| Candidato | Hex | Contraste com branco | Leitura visual |
|-----------|-----|----------------------|----------------|
| Vermelho alerta | `#c7352f` | 5.28:1 | Forte, mas perto demais de erro |
| Coral queimado | `#b85a3c` | 4.60:1 | Bom, mas no limite para texto pequeno |
| **Cobre profundo** | `#a85a32` | **5.03:1** | Melhor equilibrio: quente, adulto, harmonico com teal |
| Tijolo vivo | `#b9472f` | 5.24:1 | Presente, mas ainda muito vermelho |
| Mostarda queimado | `#b86f12` | 3.95:1 | Harmonico, mas falha para texto branco normal |

Decisao: usar `--accent-action: #a85a32` para CTAs principais. Ele mantem energia de acao sem parecer erro e conversa melhor com o fundo aqua, o teal estrutural e as imagens educacionais da hero.

---

## 3. Tipografia

```css
@import url("https://fonts.googleapis.com/css2?family=Nunito+Sans:wght@600;700;800&family=Open+Sans:wght@400;600;700;800&display=swap");

:root {
  --display: "Nunito Sans", "Open Sans", Arial, sans-serif;
  --body: "Open Sans", Arial, sans-serif;
}
```

| Papel | Fonte | Peso | Uso |
|-------|-------|------|-----|
| Display | Nunito Sans | 700-800 | H1, H2, H3, numeros de indicadores, marca verbal |
| Corpo | Open Sans | 400-700 | Paragrafos, navegacao, formularios, metadados |
| UI de acao | Open Sans | 600 | Botoes, pilulas, navegacao e chips; evita aspecto bruto em controles compactos |
| UI forte | Open Sans | 700 | Links de acao, categorias e titulos pequenos; reservar 800 para marca e numeros grandes |

Escala usada no prototipo:

```css
h1.hero { font-size: clamp(2.45rem, 5vw, 4.35rem); }
h1.catalog { font-size: clamp(2rem, 4vw, 3.15rem); }
h2.section { font-size: clamp(1.6rem, 3vw, 2.35rem); }
.lead { font-size: clamp(1rem, 1.35vw, 1.22rem); }
body { font-size: 16px; line-height: 1.55; }
```

Nao usar fonte monoespacada. Numeros, rankings e metadados permanecem em Open Sans ou Nunito Sans.

---

## 4. Layout

### Container

- Largura maxima: `1180px`.
- Respiro lateral desktop/mobile: `calc(100% - 40px)`, reduzindo para `100% - 28px` em telas pequenas.
- Secoes padrao: `64px 0`.
- Cards e controles usam raio de `8px`, evitando aparencia pill.

### Fundo

O fundo geral usa `--paper-soft` e um grid fixo muito sutil:

```css
body::before {
  opacity: .36;
  background-image:
    linear-gradient(rgba(0, 128, 128, .05) 1px, transparent 1px),
    linear-gradient(90deg, rgba(0, 128, 128, .05) 1px, transparent 1px);
  background-size: 28px 28px;
}
```

Use o grid apenas como textura de sistema. Ele nao deve competir com conteudo, imagens ou cards.

---

## 5. Componentes

### Skip link

Link de acessibilidade posicionado fora da tela e revelado no foco. Fundo `--teal-dark`, texto branco.

### Topbar

- Fundo `--teal-dark`.
- Altura minima: `34px`.
- Texto: `0.78rem`, cor `#d7efec`.
- Conteudo em duas pontas: instituicao e contexto da pagina.

Exemplos:

- "Instituto Federal do Espirito Santo - Cefor"
- "Plataforma publica de cursos abertos"
- "Catalogo publico de cursos abertos"

### Header

- Sticky no topo.
- Altura: `78px`.
- Fundo translucido `rgba(247, 251, 249, .88)`.
- Borda inferior `rgba(216, 229, 226, .85)`.
- Blur: `backdrop-filter: blur(16px)`.

Brand:

- Texto: "Cursos Abertos".
- Marca circular verde `--green`, 38px, texto branco "IF".
- Cor do texto: `--teal-dark`.
- Peso: Nunito Sans 800.

Navegacao:

- Links pequenos (`0.86rem`), peso 700.
- Estado normal `--ink-soft`.
- Hover e pagina atual `--teal-dark`.

### Botoes

Base:

```css
.btn {
  min-height: 44px;
  border-radius: var(--radius);
  padding: 0 18px;
  font-weight: 600;
}
```

Variantes:

| Classe | Fundo | Texto | Uso |
|--------|-------|-------|-----|
| `.btn-primary` | `--teal` | branco | CTA global, carregar mais, acessar Moodle |
| `.btn-accent` | `--accent-action` | branco | CTA principal da hero e acoes de alta prioridade |
| `.btn-gold` | `--gold` | `#17262c` | Chamada de servico e apoios pontuais |
| `.btn-outline` | branco translucido | `--teal-dark` | Acao secundaria |

Hover: `translateY(-1px)`. Active retorna para `0`.

Regra de peso: botoes usam `font-weight: 600`. Evitar `700/800` em CTAs como "Explorar cursos" e "Como funciona", porque deixa a interface mais pesada e menos convidativa.

### Hero da home

Estrutura:

- fundo visual com `picture.hero-bg`;
- imagem desktop: `assets/hero-ifes-desktop.png`;
- imagem mobile: `assets/hero-ifes-mobile.png`;
- overlay aqua por gradiente e radial;
- conteudo centralizado, largura maxima `850px`;
- nota flutuante lateral apenas em desktop;
- faixa de indicadores encaixada na base.

Regras:

- H1 deve comecar com "Cursos Abertos do Ifes".
- Segunda linha pode usar destaque em `--teal`.
- Kicker usa ponto vermelho antes do texto.
- CTAs: cobre profundo para "Explorar cursos", outline para acao secundaria.
- A imagem deve ser legivel e nao escurecida. A camada aqua suaviza, mas nao deve borrar a identidade visual.

### Faixa de indicadores

- Fundo `#14767c`.
- Texto branco.
- Grid desktop: texto editorial + 4 indicadores.
- Altura controlada por `--stats-height`.
- No mobile, `--stats-height` muda para `520px` e os indicadores empilham.

Indicadores usados no prototipo:

- `164+` cursos validos;
- `68 mil+` matriculas em 2025;
- `65%` fora do ES;
- `33%` certificacao media.

Esses numeros devem ser revisados quando houver atualizacao dos paineis do projeto.

### Cabecalho de secao

- Layout flex: titulo/descricao a esquerda, link textual a direita.
- H2 em `--teal-dark`.
- Descricao em `--ink-soft`.
- Em telas pequenas, empilhar.

### Card de curso

Estrutura:

1. `.course-media`
2. imagem original do curso
3. ribbons opcionais
4. `.course-body`
5. categoria
6. titulo
7. metadados
8. CTA textual

Regras visuais:

- Fundo branco.
- Radius `8px`.
- Sombra `--shadow-soft`; hover usa `--shadow`.
- Imagem em `aspect-ratio: 274 / 188` e `object-fit: cover`.
- CTA textual: "Acessar curso", cor `--teal-deep`, peso 800.
- Categoria: `--teal-deep`, `0.76rem`, peso 800.
- Metadados: `--ink-soft`, `0.78rem`.

Ribbons:

- Posicao: canto superior direito da imagem.
- Tamanho minimo: 28px.
- Fundo padrao: `--teal-dark`, texto branco.
- `.alt`: `--red`.
- `.gold`: `--gold`, texto escuro.

Rotulos usados:

- `LIB` para curso com Libras;
- `NOVO` para recentes;
- `UnAC` para projeto;
- `S` para serie no catalogo.

### Card ranqueado

Usa `.rank-card .course-body::before` com `data-rank`.

- Numero grande em Nunito Sans.
- Cor `rgba(0, 128, 128, .2)`.
- Nao usar fonte mono.

### Pilulas de area

Apesar do nome, visualmente seguem o radius global, nao pill total.

- Fundo branco.
- Borda `rgba(0, 128, 128, .18)`.
- Texto `--teal-dark`, peso 600, tamanho aproximado `.95rem`.
- Contagem em `small`, `--ink-soft`, peso 600.
- Evitar peso 800 nas pilulas; em labels longos como "Financas e Contabilidade" e "Tecnologias Educacionais", o peso alto cria blocos escuros e reduz a sofisticacao visual.

### Cards por perfil

- Grid de 4 no desktop, 2 no tablet, 1 no mobile.
- Fundo branco.
- Borda superior de 4px em `--teal`.
- Sombra `--shadow-soft`.
- Titulo em `--teal-dark`, descricao em `--ink-soft`.

### Faixa de servico

Usada em "licenca capacitacao".

- Fundo `--teal-dark`.
- Texto branco.
- Layout em duas colunas.
- Painel lateral branco com sombra forte.
- Bullets usam ponto dourado.

### Como funciona

- Grid 50/50 no desktop.
- Lista de fatos em cards compactos com borda esquerda teal.
- Passos numerados com contador CSS, fundo `--teal`, texto branco.
- Numeracao existe porque a ordem do processo importa.

### FAQ

- Usar `details` e `summary` nativos.
- Fundo branco, radius `8px`, sombra suave.
- Summary com peso 800 e cor `--teal-dark`.
- Resposta em `--ink-soft`.

### Footer

- Fundo `--teal-dark`.
- Texto secundario `#c4ddda`.
- Titulos brancos.
- Grid: coluna institucional maior + 3 colunas de links.
- Base final com divisoria branca a 10%.

---

## 6. Catalogo

### Hero interno do catalogo

- Classe: `.catalog-hero`.
- Fundo `--teal-dark`.
- Padding: `44px 0 38px`.
- Grid: texto + resumo numerico.
- Kicker em `#9ce0d9`.
- Cards de resumo brancos quase opacos.

Resumo padrao:

- total de cursos publicados;
- 15 areas canonicas.

### Layout de filtros

Desktop:

- Grid: `285px` para filtros + conteudo fluido.
- Gap: `34px`.
- Filtros sticky com `top: 96px`.
- Altura maxima: `calc(100dvh - 118px)`.

Mobile/tablet:

- Uma coluna.
- Filtros deixam de ser sticky.

### Filtros

- Painel branco com sombra suave.
- Inputs e selects: fundo `#f7fbf9`, borda `--line`, radius `8px`, padding `11px 12px`.
- Grupos com titulo `0.92rem`, peso 800.
- Opcoes com checkbox nativo e `accent-color: --teal`.
- Contagem de filtros em `--teal-deep`.

Grupos canonicos:

- Area;
- Carga horaria;
- Nivel;
- Acessibilidade;
- Projetos;
- Series.

### Toolbar

- Contagem de resultados acima.
- Titulo "Todos os cursos".
- Ordenacao em select com rotulo "Ordenar".
- Chips ativos abaixo.

Ordenacoes:

- Relevancia;
- Mais cursados;
- Recentes;
- A-Z.

### Estado vazio

- Bloco branco.
- Borda tracejada `--line`.
- Texto centralizado em `--ink-soft`.
- Mensagem: "Nenhum curso encontrado com esses filtros. Tente remover uma selecao ou buscar por outro termo."

---

## 7. Responsividade

Breakpoints do prototipo:

| Largura | Mudanca |
|---------|---------|
| `max-width: 1060px` | Indicadores reorganizam; grids de cursos/perfis viram 2 colunas; catalogo vira 1 coluna |
| `max-width: 860px` | Menu principal recolhe; CTA do header some; nota do hero some; grids 2 colunas viram layouts simples |
| `max-width: 640px` | Stats empilham; grids viram 1 coluna; botoes do hero ocupam largura confortavel; header e topbar reduzem |

Regras:

- Nunca deixar texto de botao quebrar de forma apertada.
- Em mobile, o hero deve continuar com foco no titulo e nos CTAs, sem depender da nota lateral.
- Cards de curso precisam preservar proporcao da imagem.
- O filtro do catalogo deve aparecer antes dos resultados, como no prototipo.

---

## 8. Acessibilidade

- Manter skip link para `#conteudo`.
- Usar `aria-label` em navegacao, hero e blocos de indicadores.
- `aria-current="page"` no item ativo do menu.
- `aria-live="polite"` na contagem e grid do catalogo.
- Foco visivel: `outline: 3px solid rgba(255, 188, 0, .82)`.
- Respeitar `prefers-reduced-motion: reduce`.
- Texto sobre dourado sempre escuro.
- Texto sobre teal escuro sempre branco ou tons muito claros.

---

## 9. Conteudo e Microcopy

Tom: direto, publico, prestativo, sem venda exagerada.

Termos preferidos:

- "Cursos Abertos do Ifes";
- "gratuito, on-line e com certificado";
- "Acessar curso";
- "Todos os cursos";
- "Catalogo de cursos";
- "Licenca capacitacao";
- "Perguntas frequentes".

Evitar:

- "Vitrine" em interface publica;
- "R$ 0" como metrica de gratuidade;
- nomes tecnicos internos, como CPT, ACF, taxonomia legada;
- promessas de certificado sem mencionar criterio/aproveitamento quando o contexto exigir.

Mensagem sobre e-mail:

> Hotmail e Outlook podem bloquear mensagens automaticas. Verifique o spam ou use outro provedor de e-mail, como Gmail ou e-mail institucional.

---

## 10. Do's e Don'ts

Fazer:

- Usar imagens reais dos cursos nas capas.
- Manter uma acao principal por card: "Acessar curso".
- Usar teal como cor de experiencia e verde como ancora institucional.
- Aplicar dourado com parcimonia.
- Preservar cards claros e escaneaveis.
- Revisar numeros de indicadores quando houver dados atualizados.

Nao fazer:

- Misturar Poppins/Oswald do design system anterior dentro desta direcao sem decisao explicita.
- Transformar todos os botoes em pills.
- Usar gradientes decorativos no lugar da imagem do hero.
- Colocar muitos selos no card a ponto de cobrir a imagem.
- Usar texto branco sobre dourado.
- Reintroduzir fonte monoespacada.

---

## 11. Mapeamento para WordPress

Quando esta direcao for levada ao tema WordPress:

- criar tokens CSS globais no `theme.json` ou no CSS base;
- self-hostar Nunito Sans e Open Sans sempre que possivel;
- transformar card de curso em bloco/componente reutilizavel;
- manter `aspect-ratio: 274 / 188` para thumbnails herdadas;
- usar campos do curso para categoria canonica, carga horaria, nivel, Libras, projeto e serie;
- manter filtros com inputs nativos e estados acessiveis;
- separar hero da home, hero do catalogo e faixa de servico como componentes distintos.

---

## 12. Fontes

- Prototipo home: `stages/03-design-ux/output/canonico/index.html`
- Prototipo catalogo: `stages/03-design-ux/output/canonico/cursos.html`
- CSS fonte: `stages/03-design-ux/output/canonico/estilos.css`
- Imagens hero: `stages/03-design-ux/output/canonico/assets/hero-ifes-desktop.png` e `hero-ifes-mobile.png`


