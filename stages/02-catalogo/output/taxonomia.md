# Taxonomia — Catálogo Vitrine MOOC Ifes

> **Estágio:** 02 — Catálogo · **Data:** 01/07/2026
> **Base:** `catalogo-cursos.csv` (165 cursos publicados, extração ao vivo jul/2026) + `shared/prd-vitrine-mooc-v1.md` (objetivos e trilhas) + `deep-research-ux-descoberta-mooc.md` (R7 — reforço de taxonomia).
> **Mapa por curso:** `taxonomia-cursos.csv` (curso → categorias, objetivos, trilhas).
> **⚠️ Refinamento:** as seções 3 (Objetivos) e 4 (Trilhas) foram **repensadas** em `arquitetura-informacao.md` (modelo de 5 construtos, distinção trilha × projeto, Licença Capacitação como área e navegação por público). Leia aquele documento antes de usar os objetivos/trilhas abaixo.

O catálogo é fatiado por **quatro lentes**. Duas são **fato** (extraídas do site); duas são **proposta** derivada do PRD, a validar com o CEFOR/Comissão MOOC.

| Lente | Natureza | Status |
|-------|----------|--------|
| **Categorias** (19) | Classificação acadêmica — o que o curso é | ✅ Fato (site) |
| **Tags** (430) | Palavras-chave finas e transversais | ✅ Fato (site) |
| **Objetivos** (4) | Intenção do usuário — o que ele quer | ⚠️ Proposta (PRD + regra) |
| **Trilhas** (4) | Percursos curados de cursos | ⚠️ Proposta (PRD + regra) |

---

## 1. Categorias (✅ fato)

19 categorias. Um curso pode ter mais de uma (por isso a soma dos rótulos = 199 > 165 cursos únicos).

| Categoria | slug | Nº (rótulo do site) |
|-----------|------|:---:|
| Ambiente e Saúde | `ambiente-e-saude` | 44 |
| Educação | `educacao` | 39 |
| Tecnologias e Informática | `tecnologias-e-informatica` | 18 |
| Educação a Distância | `educacao-a-distancia` | 16 |
| Tecnologias Educacionais | `tecnologias-educacionais` | 15 |
| Desenvolvimento Educacional e Social | `desenvolvimento-educacional-e-social` | 10 |
| Gestão | `gestao` | 10 |
| Inclusão e Acessibilidade | `inclusao-e-acessibilidade` | 7 |
| Ciências da Natureza | `ciencias-da-natureza` | 6 |
| Línguas | `linguas` | 6 |
| Ciências Humanas | `ciencias-humanas` | 5 |
| Matemática | `matematica` | 5 |
| Artes e Humanidades | `artes-e-humanidades` | 4 |
| Desenvolvimento Pessoal | `desenvolvimento-pessoal` | 4 |
| Ciências Exatas e da Terra | `ciencias-exatas-e-da-terra` | 3 |
| Ciências Sociais Aplicadas | `ciencias-sociais-aplicadas` | 2 |
| Design | `design` | 2 |
| Engenharia | `engenharia` | 2 |
| Produção Cultural e Design | `producao-cultural-e-design` | 1 |

**Observações:**
- O catálogo é **dominado por Educação + Ambiente/Saúde** (a maioria dos cursos ambientais é do projeto Rio Doce Escolar).
- Categorias com 1–3 cursos (`producao-cultural-e-design`, `design`, `engenharia`, `ciencias-sociais-aplicadas`) são candidatas a **fusão** com afins, para não gerar filtros quase vazios (deep-research: qualidade > quantidade de filtros).

## 2. Tags (✅ fato)

**430 tags únicas** — muitas de baixa frequência. As mais frequentes (≥3 ocorrências):

`unac`(33) · `rio-doce-escolar`(31) · `educacao-ambiental`(30) · `aprendizagem`(18) · `escolar`(17) · `formacao-de-professores`(16) · `rio-doce`(16) · `riodoceescolar`(16) · `educador-ambiental`(16) · `doce`(15) · `programacao`(10) · `inclusao`(10) · `moodle`(9) · `acessibilidade`(9) · `gestao`(9) · `pensamento-computacional`(7) · `lovelace`(6) · `matematica`(5) · `ctsa`(5) · `metodologias-ativas`(4) · `atendimento-ao-cliente`(3) · `libras`(3) · `gamificacao`(3) · `maker`(3)…

**Clusters temáticos que emergem das tags:**
- **Educação Ambiental / Rio Doce** — o maior bloco (`educacao-ambiental`, `rio-doce-escolar`, `educador-ambiental`, `ctsa`).
- **Formação de professores / metodologias** (`formacao-de-professores`, `metodologias-ativas`, `pratica-pedagogica`, `mediacao`).
- **Programação / Maker** (`programacao`, `pensamento-computacional`, `lovelace`, `maker`, `robotica`).
- **Inclusão / Acessibilidade** (`inclusao`, `acessibilidade`, `libras`).
- **Moodle / EaD** (`moodle`, `ava`, `avea`, `ead`).

**Higiene de tags a fazer (recomendação):**
- **Fragmentação do Rio Doce:** `rio-doce-escolar`(31), `rio-doce`(16), `riodoceescolar`(16), `doce`(15), `escolar`(17) descrevem a mesma coisa → **consolidar em uma única tag**.
- **Erros/artefatos:** `algoritimo`(4) → `algoritmo`; `corte-de-lovelace`(6) parece artefato de edição.
- **Tags de fornecedor/projeto** (`unac`, `embrace`) são úteis como **coleção/projeto**, não como tema (ver `projetos-especiais.md`).

## 3. Objetivos (⚠️ proposta — validar com CEFOR)

Os 4 objetivos do PRD (§4.5/5.2) organizam por **intenção**. Regra proposta: um curso entra num objetivo se sua **categoria** ou alguma **tag** casa com o conjunto do objetivo (multi-rótulo).

| Objetivo | Regra (resumo) | Cursos (nesta regra) |
|----------|----------------|:---:|
| **Inovar na sala de aula** | cat. Educação/EaD/Tec. Educacionais/Desenv. Educacional + tags de docência (formacao-de-professores, metodologias-ativas, moodle, gamificacao…) | **87** |
| **Aprender tecnologia** | cat. Tecnologias e Informática + tags de TI (programacao, python, banco-de-dados, ia, scratch…) | **27** |
| **Crescer na carreira** | cat. Gestão/Desenv. Pessoal + tags (gestao, lideranca, financas, vendas, escrita-academica…) | **24** |
| **Licença Capacitação** | tags de setor público (administracao-publica, licitar, direito, politicas-publicas…) | **8** |

> Contagens com sobreposição (um curso pode ter vários objetivos). Mapa completo em `taxonomia-cursos.csv`.

**Achado importante — 50 cursos (30%) não caem em nenhum dos 4 objetivos.** São quase todos do bloco **ambiental/ciências/Rio Doce** (ex.: "Educação Ambiental de Base Comunitária", "A Química dos produtos de limpeza", "Segurança hídrica do Rio Doce"). Interpretação e opções para o CEFOR:
- **(a)** Tratar os 4 objetivos como **atalhos de navegação parciais** (nem todo curso precisa de objetivo) — o resto se acha por categoria/busca. **[Recomendado]**
- **(b)** Criar um **5º objetivo/tema "Educação Ambiental e Ciências"**, que reflete o maior bloco real do catálogo.
- Observação: **"Licença Capacitação"** é fraco como filtro de conteúdo — no PRD ele é sobretudo um **caminho para o Planejador** (qualquer curso certificado gera horas). Sugiro tratá-lo como CTA/rota, não como recorte temático.

## 4. Trilhas (⚠️ proposta — validar/curar com CEFOR)

As 4 trilhas do PRD (§5.3). CH-alvo do PRD é meta; a **carga horária real por curso está pendente** (CON-08), então não dá para fechar o somatório ainda.

### 4.1 Atendimento e Vendas — ✅ alta confiança (3 cursos exatos)
Os três cursos "Atendente e Vendedor" formam a sequência natural:
1. Atendente e Vendedor: Fundamentos do Atendimento e Vendas
2. Atendente e Vendedor: Nível Intermediário
3. Atendente e Vendedor: Nível Avançado

### 4.2 Professor Inovador — proposta (3 de 5 candidatos)
PRD: metodologias ativas + gamificação + ferramentas digitais. **Proposta:** Metodologias Ativas: Educação Inovadora · Pedagogias ativas com uso de ferramentas digitais · Gamificação no Moodle.
*Alternantes:* Digipeda – Competências Digitais e Pedagógicas · Ferramentas Digitais para Curadoria Educacional.

### 4.3 Maker na Educação — proposta (4 de 17 candidatos)
PRD: pensamento computacional + robótica educacional. **Proposta:** Escola de Inovação: Robótica e Prototipagem para Professores · MOOC de Lovelace: Pensamento Computacional · Mooc de Lovelace: Robótica Educacional · MOOC de Mary Keller: Robótica para Educadores.
*Pool rico:* famílias **Lovelace** (6), **Educador Maker** (4), PROGRAMAKIDS, Programação Básica: Scratch, Micropráticas de Pensamento Computacional. CEFOR escolhe os 4 definitivos.

### 4.4 Educação Ambiental (Rio Doce) — proposta (curar 5 de 31)
PRD: "Cursos do Projeto Rio Doce Escolar". O **pool tem 31 cursos** (ver `projetos-especiais.md`). Precisa curar **5** para a trilha. **Proposta inicial** (introdutória → aplicada): Educação Ambiental de Base Comunitária · Educação em Saúde Ambiental · Educação Ambiental em Três Momentos Pedagógicos · Legislação em Educação Ambiental · Avaliação da Aprendizagem no Contexto da Educação Ambiental.
*CEFOR define a sequência oficial.*

## 5. Esquema de metadados por curso

Campos que estruturam cada card/curso na nova Vitrine (alinhado ao card enriquecido do PRD §4.2):

| Campo | Fonte | Status |
|-------|-------|--------|
| `titulo` | site | ✅ |
| `slug` | derivar do link Moodle | ✅ |
| `categorias[]` | site (`data-category`) | ✅ |
| `tags[]` | site (`data-tag`) | ✅ (higienizar) |
| `objetivos[]` | regra proposta | ⚠️ validar |
| `trilha` | regra proposta | ⚠️ validar |
| `libras` | site (selo) | ✅ |
| `link_curso` | site (Moodle) | ✅ (padronizar slug × `?id=`) |
| `imagem` | site | ✅ |
| `carga_horaria` | WP (campo existe) | ❌ **não populado (Raquel)** |
| `nº_inscritos` | Moodle/banco | ❌ a definir |
| `descricao` / `objetivos_aprendizagem` | a produzir | ❌ novo (card expandido) |
| `badge_novo` | derivar da data (< 3 meses) | ⚠️ regra |
| `status` | publicado / em produção | ✅ (165 publicados; 65 em produção pendentes) |

## 6. Perguntas para o CEFOR / Comissão MOOC (validação)

1. **Objetivos:** aceitam os 4 como atalhos parciais (opção a) ou querem um 5º tema "Educação Ambiental e Ciências" (opção b)?
2. **Trilhas:** confirmam os membros propostos? Quais 5 cursos oficiais da trilha Rio Doce e os 4 da Maker?
3. **Categorias:** podemos fundir as de 1–3 cursos com afins?
4. **Tags:** aprovam a consolidação das tags fragmentadas do Rio Doce?
5. **Carga horária:** cronograma da Raquel para popular os dados (bloqueia trilhas, filtros por CH e o Planejador).
6. **Em produção:** onde está a lista dos 65 cursos em produção (para incluir no catálogo)?

---

## Rastreabilidade (Audit)
- **Cobertura:** os 165 cursos publicados estão no `catalogo-cursos.csv` e no `taxonomia-cursos.csv`.
- **Classificação:** todo curso tem ≥1 categoria (fato). Objetivos/trilhas são proposta rastreável (regra explícita nas §3–4).
- **Status:** 165 = publicado; os 65 em produção estão **pendentes** (fonte `references/cursos-fonte.md`, a incorporar).
- **Esquema:** campos definidos na §5; lacunas marcadas (carga horária, inscritos, descrição).
- **Fato × Proposta:** categorias/tags = fato; objetivos/trilhas = proposta a validar (No Invention).
