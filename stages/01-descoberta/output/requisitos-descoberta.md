# Requisitos da Descoberta â€” Nova Vitrine MOOC Ifes (v2, incorpora o PRD)

> **EstÃ¡gio:** 01 â€” Descoberta Â· **VersÃ£o:** 2.0 Â· **Data:** 01/07/2026
> **Fontes:** `shared/prd-vitrine-mooc-v1.md` (PRD canÃ´nico), `shared/projeto-meta.md`, `shared/resumo-reuniao.md`, `shared/convencoes-git-deploy.md`, `stages/01-descoberta/references/html-vitrine-atual.md`, `stages/03-design-ux/references/deep-research-ux-descoberta-mooc.md`, conversa com o usuÃ¡rio (Elton).
> **Origens entre colchetes:** `[PRD]`, `[ReuniÃ£o]`, `[Vitrine atual]`, `[UsuÃ¡rio]`, `[Meta]`, `[DeepResearch]`.

Documento canÃ´nico de requisitos. A **v2 incorpora o PRD** (que define o produto em **3 camadas**) e resolve os conflitos com a **informaÃ§Ã£o mais atual**. Detalhe da reconciliaÃ§Ã£o em `analise-prd-vs-projeto.md`.

> **Nota de baseline:** por decisÃ£o do usuÃ¡rio, o build jÃ¡ iniciado pela equipe **nÃ£o Ã© considerado nesta fase**. A baseline aqui Ã© o site atual em produÃ§Ã£o + o PRD.

---

## 1. Contexto e estratÃ©gia

- Produto: **mooc.cefor.ifes.edu.br** â€” cursos abertos (MOOC) do Ifes: cursos a distÃ¢ncia **abertos Ã  comunidade**, gratuitos e certificados (conceito **5 estrelas INEP/MEC**). Objetivo oficial na **ResoluÃ§Ã£o CS 72/2020, Art. 1Âº**. `[ResoluÃ§Ã£o]`
- Vitrine atual em produÃ§Ã£o: WordPress 5.9, tema `vitrinemooctheme` (Bootstrap 4.2.1, FA 4.7), single-page. `[Vitrine atual]`
- **EstratÃ©gia tÃ©cnica:** migrar para WP7, replicar a estrutura de repositÃ³rio da Base de Conhecimento e desenvolver em **ambiente de teste** (nunca direto em produÃ§Ã£o). `[ReuniÃ£o]`
- **EstratÃ©gia de produto (PRD):** evoluÃ§Ã£o em **3 camadas** entregues de forma faseada atÃ© **agosto/2026 (CONCEFOR)**. `[PRD]`
- Setores: **CGTI** (infra â€” Eduardo) e **CGTE** (dev - Elton e equipe de desenvolvimento). AprovaÃ§Ã£o: **ComissÃ£o MOOC**. `[Meta]` `[PRD]`

## 2. Objetivos

Prioridades do usuÃ¡rio `[UsuÃ¡rio]`, alinhadas ao PRD `[PRD]`:
1. **Modernizar visual e responsividade** â€” identidade nova (design system), mobile-first, performance, acessibilidade.
2. **Melhorar a descoberta de cursos** â€” busca, filtros, navegaÃ§Ã£o por objetivo e o **Wizard** (validado pela `[DeepResearch]`).
3. **Gerar matrÃ­culas / qualificaÃ§Ã£o profissional** â€” hero com proposta de valor, selo MEC, **Planejador de LicenÃ§a CapacitaÃ§Ã£o** (maior gerador de matrÃ­culas segundo o PRD).

## 3. Escopo â€” as 3 camadas `[PRD]`

| Camada | O que Ã© | Onde vive |
|--------|---------|-----------|
| **1. Vitrine Evolutiva** | Redesign da home sobre a estrutura WordPress | home (`/`) |
| **2. Hub de QualificaÃ§Ã£o** | Planejador de LicenÃ§a, navegaÃ§Ã£o por objetivo, trilhas | pÃ¡gina interna `/qualificacao` |
| **3. Ferramenta Inteligente** | Wizard 3-4 perguntas que recomenda cursos | modal ou pÃ¡gina interna (CTA do hero) |

- **Base tÃ©cnica:** migraÃ§Ã£o para **WordPress 7.0** + reestrutura do repositÃ³rio (modelo Base de Conhecimento). `[ReuniÃ£o]`
- **Futuro (fora do escopo atual):** Ãrea do Aluno (dashboard, Moodle API, progresso). `[PRD]`
- **Fora de escopo:** alterar o Moodle (backend dos cursos) e o fluxo de autenticaÃ§Ã£o. `[PRD Â§4.3]`

## 4. Requisitos funcionais (FR)

### Camada 1 â€” Vitrine Evolutiva
| ID | Requisito | Origem |
|----|-----------|--------|
| FR-01 | Vitrine de cursos em cards (imagem, tÃ­tulo, acesso ao Moodle). | `[Vitrine atual]` |
| FR-02 | **Busca textual** com normalizaÃ§Ã£o de acentos (tÃ­tulo + categoria + tags); evoluir com autocomplete e tolerÃ¢ncia a erro. | `[Vitrine atual]` `[DeepResearch]` |
| FR-03 | **Filtros avanÃ§ados**: categoria + **carga horÃ¡ria** + **Libras**, multi-seleÃ§Ã£o, com sinalizaÃ§Ã£o de filtro ativo. | `[PRD Â§4.11]` `[DeepResearch R1]` |
| FR-04 | Selo de **Libras** nos cursos aplicÃ¡veis. | `[Vitrine atual]` |
| FR-05 | SeÃ§Ãµes "O que Ã©" e "Como Funciona" (mantidas, visual renovado). | `[PRD Â§4.7]` |
| FR-06 | **FAQ com lazy load** â€” mostra 5, "Ver todas" expande as 34. | `[PRD Â§4.8]` |
| FR-07 | Criar conta e login integrados ao Moodle. | `[Vitrine atual]` |
| FR-08 | **Barra de estatÃ­sticas** (matrÃ­culas | nÂº de cursos | 5 estrelas MEC | 100% gratuito) com **dado dinÃ¢mico**, nÃ£o hardcoded. | `[PRD Â§4.3]` |
| FR-09 | RodapÃ© com links Ãºteis + institucionais. | `[Vitrine atual]` |
| FR-10 | **Hero com proposta de valor** alinhada ao objetivo oficial (**cursos abertos Ã  comunidade**, gratuitos e certificados pelo Ifes) + **duplo CTA** (busca + Wizard) + selo MEC. **NÃ£o usar "qualificaÃ§Ã£o profissional"** (decisÃ£o 02/07 â€” contraria a ResoluÃ§Ã£o CS 72/2020). | `[ResoluÃ§Ã£o]` |
| FR-11 | **Selo 5 estrelas INEP/MEC** com destaque visual. | `[PRD Â§2.2]` |
| FR-12 | **Cards enriquecidos** â€” fechado: CH, badge "Novo" (Ãºltimos 3 meses), Libras, nÂº de inscritos; expandido: descriÃ§Ã£o, objetivos, categoria/tags, "Acessar curso", **"Compartilhar" (WhatsApp/link)**. | `[PRD Â§4.2]` |
| FR-13 | **SeÃ§Ãµes curadas** tipo Netflix: "Em destaque" (manual), "Recentes" (data), "Mais cursados" (matrÃ­culas). | `[PRD Â§4.4]` |
| FR-14 | **NavegaÃ§Ã£o por objetivo** â€” 4 cards: Inovar na sala de aula / LicenÃ§a CapacitaÃ§Ã£o / Aprender tecnologia / Crescer na carreira. | `[PRD Â§4.5/5.2]` |
| FR-15 | **Banner de LicenÃ§a CapacitaÃ§Ã£o** na home â†’ pÃ¡gina interna do Hub. | `[PRD Â§4.6]` |
| FR-16 | **Projetos parceiros** na home â€” **Rio Doce Escolar** e **UnAC** com descriÃ§Ã£o, imagem e link. | `[PRD Â§4.10]` (ver `projetos-especiais.md`) |
| FR-17 | **CorreÃ§Ãµes tÃ©cnicas** â€” `alt` corretos, cookie consent, **aviso de e-mail Hotmail/Outlook antes do cadastro**, proporÃ§Ã£o de imagens. | `[PRD Â§4.12]` |

### Camada 2 â€” Hub de QualificaÃ§Ã£o (`/qualificacao`)
| ID | Requisito | Origem |
|----|-----------|--------|
| PLC-01..09 | **Planejador de LicenÃ§a para CapacitaÃ§Ã£o** â€” formulÃ¡rio (dias/data/Ã¡rea), cÃ¡lculo de CH mÃ­nima (30h/semana), algoritmo de sugestÃ£o de cursos, resultado com links de matrÃ­cula, **exportar PDF**, orientaÃ§Ãµes Moodle, pÃ¡gina de contexto (legislaÃ§Ã£o), funcionar **sem login**, prova social. | `[PRD Â§5.1]` |
| TRL-01 | **Trilhas de aprendizagem** (percursos de 3-5 cursos): Professor Inovador (90h), Maker na EducaÃ§Ã£o (120h), EducaÃ§Ã£o Ambiental / Rio Doce (100h), Atendimento e Vendas. | `[PRD Â§5.3]` |

### Camada 3 â€” Ferramenta Inteligente (Wizard)
| ID | Requisito | Origem |
|----|-----------|--------|
| WIZ-01..06 | **Wizard de Descoberta** â€” 3-4 etapas (perfil / Ã¡rea / tempo), filtragem combinada **sem IA**, resultado em cards enriquecidos, acessÃ­vel via CTA do hero + menu, captura anÃ´nima de perfil para analytics, refazer respostas. | `[PRD Â§6]` `[DeepResearch]` |

> Tabelas completas de PLC-*, TRL e WIZ-* estÃ£o no PRD (`shared/prd-vitrine-mooc-v1.md` Â§5 e Â§6).

## 5. Requisitos nÃ£o-funcionais (NFR)

| ID | Requisito | Origem |
|----|-----------|--------|
| NFR-01 | **Responsividade mobile-first**. | `[UsuÃ¡rio]` `[PRD]` |
| NFR-02 | **Acessibilidade** (WCAG 2.2) â€” `alt` correto, teclado, contraste, foco visÃ­vel, selo Libras. | `[DeepResearch]` `[PRD]` |
| NFR-03 | **Performance** com catÃ¡logo grande â€” lazy-load/Load More + otimizaÃ§Ã£o de imagens. | `[DeepResearch R4]` |
| NFR-04 | **Analytics em GA4** (substituir o Universal/UA) + eventos do Wizard e origem do Planejador. | `[Vitrine atual]` `[PRD Â§8]` |
| NFR-05 | Stack atual e versionada (menos dependÃªncia de CDN antigo). | `[Vitrine atual]` |
| NFR-06 | CÃ³digo manutenÃ­vel em **WordPress 7** (tema/blocos/templates). | `[ReuniÃ£o]` |
| NFR-07 | **SEO** â€” ranquear "licenÃ§a capacitaÃ§Ã£o cursos gratuitos" (meta Top 3). | `[PRD Â§8]` |

## 6. RestriÃ§Ãµes (CON)

| ID | RestriÃ§Ã£o | Origem |
|----|-----------|--------|
| CON-01 | **WordPress 7.0** desde jÃ¡ (atual 5.9). | `[ReuniÃ£o]` |
| CON-02 | **Ambiente de teste dedicado** (VM CGTI); nada sobe direto em produÃ§Ã£o. | `[ReuniÃ£o]` |
| CON-03 | **Dump do banco atual** para trabalho local; a Vitrine nÃ£o pode ser travada â€” refaz-se o dump na migraÃ§Ã£o. | `[ReuniÃ£o]` |
| CON-04 | Mesmo Git; copiar estrutura da Base de Conhecimento; descartar o HTML puro antigo. | `[ReuniÃ£o]` |
| CON-05 | Branch de trabalho â†’ PR para a branch da CGTI; **nunca PR direto Ã  Master**. | `[ReuniÃ£o]` |
| CON-06 | `git push`/`gh pr` **exclusivos do @devops**. | `[ConvenÃ§Ãµes]` |
| CON-07 | **Deadline de produto: agosto/2026 (CONCEFOR)**, faseado Abrâ†’Ago (Fase 1 Planejador; Fase 2 Design System+home; Fase 3 objetivo+trilhas+projetos; Fase 4 Wizard). | `[PRD Â§7]` |
| CON-08 | **Dados de carga horÃ¡ria** â€” campo existe no WP mas **nÃ£o estÃ¡ populado**; depende da **Raquel**. Bloqueia cards, filtros por CH, trilhas e o Planejador. | `[PRD Â§7.1]` |
| CON-09 | **AprovaÃ§Ã£o da ComissÃ£o MOOC** do conceito antes da implementaÃ§Ã£o. | `[PRD Â§7.1]` |
| CON-10 | Infra da CGTI: ambiente de teste previsto por volta de **06/07/2026**. | `[ReuniÃ£o]` `[Meta]` |

## 7. DecisÃµes

| # | DecisÃ£o | SituaÃ§Ã£o |
|---|---------|----------|
| D-01 | **Arquitetura de pÃ¡ginas** | **RESOLVIDA pelo PRD:** home single-page evolutiva (estilo Netflix) + pÃ¡ginas internas (`/qualificacao`) + Wizard (modal/pÃ¡gina). |
| D-02 | Configs da CGTI (`BRANCH_PRODUCAO`, `BRANCH_TESTE`, `URL_TESTE`, `REPO_BASE_CONHECIMENTO`) | Pendente â€” `setup`/CGTI. |
| D-03 | Fonte do contador dinÃ¢mico (FR-08) | A definir (API Moodle / banco). |
| D-04 | Esquema de link do curso (slug Ã— `?id=`) | Consolidar; o Anexo B do PRD resolve vÃ¡rios por `?id=`. |

**ResoluÃ§Ã£o de conflitos (usar o dado mais atual):**
- **NÂº de cursos:** **165** (extraÃ§Ã£o ao vivo, jul/2026) â€” autoritativo. O PRD (152, abr/2026) Ã© snapshot antigo.
- **NÃºmero de topo:** usar o **contador ao vivo (~299 mil)** como matrÃ­culas/reconexÃµes; o PRD (284.595, abr) fica superado. Confirmar definiÃ§Ã£o/fonte dinÃ¢mica.
- **Carga horÃ¡ria:** permanece **pendente** (CON-08) â€” nÃ£o inventar valores.

## 8. MÃ©tricas de sucesso `[PRD Â§8]`

| MÃ©trica | Meta |
|---------|------|
| MatrÃ­culas via Planejador (origem por URL) | +15% matrÃ­culas novas |
| Uso do Wizard (analytics) | >500 usos/mÃªs |
| Tempo na pÃ¡gina (GA) | +40% |
| Taxa de conclusÃ£o (Moodle) | Aumento via trilhas |
| SEO "licenÃ§a capacitaÃ§Ã£o" (Search Console) | Top 3 |

## 9. Stakeholders e fluxo `[PRD Â§2.4]`

- **Elton** (design/UX/wireframes) â†’ **equipe de desenvolvimento** (dev WordPress/backend/Moodle) â†’ **ComissÃ£o MOOC** (aprova).
- **CGTI/Eduardo** (infra, ambiente, dump, branches). **Raquel** (dados de carga horÃ¡ria).

## 10. DependÃªncias

- **Dados de carga horÃ¡ria** (Raquel) â€” bloqueia CON-08.
- **CGTI (Eduardo):** ambiente de teste, dump, definiÃ§Ã£o de branches.
- **ComissÃ£o MOOC:** aprovaÃ§Ã£o do conceito.
- **Estrutura da Base de Conhecimento** (`REPO_BASE_CONHECIMENTO`): ainda nÃ£o fornecida â€” nÃ£o presumida.

---

## Rastreabilidade (Audit)
- **Cobertura:** as 3 camadas do PRD, os objetivos do usuÃ¡rio e os dÃ©bitos do site atual estÃ£o nas seÃ§Ãµes 3â€“6.
- **Rastreabilidade:** cada item referencia origem (`[PRD]`, `[ReuniÃ£o]`, `[Vitrine atual]`, `[UsuÃ¡rio]`, `[Meta]`, `[DeepResearch]`).
- **RestriÃ§Ãµes:** WP7, ambiente, dump, Git, deadline CONCEFOR, dados de CH e aprovaÃ§Ã£o registrados (CON-01..10).
- **Conflitos:** resolvidos pela informaÃ§Ã£o mais atual (Â§7); Build existente desconsiderado nesta fase por decisÃ£o do usuÃ¡rio.


