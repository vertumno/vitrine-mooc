# Mapa de Páginas — Vitrine MOOC Ifes

> **Estágio:** 03 — Design/UX · **Versão:** 1.4 · **Data:** 09/07/2026
> **Base:** `stages/02-catalogo/output/arquitetura-informacao.md` v4.1 (navegação/URLs) ·
> `design-system/design-system-oficial.md` (tokens, componentes e regras — canônico).
> **Protótipo canônico (vivo):** `stages/03-design-ux/output/canonico/` (Home + Catálogo, PT e EN — ver `canonico/README.md`).
> Protótipos anteriores arquivados em `_arquivo/` (ver README de lá).
> **Nome público da plataforma: "Cursos Abertos do Ifes"** — "Vitrine" é só codinome interno.

Cada página lista: **propósito**, **seções** (ordem de leitura), **dados exibidos** (com a fonte),
e **indexável?** (SEO). Metadados do curso seguem o **Art. 14 da Resolução CS 72/2020** e o
`catalogo-cursos-completo.csv`.

---

## Inventário de páginas

| # | Página | URL | Indexável | Protótipo canônico (`canonico/`) |
|---|--------|-----|:---------:|---------------------|
| 1 | Home | `/` | ✅ | `index.html` · `index-en.html` (EN) |
| 2 | Catálogo / Busca | `/cursos/` | ✅ | `cursos.html` · `cursos-en.html` (EN) |
| 3 | Página do curso | `/cursos/{slug}/` | ✅ | — (arquivado: `_arquivo/prototipo-vitrine-mooc/curso-como-criar-mooc.html`) |
| 4 | Área (categoria) | `/areas/{slug}/` | ✅ | — (arquivado: `_arquivo/prototipo-vitrine-mooc/area-educacao.html`) |
| 5 | Série | `/series/{slug}/` | ✅ | — |
| 6 | Projeto parceiro | `/v/{slug}/` (Rio Doce, UnAC) | ✅ | — |
| 7 | Licença Capacitação + Planejador | `/qualificacao/` | ✅ | `licenca-v3.html` (v3) |
| 8 | Certificação | `/certificacao/` | ✅ | — |
| 9 | Sobre | `/sobre/` | ✅ | — (arquivado: `_arquivo/prototipo-vitrine-mooc/sobre.html`) |
| 10 | Perguntas frequentes | `/faq/` | ✅ | — (arquivado: `_arquivo/prototipo-vitrine-mooc/perguntas-frequentes.html`) |

Combinações de faceta (`/cursos/?categoria=…&carga=…&publico=…`) = **não indexáveis** (`noindex`/canonical).

> **Removido (v1.2):** as páginas `/publicos/{slug}/` ("Para quem") foram eliminadas como páginas dedicadas. A navegação por público funciona apenas como **atalhos na Home** que apontam para o catálogo pré-filtrado (`/cursos/?publico=professores`). Justificativa: 107/165 cursos declaram 2+ públicos — páginas por audiência geram repetição e auto-exclusão falsa (ver `decisao-taxonomia-cenarios.md` §2b).

---

## 1. Home — `/`

**Propósito:** apresentar a Vitrine, orientar a descoberta e expor a demanda real. Público leigo, nacional, de descoberta.

**Seções (ordem):**
1. **Hero** — título/proposta de valor ("Cursos gratuitos e abertos do Ifes, com certificado"), **busca proeminente que envia para o catálogo** (`/cursos/?q=<termo>`, já pré-filtrado), CTA.
2. **Em destaque** — curadoria manual (CEFOR).
3. **Recentes** — últimos publicados (absorve levas trimestrais automaticamente).
4. **Mais cursados** — ordenado por matrículas (Power BI). Expõe demanda: Inglês, Moodle p/ Educadores, Canva, Google Drive.
5. **O que é curso MOOC? / Como funciona** — explicação do formato + passo a passo do cadastro ao certificado.
6. **Projetos e séries** — Projetos parceiros (Rio Doce Escolar, UnAC) e depois Séries (Lovelace, Educador Maker, etc.).
7. **Licença Capacitação** — chamada para servidores públicos + Planejador.
8. **Dúvidas (FAQ).**
9. **Faixa institucional / rodapé** — 4 colunas: marca + descrição · **Cursos Abertos** (Validar Certificado, Licença para Capacitação, Painel de Indicadores, Termos de Uso, Suporte) · **Institucional** (O Ifes, O Cefor, Base de Conhecimento) · **logo Ifes + tagline** ("Centro de Referência em Formação e em Educação a Distância"). Faixa base com "Ifes - Cefor". Detalhes em `design-spec.md` §2.7.

> **Alteração (v1.3):** removidos da Home os blocos **"Atalhos Para quem"** (`#publicos`) e **"Navegar por área"** (`#areas`). Após "O que é curso MOOC?", a ordem passou a ser **Projetos → Séries → Servidor público (Licença) → Dúvidas**. A navegação por público continua disponível como faceta no catálogo; as áreas seguem acessíveis pelo catálogo (`/cursos/`).

> **Alteração (v1.4):** rodapé reestruturado para as colunas **Cursos Abertos** e **Institucional** + bloco de marca Ifes/Cefor (conforme referência da comissão). Links institucionais (O Ifes, O Cefor, Licença) já resolvem; Validar Certificado, Painel de Indicadores, Termos de Uso, Suporte e Base de Conhecimento seguem como âncoras placeholder até definição dos destinos.

**Dados exibidos:** cards de curso (§dados abaixo) · nº de matrículas (Power BI, "Mais cursados").

---

## 2. Catálogo / Busca — `/cursos/`

**Propósito:** encontrar cursos por busca + facetas combináveis. Estrutura de referência: página de catálogo da DeepLearning.AI (destaques em carrossel no topo + grade com filtros laterais).

**Seções:**
1. **Hero do catálogo** (faixa teal, `.catalog-hero`) — kicker "Catálogo completo", título "Catálogo de cursos", texto de proposta de valor e dois **stat cards em glass** (total de cursos publicados + nº de áreas temáticas). Fundo com profundidade em camadas (gradiente diagonal teal→teal-deep→teal-dark + halos radiais + textura de pontos que esmaece na base). Altura compacta (`padding` vertical ~32–50px).
2. **Cursos em destaque** _(planejado, ausente no canônico v1)_ — carrossel com card grande (imagem + título + descrição + chips + carga/nível + CTAs "Saber mais"/"Começar agora"), curadoria CEFOR, indicadores de navegação (dots).
3. Facetas em **sidebar** com checkboxes e contagem por faceta (desktop; bottom-sheet mobile): Categoria (15) · Para quem · Carga horária (≤10/10–20/20–40/40–60h) · Nível · **Idioma** · Acessibilidade (Libras/AD) · Projetos · Séries. Busca (título + tags, tolerante a acento) no topo da sidebar + "Limpar filtros".

> **Alteração (20/07/2026):** a faceta **Idioma** passou de prevista a implementada, a pedido da comissão em 09/07 (Vanessa pediu, Elton aceitou). Fica entre Nível e Acessibilidade. Contagens atuais: Português 165 · Inglês 4 · Espanhol 4 · Pomerano 1 — o ganho de navegação é pequeno hoje e a faceta é sobretudo preparação para o Centro Virtual de Idiomas, como a própria Vanessa reconheceu ("poucos ainda, mas vai começar a treinar"). **Libras não entra aqui** (é acessibilidade, decisão do Marquito), e **audiodescrição ainda não é faceta** porque nenhum curso tem o recurso. Detalhes de normalização em `design-spec.md` §2.3.
4. **"Mostrando N cursos"** + título "Todos os cursos" + Ordenação: Relevância · Mais cursados · Recentes · A–Z.
5. Grade de cards com CTA por card (paginação/scroll com fallback rastreável).
6. Estado vazio (microcopy + sugestões).

**Dados:** total de cursos publicados e nº de áreas (hero); cards de curso; contagem por faceta; total de resultados.

> **Alteração (v1.4):** hero do catálogo redesenhada para o nível de acabamento do restante do canônico. Substituiu a faixa teal "chapada" (título + duas caixas brancas) por: eyebrow em pill com ponto dourado, título com trecho destacado em `teal-soft`, fundo em camadas (halos + textura de pontos com máscara) e **stat cards em glass** (`backdrop-filter`, ícone em chip, filete dourado no topo, elevação no hover) — coerentes com os `.stat` da Home. Altura reduzida a pedido. Aplicada em `canonico/cursos.html` e `canonico/cursos-en.html` (mesma estrutura, cópia PT/EN); CSS em `canonico/estilos.css` (`.catalog-hero`, `.catalog-hero-decor`, `.catalog-hero .kicker`, `.summary-box`, `.summary-icon`, `.summary-label`).

---

## 3. Página do curso — `/cursos/{slug}/`

**Propósito:** apresentar o curso e levar à matrícula no Moodle. **1 URL canônica por curso.**

**Seções:**
1. **Hero:** título, categoria(s), selos (Libras/AD/Idioma), carga horária, nível, botão primário "Acessar no Moodle".
2. **Sobre o curso:** descrição, objetivos de aprendizagem.
3. **Conteúdo programático** · **Metodologia** · **Processo de avaliação** · **Certificação** (≥60%).
4. **Ficha (sidebar):** carga horária · nível · idioma · provedor/projeto · certificação · elegível p/ Licença Capacitação.
5. **Cursos relacionados** (mesma categoria/série).

**Dados exibidos (fonte `catalogo-cursos-completo.csv` + Art. 14):**

| Campo | Fonte | Obrigatório |
|-------|-------|:---:|
| título, descrição, conteúdos, metodologia, avaliação | CSV / WP | ✅ |
| categorias[] (15) | taxonomia v4.1 | ✅ |
| carga_horaria | CSV (`carga_horaria`) | ✅ |
| idioma, nível | CSV / Art. 14 | ✅ |
| público-alvo | CSV | ✅ |
| professores/instrutores | CSV | ➖ |
| selos: libras, audiodescrição | CSV/metadado | ➖ |
| link_curso (Moodle) | CSV | ✅ |
| imagem/thumb | CSV | ✅ |
| série / projeto | editorial | ➖ |
| badge "Novo" (< 3 meses) | derivado da data | ➖ |
| Área CNPq, Eixo Tecnológico | metadado oficial (registro) | ✅ (não navegação) |

---

## 4. Área (categoria) — `/areas/{slug}/`

**Propósito:** página editorial indexável por tema (SEO — 65% das matrículas vêm de fora do ES).

**Seções:** título + texto introdutório da área · grade de cursos da categoria · facetas locais (carga/idioma/acessibilidade) · áreas relacionadas.

**Dados:** cards da categoria; contagem; texto editorial por área. **Slug:** uma das 15 categorias (`ambiente-e-saude`, `educacao`, `tecnologias-e-informatica`, …).

---

---

> **Nota (v1.2):** a página dedicada "Para quem (público)" (`/publicos/{slug}/`) foi **removida**. A autoidentificação por público agora funciona exclusivamente como **atalhos na Home** (seção 1, item 2) que direcionam para o catálogo pré-filtrado (`/cursos/?publico=professores`). O filtro "Para quem" continua disponível como **faceta** na sidebar do catálogo (página 2).

## 5. Série — `/series/{slug}/`

**Propósito:** contar a história de uma coleção de marca/produção.

**Séries:** Atendente e Vendedor (3, com níveis) · Educador Maker (4) · Lovelace (6) · Embrace (3, todos com bandeira da Gra-Bretanha e bandeira da Espanha) · Lesson Study (PT/EN = mesmo curso, versão em inglês sinalizada pela bandeira da Gra-Bretanha).

**Seções:** identidade da série · sequência sugerida de cursos · grade.

---

## 6. Projeto parceiro — `/v/{slug}/`

**Propósito:** hub de projeto com identidade institucional.

**Projetos:** **Rio Doce Escolar** (`/v/riodoce/`, 31 cursos) · **UnAC** (`/v/unac/`, 33 cursos — Universidade Aberta Capixaba, parceria Ifes/CEFOR × Governo do ES; ver `projetos-especiais.md`).

**Seções:** descrição oficial do projeto/parceria · logo · grade de cursos associados.

---

## 7. Licença Capacitação + Planejador — `/qualificacao/`

**Propósito:** serviço para servidores públicos (não é filtro de conteúdo).

**Seções (protótipo `canonico/licenca-v3.html`):** faixa de título · **barra de controles** (dias em
chips, data de início, carga mínima) · **medidor** (somado × mínimo) · **cursos do plano** +
**linha do tempo** lado a lado · botão de imprimir · **"Como se inscrever em cada curso"**, com os
seis prints reais do ambiente. Escolher curso abre um `<dialog>` com busca e filtro por área.

**Fonte do procedimento:** `references/licenca-capacitacao-pagina-oficial.md` (página oficial do
Cefor, capturada em 22/07/2026). A inscrição para licença é feita **dentro de cada curso**, na
atividade *Licença para capacitação* — por isso o plano impresso leva o endereço da sala de cada
curso, as datas a informar em cada um e o passo a passo. Regras que viraram comportamento: oferta
anual (o planejador avisa se o período atravessa o ano) e declaração emitida no mesmo dia.

**Regra de cálculo:** carga horária mínima = `ceil(dias ÷ 7 × 30h)` — a referência de 30h de curso por
semana é a do Cefor (FAQ 17). 30 dias → 129h, o mesmo número exibido na chamada da Home.

**Dados:** `cursos-dados.js` — entram os 155 cursos com carga horária conhecida e não obsoletos.
Período e dias são informados pelo usuário. Funciona sem autenticação e sem back-end (PLC-08).

**Escopo:** instrucional, conforme decisão da comissão em 09/07/2026 — soma carga horária, monta
cronograma, reúne links e imprime o plano. Não inscreve, não emite declaração, não abre processo.

---

## 8. Certificação — `/certificacao/`

**Propósito:** explicar como funciona o certificado (aproveitamento ≥60%, autoinstrucional, sem tutoria). Página indexável (busca "curso gratuito com certificado").

---

## 9. Sobre — `/sobre/`

**Propósito:** o que é a Vitrine MOOC, o CEFOR/Ifes, o objetivo (Resolução CS 72/2020 — democratização/inclusão), como participar.

---

## 10. Perguntas frequentes — `/faq/`

**Propósito:** dúvidas comuns (como me inscrevo, certificado, gratuidade, pré-requisitos, Libras). Formato acordeão. Schema `FAQPage` para AEO.

---

## Dados do card de curso (referência única)

Usado em toda grade (home, catálogo, área, público, série, projeto):

`imagem` · `ribbon_libras?` · `badge_novo?` · `categorias[]` (chips) · `titulo` ·
`carga_horaria` · `serie/projeto?` · `idiomas[]` (`en`/`es`, sem `pt`; visual = bandeiras) · `link → /cursos/{slug}/`.

Fonte: `stages/02-catalogo/output/catalogo-cursos-completo.csv`. Para a série Embrace, a coluna `idioma` registra "Português, Inglês e Espanhol"; na UI, português é implícito e os selos exibidos são as bandeiras da Gra-Bretanha e da Espanha.

---

## Versões de idioma (multilíngue)

O protótipo canônico tem **seletor de idioma** no topo (PT · EN · FR · ES). No protótipo estão prontas as versões **PT (padrão)** e **EN**:

| Página | pt-BR | English |
|--------|-------|---------|
| Home | `index.html` | `index-en.html` |
| Catálogo / Busca | `cursos.html` | `cursos-en.html` |

- **Interface traduzida**; **títulos oficiais dos cursos permanecem em pt-BR** (decisão do cliente — teste de visualização). Detalhes de i18n em `design-spec.md §3.6`.
- **FR/ES** ainda são placeholder no seletor (sem página) — conteúdo entra no estágio 05.
- No tema WordPress, a troca por sufixo `-en` deve virar **rota/locale** real.

---

## Rastreabilidade

- **Cobertura:** as 10 páginas cobrem toda a navegação da arquitetura v4.2 (Categorias, Séries, Projetos, Licença, Certificação, Sobre, FAQ). "Para quem" funciona como atalho na Home + faceta no catálogo (sem página própria).
- **Protótipos oficiais:** Home e Catálogo prontos em `prototipo-cursos-abertos/` (design system oficial). As demais páginas serão recriadas lá gradualmente; as versões antigas estão em `_arquivo/prototipo-vitrine-mooc/` apenas como consulta.
- **Escopo:** 165 cursos publicados (os 65 "em produção" ficam fora — ver `arquitetura-informacao.md` v4.2).
