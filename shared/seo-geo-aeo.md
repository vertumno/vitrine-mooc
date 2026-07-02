# Guia SEO, GEO e AEO - Vitrine MOOC Ifes

> Fonte transversal para planejar, desenhar, desenvolver e validar a Vitrine MOOC com foco em encontrabilidade por mecanismos de busca e por experiencias de IA generativa.
>
> Atualizado em: 2026-07-02.

## Principio central

Para a Pesquisa Google, AEO (answer engine optimization) e GEO (generative engine optimization) nao substituem SEO. A propria documentacao do Google afirma que otimizar para busca com IA generativa e otimizar para a experiencia de pesquisa como um todo. Portanto, a estrategia da Vitrine deve tratar SEO, GEO e AEO como uma unica disciplina operacional:

1. Conteudo util, confiavel, especifico e escrito para pessoas.
2. Conteudo publico, rastreavel, indexavel e tecnicamente claro.
3. Estrutura de informacao que ajude buscadores e IAs a entenderem entidades, relacoes e contexto.
4. Dados estruturados consistentes com o que aparece visivelmente na pagina.
5. Experiencia mobile-first rapida, acessivel e completa.
6. Monitoramento continuo via Search Console, testes de pesquisa aprimorada e auditorias periodicas.

## Objetivo para a Vitrine MOOC

A Vitrine precisa ser extremamente encontravel para consultas como:

- cursos abertos Ifes
- cursos MOOC Ifes
- curso online gratuito Ifes
- curso gratuito com certificado Ifes
- formacao continuada online Ifes
- cursos gratuitos para professores
- cursos abertos a distancia do Ifes
- cursos por area, eixo, publico-alvo, carga horaria, certificacao e status

Tambem precisa responder bem a consultas conversacionais e de IA, por exemplo:

- "Quais cursos gratuitos do Ifes tem certificado?"
- "O Ifes oferece MOOC para professores?"
- "Onde encontro cursos abertos de educacao a distancia do Ifes?"
- "Quais cursos do CEFOR/Ifes estao disponiveis para inscricao?"
- "Qual curso aberto do Ifes serve para formacao de servidores?"

## Regras de ouro

1. Cada curso importante deve ter uma URL propria, publica e canonica.
2. A pagina do curso deve responder rapidamente: o que e, para quem e, o que a pessoa aprende, carga horaria, certificacao, status, inscricao e orgao ofertante.
3. A listagem deve ser mais do que uma grade visual: precisa ter texto introdutorio, filtros rastreaveis quando relevantes, links internos e dados estruturados.
4. Facetas e filtros nao podem gerar milhares de URLs indexaveis sem controle.
5. O conteudo principal nao pode depender de clique, busca interna, login, rolagem infinita sem fallback, ou JavaScript bloqueado.
6. Titles, descriptions, H1, breadcrumbs, links internos e schema devem contar a mesma historia.
7. Conteudo criado ou reestruturado com IA precisa ser revisado por responsaveis humanos e agregar valor real, nunca virar paginas em massa.

## Arquitetura recomendada de URLs

Padrao proposto:

```text
/
/cursos/
/cursos/{slug-do-curso}/
/areas/{slug-da-area}/
/publicos/{slug-do-publico}/
/certificacao/
/sobre/
/perguntas-frequentes/
```

Regras:

- Usar slugs curtos, estaveis, descritivos e em portugues.
- Evitar IDs, parametros e codigos internos em URLs publicas.
- Manter uma URL canonica por curso, mesmo que ele apareca em varias areas ou filtros.
- Redirecionar URLs antigas para as novas com 301 quando houver migracao.
- Evitar indexar combinacoes de filtros de baixo valor, como `?area=x&status=y&ordenacao=z`, salvo quando forem landing pages editoriais reais.
- Incluir breadcrumbs visiveis e `BreadcrumbList` nas paginas principais.

## Templates e requisitos de conteudo

### Home

Deve deixar claro, no primeiro bloco:

- Nome literal do produto: Vitrine MOOC Ifes ou Cursos abertos MOOC Ifes.
- Proposta: catalogo de cursos abertos, online, gratuitos ou institucionais do Ifes, conforme decisao editorial final.
- Link direto para explorar todos os cursos.
- Destaques baseados em dados reais ou criterios editoriais explicitos.

Elementos SEO/AEO:

- `title`: "Vitrine MOOC Ifes | Cursos abertos online"
- `meta description`: resumo claro do catalogo e chamada para encontrar cursos.
- H1 unico com o nome do produto.
- Bloco curto explicando o que e MOOC, quem oferece e como acessar.
- Links para areas, publicos, certificacao e perguntas frequentes.
- Schema `Organization` ou `EducationalOrganization` para Ifes/CEFOR, quando os dados forem confirmados.

### Listagem de cursos

Deve conter:

- Introducao textual antes da grade, explicando o catalogo.
- Busca por texto.
- Filtros por area, publico-alvo, status, certificacao, carga horaria e outros campos definidos na taxonomia.
- Cards com nome do curso, descricao curta, area, carga horaria, status, certificacao e chamada para detalhes.
- Paginacao com links reais ou carregamento incremental com fallback rastreavel.

Elementos SEO/AEO:

- URL canonica `/cursos/`.
- H1: "Cursos abertos MOOC do Ifes" ou equivalente.
- Dados estruturados `ItemList` com pelo menos 3 cursos quando houver lista.
- Cada item do `ItemList` deve apontar para a URL canonica do curso.
- Evitar que ordenacoes e combinacoes de filtro criem duplicacao indexavel.

### Pagina de curso

Cada curso deve ter uma pagina propria com conteudo visivel e indexavel:

- Nome oficial do curso.
- Descricao curta.
- Descricao completa, se disponivel.
- Objetivo ou resultado educacional.
- Publico-alvo.
- Area/eixo tematico.
- Carga horaria.
- Certificacao: sim/nao e condicoes, se houver.
- Status: disponivel, em producao, encerrado, futuro, conforme taxonomia.
- Modalidade: online, aberto, MOOC.
- Instituicao/provedor: Ifes/CEFOR ou unidade responsavel.
- Link de inscricao ou acesso ao ambiente do curso.
- Pre-requisitos, quando houver.
- Data de atualizacao do cadastro.

Elementos SEO/AEO:

- `title`: "{Nome do curso} | MOOC Ifes"
- `meta description`: ate cerca de 150-160 caracteres, com beneficio, publico e certificacao/status quando relevante.
- H1 igual ou muito proximo do nome oficial.
- Subtitulos em formato de perguntas quando natural: "Para quem e este curso?", "O que voce vai aprender?", "Este curso oferece certificado?"
- Schema `Course` com `name`, `description` e `provider`.
- O conteudo marcado no schema deve existir tambem no HTML visivel.
- Breadcrumb visivel e schema `BreadcrumbList`.

### Paginas de area, publico-alvo e temas

Nao devem ser apenas resultados filtrados vazios de contexto. Para serem indexaveis, precisam ter:

- Texto introdutorio unico.
- Criterio claro do agrupamento.
- Lista de cursos relevantes.
- Links para temas relacionados.
- Title e description especificos.

Exemplos:

- `/areas/educacao/`
- `/publicos/professores/`
- `/certificacao/`

Quando uma pagina for apenas uma combinacao temporaria de filtros, use canonical para a pagina principal ou `noindex`, conforme decisao tecnica.

### Perguntas frequentes

Criar uma pagina editorial com respostas reais e mantidas, sem inflar artificialmente perguntas.

Perguntas candidatas:

- O que e um curso MOOC?
- Os cursos MOOC do Ifes sao gratuitos?
- Os cursos oferecem certificado?
- Como faco inscricao?
- Preciso ser aluno do Ifes?
- Os cursos tem tutor?
- Posso fazer mais de um curso?
- Onde vejo a carga horaria?

Observacao: dados estruturados de FAQ nao devem ser assumidos como ganho garantido. Use apenas se estiverem alinhados com as politicas vigentes do Google e com conteudo visivel.

## Dados estruturados

Preferir JSON-LD no `<head>` ou em ponto unico controlado pelo tema WordPress.

### Tipos prioritarios

| Tipo | Onde usar | Objetivo |
|------|-----------|----------|
| `Organization` ou `EducationalOrganization` | Home e pagina "Sobre" | Identidade institucional, logo, URL, contatos e perfis oficiais |
| `WebSite` | Home | Nome do site e possivel acao de busca interna |
| `BreadcrumbList` | Listagens, areas e cursos | Explicar hierarquia e melhorar exibicao nos resultados |
| `ItemList` | `/cursos/`, areas e publicos | Representar listas de cursos |
| `Course` | Pagina de curso e itens da lista | Descrever cursos para mecanismos de busca |

### `Course` minimo por curso

```json
{
  "@context": "https://schema.org",
  "@type": "Course",
  "name": "Nome oficial do curso",
  "description": "Descricao curta e fiel ao conteudo visivel da pagina.",
  "provider": {
    "@type": "Organization",
    "name": "Instituto Federal do Espirito Santo",
    "sameAs": "https://www.ifes.edu.br/"
  }
}
```

### `ItemList` minimo para listagens

```json
{
  "@context": "https://schema.org",
  "@type": "ItemList",
  "itemListElement": [
    {
      "@type": "ListItem",
      "position": 1,
      "item": {
        "@type": "Course",
        "url": "https://mooc.cefor.ifes.edu.br/cursos/slug-do-curso/",
        "name": "Nome oficial do curso",
        "description": "Descricao curta.",
        "provider": {
          "@type": "Organization",
          "name": "Instituto Federal do Espirito Santo",
          "sameAs": "https://www.ifes.edu.br/"
        }
      }
    }
  ]
}
```

### Cuidados obrigatorios

- Dados estruturados nao garantem rich results.
- Nao marcar conteudo que nao esta visivel para o usuario.
- Nao usar `Course` para eventos, videos soltos, noticias ou paginas sem resultado educacional claro.
- Marcar pelo menos 3 cursos nas listas qualificadas.
- Validar com o Teste de Pesquisa Aprimorada.
- Testar URLs publicadas com a Ferramenta de Inspecao de URL do Search Console.

## Mobile-first

O Google usa a versao mobile para indexacao e classificacao. Para a Vitrine:

- Usar design responsivo com o mesmo HTML essencial no mesmo URL.
- Garantir que mobile e desktop tenham o mesmo conteudo principal.
- Nao remover descricoes, metadados, links importantes ou schema no mobile.
- Accordions e tabs podem ser usados no mobile, desde que o conteudo esteja no HTML e nao dependa de interacao para ser carregado.
- Evitar lazy loading do conteudo principal.
- Permitir rastreamento de CSS, JS, imagens e fontes necessarias.
- Manter as mesmas tags robots em desktop e mobile.
- Usar headings claros tambem no mobile.

## Rastreamento, indexacao e canonizacao

### Cobertura da disciplina

Para a Vitrine, rastreamento e indexacao nao sao apenas "ter sitemap". A camada tecnica precisa cobrir:

- Estrutura de URL rastreavel.
- Links HTML reais entre paginas importantes.
- Sitemap XML.
- Robots.txt.
- Meta robots e X-Robots-Tag.
- Canonical.
- Redirecionamentos.
- Renderizacao JavaScript.
- Mobile-first.
- Status HTTP.
- Controle de ambientes: teste bloqueado, producao indexavel.

### Estrutura de URL rastreavel

Requisitos:

- Nao usar fragmentos (`#/curso-x`) para trocar conteudo principal. Se houver navegacao dinamica, usar URLs reais e History API.
- Usar parametros no formato comum (`?area=educacao&status=disponivel`) quando parametros forem inevitaveis.
- Preferir caminhos legiveis (`/cursos/nome-do-curso/`) para paginas permanentes.
- Usar palavras no idioma do publico-alvo.
- Evitar IDs longos, hashes e parametros de sessao em URLs indexaveis.
- Garantir que cada URL importante retorne HTML util sem depender de estado interno da aplicacao.

### Links rastreaveis

Requisitos:

- Cursos, areas, publicos e paginas institucionais precisam ser acessiveis por links `<a href="...">` reais.
- Cards de curso devem ter link HTML para a pagina do curso.
- Evitar depender apenas de clique JavaScript em `div`, filtros sem URL ou busca interna para descobrir cursos.
- Textos de link devem ser descritivos: "Ver curso Alfabetizacao e Letramento", nao apenas "Clique aqui".
- Paginas importantes devem receber links internos a partir da home, listagem, areas ou paginas editoriais relacionadas.

### Sitemap

O WordPress normalmente gera sitemap, mas a Vitrine deve validar:

- Sitemap inclui home, cursos, areas, publicos e paginas institucionais importantes.
- Cursos publicados aparecem no sitemap.
- Cursos em producao so entram no sitemap se a pagina publica fizer sentido.
- `lastmod` reflete mudancas reais quando possivel.
- Sitemap e enviado no Search Console apos publicacao/migracao.

### Robots.txt

Robots.txt serve para gerenciar rastreamento, nao para esconder paginas dos resultados.

Diretrizes:

- Nao bloquear CSS, JS, imagens ou endpoints necessarios para renderizacao.
- Nao usar robots.txt para ocultar paginas sensiveis; usar senha, controle de acesso ou `noindex`, conforme o caso.
- Em ambiente de teste, bloquear indexacao com autenticacao ou `noindex`.
- Antes de ir para producao, remover `noindex` global e validar robots.

### Canonical

Usar `rel="canonical"` para:

- Curso com multiplas rotas possiveis.
- Parametros de ordenacao, busca e filtros.
- Paginas migradas ou duplicadas temporariamente.

Preferir redirecionamento 301 quando uma URL antiga nao deve mais existir.

### Redirecionamentos e status HTTP

Requisitos:

- URLs antigas relevantes devem redirecionar com 301 para a nova URL equivalente.
- Nao encadear redirects desnecessarios.
- Paginas removidas sem equivalente devem retornar 404 ou 410, com pagina de erro util.
- Paginas publicas indexaveis devem retornar 200.
- Ambiente de teste deve exigir autenticacao ou usar `noindex`, evitando que a URL de teste seja indexada.

### JavaScript e renderizacao

Diretrizes:

- O conteudo principal de cursos e listagens deve estar disponivel no HTML renderizado e acessivel ao Google.
- Nao bloquear arquivos JS/CSS necessarios no robots.txt.
- Evitar carregar conteudo principal somente apos clique, digitacao ou interacao.
- Em componentes com lazy loading, garantir fallback ou carregamento automatico observavel.
- Dados estruturados gerados via JS precisam aparecer corretamente na renderizacao testada.
- Se houver SPA ou comportamento muito dinamico, validar com Inspecao de URL e teste mobile.

### Facetas e filtros

Politica recomendada:

- Indexar paginas editoriais de alto valor: areas principais, publicos principais e certificacao.
- Nao indexar combinacoes arbitrarias de filtros.
- Permitir rastreamento apenas do que ajuda descoberta e nao cria explosao de URLs.
- Garantir que cursos importantes sejam acessiveis por links HTML a partir da home, listagem ou paginas de area.

## Classificacao e aspecto da pesquisa

A secao de "Classificacao e aspecto da pesquisa" e util para a Vitrine porque define como o Google pode exibir o site: link de titulo, snippet, nome do site, favicon, sitelinks, imagens, breadcrumbs, resultados enriquecidos e recursos de IA. O objetivo nao e "forcar" exibicoes, e sim dar sinais consistentes para que o Google entenda e apresente melhor o conteudo.

### Links de titulo

O link de titulo e o texto clicavel do resultado. Para influenciar bons links de titulo:

- Cada pagina deve ter `<title>` unico, descritivo e alinhado ao H1.
- O nome do curso deve aparecer no inicio do title em paginas de curso.
- Evitar titles genericos como "Inicio", "Curso" ou "Detalhes".
- Evitar excesso de palavras-chave repetidas.
- Evitar titles muito longos, vagos ou promocionais.
- Usar nomenclatura consistente: "MOOC Ifes", "Vitrine MOOC Ifes", "Cursos abertos MOOC do Ifes".

### Snippets e metadescricoes

Snippets podem ser gerados pelo Google a partir do conteudo da pagina, mas metadescricoes boas ajudam.

Requisitos:

- Cada pagina importante deve ter `meta description` propria.
- A description deve resumir a pagina, nao apenas repetir o title.
- Paginas de curso devem incluir tema, publico/beneficio e atributos reais, como carga horaria, certificacao ou status.
- Evitar descricoes identicas em todos os cursos.
- Evitar texto enganoso ou promessas nao confirmadas.
- O primeiro paragrafo visivel tambem deve funcionar como resposta curta e clara.

### Snippets em destaque e respostas diretas

Para aumentar chance de ser usado em respostas, inclusive por experiencias de IA:

- Responder perguntas comuns em blocos objetivos.
- Usar subtitulos naturais: "O curso oferece certificado?", "Quem pode se inscrever?", "Qual e a carga horaria?"
- Colocar a resposta direta antes de detalhes longos.
- Usar listas quando a resposta for uma sequencia de criterios, passos ou requisitos.
- Manter informacoes factuais atualizadas.

### Nome do site

O Google pode mostrar o nome do site nos resultados. Para a Vitrine:

- Definir nome preferencial consistente: "Vitrine MOOC Ifes" ou nome decidido pela equipe.
- Usar o mesmo nome na home, title, header, `og:site_name` e dados estruturados `WebSite`.
- Incluir `alternateName` quando fizer sentido, por exemplo "MOOC Ifes" e "Cursos abertos Ifes".
- Evitar nome generico como "Cursos online gratuitos" como nome principal do site.

### Sitelinks

Sitelinks sao gerados automaticamente, mas a arquitetura ajuda:

- Navegacao principal clara para Cursos, Areas, Publicos, Certificacao, Perguntas frequentes e Sobre.
- Titulos de paginas curtos e descritivos.
- Links internos consistentes.
- Evitar paginas duplicadas competindo pelo mesmo papel.
- Garantir que paginas institucionais importantes estejam indexaveis.

### Favicon

Requisitos:

- Favicon acessivel ao Googlebot.
- Imagem quadrada, legivel em tamanho pequeno e coerente com a identidade Ifes/CEFOR.
- Declarar com `<link rel="icon" href="...">`.
- Evitar trocar favicon sem necessidade perto da migracao.

### Imagens e Google Imagens

Imagens podem ajudar descoberta, acessibilidade e confianca, mas nao substituem texto.

Requisitos:

- Usar imagens relevantes ao curso, area ou instituicao.
- Nome de arquivo descritivo quando controlavel.
- Alt text informativo quando a imagem comunicar conteudo.
- Texto essencial nunca deve estar apenas dentro da imagem.
- Usar dimensoes responsivas, compressao e lazy loading seguro.
- Garantir que imagens importantes nao estejam bloqueadas por robots.txt.
- Em cards, preferir imagens que diferenciem areas ou cursos, evitando imagens genericas repetidas.

### Experiencia na pagina e Core Web Vitals

Boa experiencia nao e um unico indicador, mas um conjunto:

- Layout responsivo e estavel.
- Conteudo principal claro e facil de distinguir.
- Baixa latencia nas paginas de listagem e curso.
- Sem pop-ups ou intersticiais que atrapalhem acesso ao conteudo.
- Busca e filtros usaveis no mobile.
- Fontes, imagens e scripts otimizados.
- Sem mudancas bruscas de layout nos cards e filtros.

### Recursos de IA na Pesquisa

Para recursos de IA, a prioridade continua sendo:

- Paginas indexaveis e qualificadas a snippet.
- Conteudo publico, rastreavel e confiavel.
- Estrutura clara de entidade: curso, provedor, area, publico, certificacao.
- Dados estruturados coerentes.
- Respostas diretas para perguntas reais.
- Informacao institucional verificavel.

### O que nao e prioridade para a Vitrine

Alguns recursos da secao de aspecto da pesquisa existem, mas nao parecem centrais neste projeto agora:

- Google Discover: pode ser util para conteudo editorial/noticias, mas nao e prioridade para catalogo de cursos.
- Videos: usar se houver paginas reais com videos institucionais ou de curso; nao criar video apenas por SEO.
- Web Stories: nao recomendado como prioridade.
- E-commerce, produto e Merchant Center: nao se aplicam diretamente a cursos gratuitos/institucionais.
- Empresa local: pode ser util para dados institucionais do Ifes/CEFOR, mas nao deve ser tratado como foco principal da Vitrine.

## Conteudo util e IA generativa

IA pode ajudar a estruturar e revisar conteudo, mas nao deve gerar paginas em massa sem valor. Todo conteudo final deve passar por revisao humana.

Checklist editorial:

- O texto traz informacao original do catalogo do Ifes?
- A pagina responde claramente a intencao do usuario?
- Ha valor alem de reescrever dados basicos?
- A fonte institucional esta clara?
- O conteudo esta atualizado?
- Ha exagero promocional ou promessa nao verificavel?
- Metadados, alt text e schema foram revisados?

Para cada curso, priorizar informacao factual:

- "Curso aberto online do Ifes sobre..."
- "Indicado para..."
- "Carga horaria..."
- "Oferece certificado..."
- "Inscricoes/acesso..."

Evitar:

- Paginas diferentes para cada variacao de pergunta sem conteudo unico.
- Titulos sensacionalistas.
- Textos genericos como "o melhor curso para transformar sua carreira".
- Descricoes inventadas quando o catalogo nao tiver dado suficiente.

## Padroes de metadados

### Titles

Padroes:

```text
Vitrine MOOC Ifes | Cursos abertos online
Cursos abertos MOOC do Ifes
{Nome do curso} | MOOC Ifes
Cursos de {Area} | MOOC Ifes
Cursos para {Publico} | MOOC Ifes
```

Regras:

- Um title unico por pagina.
- Nome do curso no inicio nas paginas de curso.
- Evitar repetir palavras-chave artificialmente.
- Evitar slogans no lugar do nome real.

### Meta descriptions

Padroes:

```text
Conheca cursos abertos online do Ifes. Busque por area, publico-alvo, carga horaria, certificacao e status.
Curso aberto online do Ifes sobre {tema}. Veja publico-alvo, carga horaria, certificacao e como acessar.
```

Regras:

- Descrever a pagina com precisao.
- Incluir atributos de decisao quando reais: gratuito, online, certificado, carga horaria, publico.
- Nao prometer certificado se o campo nao estiver confirmado.

### Headings

- Um H1 por pagina.
- H2 para secoes de decisao: "Sobre o curso", "Para quem e", "O que voce vai aprender", "Certificacao", "Como acessar".
- Evitar heading usado apenas por estilo visual.

### Imagens

- Usar imagens relevantes, com dimensoes adequadas e peso otimizado.
- Alt text deve explicar a imagem quando ela comunica informacao.
- Evitar alt text recheado de palavras-chave.
- Imagens essenciais nao devem substituir texto essencial.

## Busca interna e IA

A busca interna da Vitrine deve ajudar usuarios e tambem revelar intencoes para melhoria continua.

Requisitos:

- Busca por nome, descricao, area, publico-alvo e palavras relacionadas.
- Resultados com snippets claros.
- Pagina sem resultados com sugestoes e links para areas.
- Registrar termos buscados, quando permitido pela politica institucional.
- Usar termos reais buscados para melhorar titles, descricoes e FAQs.

## Migracao da Vitrine atual

Antes da troca:

- Inventariar URLs atuais indexadas com `site:mooc.cefor.ifes.edu.br`.
- Mapear URLs antigas para novas.
- Criar plano de redirects 301.
- Preservar ou melhorar titles e descriptions relevantes.
- Garantir que o novo ambiente de producao nao carregue `noindex`.
- Enviar sitemap atualizado.
- Inspecionar amostra de URLs no Search Console.

Depois da troca:

- Monitorar cobertura/indexacao.
- Monitorar quedas de cliques, impressoes e paginas com erro.
- Validar rich results de cursos, breadcrumbs e organizacao.
- Corrigir 404s relevantes com redirects.

## QA SEO/GEO/AEO

Checklist minimo antes de PR ou entrega:

- Home, listagem e paginas de curso retornam HTTP 200.
- Ambiente de producao nao tem `noindex` indevido.
- Ambiente de teste nao e indexavel.
- Conteudo principal aparece no HTML renderizado.
- Mobile tem o mesmo conteudo essencial do desktop.
- CSS/JS/imagens necessarios nao estao bloqueados.
- Sitemap acessivel e coerente.
- Robots.txt revisado.
- Canonical correto em home, listagem, cursos e paginas de filtros.
- Titles e meta descriptions unicos nas paginas principais.
- H1 unico e coerente.
- Breadcrumb visivel e schema valido.
- Schema `Course` valido em paginas de curso.
- Schema `ItemList` valido na listagem.
- Schema `Organization` valido na home/sobre.
- Paginas de filtros de baixo valor nao indexaveis ou canonicalizadas.
- Links internos para cursos importantes existem em HTML.
- Imagens tem alt text adequado quando necessario.
- Teste de Pesquisa Aprimorada sem erros criticos.
- Search Console configurado e sitemap enviado.
- PageSpeed Insights/Core Web Vitals sem problemas graves nas paginas-chave.

## Responsabilidades por estagio

| Estagio | Responsabilidade SEO/GEO/AEO |
|---------|-------------------------------|
| 02 Catalogo | Garantir campos completos: nome, descricao, area, publico, carga horaria, certificacao, status, provedor, URL de acesso |
| 03 Design/UX | Criar templates com hierarquia semantica, conteudo de apoio, breadcrumbs, estados vazios e mobile completo |
| 04 Setup ambiente | Garantir politica de indexacao por ambiente, dominio, SSL, robots, sitemap e Search Console |
| 05 Desenvolvimento | Implementar metadados, schema, canonical, redirects, sitemap, performance e HTML rastreavel |
| 06 QA entrega | Validar indexacao, rich results, mobile-first, Search Console, redirects e monitoramento pos-migracao |

## Fontes oficiais consultadas

- Google Search Central: Otimizar seu site para recursos de IA generativa na Pesquisa Google. https://developers.google.com/search/docs/fundamentals/ai-optimization-guide?hl=pt-br
- Google Search Central: Orientacoes sobre como usar conteudo de IA generativa no seu site. https://developers.google.com/search/docs/fundamentals/using-gen-ai-content?hl=pt-br
- Google Search Central: Praticas recomendadas para sites moveis e indexacao que prioriza dispositivos moveis. https://developers.google.com/search/docs/crawling-indexing/mobile/mobile-sites-mobile-first-indexing?hl=pt-br
- Google Search Central: Rastreamento e indexacao. https://developers.google.com/search/docs/crawling-indexing?hl=pt-br
- Google Search Central: Guia de SEO para iniciantes. https://developers.google.com/search/docs/fundamentals/seo-starter-guide?hl=pt-br
- Google Search Central: Como criar conteudo util, confiavel e que prioriza as pessoas. https://developers.google.com/search/docs/fundamentals/creating-helpful-content?hl=pt-br
- Google Search Central: Dados estruturados de lista de cursos (`Course`). https://developers.google.com/search/docs/appearance/structured-data/course?hl=pt-br
- Google Search Central: Diretrizes gerais de dados estruturados. https://developers.google.com/search/docs/appearance/structured-data/sd-policies?hl=pt-br
- Google Search Central: Dados estruturados de navegacao estrutural (`BreadcrumbList`). https://developers.google.com/search/docs/appearance/structured-data/breadcrumb?hl=pt-br
- Google Search Central: Dados estruturados da organizacao (`Organization`). https://developers.google.com/search/docs/appearance/structured-data/organization?hl=pt-br
- Google Search Central: Sitemaps. https://developers.google.com/search/docs/crawling-indexing/sitemaps/overview?hl=pt-br
- Google Search Central: Introducao ao robots.txt. https://developers.google.com/search/docs/crawling-indexing/robots/intro?hl=pt-br
- Google Search Central: Estrutura de URL para a Pesquisa Google. https://developers.google.com/search/docs/crawling-indexing/url-structure?hl=pt-br
- Google Search Central: Links rastreaveis. https://developers.google.com/search/docs/crawling-indexing/links-crawlable?hl=pt-br
- Google Search Central: Canonical e consolidacao de URLs duplicados. https://developers.google.com/search/docs/crawling-indexing/consolidate-duplicate-urls?hl=pt-br
- Google Search Central: Principios basicos de SEO em JavaScript. https://developers.google.com/search/docs/crawling-indexing/javascript/javascript-seo-basics?hl=pt-br
- Google Search Central: Aspecto da Pesquisa Google. https://developers.google.com/search/docs/appearance?hl=pt-br
- Google Search Central: Links de titulo. https://developers.google.com/search/docs/appearance/title-link?hl=pt-br
- Google Search Central: Snippets e metadescricoes. https://developers.google.com/search/docs/appearance/snippet?hl=pt-br
- Google Search Central: Imagens do Google. https://developers.google.com/search/docs/appearance/google-images?hl=pt-br
- Google Search Central: Nomes de sites. https://developers.google.com/search/docs/appearance/site-names?hl=pt-br
- Google Search Central: Sitelinks. https://developers.google.com/search/docs/appearance/sitelinks?hl=pt-br
- Google Search Central: Favicon na Pesquisa. https://developers.google.com/search/docs/appearance/favicon-in-search?hl=pt-br
- Google Search Central: Experiencia na pagina. https://developers.google.com/search/docs/appearance/page-experience?hl=pt-br
