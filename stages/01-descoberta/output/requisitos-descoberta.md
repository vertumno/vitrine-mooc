# Requisitos da Descoberta — Nova Vitrine MOOC Ifes (v2, incorpora o PRD)

> **Estágio:** 01 — Descoberta · **Versão:** 2.0 · **Data:** 01/07/2026
> **Fontes:** `shared/prd-vitrine-mooc-v1.md` (PRD canônico), `shared/projeto-meta.md`, `shared/resumo-reuniao.md`, `shared/convencoes-git-deploy.md`, `stages/01-descoberta/references/html-vitrine-atual.md`, `stages/03-design-ux/references/deep-research-ux-descoberta-mooc.md`, conversa com o usuário (Elton).
> **Origens entre colchetes:** `[PRD]`, `[Reunião]`, `[Vitrine atual]`, `[Usuário]`, `[Meta]`, `[DeepResearch]`.

Documento canônico de requisitos. A **v2 incorpora o PRD** (que define o produto em **3 camadas**) e resolve os conflitos com a **informação mais atual**. Detalhe da reconciliação em `analise-prd-vs-projeto.md`.

> **Nota de baseline:** por decisão do usuário, o build já iniciado pelo Marquito **não é considerado nesta fase**. A baseline aqui é o site atual em produção + o PRD.

---

## 1. Contexto e estratégia

- Produto: **mooc.cefor.ifes.edu.br** — cursos abertos (MOOC) do Ifes. Reposicionado pelo PRD como **ferramenta de qualificação profissional gratuita e certificada** (conceito **5 estrelas INEP/MEC**). `[PRD]`
- Vitrine atual em produção: WordPress 5.9, tema `vitrinemooctheme` (Bootstrap 4.2.1, FA 4.7), single-page. `[Vitrine atual]`
- **Estratégia técnica:** migrar para WP7, replicar a estrutura de repositório da Base de Conhecimento e desenvolver em **ambiente de teste** (nunca direto em produção). `[Reunião]`
- **Estratégia de produto (PRD):** evolução em **3 camadas** entregues de forma faseada até **agosto/2026 (CONCEFOR)**. `[PRD]`
- Setores: **CGTI** (infra — Eduardo) e **CGTE** (dev — Elton e Marquito). Aprovação: **Comissão MOOC**. `[Meta]` `[PRD]`

## 2. Objetivos

Prioridades do usuário `[Usuário]`, alinhadas ao PRD `[PRD]`:
1. **Modernizar visual e responsividade** — identidade nova (design system), mobile-first, performance, acessibilidade.
2. **Melhorar a descoberta de cursos** — busca, filtros, navegação por objetivo e o **Wizard** (validado pela `[DeepResearch]`).
3. **Gerar matrículas / qualificação profissional** — hero com proposta de valor, selo MEC, **Planejador de Licença Capacitação** (maior gerador de matrículas segundo o PRD).

## 3. Escopo — as 3 camadas `[PRD]`

| Camada | O que é | Onde vive |
|--------|---------|-----------|
| **1. Vitrine Evolutiva** | Redesign da home sobre a estrutura WordPress | home (`/`) |
| **2. Hub de Qualificação** | Planejador de Licença, navegação por objetivo, trilhas | página interna `/qualificacao` |
| **3. Ferramenta Inteligente** | Wizard 3-4 perguntas que recomenda cursos | modal ou página interna (CTA do hero) |

- **Base técnica:** migração para **WordPress 7.0** + reestrutura do repositório (modelo Base de Conhecimento). `[Reunião]`
- **Futuro (fora do escopo atual):** Área do Aluno (dashboard, Moodle API, progresso). `[PRD]`
- **Fora de escopo:** alterar o Moodle (backend dos cursos) e o fluxo de autenticação. `[PRD §4.3]`

## 4. Requisitos funcionais (FR)

### Camada 1 — Vitrine Evolutiva
| ID | Requisito | Origem |
|----|-----------|--------|
| FR-01 | Vitrine de cursos em cards (imagem, título, acesso ao Moodle). | `[Vitrine atual]` |
| FR-02 | **Busca textual** com normalização de acentos (título + categoria + tags); evoluir com autocomplete e tolerância a erro. | `[Vitrine atual]` `[DeepResearch]` |
| FR-03 | **Filtros avançados**: categoria + **carga horária** + **Libras**, multi-seleção, com sinalização de filtro ativo. | `[PRD §4.11]` `[DeepResearch R1]` |
| FR-04 | Selo de **Libras** nos cursos aplicáveis. | `[Vitrine atual]` |
| FR-05 | Seções "O que é" e "Como Funciona" (mantidas, visual renovado). | `[PRD §4.7]` |
| FR-06 | **FAQ com lazy load** — mostra 5, "Ver todas" expande as 34. | `[PRD §4.8]` |
| FR-07 | Criar conta e login integrados ao Moodle. | `[Vitrine atual]` |
| FR-08 | **Barra de estatísticas** (matrículas | nº de cursos | 5 estrelas MEC | 100% gratuito) com **dado dinâmico**, não hardcoded. | `[PRD §4.3]` |
| FR-09 | Rodapé com links úteis + institucionais. | `[Vitrine atual]` |
| FR-10 | **Hero com proposta de valor** ("Qualificação profissional gratuita e certificada pelo Ifes") + **duplo CTA** (busca + Wizard) + selo MEC. | `[PRD §4.1]` |
| FR-11 | **Selo 5 estrelas INEP/MEC** com destaque visual. | `[PRD §2.2]` |
| FR-12 | **Cards enriquecidos** — fechado: CH, badge "Novo" (últimos 3 meses), Libras, nº de inscritos; expandido: descrição, objetivos, categoria/tags, "Acessar curso", **"Compartilhar" (WhatsApp/link)**. | `[PRD §4.2]` |
| FR-13 | **Seções curadas** tipo Netflix: "Em destaque" (manual), "Recentes" (data), "Mais cursados" (matrículas). | `[PRD §4.4]` |
| FR-14 | **Navegação por objetivo** — 4 cards: Inovar na sala de aula / Licença Capacitação / Aprender tecnologia / Crescer na carreira. | `[PRD §4.5/5.2]` |
| FR-15 | **Banner de Licença Capacitação** na home → página interna do Hub. | `[PRD §4.6]` |
| FR-16 | **Projetos parceiros** na home — **Rio Doce Escolar** e **UnAC** com descrição, imagem e link. | `[PRD §4.10]` (ver `projetos-especiais.md`) |
| FR-17 | **Correções técnicas** — `alt` corretos, cookie consent, **aviso de e-mail Hotmail/Outlook antes do cadastro**, proporção de imagens. | `[PRD §4.12]` |

### Camada 2 — Hub de Qualificação (`/qualificacao`)
| ID | Requisito | Origem |
|----|-----------|--------|
| PLC-01..09 | **Planejador de Licença para Capacitação** — formulário (dias/data/área), cálculo de CH mínima (30h/semana), algoritmo de sugestão de cursos, resultado com links de matrícula, **exportar PDF**, orientações Moodle, página de contexto (legislação), funcionar **sem login**, prova social. | `[PRD §5.1]` |
| TRL-01 | **Trilhas de aprendizagem** (percursos de 3-5 cursos): Professor Inovador (90h), Maker na Educação (120h), Educação Ambiental / Rio Doce (100h), Atendimento e Vendas. | `[PRD §5.3]` |

### Camada 3 — Ferramenta Inteligente (Wizard)
| ID | Requisito | Origem |
|----|-----------|--------|
| WIZ-01..06 | **Wizard de Descoberta** — 3-4 etapas (perfil / área / tempo), filtragem combinada **sem IA**, resultado em cards enriquecidos, acessível via CTA do hero + menu, captura anônima de perfil para analytics, refazer respostas. | `[PRD §6]` `[DeepResearch]` |

> Tabelas completas de PLC-*, TRL e WIZ-* estão no PRD (`shared/prd-vitrine-mooc-v1.md` §5 e §6).

## 5. Requisitos não-funcionais (NFR)

| ID | Requisito | Origem |
|----|-----------|--------|
| NFR-01 | **Responsividade mobile-first**. | `[Usuário]` `[PRD]` |
| NFR-02 | **Acessibilidade** (WCAG 2.2) — `alt` correto, teclado, contraste, foco visível, selo Libras. | `[DeepResearch]` `[PRD]` |
| NFR-03 | **Performance** com catálogo grande — lazy-load/Load More + otimização de imagens. | `[DeepResearch R4]` |
| NFR-04 | **Analytics em GA4** (substituir o Universal/UA) + eventos do Wizard e origem do Planejador. | `[Vitrine atual]` `[PRD §8]` |
| NFR-05 | Stack atual e versionada (menos dependência de CDN antigo). | `[Vitrine atual]` |
| NFR-06 | Código manutenível em **WordPress 7** (tema/blocos/templates). | `[Reunião]` |
| NFR-07 | **SEO** — ranquear "licença capacitação cursos gratuitos" (meta Top 3). | `[PRD §8]` |

## 6. Restrições (CON)

| ID | Restrição | Origem |
|----|-----------|--------|
| CON-01 | **WordPress 7.0** desde já (atual 5.9). | `[Reunião]` |
| CON-02 | **Ambiente de teste dedicado** (VM CGTI); nada sobe direto em produção. | `[Reunião]` |
| CON-03 | **Dump do banco atual** para trabalho local; a Vitrine não pode ser travada — refaz-se o dump na migração. | `[Reunião]` |
| CON-04 | Mesmo Git; copiar estrutura da Base de Conhecimento; descartar o HTML puro antigo. | `[Reunião]` |
| CON-05 | Branch de trabalho → PR para a branch da CGTI; **nunca PR direto à Master**. | `[Reunião]` |
| CON-06 | `git push`/`gh pr` **exclusivos do @devops**. | `[Convenções]` |
| CON-07 | **Deadline de produto: agosto/2026 (CONCEFOR)**, faseado Abr→Ago (Fase 1 Planejador; Fase 2 Design System+home; Fase 3 objetivo+trilhas+projetos; Fase 4 Wizard). | `[PRD §7]` |
| CON-08 | **Dados de carga horária** — campo existe no WP mas **não está populado**; depende da **Raquel**. Bloqueia cards, filtros por CH, trilhas e o Planejador. | `[PRD §7.1]` |
| CON-09 | **Aprovação da Comissão MOOC** do conceito antes da implementação. | `[PRD §7.1]` |
| CON-10 | Infra da CGTI: ambiente de teste previsto por volta de **06/07/2026**. | `[Reunião]` `[Meta]` |

## 7. Decisões

| # | Decisão | Situação |
|---|---------|----------|
| D-01 | **Arquitetura de páginas** | **RESOLVIDA pelo PRD:** home single-page evolutiva (estilo Netflix) + páginas internas (`/qualificacao`) + Wizard (modal/página). |
| D-02 | Configs da CGTI (`BRANCH_PRODUCAO`, `BRANCH_TESTE`, `URL_TESTE`, `REPO_BASE_CONHECIMENTO`) | Pendente — `setup`/CGTI. |
| D-03 | Fonte do contador dinâmico (FR-08) | A definir (API Moodle / banco). |
| D-04 | Esquema de link do curso (slug × `?id=`) | Consolidar; o Anexo B do PRD resolve vários por `?id=`. |

**Resolução de conflitos (usar o dado mais atual):**
- **Nº de cursos:** **165** (extração ao vivo, jul/2026) — autoritativo. O PRD (152, abr/2026) é snapshot antigo.
- **Número de topo:** usar o **contador ao vivo (~299 mil)** como matrículas/reconexões; o PRD (284.595, abr) fica superado. Confirmar definição/fonte dinâmica.
- **Carga horária:** permanece **pendente** (CON-08) — não inventar valores.

## 8. Métricas de sucesso `[PRD §8]`

| Métrica | Meta |
|---------|------|
| Matrículas via Planejador (origem por URL) | +15% matrículas novas |
| Uso do Wizard (analytics) | >500 usos/mês |
| Tempo na página (GA) | +40% |
| Taxa de conclusão (Moodle) | Aumento via trilhas |
| SEO "licença capacitação" (Search Console) | Top 3 |

## 9. Stakeholders e fluxo `[PRD §2.4]`

- **Elton** (design/UX/wireframes) → **Marquito** (dev WordPress/backend/Moodle) → **Comissão MOOC** (aprova).
- **CGTI/Eduardo** (infra, ambiente, dump, branches). **Raquel** (dados de carga horária).

## 10. Dependências

- **Dados de carga horária** (Raquel) — bloqueia CON-08.
- **CGTI (Eduardo):** ambiente de teste, dump, definição de branches.
- **Comissão MOOC:** aprovação do conceito.
- **Estrutura da Base de Conhecimento** (`REPO_BASE_CONHECIMENTO`): ainda não fornecida — não presumida.

---

## Rastreabilidade (Audit)
- **Cobertura:** as 3 camadas do PRD, os objetivos do usuário e os débitos do site atual estão nas seções 3–6.
- **Rastreabilidade:** cada item referencia origem (`[PRD]`, `[Reunião]`, `[Vitrine atual]`, `[Usuário]`, `[Meta]`, `[DeepResearch]`).
- **Restrições:** WP7, ambiente, dump, Git, deadline CONCEFOR, dados de CH e aprovação registrados (CON-01..10).
- **Conflitos:** resolvidos pela informação mais atual (§7); build do Marquito desconsiderado nesta fase por decisão do usuário.
