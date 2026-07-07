# Guia: WordPress 7 Local + Dump

Como subir um ambiente WordPress 7 local para desenvolver a Vitrine com dados reais. Escrito para quem nunca instalou.

## O que e

WordPress e o CMS sobre o qual a Vitrine roda. A versao alvo e a 7.0 (a Vitrine em producao roda 5.9.4). Trabalha-se local primeiro, depois no ambiente de teste da CGTI.

## Fatos do ambiente de producao (extraidos do dump e do export WXR)

| Item | Valor |
|------|-------|
| Dump | `references/backup_vitrine_mooc.sql` (CGTI, 03/07/2026) — banco `vitrine_mooc`, MySQL 8.0.35, prefixo `wp_` |
| URL de producao | `https://mooc.cefor.ifes.edu.br/v` (WordPress em subdiretorio `/v`) |
| Tema ativo | `vitrinemooctheme` |
| Plugins ativos | Advanced Custom Fields, Custom Post Type UI, Disable Comments, Post Types Order |
| Conteudo | 167 cursos (165 publicados + 2 privados), 6 paginas, 243 midias |
| Idioma / permalinks | `pt_BR` / `/%postname%/` |

Modelo de dados completo: `../../01-descoberta/output/modelo-dados-vitrine-atual.md`.

## Pre-requisitos

- Stack PHP + MySQL/MariaDB local. Opcoes comuns: Local (by Flywheel), XAMPP, Laragon ou Docker.
- PHP na versao minima exigida pelo WordPress 7 (verifique a exigencia da release e alinhe com a CGTI a versao da VM de teste, para manter paridade local = teste = producao).
- WP-CLI (recomendado — os passos abaixo usam).
- Git instalado.

## Passos

1. Instale o stack local e crie um site novo apontando para WordPress 7.0.
2. Clone o repositorio da Vitrine (mesmo Git atual) e copie a estrutura de pastas do repositorio da Base de Conhecimento ({{REPO_BASE_CONHECIMENTO}}).
3. Coloque o tema `vitrinemooctheme` em `wp-content/themes/` conforme a estrutura adotada.
4. Instale e ative os plugins que o dump exige, ANTES de validar:
   - **Custom Post Type UI** — registra o CPT `curso`; sem ele os 167 cursos ficam invisiveis no admin;
   - **Advanced Custom Fields** — campos do curso (imagem, links Moodle, Libras, disponibilidade);
   - **Post Types Order** — ordenacao manual vigente dos cursos (`menu_order`).
5. Importe o dump:
   - via linha de comando: `mysql -u USUARIO -p vitrine_mooc < references/backup_vitrine_mooc.sql`
   - ou pelo phpMyAdmin/Adminer do seu stack.
6. Troque a URL de producao pela local com search-replace (cobre dados serializados — NAO edite so `siteurl`/`home`):
   - `wp search-replace 'https://mooc.cefor.ifes.edu.br/v' 'http://SEU-DOMINIO-LOCAL' --all-tables --precise`
7. Atualize o schema do banco 5.9 -> 7.0: `wp core update-db`.
8. Ative o tema: `wp theme activate vitrinemooctheme`.
9. Percorra o admin procurando erros do salto de versao (plugin antigo pode quebrar; anote tudo no registro de ambiente).

## Como verificar

- `Painel > Atualizacoes` mostra WordPress 7 e nenhum upgrade de banco pendente.
- O admin lista **167 cursos** (165 publicados + 2 privados) no menu do CPT.
- Um curso aberto no admin mostra os campos ACF preenchidos.
- O site abre no navegador com o tema ativo e os cursos renderizados.

## Limitacoes conhecidas

- **Imagens quebradas no local:** o dump traz os registros das 243 midias, mas nao os arquivos de `wp-content/uploads/`. Peca a CGTI uma copia da pasta `uploads` (ou trabalhe com imagens quebradas ate la).
- **Dados sensiveis (LGPD):** o dump contem `wp_users` (e-mails + hashes de senha), `wp_usermeta` e `wp_ip_tracking` (IPs de visitantes). Esta no `.gitignore` — nunca versione nem copie para ambiente nao controlado.
- **Lixo residual no banco:** 74 logs `postman_sent_mail`, residuos de WPCode e Category Ajax Filter — sem efeito no site; a limpeza fica para a virada (estagio 06).

## Como o workspace usa

- O dump e uma "fotografia" de 03/07/2026. No momento da migracao, refaz-se o dump (ver `shared/convencoes-git-deploy.md`).
- A Vitrine nao pode ser travada para insercoes, entao o dump local pode ficar defasado: rebaixe quando necessario.
- Nunca faca push direto para a Master. PRs vao para {{BRANCH_TESTE}}.

## Observacao sobre o HTML antigo

O HTML puro que existia no repositorio era rascunho e foi descartado. O HTML da Vitrine atual fica apenas como referencia em `../../01-descoberta/references/html-vitrine-atual.md`.
