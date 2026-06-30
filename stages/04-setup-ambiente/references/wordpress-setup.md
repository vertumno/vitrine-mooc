# Guia: WordPress 7 Local + Dump

Como subir um ambiente WordPress 7 local para desenvolver a Vitrine com dados reais. Escrito para quem nunca instalou.

## O que e

WordPress e o CMS sobre o qual a Vitrine roda. A versao alvo e a 7.0 (a Vitrine em producao ainda esta na 5.9). Trabalha-se local primeiro, depois no ambiente de teste da CGTI.

## Pre-requisitos

- Stack PHP + MySQL/MariaDB local. Opcoes comuns: Local (by Flywheel), XAMPP, Laragon ou Docker.
- Git instalado.
- Acesso ao dump do banco fornecido pela CGTI.

## Passos

1. Instale o stack local escolhido e crie um site novo apontando para WordPress 7.0.
2. Confirme a versao do PHP compativel com o WordPress 7 (verifique a exigencia da release antes).
3. Clone o repositorio da Vitrine (mesmo Git atual) e copie a estrutura de pastas do repositorio da Base de Conhecimento.
4. Coloque o tema da Vitrine em `wp-content/themes/` conforme a estrutura adotada.
5. Importe o dump do banco da CGTI:
   - via linha de comando: `mysql -u USUARIO -p NOME_DO_BANCO < caminho/para/dump.sql`
   - ou pelo phpMyAdmin/Adminer do seu stack.
6. Ajuste `wp-config.php` (credenciais do banco local) e a URL do site (`siteurl`/`home`) para o dominio local.
7. Ative o tema da Vitrine no painel do WordPress.

## Como verificar

- O site local abre no navegador com os dados do dump (cursos aparecem).
- A versao em `Painel > Atualizacoes` ou no rodape do admin mostra WordPress 7.
- O tema da Vitrine esta ativo.

## Como o workspace usa

- O dump e uma "fotografia de hoje". No momento da migracao, refaz-se o dump (ver `shared/convencoes-git-deploy.md`).
- A Vitrine nao pode ser travada para insercoes, entao o dump local pode ficar defasado: rebaixe quando necessario.
- Nunca faca push direto para a Master. PRs vao para {{BRANCH_TESTE}}.

## Observacao sobre o HTML antigo

O HTML puro que existia no repositorio era rascunho e foi descartado. O HTML da Vitrine atual fica apenas como referencia em `../01-descoberta/references/html-vitrine-atual.md`.
