# Modelo de Dados da Vitrine Atual — Export WXR

> **Estágio:** 01 — Descoberta
> **Data:** 06/07/2026
> **Fontes:**
> 1. `stages/01-descoberta/references/vitrinemooc.WordPress.2026-07-06.xml` (export oficial WXR 1.2, gerado em Ferramentas > Exportar do WordPress 5.9.4 da Vitrine em produção, site base `https://mooc.cefor.ifes.edu.br/v`).
> 2. `stages/04-setup-ambiente/references/backup_vitrine_mooc.sql` (dump MySQL 8.0 completo do banco `vitrine_mooc`, gerado pela CGTI em 03/07/2026 — **não versionado no Git**: contém e-mails, hashes de senha e IPs; ver `.gitignore`).

Primeira visão do **interior** do WordPress da Vitrine (a análise anterior via só o HTML renderizado). Documenta o modelo de dados real do curso, a taxonomia vigente e os plugins em uso. Insumo direto para os estágios 04 (setup) e 05 (desenvolvimento/migração).

---

## 1. O que o export contém

| Tipo | Qtde | Observação |
|------|------|------------|
| `attachment` (mídia) | 243 | Imagens dos cards de curso (172 png, 63 jpg, 7 webp, 1 gif), uploads de 2022/05 a 2026/06 |
| `page` | 6 | `riodoce`, `unac`, `licenca-capacitacao`, `pagina-interna`, `pagina-exemplo`, `politica-de-privacidade` (draft) |
| `acf-field-group` + `acf-field` | 1 + 6 | Field group **"Curso Vitrine"** — define o modelo de dados do curso |
| `custom_css` | 1 | 15,8 mil caracteres de CSS custom do `vitrinemooctheme` (débito a absorver no tema novo) |
| `wp_global_styles` | 2 | `twentytwentytwo` e `vitrinemooctheme` |
| Categorias | 21 | Taxonomia vigente dos cursos (ver §3) |
| Tags | 452 | Sujas: duplicatas com typo, tags compostas por `;` (ver §4) |

## 2. Modelo de dados do curso (ACHADO PRINCIPAL)

A Vitrine atual **já usa um custom post type `curso`** — o field group ACF "Curso Vitrine" tem regra de localização `post_type == curso`. Campos:

| Campo (name) | Label | Tipo | Obrigatório | Observação |
|--------------|-------|------|-------------|------------|
| `imagem_curso` | Imagem | image (URL, media library) | Sim | Imagem do card |
| `link_do_curso_atual` | Link do curso - Atual | url | Sim | Ex.: `https://mooc.cefor.ifes.edu.br/moodle/enrol/index.php?id=141` |
| `link_do_curso_proximo` | Link do curso - Próxima oferta | url | Não | Mesmo padrão Moodle |
| `data_de_virada_` | Data de virada | text (`dd/mm/aaaa`) | Não | Texto livre, não date picker — fragilidade a corrigir |
| `traducao_libras` | Tradução em Libras | radio Sim/Não | Sim | Alimenta o selo de Libras |
| `em_breve` | Disponibilidade do curso | radio "Em breve" / "Curso disponível agora" | Não | Status de publicação do card |

**Implicação:** o estágio 05 não cria um modelo do zero — **evolui um CPT existente**. A migração vira upgrade de schema: manter `curso`, somar os metadados da taxonomia v4 (estágio 02) aos 6 campos atuais.

**Confirmado pelo dump (03/07/2026):** o banco tem **167 cursos (165 publish + 2 private)** — bate com o catálogo do estágio 02 — todos com os 6 campos ACF preenchidos no `wp_postmeta` e 1.092 relações curso↔termo (categorias + tags). Há ainda **2 campos legados órfãos** (`imagem_em_breve` e `escolha_de_link`, presentes em só 74 cursos antigos e sem definição ACF ativa): ignorar na migração. O CPT `curso` é registrado pelo plugin **Custom Post Type UI** (opção `cptui_post_types` no banco), **não pelo código do tema** — sem o plugin (ou sem reimplementar o registro), os cursos ficam invisíveis no admin.

## 3. Taxonomia vigente (21 categorias)

Ambiente e Saúde · Artes e Humanidades · Ciências da Natureza · Ciências Exatas e da Terra · Ciências Humanas · Ciências Sociais Aplicadas · Desenvolvimento Educacional e Social · Desenvolvimento Pessoal · Design · Educação · Educação a Distância · Engenharia · Gestão · Inclusão e Acessibilidade · Línguas · Matemática · Produção Cultural e Design · Sem categoria · Tecnologias e Informática · Tecnologias Educacionais · UnAC

Para a migração, é preciso um **mapa categoria-atual → taxonomia v4** (`stages/02-catalogo/output/taxonomia.md`). Nota: "UnAC" é usada como categoria E como página/projeto especial — confirmar tratamento em `projetos-especiais.md`.

## 4. Tags: 452, precisam de limpeza

Evidências de cadastro manual sem curadoria: `acessbilidade`/`acessibilidade`, `ABP`/`ABP.`, `código`/`código]`, `eleições`/`eleições.`, e tags compostas inteiras num único termo (ex.: "Atendimento ao Cliente; Técnicas de Vendas; Comunicação no Comércio; Ética Profissional"). A migração deve normalizar (dedupe, split por `;`, fix de typos) ou descartar tags a favor dos metadados da taxonomia v4.

## 5. Plugins e temas (confirmado pelo dump — `active_plugins`)

| Plugin | Status | Papel |
|--------|--------|-------|
| **Advanced Custom Fields** | ATIVO | Campos do curso (§2) — decidir: manter ACF no WP7 ou migrar para campos nativos/blocos |
| **Custom Post Type UI** | ATIVO | **Registra o CPT `curso`** via `cptui_post_types` no banco — dependência crítica: instalar no local antes de importar o dump |
| **Disable Comments** | ATIVO | Desativa comentários |
| **Post Types Order** | ATIVO | Ordenação manual dos cursos (campo `menu_order`) — a ordem exibida na Vitrine atual vem daqui |
| WPCode | inativo | 2 posts `wpcode` residuais no banco (snippets PHP) — sem efeito, mas auditar antes de descartar |
| Postman SMTP | inativo | 74 logs `postman_sent_mail` no banco — lixo, pode limpar |
| Category Ajax Filter (CAF) | inativo | 1 post `caf_posts` de configuração residual do filtro de categorias |

Temas no banco: `vitrinemooctheme` (ativo) + `twentytwentytwo`. Tabelas extras: `wp_ip_tracking` (IPs de visitantes — contador de acessos; **dado pessoal, LGPD**) e `wp_wpfm_backup` (WP File Manager). URL base `/v` (subdiretório) — atenção no `search-replace` da migração local. Idioma `pt_BR`, permalinks `/%postname%/`.

## 6. ~~LACUNA CRÍTICA~~ RESOLVIDA: o dump SQL trouxe os cursos

O export WXR não continha os posts do CPT `curso`. O **dump da CGTI (03/07/2026) resolveu**: os 167 cursos estão em `wp_posts` com todo o `wp_postmeta` do ACF. O XML segue útil como documentação legível do schema ACF; o dump é a fonte de dados para o ambiente local e para prototipar a migração.

**Atenção (LGPD):** o dump contém `wp_users` (9 usuários com e-mail e hash de senha), `wp_usermeta` e `wp_ip_tracking` (IPs de visitantes). Por isso está no `.gitignore` — nunca versionar nem copiar para ambientes não controlados.

## 7. Uso pelos próximos estágios

| Estágio | O que usar daqui |
|---------|------------------|
| 04 — Setup | Dump em `references/backup_vitrine_mooc.sql` pronto para importar; instalar **ACF + Custom Post Type UI + Post Types Order** antes de validar (sem CPT UI os cursos não aparecem); `search-replace` da URL `https://mooc.cefor.ifes.edu.br/v` → local |
| 05 — Desenvolvimento | §2 como schema de origem da migração (ignorar campos legados); §3 para o mapa → taxonomia v4; §4 para regras de limpeza; `menu_order` (Post Types Order) como ordenação vigente; CSS custom como débito a absorver |
| 06 — QA/Entrega | Páginas especiais (riodoce, unac, licenca-capacitacao) no checklist de migração; redirecionamentos das URLs atuais; limpar `postman_sent_mail`, `wp_ip_tracking` e resíduos WPCode/CAF na virada |
