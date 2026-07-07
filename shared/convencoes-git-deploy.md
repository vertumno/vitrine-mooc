# Convencoes de Git e Deploy

Regras de versionamento e migracao da Vitrine MOOC. Fonte canonica, referenciada pelos estagios 04 (setup) e 06 (entrega).

## Fluxo de Branches

```
branch de trabalho (dev) ---PR---> {{BRANCH_TESTE}} ---validacao---> {{BRANCH_PRODUCAO}} (Master = producao)
```

- Trabalhe sempre em uma branch de desenvolvimento, nunca direto na Master.
- Abra PR sempre para a branch indicada pela CGTI ({{BRANCH_TESTE}}).
- NUNCA abra PR direto para a Master. Atencao: o GitHub sugere a Master por padrao, confira o destino antes de criar o PR.
- Master representa producao.

## Regra de Autoridade (AIOX)

`git push`, `gh pr create` e `gh pr merge` sao exclusivos do agente `@devops`. Os demais agentes fazem apenas operacoes locais (`git add`, `git commit`, `git branch`).

## Ambiente e Migracao

- Desenvolve-se em teste, com banco de teste. Nada sobe em producao para depois "virar".
- A Vitrine NAO pode ser travada para insercoes: trabalha-se com uma "fotografia de hoje" (dump) e refaz-se o dump no momento da migracao.
- Dumps de banco (`*.sql`) NUNCA sao versionados: contem dados pessoais (e-mails, hashes de senha, IPs — LGPD). O `.gitignore` da raiz ja bloqueia. Dump atual: `stages/04-setup-ambiente/references/backup_vitrine_mooc.sql` (CGTI, 03/07/2026).
- O diretorio de HTML puro que existia era rascunho e foi descartado. O HTML da Vitrine atual fica preservado apenas como referencia em `stages/01-descoberta/references/html-vitrine-atual.md`.

## Estrutura do Repositorio

- Mesmo Git da Vitrine atual.
- Copiar a estrutura de pastas do repositorio da Base de Conhecimento ({{REPO_BASE_CONHECIMENTO}}), modelo que ja funcionou.

## Checklist antes de abrir PR

- [ ] Branch de trabalho atualizada com a base.
- [ ] Destino do PR e {{BRANCH_TESTE}}, nao a Master.
- [ ] Build/local validado (ver `stages/06-qa-entrega/CONTEXT.md`).
- [ ] Operacao de push/PR delegada ao `@devops`.
