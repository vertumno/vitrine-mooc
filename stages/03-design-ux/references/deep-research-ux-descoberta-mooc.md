# Deep Research — UX de Descoberta em Vitrines MOOC

> **Squad:** deep-research (pipeline completo: Classificação → Diagnóstico → Execução → QA → Síntese)
> **Orquestrador:** research-chief · **Data:** 01/07/2026
> **Escopo:** padrões de UX de descoberta (busca, filtros, taxonomia, cards, performance, acessibilidade) aplicáveis à nova Vitrine MOOC do Ifes (~165–230 cursos, redesign, mobile-first).
> **Uso pretendido:** referência de entrada para o Estágio 03 (Design/UX) e, parcialmente, o Estágio 02 (taxonomia).
> **Rastreabilidade:** referencia os requisitos de `stages/01-descoberta/output/` (FR-*, NFR-*).

---

## 1. Sumário executivo

1. **Filtros facetados são o maior alavancador de descoberta — e o mais mal executado do mercado.** A Baymard estima que apenas ~16% dos sites oferecem uma experiência de filtro realmente eficaz, e que filtros bem-feitos podem elevar conversão em ~26%. A Vitrine atual tem filtro de **categoria única** (um slug por vez); o salto de maior impacto é adotar **facetas multi-seleção** (categoria + tag) com contadores e chips de filtros ativos. `[Confiança: ALTA]`
2. **Busca e filtro atendem a intenções diferentes — os dois precisam coexistir bem.** "Spearfishers" (busca) querem o curso exato rápido; "browsers" (navegação por categoria) exploram. Boa *information scent* (rótulos descritivos + contadores) reduz tempo de navegação de forma expressiva e aumenta a tendência a explorar. `[Confiança: ALTA para o princípio; MÉDIA para os percentuais]`
3. **A busca da Vitrine já acerta o básico (normalização de acento) — falta autocomplete, tolerância a erro de digitação e ranqueamento.** Sugestões instantâneas (<100ms), *typo tolerance* e "você quis dizer…" são padrão consolidado e especialmente valiosos no mobile ("fat finger"). `[Confiança: ALTA]`
4. **Para catálogo grande, "Load More" > scroll infinito > paginação clássica.** A Baymard recomenda **Load More** para listas orientadas a tarefa (caso da Vitrine); scroll infinito prejudica orientação, acessibilidade e performance. Resolve o débito de renderizar ~230 cards de uma vez (NFR-03). `[Confiança: ALTA]`
5. **Cards são ótimos para *navegar*, mas fracos para *escanear resultados de busca*.** A recomendação é usar cards ricos no modo browse e considerar uma visão mais densa/lista no modo busca — além de padronizar `alt`, hierarquia visual e foco de teclado (corrige débitos de acessibilidade da Vitrine atual, NFR-02). `[Confiança: MÉDIA-ALTA]`

**Recomendação-âmbar (viés):** as melhores práticas vêm majoritariamente de e-commerce e de fornecedores de busca. Antes de redesenhar, **estabeleça uma linha de base com os dados que a Vitrine já coleta (Hotjar + Google Analytics)** para não otimizar no escuro (ver §4 e §6).

---

## 2. Desenho da pesquisa (Tier 0)

**🎯 Sackett — PICO (adaptado, não-clínico):**
- **P (contexto):** visitantes de uma vitrine MOOC pública em PT-BR, buscando cursos num catálogo de ~165–230 itens, majoritariamente mobile.
- **I (intervenção):** padrões de descoberta — busca (autocomplete, tolerância a acento/erro), filtros facetados, arquitetura de informação/taxonomia, design de cards, ordenação, paginação/lazy-load.
- **C (comparação):** padrão atual da Vitrine (busca client-side + filtro de categoria única + grid com todos os cards) e a mediana de mercado.
- **O (desfecho):** findability/success rate, tempo até "Acessar curso", conversão de clique, uso de busca vs filtro, bounce, acessibilidade (WCAG 2.2), performance (LCP).
- **Tipo:** therapeutic + prognostic. **Nível de evidência-alvo:** guidelines de alta credibilidade + estudos de HCI/e-learning + benchmark de plataformas reais (não há RCTs no domínio).

**📐 Booth — metodologia:** Scoping review + benchmarking competitivo (SALSA). Fontes: literatura cinza de UX (NN/g, Baymard, W3C, Material, USWDS), literatura acadêmica (ACM SIGIR, Springer, Open Praxis) e plataformas reais (Coursera, edX, FutureLearn; Lúmina/UFRGS, USP eaulas, FGV). Síntese narrativa temática + tabela comparativa.

**🔀 Creswell — design:** Qualitativo dominante + quant leve (QUAL+quant). Síntese temática apoiada por dados quantitativos quando disponíveis, integrados em *joint display* (padrão × evidência × exemplar × aplicação à Vitrine — ver §3.7).

**Classificação (research-chief):** UC-004 Evidence Synthesis (primário) + UC-003 Competitive Intelligence (secundário). Agentes ativados: Cochrane, Higgins, Gilad, Klein + QA (Ioannidis, Kahneman).

---

## 3. Achados (Tier 1)

### 3.1 Filtros facetados (o maior alavancador) — FR-03
Evidência convergente (Baymard, Nosto, Fact-Finder, LogRocket):
- **Multi-seleção com checkbox**, nunca radio: lógica **OR dentro do grupo, AND entre grupos** (ex.: "Educação OR Tecnologias" combinado com "Libras").
- **Contadores por opção** ("Ambiente e Saúde (44)") aumentam confiança e evitam becos sem saída — a Vitrine atual já exibe contadores por categoria; manter e estender às tags.
- **Chips de filtros ativos** acima do grid, cada um com "×", + "Limpar tudo". ~20% dos sites falham em manter os filtros visíveis.
- **Desktop:** sidebar persistente + atualização em tempo real. **Mobile:** painel em *bottom-sheet*/tela cheia, botão "Mostrar X resultados", chips em rolagem horizontal, alvos de toque ≥44×44pt.
- **Qualidade > quantidade:** 5–10 facetas relevantes; recolher secundárias em accordion; permitir buscar dentro de listas longas de filtro.
- **Persistir estado do filtro na URL** (query params) para back/compartilhamento.
- **Tratar zero-resultados** com aviso/alternativas.
> **Estatísticas-âncora (Baymard):** ~16% dos sites têm faceted search eficaz; filtros podem elevar conversão ~26%. `[Confiança: ALTA no padrão; MÉDIA nos números — fonte única, não peer-reviewed]`

### 3.2 Busca textual — FR-02
- **Autocomplete/sugestões instantâneas** (<100ms), com ranqueamento por popularidade/contexto.
- **Tolerância a erro de digitação** (fuzzy matching) e "você quis dizer…"; a Vitrine já normaliza acentos (bom) — falta o resto.
- **Mobile:** preferir **sugestões** a resultados diretos (efeito "fat finger"); busca é crítica quando o catálogo é grande.
- Busca casando por **título + categoria + tag** (a Vitrine já faz) — manter e enriquecer com sinônimos. `[Confiança: ALTA]`

### 3.3 Busca vs. Navegação e *information scent* — FR-02/FR-03
- Usuários escolhem buscar ou navegar conforme a **largura do menu** e a **força da pista informacional**. Com categorias concretas e bem rotuladas, a navegação predomina (buscas em <10% das tentativas em menus grandes).
- **Information scent forte** (rótulos específicos, snippets, indicadores claros) reduz tempo de navegação e aumenta descoberta de conteúdo.
- Comportamento **difere entre mobile e desktop** — testar nos dois.
> Implicação: investir tanto na **taxonomia/rotulagem de categorias** (Estágio 02) quanto na busca. `[Confiança: ALTA no princípio; MÉDIA nos percentuais agregados]`

### 3.4 Carregamento de listas grandes (Load More) — NFR-03
- Para listas **orientadas a tarefa** (caso da Vitrine), **Load More** supera scroll infinito e paginação clássica (Baymard).
- **Scroll infinito** serve a feeds de descoberta, mas gera desorientação, problemas de acessibilidade e de performance — evitar.
- Combinar com **lazy-load de imagens** dos cards para melhorar LCP (a Vitrine hoje injeta ~230 cards + imagens de uma vez). `[Confiança: ALTA]`

### 3.5 Design de cards — FR-01/NFR-02
- Card = **uma unidade digerível**: imagem (aspect ratio consistente), título como **link primário**, metadados úteis, CTA.
- **Hierarquia visual** clara e **texto truncado em contagem fixa** para cards de tamanho uniforme.
- Metadados de curso comuns e úteis: **categoria, carga horária, nível, selo (ex.: Libras), rating/○ inscritos** quando houver dado. A Vitrine hoje mostra só imagem+título+CTA — há espaço para enriquecer (carga horária máx. 60h já é um fato do produto).
- **Acessibilidade:** usar `<ul>/<li>` para o grupo de cards; foco de teclado visível; contraste WCAG; **`alt` descritivo por curso** (corrige o `alt` repetido "Como criar Mooc" da Vitrine atual).
- **Nuance importante:** cards favorecem **navegação**; para **resultados de busca**, uma visão em lista/densa escaneia melhor. Considerar alternância de visão. `[Confiança: MÉDIA-ALTA]`

### 3.6 Acessibilidade (WCAG 2.2) — NFR-02
- **Operável por teclado** em toda a jornada (busca, filtros, cards).
- **Indicador de foco** visível e de alto contraste (2.2 reforça *Focus Appearance*).
- **Ordem de foco** lógica; **gestão de foco em conteúdo dinâmico** (ao filtrar/carregar mais, anunciar resultados ao leitor de tela; ao abrir o painel de filtro mobile, mover foco; ao fechar, retornar ao gatilho).
- Preservar/ampliar o **selo de Libras** como recurso de inclusão. `[Confiança: ALTA]`

### 3.7 Benchmark de plataformas (joint display)

| Plataforma | Escala | Padrões de descoberta observados | Lição p/ a Vitrine |
|-----------|--------|----------------------------------|--------------------|
| **Coursera** | ~16k cursos, 205M alunos | Busca robusta + facetas (assunto, nível, idioma, tipo), UI amigável, app mobile | Referência de facetas — mas **não ancorar** na complexidade de mega-catálogo |
| **edX** | ~6k cursos | Catálogo amplo; navegação relatada como mais "pesada" | Evitar navegação truncada/cumbersome |
| **FutureLearn** | 22M usuários | Página de curso social; discussões próximas ao conteúdo | Menos relevante p/ vitrine-só-showcase |
| **Lúmina (UFRGS)** | 116 cursos, autoinstrucional | Catálogo público de MOOCs de instituição federal — escala comparável | **Par direto** de benchmark BR |
| **USP (eaulas)** | Catálogo aberto | Vitrine de aulas/cursos abertos | Benchmark BR de organização de catálogo |
| **FGV (cursos gratuitos)** | 100+ cursos c/ certificado | Vitrine de cursos gratuitos com certificado | Benchmark BR de apresentação/CTA |

> Existe um guia mapeando **50+ plataformas de MOOCs de instituições públicas brasileiras** (Institutos Federais, universidades, CEFETs) — fonte útil para o Estágio 02/03 comparar taxonomias e apresentação. `[Confiança: MÉDIA — benchmark observacional]`

### 3.8 Contexto empírico (MOOC) — ancoragem de desfecho
- Barreiras de aprendizagem em MOOCs classificadas em: **habilidades técnicas/online, contexto social, design do curso, tempo/suporte/motivação**. Evasão associada a falta de personalização e de trilha clara.
- Não há, no corpus levantado, estudo isolando *findability de catálogo* como variável primária — evidência **indireta**: a descoberta é parte do "course design/navigation". `[Confiança: MÉDIA — peer-reviewed, porém indireto]`

---

## 4. Avaliação de qualidade (QA)

### ⚖️ Ioannidis — confiabilidade da evidência
- **Triangulação forte** nos padrões nucleares (facetas multi-seleção, chips de filtros, contadores, typo tolerance, Load More, foco de teclado): múltiplas fontes independentes convergem → **PPV alto**.
- **Viés comercial:** parte relevante das fontes são **fornecedores de busca/filtro** (Algolia, Meilisearch, Nosto, Prefixbox, Fact-Finder) com incentivo a superestimar benefícios de busca/autocomplete. Ponderado para baixo; priorizadas fontes independentes (Baymard, W3C, USWDS, Material, academia).
- **Estatísticas específicas** ("16% eficaz", "+26% conversão", "scent −30–50% tempo") vêm de **fontes únicas não peer-reviewed** → tratadas como **indicativas**, não como fato assentado.
- **Transferência de domínio:** grande parte da evidência é **e-commerce**; aplicar a educação aberta exige cautela (ver Kahneman).
- **Evidência acadêmica** (SIGIR, Springer, Open Praxis) é peer-reviewed, porém **indireta** ao problema de catálogo.
- **Contradição sinalizada (→ Klein):** entusiasmo por cards × "cards são fracos para resultados de busca". **Resolução:** cards no browse, visão densa/lista no modo busca. Não é contradição real, é dependência de contexto.

### 🧠 Kahneman — auditoria de vieses (essência do checklist de 12 pontos)
- **Viés de disponibilidade/e-commerce:** o material puxa para "conversão de venda". **Reenquadrar** o desfecho para **findability e acesso ao curso** (não há compra). Aplicado nas recomendações.
- **Viés de confirmação (a favor do redesign):** *premortem* — e se a simplicidade atual já servir a usuários recorrentes e o redesign aumentar a fricção? **Mitigação:** medir antes/depois.
- **WYSIATI (o que vejo é tudo):** **não há dado do usuário real desta Vitrine** no corpus. Porém a Vitrine **já tem Hotjar e Google Analytics** instalados → usar mapas de calor e funis para calibrar decisões localmente.
- **Ancoragem:** não copiar a UX de mega-catálogo (Coursera/edX, milhares de cursos) para ~230 cursos; **dimensionar** os padrões (ex.: talvez não precise de busca-dentro-de-filtro).
- **Veredito Kahneman:** recomendações **APROVADAS com ressalva** — implementar com **teste de usabilidade leve** e leitura dos analytics existentes antes de decisões irreversíveis de IA/navegação.

**Quality gates:** QG-003 (≥5 fontes únicas) ✅ · QG-004 (nenhum achado forte com PPV<0,3; recomendações sem 2+ vieses não mitigados) ✅.

---

## 5. Recomendações (acionáveis, priorizadas)

| # | Recomendação | Liga a | Confiança | Esforço |
|---|--------------|--------|-----------|---------|
| R1 | **Filtros facetados multi-seleção** (categoria + tag) com contadores, chips de ativos e "Limpar tudo"; OR intra-grupo / AND entre grupos. | FR-03 | ALTA | Médio |
| R2 | **Padrão mobile de filtro:** bottom-sheet + "Mostrar X resultados" + chips horizontais + toque ≥44px. | FR-03/NFR-01 | ALTA | Médio |
| R3 | **Busca com autocomplete + typo tolerance + "você quis dizer"**, mantendo a normalização de acento atual; sugestões <100ms. | FR-02 | ALTA | Médio-Alto |
| R4 | **Load More + lazy-load de imagens** no grid (substituir a renderização de todos os cards de uma vez). | NFR-03 | ALTA | Baixo-Médio |
| R5 | **Cards acessíveis e enriquecidos:** `<ul>/<li>`, título como link, foco visível, contraste WCAG, **`alt` por curso**, e metadados (carga horária, nível, selo Libras). | FR-01/NFR-02 | ALTA | Baixo-Médio |
| R6 | **Modo lista/denso para resultados de busca** (alternância com o grid de cards). | FR-01/FR-02 | MÉDIA | Médio |
| R7 | **Reforçar information scent da taxonomia** (rótulos claros, contadores) — insumo direto do Estágio 02. | FR-03 | ALTA | Baixo |
| R8 | **Gestão de foco em conteúdo dinâmico** (filtrar, carregar mais, abrir/fechar painel) anunciada a leitores de tela. | NFR-02 | ALTA | Médio |
| R9 | **Preservar filtros na URL** (deep-link/compartilhamento/back). | FR-03 | MÉDIA-ALTA | Médio |
| R10 | **Antes de decisões de IA irreversíveis:** ler Hotjar + GA atuais e rodar teste de usabilidade leve (5–8 pessoas). | Governo do redesign | ALTA | Baixo |

---

## 6. Limitações
- **Sem evidência direta do usuário desta Vitrine** — recomendações são de mercado, não medidas localmente (mitigável via Hotjar/GA já instalados).
- **Viés de domínio:** maioria da evidência é e-commerce; "conversão" foi reenquadrada como findability/acesso.
- **Estatísticas indicativas**, não peer-reviewed (Baymard, blogs de UX) — usar como direção, não como meta.
- **Benchmark BR observacional** (não houve teste sistemático das plataformas); um fetch (mapaeducacional) retornou 403 e foi suprido pelo snippet de busca.
- **Sem RCTs** no domínio; nível de evidência realista é síntese de boas práticas + benchmark.

## 7. Fontes (com credibilidade)

**Alta credibilidade (independentes / padrões / peer-reviewed):**
- [Baymard — Ecommerce Filter UI Best Practices](https://baymard.com/learn/ecommerce-filter-ui) — pesquisa de usabilidade em larga escala
- [W3C — WCAG 2.2](https://www.w3.org/TR/WCAG22/) — padrão de acessibilidade
- [U.S. Web Design System — Card](https://designsystem.digital.gov/components/card/) — design system governamental
- [Material Design 3 — Cards](https://m3.material.io/components/cards/guidelines)
- [Nielsen Norman Group](https://www.nngroup.com/) — pesquisa de UX
- [ACM SIGIR — Information Scent, Mobile vs Desktop Search](https://dl.acm.org/doi/10.1145/3077136.3080817) — peer-reviewed
- [Open Praxis — Barriers to Learning in MOOCs](https://openpraxis.org/articles/10.5944/openpraxis.13.2.124) — peer-reviewed
- [Springer — Systematic review of MOOC platforms](https://link.springer.com/article/10.1007/s44217-025-01085-2) — peer-reviewed

**Média credibilidade (prática / agregadores / benchmark):**
- [Class Central — MOOC Platforms](https://www.classcentral.com/report/mooc-platforms/) · [Programming course on 3 platforms](https://www.classcentral.com/report/programming-course-comparison/)
- [Fact-Finder — Faceted search best practices](https://www.fact-finder.com/blog/faceted-search/) · [Nosto](https://www.nosto.com/blog/faceted-search-for-ecommerce-best-practices/) · [LogRocket — Faceted filtering](https://blog.logrocket.com/ux-design/faceted-filtering-better-ecommerce-experiences/)
- [Pagination vs Infinite Scroll vs Load More — LogRocket](https://blog.logrocket.com/ux-design/pagination-vs-infinite-scroll-ux/)
- [UX Magazine — Autosuggest best practices](https://uxmag.com/articles/best-practices-designing-autosuggest-experiences) · [Freshconsulting](https://www.freshconsulting.com/insights/blog/autocomplete-benefits-ux-best-practices/)
- [Information Scent — UX/UI Principles](https://uxuiprinciples.com/en/principles/information-scent) *(estatísticas agregadas — tratar como indicativas)*
- [Algolia — Mobile search UX](https://www.algolia.com/blog/ux/mobile-search-ux-best-practices) *(fornecedor — viés comercial)*
- Benchmark BR: [Lúmina/UFRGS](https://lumina.ufrgs.br/) · [MOOCs SEAD/UFRGS](https://www.ufrgs.br/sead/cursos-a-distancia/moocs-cursos-online-gratuitos/) · [Guia 50+ plataformas públicas — Mapa Educacional](https://www.mapaeducacional.com.br/noticia/mapa-educacional-moocs-gratuitos-institutos-federais-universidades) *(403 no fetch; via snippet)*

## 8. Notas de metodologia
- **PICO:** ver §2. **Tipo de revisão:** scoping + benchmarking (SALSA). **Design:** QUAL+quant (Creswell).
- **Pipeline:** wf-deep-research (5 fases). **Casos de uso:** UC-004 (primário) + UC-003 (secundário).
- **Busca ao vivo:** executada via WebSearch/WebFetch nativos (os scripts TS do squad exigiriam API keys/Node) — 3 lotes, ~13 fontes únicas.
- **Níveis de confiança:** ALTA = múltiplas fontes independentes convergentes, sem viés dominante; MÉDIA = corroboração parcial ou fonte com viés/indireta; BAIXA = fonte única/estatística não verificada.
- **QA:** Ioannidis (confiabilidade/PPV, viés comercial) + Kahneman (12 vieses, premortem, veredito APROVADO com ressalva).

---
*Deep Research Squad · "Every research question deserves a structured, evidence-based answer."*
