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

## Limitações conhecidas / próximos passos
- **FR/ES** sem página própria — desde 20/07/2026 aparecem **desabilitados**, com selo "em breve", em vez de trocar só o rótulo (o que parecia bug). Integrar i18n de verdade no estágio 05 (WordPress/tema).
- Catálogo em EN mantém títulos de curso em pt-BR (decisão acima).
- Troca de idioma é por **página irmã** (sufixo `-en`), não por parâmetro/rota. No tema WordPress isso deve virar rota/locale.
- **Versão em inglês desatualizada** — trabalho em inglês pausado a pedido do cliente em 20/07/2026. Falta, em relação ao PT:
  - `index-en.html`: retirar o curso "Moodle para Educadores" dos mais cursados (renumerando os ranks e incluindo "Introdução à Libras") e aplicar o novo texto do planejador de licença.
  - `cursos-en.html`: desabilitar FR/ES no seletor de idioma (`data-soon` + `aria-disabled`), como já está nas outras três páginas.
- **Carrosséis da Home são estáticos** — "Em destaque", "Mais cursados" e "Recentes" estão fixos no HTML. A comissão pediu (09/07) que venham de consulta ao banco com janela temporal configurável; é requisito do estágio 05. As ordenações "Mais cursados"/"Recentes" do catálogo também não funcionam de fato: dependem de campos (`demanda`, `recente`) que não existem em `cursos-dados.js`.
