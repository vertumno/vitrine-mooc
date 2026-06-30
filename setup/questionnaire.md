# Onboarding - Vitrine MOOC Ifes

<!-- Instrucoes ao agente: leia este arquivo quando o usuario digitar "setup". Faca TODAS as
     perguntas em uma unica passada conversacional. Colete as respostas, substitua os
     placeholders nos arquivos indicados e, ao final, verifique que nenhum padrao de chave
     dupla restou no workspace. Onboarding so termina com zero placeholders. -->

### Q1: Qual e a branch de PRODUCAO (Master) do repositorio da Vitrine?
- Placeholder: `{{BRANCH_PRODUCAO}}`
- Arquivos: `shared/projeto-meta.md`, `shared/convencoes-git-deploy.md`, `stages/04-setup-ambiente/CONTEXT.md`
- Tipo: texto livre
- Default: `master` (confirmar com a CGTI / Eduardo)

### Q2: Para qual branch os PRs devem ser abertos (branch de teste/destino)?
- Placeholder: `{{BRANCH_TESTE}}`
- Arquivos: `shared/projeto-meta.md`, `shared/convencoes-git-deploy.md`, `stages/04-setup-ambiente/CONTEXT.md`, `stages/04-setup-ambiente/references/wordpress-setup.md`, `stages/06-qa-entrega/CONTEXT.md`
- Tipo: texto livre
- Default: a ser indicada pela CGTI (nunca a Master)

### Q3: Qual a URL do ambiente de teste da Vitrine?
- Placeholder: `{{URL_TESTE}}`
- Arquivos: `shared/projeto-meta.md`
- Tipo: texto livre
- Default: a definir (ambiente previsto por volta de 06/07)

### Q4: Qual o repositorio modelo da Base de Conhecimento (URL ou caminho)?
- Placeholder: `{{REPO_BASE_CONHECIMENTO}}`
- Arquivos: `shared/projeto-meta.md`, `shared/convencoes-git-deploy.md`, `stages/04-setup-ambiente/CONTEXT.md`
- Tipo: texto livre

### Q5: Em qual estagio voce costuma comecar?
- Placeholder: `{{ESTAGIO_INICIAL}}`
- Arquivos: `shared/projeto-meta.md`
- Tipo: selecao
- Opcoes: 01-descoberta, 02-catalogo, 03-design-ux, 04-setup-ambiente, 05-desenvolvimento, 06-qa-entrega
- Default: 01-descoberta

### Q6: Cores da Vitrine (do AI/UX Studio). Informe os hex que tiver.
- Placeholders: `{{COR_PRIMARIA}}`, `{{COR_SECUNDARIA}}`, `{{COR_ACENTO}}`, `{{COR_TEXTO}}`, `{{COR_FUNDO}}`, `{{COR_BORDA}}`, `{{COR_SUCESSO}}`, `{{COR_ALERTA}}`, `{{COR_ERRO}}`
- Arquivos: `design-system/palette.md`
- Tipo: texto livre
- Default: usar a identidade visual oficial do Ifes (verde institucional). O que faltar fica TBD ate o design fechar no estagio 03.

### Q7: Tipografia da Vitrine (do AI/UX Studio).
- Placeholders: `{{FONTE_TITULO}}`, `{{FONTE_CORPO}}`, `{{TAMANHO_H1}}`, `{{TAMANHO_H2}}`, `{{TAMANHO_H3}}`, `{{TAMANHO_CORPO}}`, `{{TAMANHO_LEGENDA}}`
- Arquivos: `design-system/typography.md`
- Tipo: texto livre
- Default: TBD ate o design fechar no estagio 03 (preferir fontes com bom suporte a acentuacao).

---

## Depois do Onboarding

Informe ao usuario o que foi configurado (branches, ambiente, repo modelo, estagio inicial e design) e onde comecar (geralmente `stages/01-descoberta/CONTEXT.md`).

Ao final, varra o workspace por padroes `{{` restantes. Se houver, liste-os e peca a informacao que falta.
