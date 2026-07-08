# AnÃ¡lise do PRD vs. o que jÃ¡ temos â€” o que incorporar

> **EstÃ¡gio:** 01 â€” Descoberta (reconciliaÃ§Ã£o) Â· **Data:** 01/07/2026
> **PRD analisado:** `shared/prd-vitrine-mooc-v1.md` (v1.0, 02/04/2026, Elton + equipe de desenvolvimento) Â· fonte: `shared/prd-vitrine-mooc-v1-fonte.txt`
> **Compara com:** artefatos dos EstÃ¡gios 01â€“03 jÃ¡ produzidos.

O PRD Ã© o **documento canÃ´nico de requisitos do produto** e Ã© **muito mais amplo** do que a descoberta inicial capturou. Esta anÃ¡lise reconcilia os dois e lista o que precisa ser incorporado.

---

## 1. Impacto geral â€” o que muda no nosso entendimento

1. **O escopo triplicou.** TratÃ¡vamos como "migraÃ§Ã£o WP7 + redesign + catÃ¡logo". O PRD define **3 camadas**, sendo **duas de mÃ³dulos inteligentes inÃ©ditos**: o **Planejador de LicenÃ§a CapacitaÃ§Ã£o** e o **Wizard de Descoberta**. O redesign da vitrine Ã© sÃ³ a Camada 1.
2. **a equipe de desenvolvimento ja construiu boa parte da Camada 1.** O PRD (reuniÃ£o 17/03/2026) revela que ele jÃ¡ tem um tema WP customizado com seÃ§Ãµes Netflix, busca+filtro combinados, lazy loading, FAQ 5+ver todas, tÃ­tulo no hover e campo de CH. â†’ **A baseline de desenvolvimento nÃ£o Ã© o site antigo que analisamos.**
3. **O PRD resolve a decisÃ£o que deixamos em aberto (D-01: arquitetura de pÃ¡ginas).** Resposta: **home evolutiva (single-page, estilo Netflix) + pÃ¡ginas internas (`/qualificacao`) + Wizard (modal/pÃ¡gina)**. HÃ­brido â€” nossa "tendÃªncia single-page" estava sÃ³ parcialmente certa.
4. **A deep-research valida o PRD.** O Wizard Ã© exatamente a resposta ao problema "usuÃ¡rio nÃ£o sabe o que procura" (busca Ã— navegaÃ§Ã£o). Filtros facetados, cards enriquecidos e acessibilidade â€” tudo alinhado. Nossa pesquisa **embasa** as escolhas do PRD.
5. **Deadline real: Agosto 2026 (CONCEFOR)**, faseado Abrâ€“Ago. Difere do "ambiente de teste ~06/07" da nossa meta (que era sÃ³ infra da CGTI).

## 2. O que JÃ TEMOS que o PRD confirma (alinhamento)

| Nosso artefato | Como o PRD confirma/usa |
|----------------|-------------------------|
| `projetos-especiais.md` (Rio Doce Escolar, UnAC) | PRD Â§4.10 "Projetos parceiros" na home + Â§5.3 Rio Doce vira **Trilha** (5 cursos/100h). **Alinhamento perfeito.** |
| `catalogo-cursos.md` + `.csv` (165 cursos) | PRD Anexo A/B (152 cursos). Base do catÃ¡logo a manter e enriquecer. |
| `deep-research-...md` (R1 facetas, R3 busca, R4 Load More, R5 cards/a11y) | PRD adota tudo: filtros avanÃ§ados (Â§4.11), cards enriquecidos (Â§4.2), correÃ§Ãµes de alt/acessibilidade (Â§4.12). |
| `analise-vitrine-atual.md` (dÃ©bitos: alt errado, hero vago) | PRD Â§2.3 lista os **mesmos problemas** (hero vago, alt genÃ©rico, LicenÃ§a enterrada). |
| `requisitos-descoberta.md` (FR busca/filtro/Libras/FAQ/Moodle) | Continuam vÃ¡lidos; viram base da Camada 1. |

## 3. O que precisa ser INCORPORADO (deltas do PRD)

### 3.1 Requisitos novos (nÃ£o existiam na nossa descoberta)
- **Planejador de LicenÃ§a CapacitaÃ§Ã£o** (PLC-01 a PLC-09) â€” feature-carro-chefe, "Ãºnica no Brasil entre IFs". Calcula CH mÃ­nima (30h/semana), sugere combinaÃ§Ã£o de cursos, exporta PDF. Funciona sem login.
- **Wizard de Descoberta** (WIZ-01 a WIZ-06) â€” 3-4 perguntas (perfil, Ã¡rea, tempo) â†’ recomendaÃ§Ãµes. Sem IA, lÃ³gica de filtro.
- **NavegaÃ§Ã£o por objetivo** (4 cards): Inovar na sala de aula / LicenÃ§a CapacitaÃ§Ã£o / Aprender tecnologia / Crescer na carreira.
- **Trilhas de aprendizagem** (4): Professor Inovador, Maker na EducaÃ§Ã£o, EducaÃ§Ã£o Ambiental (Rio Doce), Atendimento e Vendas.
- **Selo 5 estrelas INEP/MEC** com destaque visual (proposta de valor central).
- **Barra de estatÃ­sticas** (284.595 matrÃ­culas | 100+ cursos | 5 estrelas | 100% gratuito).
- **Card enriquecido** â€” visÃ£o fechada + expandida; botÃ£o **Compartilhar (WhatsApp)**.
- **CorreÃ§Ãµes tÃ©cnicas** â€” cookie consent, **warning de email Hotmail/Outlook prÃ©-cadastro**, proporÃ§Ã£o de imagens.
- **SEO** â€” ranquear "licenÃ§a capacitaÃ§Ã£o cursos gratuitos" (Top 3).
- **MÃ©tricas de sucesso** (nÃ£o tÃ­nhamos): matrÃ­culas via planejador +15%, wizard >500/mÃªs, tempo +40%, SEO Top 3.

### 3.2 Design system (atualizar `design-system/`)
- **Tipografia definida:** Serif (tÃ­tulos) + Sans (corpo) + **Mono (dados numÃ©ricos)**. â†’ Atualizar `design-system/typography.md`.
- Hero com proposta de valor clara + duplo CTA (busca + Wizard).

### 3.3 Faseamento (adotar o cronograma do PRD)
Fase 1 (Abrâ€“Mai): Planejador LicenÃ§a (independente) Â· Fase 2 (Maiâ€“Jun): Design System + redesign home Â· Fase 3 (Junâ€“Jul): Nav objetivo + Trilhas + Projetos Â· Fase 4 (Julâ€“Ago): Wizard + CONCEFOR.

### 3.4 Stakeholders novos
- **ComissÃ£o MOOC** (aprova o conceito antes da implementaÃ§Ã£o).
- **Raquel** (responsÃ¡vel por popular os dados de carga horÃ¡ria).

## 4. Conflitos e discrepÃ¢ncias a resolver

| # | Tema | Nosso dado | PRD | AÃ§Ã£o |
|---|------|-----------|-----|------|
| C1 | **Baseline de anÃ¡lise** | `analise-vitrine-atual.md` descreve o **site antigo** (single-page, Bootstrap 4, todos os cards, FAQ com 34) | a equipe de desenvolvimento **ja tem** tema novo com Netflix/lazy/busca+filtro/FAQ 5+ver todas | **Ver o Build existente** e refazer a baseline; marcar itens da deep-research jÃ¡ feitos |
| C2 | **NÂº de cursos** | 165 (extraÃ§Ã£o ao vivo, jul/2026) | 152 (Anexo A/B, abr/2026) | Reconciliar os ~13 cursos novos; usar nosso catÃ¡logo como atual |
| C3 | **MÃ©trica de topo** | Site: ~299 mil "reconexÃµes" | PRD: 284.595 "matrÃ­culas" | Alinhar definiÃ§Ã£o/fonte do nÃºmero (dinÃ¢mico) |
| C4 | **Carga horÃ¡ria** | NÃ£o temos | Campo existe, **nÃ£o populado** (dep. Raquel) | Bloqueio p/ cards, filtros CH, trilhas e Planejador |
| C5 | **Deadline** | Ambiente teste ~06/07 (infra CGTI) | CONCEFOR Ago/2026 (produto) | SÃ£o coisas diferentes; adotar ambos nos seus contextos |
| C6 | **Links do curso** | Slug (`?nome`) + 2 por `?id=` | Anexo B resolve vÃ¡rios por `?id=` (642, 793, 796â€¦) | Consolidar esquema de link definitivo |

## 5. Impacto por artefato (o que atualizar)

| Artefato | AÃ§Ã£o recomendada |
|----------|------------------|
| `requisitos-descoberta.md` | **Expandir** com as 3 camadas, PLC-*, WIZ-*, selo MEC, estatÃ­sticas, nav objetivo, trilhas, correÃ§Ãµes tÃ©cnicas, mÃ©tricas. |
| `analise-vitrine-atual.md` | Adicionar seÃ§Ã£o "Build existente (17/03)" e marcar quais dÃ©bitos **jÃ¡ foram resolvidos**. |
| `catalogo-cursos.md/.csv` | Reconciliar 165 vs 152; incorporar do Anexo B os `?id=` e (quando popular) a carga horÃ¡ria. |
| `projetos-especiais.md` | JÃ¡ alinhado â€” evoluir para "Projetos parceiros" (home) + Trilha Rio Doce. |
| `deep-research-...md` | Anotar recomendaÃ§Ãµes jÃ¡ implementadas pela equipe (R4 Load More, FAQ lazy, R3 busca+filtro). Segue vÃ¡lido. |
| `design-system/typography.md` | Definir Serif/Sans/Mono conforme PRD Â§4.9. |
| Cronograma/planejamento | Adotar o faseamento Abrâ€“Ago do PRD (Â§7). |

## 6. PrÃ³ximos passos sugeridos

1. **Obter o build atual existente** (tema WP customizado) â€” Ã© a verdadeira baseline. Sem isso, corremos risco de redesenhar o que jÃ¡ existe.
2. **Priorizar a Fase 1 (Planejador de LicenÃ§a)** â€” o PRD marca como independente e maior gerador de matrÃ­culas; pode avanÃ§ar sem o redesign completo.
3. **Destravar os dados de carga horÃ¡ria** com a Raquel (bloqueia cards, filtros, trilhas, Planejador).
4. **Atualizar `requisitos-descoberta.md`** para refletir as 3 camadas (posso fazer a seguir).
5. **Fechar o EstÃ¡gio 02 (taxonomia)** jÃ¡ considerando: navegaÃ§Ã£o por objetivo, trilhas e filtros por CH/Libras.

> **ObservaÃ§Ã£o (No Invention):** todos os itens acima vÃªm do PRD ou dos nossos artefatos. NÃºmeros do PRD (284.595, 152, metas) sÃ£o de abril/2026 â€” confirmar valores atuais com a equipe antes de fixÃ¡-los.


