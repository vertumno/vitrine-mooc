# Análise do PRD vs. o que já temos — o que incorporar

> **Estágio:** 01 — Descoberta (reconciliação) · **Data:** 01/07/2026
> **PRD analisado:** `shared/prd-vitrine-mooc-v1.md` (v1.0, 02/04/2026, Elton + Marquito) · fonte: `shared/prd-vitrine-mooc-v1-fonte.txt`
> **Compara com:** artefatos dos Estágios 01–03 já produzidos.

O PRD é o **documento canônico de requisitos do produto** e é **muito mais amplo** do que a descoberta inicial capturou. Esta análise reconcilia os dois e lista o que precisa ser incorporado.

---

## 1. Impacto geral — o que muda no nosso entendimento

1. **O escopo triplicou.** Tratávamos como "migração WP7 + redesign + catálogo". O PRD define **3 camadas**, sendo **duas de módulos inteligentes inéditos**: o **Planejador de Licença Capacitação** e o **Wizard de Descoberta**. O redesign da vitrine é só a Camada 1.
2. **Marquito já construiu boa parte da Camada 1.** O PRD (reunião 17/03/2026) revela que ele já tem um tema WP customizado com seções Netflix, busca+filtro combinados, lazy loading, FAQ 5+ver todas, título no hover e campo de CH. → **A baseline de desenvolvimento não é o site antigo que analisamos.**
3. **O PRD resolve a decisão que deixamos em aberto (D-01: arquitetura de páginas).** Resposta: **home evolutiva (single-page, estilo Netflix) + páginas internas (`/qualificacao`) + Wizard (modal/página)**. Híbrido — nossa "tendência single-page" estava só parcialmente certa.
4. **A deep-research valida o PRD.** O Wizard é exatamente a resposta ao problema "usuário não sabe o que procura" (busca × navegação). Filtros facetados, cards enriquecidos e acessibilidade — tudo alinhado. Nossa pesquisa **embasa** as escolhas do PRD.
5. **Deadline real: Agosto 2026 (CONCEFOR)**, faseado Abr–Ago. Difere do "ambiente de teste ~06/07" da nossa meta (que era só infra da CGTI).

## 2. O que JÁ TEMOS que o PRD confirma (alinhamento)

| Nosso artefato | Como o PRD confirma/usa |
|----------------|-------------------------|
| `projetos-especiais.md` (Rio Doce Escolar, UnAC) | PRD §4.10 "Projetos parceiros" na home + §5.3 Rio Doce vira **Trilha** (5 cursos/100h). **Alinhamento perfeito.** |
| `catalogo-cursos.md` + `.csv` (165 cursos) | PRD Anexo A/B (152 cursos). Base do catálogo a manter e enriquecer. |
| `deep-research-...md` (R1 facetas, R3 busca, R4 Load More, R5 cards/a11y) | PRD adota tudo: filtros avançados (§4.11), cards enriquecidos (§4.2), correções de alt/acessibilidade (§4.12). |
| `analise-vitrine-atual.md` (débitos: alt errado, hero vago) | PRD §2.3 lista os **mesmos problemas** (hero vago, alt genérico, Licença enterrada). |
| `requisitos-descoberta.md` (FR busca/filtro/Libras/FAQ/Moodle) | Continuam válidos; viram base da Camada 1. |

## 3. O que precisa ser INCORPORADO (deltas do PRD)

### 3.1 Requisitos novos (não existiam na nossa descoberta)
- **Planejador de Licença Capacitação** (PLC-01 a PLC-09) — feature-carro-chefe, "única no Brasil entre IFs". Calcula CH mínima (30h/semana), sugere combinação de cursos, exporta PDF. Funciona sem login.
- **Wizard de Descoberta** (WIZ-01 a WIZ-06) — 3-4 perguntas (perfil, área, tempo) → recomendações. Sem IA, lógica de filtro.
- **Navegação por objetivo** (4 cards): Inovar na sala de aula / Licença Capacitação / Aprender tecnologia / Crescer na carreira.
- **Trilhas de aprendizagem** (4): Professor Inovador, Maker na Educação, Educação Ambiental (Rio Doce), Atendimento e Vendas.
- **Selo 5 estrelas INEP/MEC** com destaque visual (proposta de valor central).
- **Barra de estatísticas** (284.595 matrículas | 100+ cursos | 5 estrelas | 100% gratuito).
- **Card enriquecido** — visão fechada + expandida; botão **Compartilhar (WhatsApp)**.
- **Correções técnicas** — cookie consent, **warning de email Hotmail/Outlook pré-cadastro**, proporção de imagens.
- **SEO** — ranquear "licença capacitação cursos gratuitos" (Top 3).
- **Métricas de sucesso** (não tínhamos): matrículas via planejador +15%, wizard >500/mês, tempo +40%, SEO Top 3.

### 3.2 Design system (atualizar `design-system/`)
- **Tipografia definida:** Serif (títulos) + Sans (corpo) + **Mono (dados numéricos)**. → Atualizar `design-system/typography.md`.
- Hero com proposta de valor clara + duplo CTA (busca + Wizard).

### 3.3 Faseamento (adotar o cronograma do PRD)
Fase 1 (Abr–Mai): Planejador Licença (independente) · Fase 2 (Mai–Jun): Design System + redesign home · Fase 3 (Jun–Jul): Nav objetivo + Trilhas + Projetos · Fase 4 (Jul–Ago): Wizard + CONCEFOR.

### 3.4 Stakeholders novos
- **Comissão MOOC** (aprova o conceito antes da implementação).
- **Raquel** (responsável por popular os dados de carga horária).

## 4. Conflitos e discrepâncias a resolver

| # | Tema | Nosso dado | PRD | Ação |
|---|------|-----------|-----|------|
| C1 | **Baseline de análise** | `analise-vitrine-atual.md` descreve o **site antigo** (single-page, Bootstrap 4, todos os cards, FAQ com 34) | Marquito **já tem** tema novo com Netflix/lazy/busca+filtro/FAQ 5+ver todas | **Ver o build do Marquito** e refazer a baseline; marcar itens da deep-research já feitos |
| C2 | **Nº de cursos** | 165 (extração ao vivo, jul/2026) | 152 (Anexo A/B, abr/2026) | Reconciliar os ~13 cursos novos; usar nosso catálogo como atual |
| C3 | **Métrica de topo** | Site: ~299 mil "reconexões" | PRD: 284.595 "matrículas" | Alinhar definição/fonte do número (dinâmico) |
| C4 | **Carga horária** | Não temos | Campo existe, **não populado** (dep. Raquel) | Bloqueio p/ cards, filtros CH, trilhas e Planejador |
| C5 | **Deadline** | Ambiente teste ~06/07 (infra CGTI) | CONCEFOR Ago/2026 (produto) | São coisas diferentes; adotar ambos nos seus contextos |
| C6 | **Links do curso** | Slug (`?nome`) + 2 por `?id=` | Anexo B resolve vários por `?id=` (642, 793, 796…) | Consolidar esquema de link definitivo |

## 5. Impacto por artefato (o que atualizar)

| Artefato | Ação recomendada |
|----------|------------------|
| `requisitos-descoberta.md` | **Expandir** com as 3 camadas, PLC-*, WIZ-*, selo MEC, estatísticas, nav objetivo, trilhas, correções técnicas, métricas. |
| `analise-vitrine-atual.md` | Adicionar seção "Build do Marquito (17/03)" e marcar quais débitos **já foram resolvidos**. |
| `catalogo-cursos.md/.csv` | Reconciliar 165 vs 152; incorporar do Anexo B os `?id=` e (quando popular) a carga horária. |
| `projetos-especiais.md` | Já alinhado — evoluir para "Projetos parceiros" (home) + Trilha Rio Doce. |
| `deep-research-...md` | Anotar recomendações já implementadas por Marquito (R4 Load More, FAQ lazy, R3 busca+filtro). Segue válido. |
| `design-system/typography.md` | Definir Serif/Sans/Mono conforme PRD §4.9. |
| Cronograma/planejamento | Adotar o faseamento Abr–Ago do PRD (§7). |

## 6. Próximos passos sugeridos

1. **Obter o build atual do Marquito** (tema WP customizado) — é a verdadeira baseline. Sem isso, corremos risco de redesenhar o que já existe.
2. **Priorizar a Fase 1 (Planejador de Licença)** — o PRD marca como independente e maior gerador de matrículas; pode avançar sem o redesign completo.
3. **Destravar os dados de carga horária** com a Raquel (bloqueia cards, filtros, trilhas, Planejador).
4. **Atualizar `requisitos-descoberta.md`** para refletir as 3 camadas (posso fazer a seguir).
5. **Fechar o Estágio 02 (taxonomia)** já considerando: navegação por objetivo, trilhas e filtros por CH/Libras.

> **Observação (No Invention):** todos os itens acima vêm do PRD ou dos nossos artefatos. Números do PRD (284.595, 152, metas) são de abril/2026 — confirmar valores atuais com a equipe antes de fixá-los.
