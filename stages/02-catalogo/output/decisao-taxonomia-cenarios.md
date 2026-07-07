# Decisão em aberto — Taxonomia e Navegação (cenários)

> **Estágio:** 02 — Catálogo · **Data:** 01/07/2026 · **Status:** ✅ DECIDIDO — **Cenário C** (02/07/2026).
> **Modelo final:** ver `arquitetura-informacao.md` **v4.1** (Cenário C + separação área oficial × navegação + selos Libras/Audiodescrição/Idioma + SEO). Este documento fica como **registro histórico** de como se chegou à decisão.
> **Complementa:** `arquitetura-informacao.md` (v4.1) e `taxonomia.md`.
> **Atualização (06/07/2026):** **sem tree test / card sorting** — rótulos definidos por decisão editorial do CEFOR. Pendências da §5 resolvidas: **UnAC** definido; **carga horária** populada em `catalogo-cursos-completo.csv`; **65 "em produção"** ficam fora deste projeto (escopo = 165 publicados).

Documento de apoio à decisão sobre **como a nova Vitrine organiza e apresenta os 165 cursos**. Reúne o inventário das camadas, os fatores que pesam (inclusive os menos óbvios) e três cenários. Nada aqui é oficial: é subsídio para o CEFOR/Comissão MOOC decidir.

---

## 1. Inventário das camadas (o que existe ou foi proposto)

| Camada | Status | Como funciona | Ganho | Custo/risco |
|--------|--------|---------------|-------|-------------|
| **Categorias (19)** | ✅ Existe no site | Tema acadêmico; ≥1 por curso na publicação; filtro | Base estável; todo curso tem; já conhecida | **Desbalanceadas: 44 vs 1**. Filtro quase vazio quebra confiança |
| **Tags (430)** | ✅ Existe no site | Palavras-chave livres; alimentam a busca | Busca por sinônimo/tema fino | **Vocabulário sem controle** (5 grafias de "Rio Doce", `algoritimo`). Degrada a cada leva |
| **Selo Libras** | ✅ Existe | Flag binária no card | Inclusão visível, diferencial | Nenhum — manter |
| **Seções curadas** (Destaque/Recentes/Mais cursados) | 📄 PRD | Ordenação automática (data, matrículas) + 1 manual | Expõe demanda real; "Recentes" absorve as levas trimestrais **automaticamente** | "Em destaque" manual precisa de dono |
| **Objetivos — 4 do PRD** | 📄 PRD | Cards de intenção: Inovar na sala / Licença / Aprender tecnologia / Crescer na carreira | Fala a língua do usuário | **30% do catálogo órfão**; "Licença" errado como filtro |
| **Objetivos — proposta v2** | 💡 Proposta | 4 intenções (Ensinar / Tecnologia / Trabalho / Comunidade) + Inclusão | Cobre o catálogo; ancorado em público | Rótulos "espertos" fracos; sobreposição alta |
| **Séries** (Lovelace, Educador Maker, Atendente e Vendedor, Embrace, Lesson Study) | ✅ Decidido | Selo no card + página de coleção | Storytelling; quem conhece a marca acha junto | Baixo — é fato |
| **Projetos parceiros** (Rio Doce, UnAC) | ✅ Decidido | Série grande com identidade + hub | Casa aos 31+33 cursos sem inundar o grid | Descrição oficial (UnAC indefinido) |
| **Área Licença Capacitação** | ✅ Decidido | Página + Planejador (não é filtro) | Corrige erro conceitual; maior gerador de matrículas | Depende de carga horária (Raquel) |
| **Facetas** (carga horária, nível, Libras) | 📄 PRD + deep-research | Refinamento combinável na listagem | O que realmente estreita a escolha | `nivel` **não existe hoje**; CH **já populada** (`catalogo-cursos-completo.csv`) |
| **Wizard** | 📄 PRD | 3 perguntas → recomenda | Serve quem não sabe o que quer | **Consome** os metadados acima; só funciona se existirem |

## 2. Fatores que pesam na decisão (inclusive os menos óbvios)

**a) O gargalo maior são as 19 categorias, não os objetivos.** A fundação está torta: 1 categoria com 44 cursos (não discrimina) e 4 com 1–3 (filtro vazio). **Rebalancear 19 → ~10 categorias de tamanho comparável provavelmente melhora mais a descoberta do que qualquer sistema de objetivos.** Esboço ilustrativo (a validar):

| Consolidação proposta | Junta | ~Cursos |
|---|---|---|
| Meio Ambiente e Sustentabilidade | maior parte de Ambiente e Saúde | ~35 |
| Saúde e Segurança | saúde mental, vacinas, bombeiros, SST | ~9 |
| Educação e Docência | Educação | ~39 |
| EaD e Tecnologias Educacionais | EaD + Tec. Educacionais | ~28 |
| Tecnologia e Programação | Tec. e Informática + Engenharia | ~20 |
| Gestão e Setor Público | Gestão + C. Sociais Aplicadas | ~12 |
| Ciências e Matemática | C. Natureza + Exatas + Matemática | ~14 |
| Idiomas | Línguas | ~6 |
| Artes, Design e Cultura | Artes + Design + Prod. Cultural | ~7 |
| Inclusão e Acessibilidade | mantém (+ selo transversal) | ~7 |

> Nota: "Educação e Docência" (~39) ainda ficaria grande — pode ser subdividida ou refinada com facetas. É ponto de partida, não fechado.

**b) Navegação por público tem modo de falha documentado.** IA clássica (Nielsen) mostra que navegação por audiência falha quando o conteúdo se sobrepõe muito — e **107 dos 165 cursos declaram 2+ públicos** `[Público]`. Efeitos: o mesmo curso aparece em 3 entradas (parece repetição) e gera **auto-exclusão falsa** ("não sou professor, ignoro 'Para ensinar'"). Não invalida objetivos, mas exige que sejam **atalhos**, nunca a rota única até o curso.

**c) Rótulo concreto vence rótulo esperto.** "Para professores e educadores" (autoidentificação) supera "Para ensinar melhor" (marketing) em usabilidade. Se formos por objetivos, os nomes devem ser **testados**.

**d) SEO: categoria/tema gera página indexável; objetivo, não.** 65% das matrículas vêm de fora do ES `[PowerBI]` — Google é canal real. Buscam "curso gratuito de educação ambiental com certificado", não "para ensinar melhor". Páginas de tema bem nomeadas são landing pages de SEO. Pesa a favor de temas fortes como espinha dorsal.

**e) Governança é o assassino silencioso.** Cada camada precisa de **dono**, **regra de atribuição na publicação** e **densidade mínima** (nenhuma entrada com <4–5 cursos). Com levas trimestrais de autores diferentes, camada baseada em julgamento sem regra escrita apodrece em 2–3 ciclos. Categorias e facetas sobrevivem (são regra); objetivos mal definidos viram ruína.

**f) Cada camada só se justifica se tiver função única.** Categorias = navegar+SEO · Tags = busca · Seções curadas = demanda · Séries/Projetos = marca/proveniência · Facetas = estreitar · Wizard = quem não sabe. **Que função os objetivos cumprem que as outras não?** Só uma: *atalho de autoidentificação na home*. É útil, mas é **merchandising, não fundação**.

**g) Dá para testar barato.** *Card sorting* e *tree testing* resolveriam com 15–20 participantes. **Decisão (06/07/2026): não faremos tree test/card sorting** — os rótulos são definidos por decisão editorial do CEFOR. (Hotjar/GA seguem instalados para monitorar o comportamento real pós-lançamento.)

## 3. Os três cenários

| | **A — 4 objetivos do PRD** | **B — Proposta v2 (intenções)** | **C — Temas consolidados + "Para quem" como atalho** |
|---|---|---|---|
| Espinha dorsal | Objetivos | Objetivos | **Categorias rebalanceadas (~10)** |
| Papel dos objetivos | Navegação principal | Navegação principal | **Chips/atalhos secundários** |
| Cobertura | 70% (30% órfão) | ~100% | 100% (categoria cobre por regra) |
| SEO | Fraco | Fraco | **Forte** |
| Risco de sobreposição | Alto | Alto | Baixo (atalho não é rota única) |
| Governança | Frágil | Ok | **Mais simples** |
| Fidelidade ao PRD | Total | Parcial | Parcial (mantém intenção na home) |

## 4. Recomendação (parecer técnico)

**Cenário C.** Espinha dorsal = **temas consolidados e balanceados** (~10; estáveis, SEO, regra automática para as levas trimestrais) + **seções curadas por demanda** + **3–4 atalhos "Para quem"** na home (camada fina de conveniência) + **facetas** (CH, nível, Libras) + **Wizard** por cima. Assim os objetivos deixam de ser decisão estrutural arriscada e viram o que são: atalhos de home, ajustáveis sem quebrar nada.

**Validação antes de fixar:** ~~*tree test* com 15–20 usuários~~ → **decidido (06/07/2026): sem tree test**; rótulos definidos por decisão editorial do CEFOR.

## 5. O que decidir ao retomar
1. ~~Escolher cenário~~ → **decidido: Cenário C.**
2. Se C: aprovar (ou ajustar) a consolidação de categorias da §2a. → tratado na v4.1 (15 Categorias).
3. ~~Definir se rodamos card sorting / tree test~~ → **decidido: sem tree test** (rótulos = decisão editorial do CEFOR).
4. Pendências: ~~o que é **UnAC**~~ (definido — Universidade Aberta Capixaba); ~~**carga horária**~~ (populada em `catalogo-cursos-completo.csv`); ~~**65 cursos em produção**~~ (fora deste projeto); **duplicatas** (Lesson Study PT/EN = mesmo curso com selo de idioma; Lovelace PC/PC-Feminino) seguem para tratamento na migração.
