# Arquitetura de Informação — Vitrine MOOC (modelo definitivo)

> **Estágio:** 02 — Catálogo · **Versão:** 4.1 · **Data:** 06/07/2026 · **Papel:** arquitetura de informação
> **Decisões travadas:** (1) **objetivo** ancorado na Resolução CS 72/2020 — "abertos à comunidade" (**"qualificação profissional" removido**); (2) **navegação primária = as 15 Categorias do formulário**; (3) **Eixo Tecnológico + Área CNPq = metadados oficiais**; (4) **trilha removida** (só Séries + Projetos); (5) **Licença Capacitação = área**, não objetivo; (6) selos **Libras + Audiodescrição + Idioma**; (7) **escopo = 165 cursos publicados** — os 65 "em produção" ficam **fora deste projeto**; (8) **carga horária resolvida** — populada em `catalogo-cursos-completo.csv` (coluna `carga_horaria`); (9) **UnAC definido** (§7); (10) **sem tree test** — rótulos "Para quem" são decisão editorial do CEFOR.
> **Âncoras:** `shared/resolucao-cs-72-2020-mooc.md`, `shared/seo-geo-aeo.md`, `comparativo-taxonomias.md`, `relatorio-publicos-alvo-mooc-ifes.md`, `powerbi-mooc-ifes/`.
> **Substitui** as §3–4 de `taxonomia.md` e encerra `decisao-taxonomia-cenarios.md` e `comparativo-taxonomias.md`.

---

## 0. Objetivo e princípios

**Objetivo oficial** (Resolução CS 72/2020, Art. 1º): MOOC = **"cursos oferecidos a distância e abertos à comunidade"** — democratização/inclusão social, para o **público leigo, nacional, de descoberta**. É extensão/curso livre, gratuito, sem tutoria, sem seleção, ≤60h, certificado (≥60%). **Toda a categorização reflete isto: falar a língua do cidadão comum.**

Princípios: (1) curso é autossuficiente — nada trava curso, agrupamento é sugestão; (2) o catálogo cresce a cada 3 meses → a estrutura primária classifica curso novo **por regra/metadado** preenchido na fonte; (3) sucesso = achar + concluir + ser indexável (SEO/GEO/AEO é parte da arquitetura).

## 1. Contexto que a arquitetura enfrenta

**Descompasso oferta × demanda** `[PowerBI]`: catálogo dominado por educação/ambiental (Rio Doce = 31), mas demanda concentrada em prático — Inglês (22.390), Moodle Educadores (11.392), Canva (8.589), Google Drive (8.007). 65% das matrículas fora do ES. → A navegação primária favorece **descoberta + demanda**; proveniência (séries/projetos) fica secundária.

## 2. As camadas do modelo

| Camada | Contém | Natureza | Papel |
|--------|--------|----------|-------|
| **A. Metadados oficiais** | Art. 14 da resolução: Área CNPq, **Eixo Tecnológico**, Idioma, Nível, Público-alvo, Objetivos, carga horária, certificação, status, provedor | Registro (fonte da verdade) | Alimenta tudo |
| **B. Navegação (UX + SEO)** | **Categorias (15)** [primária], **"Para quem"** (público), Busca (tags), Facetas, Seções curadas, Wizard | Apresentação | Como o usuário e o Google acham |
| **C. Proveniência** | **Séries** (Lovelace, Educador Maker…), **Projetos parceiros** (Rio Doce, UnAC) | Editorial | Página/selo próprios |
| **D. Selos transversais** | **Libras, Audiodescrição, Idioma** | Metadado/flag | Acessibilidade + idioma |
| **E. Área dedicada** | **Licença para Capacitação** + Planejador | Destino | Serviço, não filtro |

## 3. Classificação oficial × Navegação

A resolução (Art. 14) obriga **duas** classificações oficiais por curso, ambas **metadados**:
- **Área do conhecimento (CNPq)** — inciso VIII. Para relatório/registro. Jargão acadêmico → não é navegação.
- **Eixo Tecnológico** — inciso IX, **1 de 13** (padrão CNCT). Seleção única, oficial. Vira **filtro secundário + metadado + relatório** (termos industriais e ~7 eixos vazios neste catálogo → ruim como vitrine principal).

A **navegação** usa uma terceira coisa, amigável ao público: as **15 Categorias** do formulário (múltipla). Não se inventou nada — é o campo que o professor já preenche.

**Por que o filtro atual (19) é ruim:** ele **mistura** as três taxonomias num campo só. Ao separar:

| Rótulos do site (19) | Destino |
|----------------------|---------|
| 14 rótulos temáticos (Educação, Línguas, Ambiente e Saúde, Design, Matemática, Engenharia, Gestão, Inclusão, Tec. e Informática, Tec. Educacionais, EaD, Desenv. Pessoal, Artes e Humanidades, Ciências da Natureza) | ✅ **mantêm** como Categoria |
| Ciências Humanas · Ciências Sociais Aplicadas · Ciências Exatas e da Terra | → eram **Área CNPq** (viram metadado) |
| Desenvolvimento Educacional e Social · Produção Cultural e Design | → eram **Eixo Tecnológico** (viram metadado) |
| *(nova)* Finanças e Contabilidade | ➕ destacada (estava escondida em Gestão) |

## 4. Navegação primária — as 15 Categorias

Múltipla seleção (um curso pode ter várias). Tamanho aproximado do legado (real virá do dump):

| Categoria | Reúne | ~Tam. |
|-----------|-------|:---:|
| Ambiente e Saúde | Educação ambiental, saúde, Rio Doce | ~44 |
| Educação | Docência, práticas pedagógicas, formação de professores | ~39 |
| Tecnologias e Informática | Programação, dados, sistemas | ~18 |
| Educação a Distância | Moodle, EaD, mediação | ~16 |
| Tecnologias Educacionais | Ferramentas digitais no ensino | ~15 |
| Gestão | Gestão pública/escolar, liderança | ~10 |
| Inclusão e Acessibilidade | Libras, educação especial, acessibilidade | ~7 |
| Ciências da Natureza | Biologia, química, física, astronomia | ~6 |
| Línguas | Inglês, espanhol | ~6 |
| Matemática | Educação matemática, lógica | ~5 |
| Artes e Humanidades | Cultura, filosofia, história | ~4 |
| Desenvolvimento Pessoal | Hábitos de estudo, finanças pessoais | ~4 |
| Design | Design gráfico, game design | ~2 |
| Engenharia | Eficiência energética, saneamento | ~2 |
| Finanças e Contabilidade | Finanças, contabilidade | ~1–3 |

Cada Categoria vira **`/areas/{slug}/`** (página editorial indexável: texto + lista + links) `[SEO]`.

> **⚠️ AÇÃO DE MIGRAÇÃO (obrigatória):** na migração, **recategorizar todos os cursos conforme as 15 Categorias**. Os cursos legados carregam o esquema antigo (19, com CNPq e Eixo infiltrados). É preciso: (a) remapear os 5 rótulos infiltrados (Ciências Humanas/Sociais/Exatas → Área CNPq metadado; Desenv. Educacional e Social / Produção Cultural e Design → Eixo Tecnológico metadado); (b) atribuir a cada curso **1+ das 15 Categorias**; (c) conferir/preencher **Eixo Tecnológico (1), Idioma, Nível, Público-alvo, carga horária**. Executar nos **Estágios 04 (setup/dump) e 06 (QA/entrega)**; validar com o CEFOR.

## 5. "Para quem" (camada de atalho — não é a espinha)

Atalhos por público na home + **`/publicos/{slug}/`** (indexáveis — "cursos para professores" é busca-alvo `[SEO]`). São atalhos, nunca rota única (107/165 cursos têm 2+ públicos):

- Para professores e educadores (~66%) · Para a comunidade (comece do zero) (~48%) · Para o trabalho e a carreira · Para servidores e setor público (→ liga à área de Licença).

Rótulos definidos por decisão editorial do CEFOR (rótulo concreto > esperto). **Sem tree test.**

## 6. Selos transversais (oficiais — Art. 14 VI + Arts. 13/16)

| Selo | Sinaliza | Schema.org |
|------|----------|-----------|
| **Libras** | Tradução/interpretação em Libras | `accessibilityFeature: "signLanguage"` |
| **Audiodescrição** | Recurso para cegos/baixa visão | `accessibilityFeature: "audioDescription"` |
| **Idioma** | Idioma em que o curso é ministrado | `inLanguage` |

Idioma resolve duplicatas: "Lesson Study" PT e EN = **mesmo curso, dois selos de idioma**.

## 7. Séries e Projetos (proveniência)

- **Séries** (marca/produção; selo + página de coleção): Atendente e Vendedor (3, com níveis), Educador Maker (4), Lovelace (6, paralelos), Embrace (3), Lesson Study (PT/EN = mesmo curso).
- **Projetos parceiros** (parceria + hub próprio): **Rio Doce Escolar** (31, `/v/riodoce/`), **UnAC** (33, `/v/unac/`) — **Universidade Aberta Capixaba**, programa do Governo do Estado do Espírito Santo para expandir e democratizar o Ensino Superior gratuito; parceria Ifes (via CEFOR) × Governo do ES na oferta de cursos abertos, massivos e online de alta qualidade para toda a sociedade.
- Um Projeto é uma Série grande com identidade institucional.

## 8. Licença para Capacitação = área

Qualquer curso certificado gera horas → Licença não filtra conteúdo. `/qualificacao/`: instruções (o que é, quem tem direito, legislação) + Planejador (PRD Camada 2).

## 9. SEO/GEO/AEO `[SEO]`

URLs slug (`/cursos/{slug}/`, `/areas/{categoria}/`, `/publicos/{publico}/`, `/certificacao/`, `/qualificacao/`); **1 URL canônica por curso** (resolve multi-categoria/multi-público sem duplicar índice); indexável = categorias + públicos + certificação (páginas editoriais reais); **não indexável** = combinações de filtro (`noindex`/canonical); schema `Course` + `ItemList` + `BreadcrumbList` + `Organization` + `inLanguage`/`accessibilityFeature`; conteúdo principal no HTML (cuidado com "carregar mais" — fallback rastreável).

## 10. Metadados por curso = Art. 14 da resolução (Camada A)

| Campo | Origem | Obrigatório |
|-------|--------|:---:|
| Nome, proponente, campus, ano/semestre | Art. 14 I–IV | ✅ |
| Carga horária (≤60h) | Art. 14 V | ✅ (populada em `catalogo-cursos-completo.csv`) |
| **Idioma** | Art. 14 VI | ✅ (selo) |
| **Nível** (básico/interm./avançado) | Art. 14 VII | ✅ |
| **Área do conhecimento (CNPq)** | Art. 14 VIII | ✅ (metadado) |
| **Eixo Tecnológico** (1 de 13) | Art. 14 IX | ✅ (metadado/filtro) |
| **Categorias (15)** | formulário | ✅ ≥1 (**navegação**) |
| **Público-alvo** | Art. 14 XII | ✅ (atalho "Para quem") |
| Objetivos, ementa, metodologia, perfil do egresso, avaliação, bibliografia | Art. 14 XV–XXII | ✅ (página/SEO) |
| Certificação, status (publicado/produção/encerrado) | resolução | ✅ |
| **Libras, Audiodescrição** | Arts. 13/16 | ➖ (selo) |
| Série, Projeto | editorial | ➖ |
| tags | formulário | ✅ (busca) |

**Regra de publicação:** preenchido o Art. 14, o curso entra em busca, filtros, `/areas/`, `/publicos/`, "Recentes" e selos **automaticamente**.

## 11. Navegação (o teste de "achar o curso")

| Usuário | Caminho | Camada |
|---------|---------|--------|
| Sabe o tema | Busca / **Categoria** (`/areas/`) | B |
| Sabe quem é | **"Para quem"** (`/publicos/`) | B |
| Precisa de acessibilidade | Filtro/selo (Libras/Audiodescrição/Idioma) | D |
| Não sabe o que quer | Wizard | B |
| Servidor querendo horas | Área Licença + Planejador | E |
| Quer o mais buscado | "Mais cursados" | B |
| Interessado num projeto/marca | Página do Projeto/Série | C |
| Chega pelo Google | `/cursos/`, `/areas/`, `/publicos/` indexáveis | B+SEO |

## 12. Pendências

1. **Migração:** recategorizar cursos nas 15 Categorias + conferir/popular Eixo/Idioma/Nível/Público no destino (§4, Estágios 04/06). Carga horária já disponível como fonte em `catalogo-cursos-completo.csv`.
2. **Dados:** extrair os campos reais do **dump** (nosso `catalogo-cursos.csv` tem as 19 legadas).

**Resolvidas (06/07/2026):** **UnAC** definido (§7); **carga horária** populada em `catalogo-cursos-completo.csv`; **escopo = 165 publicados** (os 65 "em produção" ficam fora deste projeto); **sem tree test** (rótulos "Para quem" = decisão editorial do CEFOR).

---

## Rastreabilidade
- **Oficial:** objetivo e metadados vêm da Resolução CS 72/2020; Eixo Tecnológico = CNCT; Categorias = formulário do CEFOR.
- **Evidência:** demanda `[PowerBI]`; público **sugerido pelos autores** `[Público]`; SEO `[SEO]`.
- **Decisão do usuário (02/07):** 15 Categorias = navegação primária; recategorização na migração.
- **Coerência MOOC:** sem trilhas/pré-requisitos; classificação oficial preservada como metadado; navegação amigável por cima.
