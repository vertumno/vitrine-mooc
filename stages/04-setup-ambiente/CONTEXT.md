# Estagio 04: Setup de Ambiente

Preparar WordPress 7 local, a estrutura do repositorio e o dump do banco, com o fluxo Git correto.

## Inputs

| Fonte | Arquivo/Local | Escopo | Por que |
|-------|---------------|--------|---------|
| Descoberta | `../01-descoberta/output/` | Arquivos completos | Restricoes de ambiente e tecnologia |
| Convencoes | `../../shared/convencoes-git-deploy.md` | Arquivo completo | Branches, regra de PR e estrutura de repo |
| Guia | `references/wordpress-setup.md` | Arquivo completo | Passos de instalacao do WP7 local e dump |

## Process

1. Instale o WordPress 7 local seguindo `references/wordpress-setup.md`.
2. Importe o dump do banco fornecido pela CGTI para trabalhar com dados reais.
3. Copie a estrutura de pastas do repositorio da Base de Conhecimento ({{REPO_BASE_CONHECIMENTO}}).
4. Configure a branch de trabalho e confirme com a CGTI qual e a branch de teste ({{BRANCH_TESTE}}) e a de producao ({{BRANCH_PRODUCAO}}).
5. **[Checkpoint]** Confirme que o ambiente sobe, o tema carrega e o dump abre.
6. Rode os checks de Audit. Se algum falhar, corrija antes de registrar.
7. Registre o estado do ambiente em `output/`.

## Checkpoints

| Apos passo | Agente apresenta | Humano decide |
|------------|------------------|---------------|
| 4 | Ambiente local no ar + estrutura de repo + branches configuradas | Se pode seguir para desenvolvimento |

## Audit

| Check | Condicao de aprovacao |
|-------|------------------------|
| Versao | WordPress local esta na versao 7 |
| Dados | Dump importado e site abre com dados reais |
| Estrutura | Pastas seguem o modelo da Base de Conhecimento |
| Git | Branch de trabalho criada; destino de PR e {{BRANCH_TESTE}}, nao a Master |

## Outputs

| Artefato | Local | Formato |
|----------|-------|---------|
| Registro de ambiente | `output/setup-ambiente.md` | Markdown: versoes, passos, estrutura, branches |
