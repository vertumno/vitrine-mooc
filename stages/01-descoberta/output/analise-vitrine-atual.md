# Análise da Vitrine Atual — MOOC Ifes

> **Estágio:** 01 — Descoberta
> **Data:** 01/07/2026
> **Fonte:** `stages/01-descoberta/references/html-vitrine-atual.md` (HTML renderizado de `https://mooc.cefor.ifes.edu.br/`).

Levantamento da estrutura, recursos e débitos da Vitrine atual, classificando o que **manter**, **mudar/melhorar** e **descartar** na nova versão. Serve de base para o catálogo (estágio 02) e o design (estágio 03).

---

## 1. Visão geral técnica

| Aspecto | Estado atual |
|---------|--------------|
| Plataforma | WordPress 5.9, tema `vitrinemooctheme` |
| CSS/UI | Bootstrap 4.2.1 (CDN), Font Awesome 4.7 (CDN), `style.css` do tema |
| JS | jQuery 3.3.1, Popper 1.14.6, Bootstrap 4.2.1, `diacritic` 0.0.2 (todos via CDN) + script inline |
| Arquitetura | **Single-page**: uma única página com navegação por âncoras |
| Analytics | Google Analytics **Universal (UA-96660984-4)** + Hotjar (hjid 4968339) |
| Integração | Cursos e login apontam para o **Moodle** (`/moodle/...`) |

## 2. Mapa de seções (ordem da página)

1. **Navbar fixa** (`#topo`) — logo Ifes + "Cursos abertos"; âncoras (Nossos Cursos, Como Funciona, Dúvidas) + Criar Conta / Entrar → Moodle.
2. **Hero 1** (`#hero1`) — contador de "reconexões com o saber" (número **hardcoded** no HTML).
3. **Nossos Cursos** (`#cursos`) — título, campo de busca, lista de categorias com contadores, grid de `.card-curso` (imagem + título + "Acessar curso" → Moodle). Selo de Libras em cursos elegíveis.
4. **Como Funciona** (`#como-funciona`) — "O que é?" (definição de MOOC: gratuitos, sem tutoria, abertos, certificados com ≥60%, até 60h) + 4 cards de passos (Cadastre-se, Escolha o Curso, Faça o Curso, Emita seu Certificado).
5. **Ferramentas** (`#ferramentas`) — 4 cards (Vídeos, Fóruns, Materiais Textuais, Outras mídias).
6. **Hero 4** + **Matriculados** (`#matriculados`) — segundo contador (também hardcoded).
7. **Área do estudante** (`#area-do-estudante`) — bloco criar conta + form de login (ambos → Moodle).
8. **Perguntas Frequentes** (`#perguntas-frequentes`) — accordion Bootstrap.
9. **Rodapé** — coluna "Cursos Abertos" (Validar Certificado, Licença para Capacitação, Painel de Indicadores, Termos de Uso, Suporte), coluna "Institucional" (O Ifes, O Cefor, Base de Conhecimento) e logo Cefor.

## 3. Recursos / funcionalidades

- **Busca client-side** (`#search-box`): normaliza acentos (NFD) e filtra por título + `data-category` + `data-tag`.
- **Filtro por categoria** (`.cat-list_item` com `data-slug`): mostra/oculta cards; categoria "Todos os cursos" reseta. Contadores exibidos por categoria (ex.: Ambiente e Saúde (44), Educação (39), Tecnologias e Informática (18)…).
- **Selo de Libras** (`img-libras`) em cursos elegíveis.
- **Smooth scroll** para âncoras.
- **FAQ** em accordion.
- **Integração Moodle** para acesso a cursos, cadastro e login.

## 4. O que MANTER

| Item | Justificativa |
|------|---------------|
| Vitrine em cards de curso → Moodle | É o coração do produto e funciona. `[FR-01]` |
| Busca com normalização de acentos | UX sólida para catálogo em português. `[FR-02]` |
| Filtro por categoria com contadores | Essencial para descoberta (objetivo priorizado). `[FR-03]` |
| Selo de Libras | Acessibilidade/inclusão — diferencial a preservar. `[FR-04]` |
| Seções institucionais (Como Funciona, Ferramentas, FAQ) | Explicam o modelo MOOC e reduzem dúvidas. `[FR-05/06]` |
| Integração de cadastro/login com Moodle | Fluxo de autenticação permanece como está. `[FR-07]` |
| Estrutura do rodapé (links úteis + institucional) | Referências importantes (certificado, suporte, indicadores). `[FR-09]` |

## 5. O que MUDAR / MELHORAR

| Item | Problema atual | Direção |
|------|----------------|---------|
| **Contadores** | Números hardcoded no HTML (não refletem realidade). | Alimentar por dado real/dinâmico. `[FR-08]` `[D-03]` |
| **Analytics** | Google Analytics Universal (UA-) descontinuado desde jul/2023. | Migrar para **GA4**. `[NFR-04]` |
| **Stack de UI** | Bootstrap 4.2.1 e FA 4.7 desatualizados, via CDN externo. | Stack atual e versionada, menos dependência de CDN. `[NFR-05]` |
| **Performance** | ~165 cards (e ~230 em breve) renderizados de uma vez. | Paginação / lazy-load / otimização. `[NFR-03]` |
| **Acessibilidade** | `alt` repetido e incorreto ("Como criar Mooc" em todos os cards). | `alt` descritivo por curso + revisão WCAG. `[NFR-02]` |
| **Links dos cards** | Inconsistentes: uns por slug (`?slug`), outros por id (`?id=646`). | Padronizar o esquema de link para o Moodle. |
| **Responsividade** | Herda o layout Bootstrap 4 atual. | Redesign mobile-first (estágio 03). `[NFR-01]` |
| **Identidade visual** | Layout antigo. | Aplicar interfaces do IA/UX Studio. `[Escopo: redesign]` |

## 6. O que DESCARTAR

| Item | Motivo |
|------|--------|
| **Diretório de HTML puro** anterior no repositório | Era rascunho/erro; explicitamente descartado. `[Reunião]` |
| **Tag do Google Analytics Universal (UA-)** | Descontinuada; substituída por GA4. |
| **Versões antigas de Bootstrap/FA via CDN** | Substituídas pela nova stack. |
| Números de contador fixos no markup | Substituídos por dado dinâmico. |

> O HTML da Vitrine atual permanece **apenas como referência** em `stages/01-descoberta/references/html-vitrine-atual.md`. `[Convenções]`

## 7. Riscos técnicos

- **Migração de dados:** a Vitrine não pode ser travada; risco de divergência entre o dump usado no dev e o estado em produção no momento da migração — mitigado refazendo o dump na hora. `[CON-03]`
- **Paridade de conteúdo:** garantir que os ~165 cursos (+65) e suas categorias/tags sejam preservados na migração — validar contra o catálogo (estágio 02).
- **Dependência da CGTI:** ambiente de teste, dump e definição de branches são pré-requisitos externos. `[Dependências]`

---

## Rastreabilidade (Audit)

- **Cobertura:** todas as seções e recursos observados no HTML atual foram classificados em manter/mudar/descartar.
- **Rastreabilidade:** cada decisão referencia o HTML da Vitrine atual, a reunião de kickoff ou os requisitos (`FR-*`, `NFR-*`, `CON-*`, `D-*` de `requisitos-descoberta.md`).
- **Restrições:** débitos ligados a WP7, ambiente, dump e Git remetem às restrições correspondentes.
