# PRD â€” Vitrine MOOC CEFOR (v1.0)

> **Documento canÃ´nico de requisitos do produto.** VersÃ£o limpa das seÃ§Ãµes narrativas.
> **Fonte integral (com Anexos A e B):** `shared/prd-vitrine-mooc-v1-fonte.txt`
> **Produto:** mooc.cefor.ifes.edu.br Â· **VersÃ£o:** 1.0 Â· **Data:** 02/04/2026
> **Autores:** Elton Vinicius (Design) + equipe de desenvolvimento â€” CEFOR/CGTE, Ifes
> **Deadline:** Agosto 2026 (CONCEFOR)

## 1. VisÃ£o geral

Plataforma de cursos abertos do Ifes: **284.595 matrÃ­culas**, **100+ cursos** em **20 categorias**, gratuitos e certificados (conceito **MEC 5 estrelas**, avaliaÃ§Ã£o mÃ¡xima INEP/MEC em EaD).

EvoluÃ§Ã£o em **trÃªs camadas** entregues de forma faseada atÃ© agosto/2026 (CONCEFOR):
1. **Vitrine Evolutiva** â€” redesign visual e funcional sobre a estrutura WordPress existente, mantendo o que jÃ¡ hÃ¡.
2. **Hub de QualificaÃ§Ã£o Profissional** â€” pÃ¡gina interna com Planejador de LicenÃ§a CapacitaÃ§Ã£o, navegaÃ§Ã£o por objetivo e trilhas.
3. **Ferramenta Inteligente** â€” Wizard de Descoberta que recomenda cursos por perfil (Ãºnico entre IFs).

**VersÃ£o futura:** Ãrea do Aluno com dashboard, integraÃ§Ã£o Moodle via API, histÃ³rico e progresso.

## 2. Contexto e estado atual

### 2.1 O que a equipe de desenvolvimento ja construiu (reuniÃ£o 17/03/2026)
No tema WordPress customizado jÃ¡ estÃ£o implementados:
- SeÃ§Ãµes tipo **Netflix**: "Em destaque" (manual), "Adicionados recentemente" (por data), "Mais cursados" (por matrÃ­culas).
- **Busca por texto + filtro por categoria** combinados, com indicador de categoria ativa.
- **Lazy loading** ("carregar mais cursos").
- **Menu reorganizado**: DÃºvidas frequentes, ValidaÃ§Ã£o de certificado, Painel de indicadores, Suporte.
- **Campo de carga horÃ¡ria** criado no cadastro WordPress (pendente: popular dados).
- **TÃ­tulo do curso fora da imagem** (aparece no hover).
- **FAQ reduzido a 5 perguntas** com botÃ£o "ver todas".

### 2.2 ConteÃºdo existente a manter
- **"O que Ã©":** MOOCs 100% on-line, gratuitos, sem tutoria, abertos (sem seleÃ§Ã£o), certificados (â‰¥60% de aproveitamento), CH mÃ¡x. 60h.
- **"Como Funciona":** 4 etapas â€” Cadastre-se â†’ Escolha o Curso â†’ FaÃ§a o Curso â†’ Emita seu Certificado (reconhecido MEC).
- **Selo de Qualidade:** 5 Estrelas INEP/MEC â€” deve ter destaque visual.
- **FAQ completo:** 34 perguntas (com lazy load: mostra 5, expande sob demanda).
- **CatÃ¡logo:** manter os 100+ cursos com imagens atuais; cards enriquecidos (Â§4.2). Lista completa no Anexo A.

### 2.3 Problemas a resolver
| Problema | DescriÃ§Ã£o | Impacto |
|----------|-----------|---------|
| Hero vago | "ReconexÃµes com o saber" nÃ£o comunica proposta de valor | ConversÃ£o baixa |
| Cards sem info | Sem carga horÃ¡ria, badges, descriÃ§Ã£o | Cliques desperdiÃ§ados |
| Alt texts genÃ©ricos | "Como criar Mooc" em todas as imagens | Acessibilidade + SEO |
| LicenÃ§a CapacitaÃ§Ã£o enterrada | Info vital na pergunta 16 do FAQ, nÃ£o na navegaÃ§Ã£o | Perde servidores pÃºblicos |
| Email Hotmail/Outlook | RestriÃ§Ã£o nÃ£o comunicada antes do cadastro | Abandono silencioso |

### 2.4 PapÃ©is
- **Elton:** design, identidade visual, UX, wireframes, prioridades de design.
- **Equipe de desenvolvimento:** desenvolvimento WordPress, implementaÃ§Ã£o, backend, integraÃ§Ã£o Moodle.
- **Fluxo:** Elton desenha â†’ equipe de desenvolvimento implementa â†’ **ComissÃ£o MOOC** aprova.

## 3. Arquitetura da soluÃ§Ã£o

| Camada | O que Ã© | Onde vive |
|--------|---------|-----------|
| Vitrine Evolutiva | Redesign da home sobre WordPress existente | mooc.cefor.ifes.edu.br (home) |
| Hub Profissional | Planejador de LicenÃ§a, navegaÃ§Ã£o por objetivo, trilhas | `/qualificacao` (pÃ¡gina interna) |
| Ferramenta Inteligente | Wizard 3-4 perguntas que recomenda cursos | Modal ou pÃ¡gina interna via CTA do hero |

**Fluxo do usuÃ¡rio:** home com hero (proposta de valor + duplo CTA busca/wizard) â†’ seÃ§Ãµes curadas â†’ navegaÃ§Ã£o por objetivo â†’ se servidor, banner LicenÃ§a â†’ Planejador â†’ plano imprimÃ­vel â†’ matrÃ­cula; ou Wizard â†’ recomendaÃ§Ãµes; FAQ/O que Ã©/Como funciona/criar conta a qualquer momento.

## 4. Camada 1 â€” Vitrine Evolutiva

### 4.1 Prioridades de design
1. **Hero com proposta de valor direta** â€” ~~"QualificaÃ§Ã£o profissional gratuita e certificada pelo Ifes"~~ **[REMOVIDO em 02/07 â€” contraria o objetivo oficial "aberto Ã  comunidade" da ResoluÃ§Ã£o CS 72/2020. Usar proposta de valor de educaÃ§Ã£o aberta, gratuita e certificada.]** Duplo CTA (busca + Wizard). Selo 5 estrelas MEC visÃ­vel.
2. **Cards enriquecidos** â€” CH visÃ­vel (ex.: 20h), badge "Novo", selo Libras, nÂº de inscritos; ao clicar, detalhes expandidos (descriÃ§Ã£o, objetivos, estrutura).
3. **Barra de estatÃ­sticas** â€” 284.595 matrÃ­culas | 100+ cursos | 5 estrelas MEC | 100% gratuito (prova social acima da dobra).
4. **SeÃ§Ãµes curadas** â€” "Em destaque" / "Recentes" / "Mais cursados" (evolui o que a equipe fez).
5. **NavegaÃ§Ã£o por objetivo** â€” 4 cards: Inovar na sala de aula / LicenÃ§a CapacitaÃ§Ã£o / Aprender tecnologia / Crescer na carreira.
6. **Banner LicenÃ§a CapacitaÃ§Ã£o** â€” CTA proeminente na home â†’ pÃ¡gina interna do Hub.
7. **O que Ã© + Como funciona** â€” mantidas, visual renovado.
8. **FAQ com lazy load** â€” 5 primeiras + "Ver todas" (34 mantidas).
9. **Paleta e tipografia** â€” design system: **Serif** para tÃ­tulos, **Sans** para corpo, **Mono** para dados numÃ©ricos.
10. **Projetos parceiros** â€” **Rio Doce Escolar** e **UnAC** com descriÃ§Ã£o, imagem e link, visÃ­veis na home.
11. **Filtros avanÃ§ados** â€” Categoria + carga horÃ¡ria + Libras; sinalizaÃ§Ã£o visual de busca ativa.
12. **CorreÃ§Ãµes tÃ©cnicas** â€” alt texts, cookie consent, warning de email prÃ©-cadastro, proporÃ§Ã£o de imagens.

### 4.2 Card do curso
- **Fechado (grid):** imagem (existente), selo Libras, badge "Novo" (Ãºltimos 3 meses), carga horÃ¡ria, tÃ­tulo, nÂº de inscritos.
- **Expandido (ao clicar):** descriÃ§Ã£o, objetivos de aprendizagem, categoria e tags, botÃ£o "Acessar curso" (â†’ Moodle), botÃ£o "Compartilhar" (WhatsApp/link).

### 4.3 O que NÃƒO muda
Estrutura WordPress + tema customizado existente; Moodle como backend; fluxo de cadastro/inscriÃ§Ã£o; catÃ¡logo e imagens atuais; seÃ§Ãµes Netflix (evoluem visualmente).

## 5. Camada 2 â€” Hub de QualificaÃ§Ã£o Profissional

PÃ¡gina interna (`/qualificacao`) que reposiciona os MOOCs como ferramenta de qualificaÃ§Ã£o profissional.

### 5.1 Planejador de LicenÃ§a para CapacitaÃ§Ã£o (ferramenta principal â€” Ãºnica no Brasil entre IFs)
**Fluxo:** servidor acessa â†’ lÃª orientaÃ§Ãµes (o que Ã©, quem tem direito, legislaÃ§Ã£o, como funciona no Moodle) â†’ preenche formulÃ¡rio (dias de licenÃ§a + data inÃ­cio + Ã¡rea) â†’ sistema calcula CH mÃ­nima (30h/semana) â†’ sugere combinaÃ§Ã£o de cursos â†’ gera resultado (cursos + links de matrÃ­cula + datas + CH) â†’ imprime/exporta PDF â†’ orientaÃ§Ãµes de matrÃ­cula no Moodle.

| ID | Requisito | Prioridade |
|----|-----------|------------|
| PLC-01 | FormulÃ¡rio: dias de licenÃ§a, data inÃ­cio, Ã¡rea de interesse | Essencial |
| PLC-02 | CÃ¡lculo automÃ¡tico de CH mÃ­nima (30h/semana) | Essencial |
| PLC-03 | Algoritmo de sugestÃ£o de cursos por CH + categoria | Essencial |
| PLC-04 | Resultado com curso + link de matrÃ­cula + CH + perÃ­odo estimado | Essencial |
| PLC-05 | Exportar/imprimir plano em PDF para processo administrativo | Essencial |
| PLC-06 | OrientaÃ§Ãµes de matrÃ­cula no Moodle | Essencial |
| PLC-07 | PÃ¡gina de contexto: o que Ã© licenÃ§a, quem tem direito, legislaÃ§Ã£o | Essencial |
| PLC-08 | Funcionar sem autenticaÃ§Ã£o | Importante |
| PLC-09 | Destacar quantidade de matrÃ­culas como prova social | Importante |

**Por que Ã© o maior gerador de matrÃ­culas:** matrÃ­culas mÃºltiplas (3-4 por uso), SEO sem concorrente ("licenÃ§a capacitaÃ§Ã£o cursos gratuitos"), viralidade (WhatsApp), independente (pode ir ao ar antes do redesign).

### 5.2 NavegaÃ§Ã£o por objetivo profissional
4 cards por intenÃ§Ã£o real: Inovar na sala de aula / LicenÃ§a CapacitaÃ§Ã£o / Aprender tecnologia / Crescer na carreira.

### 5.3 Trilhas de aprendizagem
| Trilha | DescriÃ§Ã£o | CH |
|--------|-----------|----|
| Professor Inovador | Metodologias ativas + gamificaÃ§Ã£o + ferramentas digitais | 3 cursos / 90h |
| Maker na EducaÃ§Ã£o | Pensamento computacional + robÃ³tica educacional | 4 cursos / 120h |
| EducaÃ§Ã£o Ambiental | Cursos do Projeto Rio Doce Escolar | 5 cursos / 100h |
| Atendimento e Vendas | Fundamentos + IntermediÃ¡rio + AvanÃ§ado | 3 cursos |

## 6. Camada 3 â€” Ferramenta Inteligente (Wizard)

Wizard de Descoberta: 3-4 perguntas que recomendam cursos personalizados (nenhum IF possui similar).

**Fluxo:** P1 Quem Ã© vocÃª? (Professor/Servidor/Estudante/Profissional/Outro) â†’ P2 O que busca? (Ã¡rea) â†’ P3 Tempo disponÃ­vel? (atÃ© 20h / 20-40h / 40-60h) â†’ Resultado (cursos ordenados por relevÃ¢ncia).

| ID | Requisito | Prioridade |
|----|-----------|------------|
| WIZ-01 | Interface passo-a-passo 3-4 etapas, navegÃ¡vel por clique | Essencial |
| WIZ-02 | Filtragem combinada perfil + Ã¡rea + CH (sem IA, lÃ³gica de filtro) | Essencial |
| WIZ-03 | Resultado com cards enriquecidos | Essencial |
| WIZ-04 | AcessÃ­vel via CTA no hero + link no menu | Essencial |
| WIZ-05 | Captura anÃ´nima de perfil para analytics (sem login) | Importante |
| WIZ-06 | Refazer/ajustar respostas sem reiniciar | DesejÃ¡vel |

**Valor estratÃ©gico:** diferenciaÃ§Ã£o (Ãºnico entre IFs), dados de perfil, conversÃ£o (reduz barreira de descoberta), narrativa CONCEFOR.

## 7. Faseamento e cronograma

| Fase | Entregas | PerÃ­odo | DependÃªncia |
|------|----------|---------|-------------|
| 1 | PÃ¡gina LicenÃ§a CapacitaÃ§Ã£o + Planejador (independente) | Abrâ€“Mai 2026 | Dados de CH |
| 2 | Design System + redesign visual da home | Maiâ€“Jun 2026 | Fase 1 |
| 3 | NavegaÃ§Ã£o por objetivo + Trilhas + Projetos parceiros | Junâ€“Jul 2026 | Fase 2 |
| 4 | Wizard de Descoberta + lanÃ§amento CONCEFOR | Julâ€“Ago 2026 | Fase 3 |
| Futuro | Ãrea do Aluno (dashboard, Moodle API, progresso) | PÃ³s-CONCEFOR | DecisÃ£o institucional |

**DependÃªncias crÃ­ticas:** dados de carga horÃ¡ria (campo existe, precisa popular ~100+ cursos â€” **Raquel**); aprovaÃ§Ã£o da **ComissÃ£o MOOC**; Banda de desenvolvimento (em paralelo com Knowledge Base); heatmap (ferramenta JS prÃ³pria, qualquer fase).

## 8. MÃ©tricas de sucesso

| MÃ©trica | Como medir | Meta |
|---------|------------|------|
| MatrÃ­culas via Planejador | ParÃ¢metro URL | +15% matrÃ­culas novas |
| Uso do Wizard | Analytics (inÃ­cio/conclusÃ£o/abandono) | >500 usos/mÃªs |
| Tempo na pÃ¡gina | Google Analytics | +40% |
| Taxa de conclusÃ£o | Moodle analytics | Aumento via trilhas |
| SEO "licenÃ§a capacitaÃ§Ã£o" | Search Console | Top 3 |

## Anexos (no arquivo-fonte)

- **Anexo A â€” CatÃ¡logo completo (152 cursos):** nome, categoria, Libras, imagem. Ver `prd-vitrine-mooc-v1-fonte.txt`. Reconciliar com `stages/02-catalogo/output/catalogo-cursos.md` (extraÃ§Ã£o ao vivo = 165 cursos em jul/2026).
- **Anexo B â€” URLs de imagens e cursos (152):** URL da imagem + link do curso no Moodle + Libras. Alguns links resolvidos por `?id=` (ex.: `?id=642`). Fonte Ãºtil para implementaÃ§Ã£o.


