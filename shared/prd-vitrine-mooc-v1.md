# PRD — Vitrine MOOC CEFOR (v1.0)

> **Documento canônico de requisitos do produto.** Versão limpa das seções narrativas.
> **Fonte integral (com Anexos A e B):** `shared/prd-vitrine-mooc-v1-fonte.txt`
> **Produto:** mooc.cefor.ifes.edu.br · **Versão:** 1.0 · **Data:** 02/04/2026
> **Autores:** Elton Vinicius (Design) + Marquito (Desenvolvimento) — CEFOR/CGTE, Ifes
> **Deadline:** Agosto 2026 (CONCEFOR)

## 1. Visão geral

Plataforma de cursos abertos do Ifes: **284.595 matrículas**, **100+ cursos** em **20 categorias**, gratuitos e certificados (conceito **MEC 5 estrelas**, avaliação máxima INEP/MEC em EaD).

Evolução em **três camadas** entregues de forma faseada até agosto/2026 (CONCEFOR):
1. **Vitrine Evolutiva** — redesign visual e funcional sobre a estrutura WordPress existente, mantendo o que já há.
2. **Hub de Qualificação Profissional** — página interna com Planejador de Licença Capacitação, navegação por objetivo e trilhas.
3. **Ferramenta Inteligente** — Wizard de Descoberta que recomenda cursos por perfil (único entre IFs).

**Versão futura:** Área do Aluno com dashboard, integração Moodle via API, histórico e progresso.

## 2. Contexto e estado atual

### 2.1 O que Marquito já construiu (reunião 17/03/2026)
No tema WordPress customizado já estão implementados:
- Seções tipo **Netflix**: "Em destaque" (manual), "Adicionados recentemente" (por data), "Mais cursados" (por matrículas).
- **Busca por texto + filtro por categoria** combinados, com indicador de categoria ativa.
- **Lazy loading** ("carregar mais cursos").
- **Menu reorganizado**: Dúvidas frequentes, Validação de certificado, Painel de indicadores, Suporte.
- **Campo de carga horária** criado no cadastro WordPress (pendente: popular dados).
- **Título do curso fora da imagem** (aparece no hover).
- **FAQ reduzido a 5 perguntas** com botão "ver todas".

### 2.2 Conteúdo existente a manter
- **"O que é":** MOOCs 100% on-line, gratuitos, sem tutoria, abertos (sem seleção), certificados (≥60% de aproveitamento), CH máx. 60h.
- **"Como Funciona":** 4 etapas — Cadastre-se → Escolha o Curso → Faça o Curso → Emita seu Certificado (reconhecido MEC).
- **Selo de Qualidade:** 5 Estrelas INEP/MEC — deve ter destaque visual.
- **FAQ completo:** 34 perguntas (com lazy load: mostra 5, expande sob demanda).
- **Catálogo:** manter os 100+ cursos com imagens atuais; cards enriquecidos (§4.2). Lista completa no Anexo A.

### 2.3 Problemas a resolver
| Problema | Descrição | Impacto |
|----------|-----------|---------|
| Hero vago | "Reconexões com o saber" não comunica proposta de valor | Conversão baixa |
| Cards sem info | Sem carga horária, badges, descrição | Cliques desperdiçados |
| Alt texts genéricos | "Como criar Mooc" em todas as imagens | Acessibilidade + SEO |
| Licença Capacitação enterrada | Info vital na pergunta 16 do FAQ, não na navegação | Perde servidores públicos |
| Email Hotmail/Outlook | Restrição não comunicada antes do cadastro | Abandono silencioso |

### 2.4 Papéis
- **Elton:** design, identidade visual, UX, wireframes, prioridades de design.
- **Marquito:** desenvolvimento WordPress, implementação, backend, integração Moodle.
- **Fluxo:** Elton desenha → Marquito implementa → **Comissão MOOC** aprova.

## 3. Arquitetura da solução

| Camada | O que é | Onde vive |
|--------|---------|-----------|
| Vitrine Evolutiva | Redesign da home sobre WordPress existente | mooc.cefor.ifes.edu.br (home) |
| Hub Profissional | Planejador de Licença, navegação por objetivo, trilhas | `/qualificacao` (página interna) |
| Ferramenta Inteligente | Wizard 3-4 perguntas que recomenda cursos | Modal ou página interna via CTA do hero |

**Fluxo do usuário:** home com hero (proposta de valor + duplo CTA busca/wizard) → seções curadas → navegação por objetivo → se servidor, banner Licença → Planejador → plano imprimível → matrícula; ou Wizard → recomendações; FAQ/O que é/Como funciona/criar conta a qualquer momento.

## 4. Camada 1 — Vitrine Evolutiva

### 4.1 Prioridades de design
1. **Hero com proposta de valor direta** — "Qualificação profissional gratuita e certificada pelo Ifes". Duplo CTA (busca + Wizard). Selo 5 estrelas MEC visível.
2. **Cards enriquecidos** — CH visível (ex.: 20h), badge "Novo", selo Libras, nº de inscritos; ao clicar, detalhes expandidos (descrição, objetivos, estrutura).
3. **Barra de estatísticas** — 284.595 matrículas | 100+ cursos | 5 estrelas MEC | 100% gratuito (prova social acima da dobra).
4. **Seções curadas** — "Em destaque" / "Recentes" / "Mais cursados" (evolui o que Marquito fez).
5. **Navegação por objetivo** — 4 cards: Inovar na sala de aula / Licença Capacitação / Aprender tecnologia / Crescer na carreira.
6. **Banner Licença Capacitação** — CTA proeminente na home → página interna do Hub.
7. **O que é + Como funciona** — mantidas, visual renovado.
8. **FAQ com lazy load** — 5 primeiras + "Ver todas" (34 mantidas).
9. **Paleta e tipografia** — design system: **Serif** para títulos, **Sans** para corpo, **Mono** para dados numéricos.
10. **Projetos parceiros** — **Rio Doce Escolar** e **UnAC** com descrição, imagem e link, visíveis na home.
11. **Filtros avançados** — Categoria + carga horária + Libras; sinalização visual de busca ativa.
12. **Correções técnicas** — alt texts, cookie consent, warning de email pré-cadastro, proporção de imagens.

### 4.2 Card do curso
- **Fechado (grid):** imagem (existente), selo Libras, badge "Novo" (últimos 3 meses), carga horária, título, nº de inscritos.
- **Expandido (ao clicar):** descrição, objetivos de aprendizagem, categoria e tags, botão "Acessar curso" (→ Moodle), botão "Compartilhar" (WhatsApp/link).

### 4.3 O que NÃO muda
Estrutura WordPress + tema do Marquito; Moodle como backend; fluxo de cadastro/inscrição; catálogo e imagens atuais; seções Netflix (evoluem visualmente).

## 5. Camada 2 — Hub de Qualificação Profissional

Página interna (`/qualificacao`) que reposiciona os MOOCs como ferramenta de qualificação profissional.

### 5.1 Planejador de Licença para Capacitação (ferramenta principal — única no Brasil entre IFs)
**Fluxo:** servidor acessa → lê orientações (o que é, quem tem direito, legislação, como funciona no Moodle) → preenche formulário (dias de licença + data início + área) → sistema calcula CH mínima (30h/semana) → sugere combinação de cursos → gera resultado (cursos + links de matrícula + datas + CH) → imprime/exporta PDF → orientações de matrícula no Moodle.

| ID | Requisito | Prioridade |
|----|-----------|------------|
| PLC-01 | Formulário: dias de licença, data início, área de interesse | Essencial |
| PLC-02 | Cálculo automático de CH mínima (30h/semana) | Essencial |
| PLC-03 | Algoritmo de sugestão de cursos por CH + categoria | Essencial |
| PLC-04 | Resultado com curso + link de matrícula + CH + período estimado | Essencial |
| PLC-05 | Exportar/imprimir plano em PDF para processo administrativo | Essencial |
| PLC-06 | Orientações de matrícula no Moodle | Essencial |
| PLC-07 | Página de contexto: o que é licença, quem tem direito, legislação | Essencial |
| PLC-08 | Funcionar sem autenticação | Importante |
| PLC-09 | Destacar quantidade de matrículas como prova social | Importante |

**Por que é o maior gerador de matrículas:** matrículas múltiplas (3-4 por uso), SEO sem concorrente ("licença capacitação cursos gratuitos"), viralidade (WhatsApp), independente (pode ir ao ar antes do redesign).

### 5.2 Navegação por objetivo profissional
4 cards por intenção real: Inovar na sala de aula / Licença Capacitação / Aprender tecnologia / Crescer na carreira.

### 5.3 Trilhas de aprendizagem
| Trilha | Descrição | CH |
|--------|-----------|----|
| Professor Inovador | Metodologias ativas + gamificação + ferramentas digitais | 3 cursos / 90h |
| Maker na Educação | Pensamento computacional + robótica educacional | 4 cursos / 120h |
| Educação Ambiental | Cursos do Projeto Rio Doce Escolar | 5 cursos / 100h |
| Atendimento e Vendas | Fundamentos + Intermediário + Avançado | 3 cursos |

## 6. Camada 3 — Ferramenta Inteligente (Wizard)

Wizard de Descoberta: 3-4 perguntas que recomendam cursos personalizados (nenhum IF possui similar).

**Fluxo:** P1 Quem é você? (Professor/Servidor/Estudante/Profissional/Outro) → P2 O que busca? (área) → P3 Tempo disponível? (até 20h / 20-40h / 40-60h) → Resultado (cursos ordenados por relevância).

| ID | Requisito | Prioridade |
|----|-----------|------------|
| WIZ-01 | Interface passo-a-passo 3-4 etapas, navegável por clique | Essencial |
| WIZ-02 | Filtragem combinada perfil + área + CH (sem IA, lógica de filtro) | Essencial |
| WIZ-03 | Resultado com cards enriquecidos | Essencial |
| WIZ-04 | Acessível via CTA no hero + link no menu | Essencial |
| WIZ-05 | Captura anônima de perfil para analytics (sem login) | Importante |
| WIZ-06 | Refazer/ajustar respostas sem reiniciar | Desejável |

**Valor estratégico:** diferenciação (único entre IFs), dados de perfil, conversão (reduz barreira de descoberta), narrativa CONCEFOR.

## 7. Faseamento e cronograma

| Fase | Entregas | Período | Dependência |
|------|----------|---------|-------------|
| 1 | Página Licença Capacitação + Planejador (independente) | Abr–Mai 2026 | Dados de CH |
| 2 | Design System + redesign visual da home | Mai–Jun 2026 | Fase 1 |
| 3 | Navegação por objetivo + Trilhas + Projetos parceiros | Jun–Jul 2026 | Fase 2 |
| 4 | Wizard de Descoberta + lançamento CONCEFOR | Jul–Ago 2026 | Fase 3 |
| Futuro | Área do Aluno (dashboard, Moodle API, progresso) | Pós-CONCEFOR | Decisão institucional |

**Dependências críticas:** dados de carga horária (campo existe, precisa popular ~100+ cursos — **Raquel**); aprovação da **Comissão MOOC**; banda do Marquito (em paralelo com Knowledge Base); heatmap (ferramenta JS própria, qualquer fase).

## 8. Métricas de sucesso

| Métrica | Como medir | Meta |
|---------|------------|------|
| Matrículas via Planejador | Parâmetro URL | +15% matrículas novas |
| Uso do Wizard | Analytics (início/conclusão/abandono) | >500 usos/mês |
| Tempo na página | Google Analytics | +40% |
| Taxa de conclusão | Moodle analytics | Aumento via trilhas |
| SEO "licença capacitação" | Search Console | Top 3 |

## Anexos (no arquivo-fonte)

- **Anexo A — Catálogo completo (152 cursos):** nome, categoria, Libras, imagem. Ver `prd-vitrine-mooc-v1-fonte.txt`. Reconciliar com `stages/02-catalogo/output/catalogo-cursos.md` (extração ao vivo = 165 cursos em jul/2026).
- **Anexo B — URLs de imagens e cursos (152):** URL da imagem + link do curso no Moodle + Libras. Alguns links resolvidos por `?id=` (ex.: `?id=642`). Fonte útil para implementação.
