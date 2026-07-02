# Comparativo de Taxonomias — qual vira a navegação primária

> **Estágio:** 02 — Catálogo · **Data:** 02/07/2026 · **Status:** ✅ DECIDIDO — **navegação primária = as 15 Categorias do formulário** (02/07). Modelo final em `arquitetura-informacao.md` v4. Ação registrada: recategorizar cursos nas 15 Categorias na migração.
> **Âncora:** objetivo oficial da plataforma (Resolução CS 72/2020, Art. 1º): **"cursos oferecidos a distância e abertos à comunidade"** → público **leigo, nacional, de descoberta**. A navegação tem que falar a língua do cidadão comum, cobrir o catálogo e **escalar sozinha** (curso novo a cada 3 meses).
> **Novidade decisiva:** o **formulário de cadastro** que o professor preenche já coleta, **na fonte**, três campos de classificação.

---

## 1. O que o formulário de cadastro revela

Ao criar um MOOC, o professor preenche (além dos campos do Art. 14 da resolução):

| Campo do formulário | Seleção | Nº de opções | Natureza |
|---------------------|---------|:---:|----------|
| **Eixo Tecnológico** | **única** | 13 | Oficial — eixos do Catálogo Nacional (CNCT); é o Art. 14 IX da resolução |
| **Categorias** | **múltipla** | 15 | Temática/institucional (lista do CEFOR) |
| **Palavras-chave (tags)** | livre (`;`) | — | Busca |

**Descoberta importante:** o filtro de **19 categorias do site atual** (o desbalanceado, 44 vs 1) parece ser uma **mistura** de Eixo Tecnológico + Área CNPq + Categorias jogados num campo só — por isso a bagunça. O formulário mostra que **são coisas separadas**. As 15 categorias do formulário **não** são iguais às 19 do site (o formulário tem "Finanças e Contabilidade" e **não** tem "Ciências Humanas", "Ciências Sociais Aplicadas", "Ciências Exatas e da Terra", "Desenvolvimento Educacional e Social", "Produção Cultural e Design" — essas eram, na verdade, valores de Área CNPq / Eixo Tecnológico infiltrados no filtro).

> **Consequência prática:** não precisamos **inventar** uma taxonomia de navegação. Já existem **duas oficiais, preenchidas na fonte** (governança zero para curso novo). A decisão é **qual delas vira a navegação primária** — e qual fica como filtro/metadado.

## 2. Tabela comparativa (candidatas a navegação PRIMÁRIA)

| # | Opção | Fonte | Oficial? | Seleção | Nº | Categorias vazias neste catálogo? | Governança (curso novo) | Fala com o público leigo (objetivo)? | SEO |
|---|-------|-------|:---:|---------|:---:|-----------------------------------|-------------------------|--------------------------------------|-----|
| 1 | **Eixo Tecnológico** | Formulário (Art. 14 IX) | ✅ CNCT | Única | 13 | ⚠️ **Muitas** (Militar, Produção Industrial/Alimentícia, Controle de Processos, Infraestrutura ≈ 0) | **Zero** | ⚠️ Termos **industriais/técnicos** | Fraco ("Recursos Naturais" ninguém busca) |
| 2 | **Categorias (formulário)** | Formulário | Semi (institucional) | **Múltipla** | 15 | Poucas | **Zero** | ✅ **Amigável** (Educação, Línguas, Ambiente e Saúde, Design…) | ✅ Forte |
| 3 | Categorias do site atual | Site (legado) | ❌ | Múltipla | 19 | ⚠️ Sim (44 vs 1) | Manual/bagunçada | Médio (mistura jargão) | Médio |
| 4 | Área do conhecimento (CNPq) | Art. 14 VIII | ✅ CNPq | Única | ~9 | ⚠️ acadêmica | Zero | ❌ **Jargão acadêmico** | Fraco |
| 5 | Temas consolidados (derivados) | **Nós** | ❌ | Múltipla | ~10 | Balanceada | ⚠️ **Precisa regra + dono** | ✅ Sim | ✅ Forte |
| 6 | Público-alvo ("Para quem") | Art. 14 XII | ✅ | Múltipla | ~6 | — | Zero | ✅ Autoidentificação | ✅ (`/publicos/`) |

**Como cada uma se correlaciona com o objetivo ("aberto à comunidade"):**
- **Opção 1 (Eixo Tecnológico):** é a mais "limpa" tecnicamente (seleção única = zero sobreposição) e 100% oficial, mas foi desenhada para **educação técnica/profissional**. Num catálogo de **extensão aberto ao público**, os rótulos ("Controle e Processos Industriais", "Militar") **destoam da missão** e ~metade fica vazia. **Ótima como metadado/relatório; ruim como vitrine principal.**
- **Opção 2 (Categorias do formulário):** rótulos que o **cidadão comum entende**, já preenchidos na fonte, bons para SEO. É a que **mais combina com "aberto à comunidade"**. O preço é a sobreposição (múltipla), resolvida com URL canônica por curso.
- **Opção 4 (CNPq):** essencial como **metadado oficial** (Art. 14 VIII) e para relatório, mas "Ciências Sociais Aplicadas" não é vitrine para leigo.
- **Opção 5 (derivada):** era minha proposta do Cenário C. **Deixa de fazer sentido** agora — inventar e manter uma taxonomia dá trabalho (governança) quando já existe uma oficial na fonte.
- **Opção 6 (público):** não é a espinha temática, é a **camada de atalho** "Para quem".

## 3. Recomendação (correlacionada com o objetivo)

| Papel | Taxonomia escolhida | Por quê |
|-------|---------------------|---------|
| **Navegação PRIMÁRIA (tema)** | **Categorias do formulário (15)** | At-source (governança zero), amigável ao leigo (bate com "aberto à comunidade"), boa para SEO, multi-rótulo reflete a realidade |
| **Filtro secundário + metadado + relatório** | **Eixo Tecnológico (13)** | Oficial, seleção única (corte alternativo limpo), mas termos técnicos/empties o desqualificam como vitrine |
| **Metadado/relatório apenas** | **Área CNPq (9)** | Oficial (Art. 14 VIII), mas jargão acadêmico |
| **Camada de atalho** | **"Para quem" / público-alvo (6)** | `/publicos/…`, autoidentificação, SEO ("cursos para professores") |
| **Busca** | **Tags** | Higienizar vocabulário |
| **Selos transversais** | **Libras, Audiodescrição, Idioma** | Oficiais (Art. 14 VI + Arts. 13/16) |

**Mudança honesta em relação ao Cenário C:** eu recomendava **inventar ~10 temas consolidados**. **Retiro essa parte.** Com as **Categorias do formulário (15)** existindo na fonte, criar uma taxonomia derivada só adiciona governança sem ganho. O **espírito** do Cenário C sobrevive (tema como espinha + público como atalho + facetas + demanda), mas o "tema" **é a lista oficial de 15**, não uma invenção nossa. *(Se, ao ver os números reais, alguma das 15 ficar minúscula, aí sim faz-se um ajuste pontual de agrupamento — mas partindo do oficial.)*

## 4. Sobre o desbalanceamento (para não repetir o erro do site atual)

Qualquer taxonomia terá "Educação" e "Ambiente e Saúde" grandes e "Matemática" pequena — é a **cara do catálogo**, não defeito da taxonomia. Isso **não se resolve trocando de taxonomia**, e sim com as **outras camadas**: facetas (público, nível, carga horária, idioma), seção "Mais cursados" (demanda) e busca. O erro do site atual não foi "ter categorias", foi **misturar três taxonomias num filtro só**.

## 5. Reconciliação de dados (pendência)

Nosso `catalogo-cursos.csv` tem as **19 categorias do site antigo**. Os campos reais do formulário (**Eixo Tecnológico + as 15 Categorias + idioma + nível**) estão no **cadastro WordPress de cada curso** — precisamos **extrair do banco** (dump) para popular o catálogo com a taxonomia correta. Enquanto isso, trabalhamos com aproximação.

## 6. Decisão a tomar (definitiva)

1. **Confirmar a navegação primária = Categorias do formulário (15)** (recomendado), com Eixo Tecnológico e CNPq como metadado/filtro?
2. Confirmar que **"Para quem" (público)** é camada de atalho, não a espinha.
3. Autorizar a **extração dos campos reais** (eixo, categorias, idioma, nível) do dump para o catálogo.

> Decidido isto, consolido no `arquitetura-informacao.md` **v4** (com objetivo ancorado na resolução, camada A = Art. 14, e navegação = Categorias 15).
