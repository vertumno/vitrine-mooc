# Arquitetura de Informação — Navegação, Objetivos, Séries e Projetos

> **Estágio:** 02 — Catálogo (refinamento de taxonomia) · **Versão:** 2.0 · **Data:** 01/07/2026 · **Papel:** arquitetura de informação
> **Decisões desta versão:** (1) **conceito de "trilha" removido** — fica apenas **Série** como agrupamento de cursos relacionados; (2) **objetivos** redesenhados (proposta concreta em avaliação na §4).
> **Refina:** as §3–4 de `taxonomia.md`.
> **Evidências:** `relatorio-publicos-alvo-mooc-ifes.md` `[Público]` (público **sugerido pelos autores**, não confirmado), `powerbi-mooc-ifes/analise-insights-powerbi-mooc-ifes.md` `[PowerBI]` (real; 2026 parcial), `catalogo-cursos.csv` `[Catálogo]`, `shared/prd-vitrine-mooc-v1.md` `[PRD]`.

Teste único de tudo aqui: **a pessoa encontra o curso que quer, rápido e sem se perder?**

---

## 0. Princípios (o que a natureza do MOOC impõe)

1. **Curso é autossuficiente** — gratuito, sem tutoria, sem seleção, ritmo próprio, ≤60h. Nada trava curso; todo agrupamento é **sugestão**, não pré-requisito. *(Foi por isso que a trilha saiu: ela sugere um percurso obrigatório que não combina com autoestudo.)*
2. **O catálogo cresce a cada 3 meses** — a estrutura **primária** classifica curso novo **por regra/metadado** (automático na publicação). Curadoria (séries, destaques) é **camada editorial**; se o curso novo não entrar numa série, a Vitrine não quebra.
3. **Sucesso é achar e concluir** — certificação média de **33%** `[PowerBI]`. Estrutura que confunde a escolha aumenta abandono.

## 1. O problema real (por que não basta espelhar o catálogo)

Há um **descompasso entre oferta e demanda**:
- **Oferta** dominada por educação/ambiental — o projeto **Rio Doce Escolar** tem **31 cursos** `[Catálogo]`.
- **Demanda** concentrada em poucos práticos `[PowerBI]`: Inglês Comunicativo (**22.390**), Moodle para Educadores (11.392), Uso do Canva (8.589), Google Drive (8.007), Acessibilidade e Tecnologia (7.800), Lovelace Python/C (6.310). **50 cursos = 74% das matrículas.**
- Cursos ambientais: baixa matrícula, alta conclusão. **65% das matrículas vêm de fora do ES** — Vitrine é porta **nacional**.

**Consequência:** a navegação primária **não pode espelhar a produção** (pesada em projetos/séries). Ela favorece **intenção do usuário + demanda**; proveniência (séries/projetos) fica em camada secundária.

## 2. Os quatro construtos (sem trilha)

| Construto | Pergunta | Critério de entrada | Curso novo entra… | Papel na UX |
|-----------|----------|---------------------|-------------------|-------------|
| **Categoria (tema)** | "Sobre o quê é?" | Área de conhecimento (regra) | automático (≥1) | Filtro/base |
| **Objetivo (para quê/quem)** | "Serve pra mim?" | Intenção + público (regra) | automático (marcação) | **Navegação primária** |
| **Série / Coleção** | "Faz parte de um conjunto?" | Mesma marca/produção | se pertence à série | Curadoria |
| **Projeto parceiro** | "De onde veio?" | Parceria institucional + hub | se o projeto produziu | Página/selo próprio |

Os dois primeiros são **estrutura** (regra, cobrem 100%, escalam sozinhos). Os dois últimos são **curadoria/proveniência** (parciais, editoriais).

## 3. Série × Projeto parceiro (a distinção que resta)

Com a trilha fora, a única confusão a resolver é esta:

| | **Série / Coleção** | **Projeto parceiro** |
|---|---|---|
| O que é | Família de cursos de mesma marca/produção | Programa/parceria institucional |
| Exemplos | Lovelace (6), Educador Maker (4), Lesson Study, Atendente e Vendedor (3) | Rio Doce Escolar (31), UnAC (33) |
| Tamanho | Pequena (3–6) | Grande (dezenas) |
| Identidade | Marca editorial | Identidade institucional + **hub próprio** (`/v/riodoce/`, `/v/unac/`) |
| Na Vitrine | Selo no card + página de coleção | Página do projeto (institucional) + selo |

**Como pensar:** uma **Série** é editorial ("estes cursos são irmãos"); um **Projeto** é institucional ("estes cursos vêm de uma parceria/programa"). Na prática, **um Projeto é uma Série grande com identidade própria** — o mesmo mecanismo de agrupamento, com um selo de "projeto parceiro" e página institucional. Isso mantém **um só conceito de agrupamento (Série)**, com o Projeto como um tipo especial.

## 4. Objetivos — proposta concreta (EM AVALIAÇÃO)

**Correção que você já validou:** "Licença Capacitação" **não é objetivo** (qualquer curso certificado serve). Vira **área dedicada** (§6).

**O que muda em relação ao PRD:** mantenho 3 dos 4 objetivos do PRD (renomeados para linguagem de intenção), removo o errado (Licença → área) e ajusto para que **cubram o catálogo** e a **demanda real**. Objetivo é **multi-rótulo** (curso pode ter mais de um).

| # | Objetivo (rótulo na Vitrine) | Para quê / quem | Regra de entrada (resumo) | Tamanho aprox. | Exemplos |
|---|------------------------------|-----------------|---------------------------|:---:|----------|
| 1 | **Para ensinar melhor** | Professores e educadores: prática pedagógica, tecnologias educacionais, Moodle, avaliação, inclusão na escola | cat. Educação / Tec. Educacionais / Desenv. Educacional / EaD, ou tags de docência | **~66%** (maior público) | Metodologias Ativas, Gamificação no Moodle, Educador Maker, Mediação pedagógica |
| 2 | **Para aprender tecnologia** | Programação, dados, ferramentas digitais | cat. Tecnologias e Informática, ou tags (programacao, python, dados, canva, scratch…) | ~25–30 cursos | Lovelace Python/C, Estatística com R, Uso do Canva, Node.js, Google Drive |
| 3 | **Para o trabalho e a carreira** | Empregabilidade, gestão, finanças, atendimento/vendas, escrita | cat. Gestão / Desenv. Pessoal / Ciências Sociais, ou tags (gestao, vendas, financas, carreira…) | ~20–25 cursos | Atendente e Vendedor, Gestão de Finanças, Escrita Acadêmica, Inglês para Turismo |
| 4 | **Para a comunidade (comece do zero)** | Interesse geral, sem pré-requisito, iniciante | público "comunidade em geral" na ficha, ou nível iniciante sem pré-requisito | **~48%** se declaram abertos | Inglês Comunicativo, A Química dos produtos de limpeza, Operador de Computador, Espanhol Comunicativo |
| — | **Inclusão e acessibilidade** *(transversal)* | Libras, acessibilidade, neurodiversidade, mulheres na computação | flag/tags (libras, acessibilidade, inclusao…) | ~10 (6%) | Introdução à Libras, Acessibilidade e Tecnologia, Lovelace no Cotidiano Feminino |

**Decisões de arquitetura por trás disso (para você avaliar):**
- **Por que 4 (e não 6)?** Mais de 4–5 entradas viram poluição (deep-research: qualidade > quantidade). "Professores" (66%) + "Comunidade" (48%) já cobrem quase todo o acervo; "Tecnologia" e "Trabalho" destacam onde está a **demanda real**.
- **Cadê "Meio ambiente e ciências"?** É o maior bloco de **oferta**, mas de **baixa demanda por curso**. Misturar um **tema** no meio de **intenções** quebra a lógica. Ele já é coberto por **Categoria** (Ambiente e Saúde) + pelos objetivos "Para ensinar" e "Para a comunidade" (é para onde o público desses cursos aponta) + pela **página do Projeto Rio Doce**. Não precisa de objetivo próprio. *(Se você preferir, dá para promovê-lo a objetivo — mas aí é tema, não intenção.)*
- **Cadê "Servidores / setor público"?** Em parte vira a **área de Licença Capacitação**; o resto (gestão pública) cabe em "Trabalho e carreira". Manter como objetivo separado é opcional (público de 17%).
- **Inclusão** funciona melhor como **filtro/selo transversal** do que como card grande — mas precisa ser fácil de achar.
- **Ressalva honesta:** os tamanhos vêm do `[Público]`, que é **sugerido pelos autores**. Antes de fechar, vale cruzar com quem realmente se inscreve.

## 5. Séries e Coleções (a camada de agrupamento)

Critério de **Série**: cursos que compartilham **marca/produção** e se apresentam como um conjunto. Não exigem ordem (mas podem ter níveis).

| Série | Nº | Tem níveis/ordem? | Observação |
|-------|----|-------------------|------------|
| **Atendente e Vendedor** | 3 | Sim (Fundamentos→Interm.→Avançado) | Série com progressão clara |
| **Educador Maker** | 4 | Sim (progride) | Primeiros Passos → ABP → mão na massa → Da Vinci |
| **Mooc de Lovelace** | 6 | Não | Cursos paralelos (Arte&Game, Robótica, Python, Scratch, Pensamento Computacional…); há quase-duplicatas |
| **Embrace** | 3 | Parcial | Projeto europeu (tag `embrace`) |
| **Lesson Study** | 2–3 | Não | **PT e EN são o mesmo curso em dois idiomas** — não são dois cursos distintos |

Cada série ganha **selo no card + página de coleção**. Bom para quem já conhece a marca; **não é a via principal** de quem chega sem saber o que quer.

## 6. Licença para Capacitação = área dedicada (não objetivo)

Qualquer curso certificado gera horas. Logo, Licença não filtra conteúdo — é um **destino** com instruções (o que é, quem tem direito, legislação) + o **Planejador** do PRD (`/qualificacao`). É a Camada 2 do PRD.

## 7. Modelo de navegação recomendado

| Usuário chega… | Caminho | Estrutura |
|----------------|---------|-----------|
| Sabe o tema ("quero inglês") | Busca + Categoria | Categoria + tags |
| Sabe a intenção ("sou professor") | **Objetivo** ("Para ensinar melhor") | Objetivo |
| Não sabe o que quer | Wizard (perfil+área+tempo) | Público × categoria × carga |
| Servidor querendo horas | **Área Licença Capacitação** + Planejador | Área dedicada |
| Quer o mais buscado | Seção "Mais cursados" | Demanda `[PowerBI]` |
| Interessado num projeto | Página do Projeto (Rio Doce/UnAC) | Projeto parceiro |
| Reconhece uma marca | Página da Série (Lovelace…) | Série |

## 8. Metadados por curso (para o novo curso encaixar por regra)

| Campo | Preenchimento | Obrigatório? |
|-------|---------------|:---:|
| `categoria[]` | tema | ✅ ≥1 |
| `objetivo[]` | intenção/público (regra) | ✅ ≥1 |
| `publico[]` | público-alvo (ficha) | ✅ ≥1 |
| `nivel` | iniciante/interm./avançado | ✅ |
| `carga_horaria` | horas (dep. Raquel) | ✅ (bloqueado hoje) |
| `tags[]` | palavras-chave (higienizar) | ✅ |
| `descricao` / `objetivos_aprendizagem` | texto | ✅ |
| `alt_imagem` | descrição real | ✅ |
| `serie` | Lovelace / Educador Maker… | ➖ opcional |
| `projeto` | Rio Doce / UnAC… | ➖ opcional |
| `inclusao` | selo Libras/acessibilidade | ➖ quando aplicável |

**Regra de publicação:** com categoria + objetivo + público + nível + carga + tags, o curso já aparece em busca, filtros, "Recentes" e nas entradas por objetivo **automaticamente**. Série/projeto/destaque são camadas editoriais opcionais.

## 9. Decisões para a Comissão MOOC / CEFOR

1. **Objetivos:** aprovar os **4 propostos** (§4) no lugar dos 4 do PRD? Manter "Meio ambiente e ciências" como **tema/categoria** (recomendado) ou promover a objetivo?
2. **Licença Capacitação:** confirmada como **área** (não objetivo). ✅
3. **Servidores/setor público:** entrada própria ou coberto por Licença + "Trabalho e carreira"?
4. **UnAC:** o que é? (para descrever o projeto sem inventar)
5. **Duplicatas:** Lesson Study PT/EN e Lovelace PC/PC-Feminino — agrupar ou manter visíveis?
6. **Carga horária** (Raquel): sem ela, nível e filtro por esforço ficam parados.

---

## Rastreabilidade
- **Fato:** categorias, tags, séries e projetos vêm do `[Catálogo]`; demanda do `[PowerBI]`.
- **Hipótese:** público-alvo é **sugerido pelos autores** `[Público]`.
- **Proposta em avaliação:** os 4 objetivos (§4) e a navegação (§7) aguardam validação. **Nada inventado como oficial.**
- **Coerência MOOC:** sem trilhas/pré-requisitos; tudo standalone; séries e projetos são agrupamentos, não percursos obrigatórios.
