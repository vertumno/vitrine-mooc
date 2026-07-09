# Plano de Atualizacao - Validacao com a equipe

> **Projeto:** Vitrine MOOC Ifes / Cursos Abertos do Ifes  
> **Estagio:** 03 - Design/UX  
> **Data da conversa:** 07/07/2026  
> **Base visual aprovada:** `stages/03-design-ux/output/hero-openlearning-ifes/index.html`  
> **Prototipo alvo:** `stages/03-design-ux/output/prototipo-cursos-abertos/`  
> **Objetivo imediato:** preparar uma primeira versao apresentavel para a reuniao da comissao MOOC de 09/07/2026.

## 1. Direcao aprovada

A versao visual de referencia passa a ser a hero mais azul/teal, alinhada ao ambiente Moodle/OpenLearning, por ter sido considerada mais interessante visualmente e mais conectada com a experiencia que o usuario tera ao acessar os cursos.

O verde Ifes continua como vinculo institucional, mas deixa de dominar a primeira dobra. A nova direcao deve combinar:

- base clara em mint/branco;
- azul/teal como cor de navegacao, destaque e continuidade com o Moodle;
- dourado apenas para CTAs ou chamadas pontuais;
- vermelho/verde Ifes como acentos controlados, principalmente em marca, selos ou pequenos elementos institucionais.

## 2. Prioridade para a primeira versao

### P0 - Obrigatorio antes da apresentacao

1. **Aplicar a nova hero na Home**
   - Usar `hero-openlearning-ifes/index.html` como matriz visual.
   - Adaptar o header, titulo, texto, CTAs, imagem de fundo e faixa de indicadores ao prototipo principal.
   - Garantir que o CTA "Explorar cursos" leve claramente ao catalogo.
   - Manter "Montar plano" apenas se apontar para uma secao ou pagina minimamente coerente; caso contrario, trocar por CTA secundario mais seguro, como "Como funciona".

2. **Deixar o acesso a todos os cursos evidente**
   - Incluir "Explorar cursos" ou "Ver todos os cursos" ja na hero.
   - Manter links de "Ver todos os cursos" nas secoes de destaque, mas sem depender deles como unica entrada para o catalogo.
   - Evitar que o usuario precise rolar varias secoes para encontrar busca e filtros.

3. **Ajustar dados de indicadores para nao parecerem dinamicos**
   - Revisar numeros da hero e da secao "Mais cursados".
   - Se nao houver integracao dinamica, escrever como dado editorial: "mais de 68 mil matriculas em 2025", "65% das matriculas fora do ES", etc.
   - Indicar fonte/periodicidade no texto de apoio ou comentario de implementacao.
   - Remover qualquer metrica que nao possa ser sustentada na reuniao.

4. **Corrigir categorias e ordenacao**
   - Garantir que o catalogo use a taxonomia nova de 15 categorias.
   - Remover categorias antigas ou compostas indevidas, como "Design / Producao cultural e design", quando nao fizerem parte da taxonomia aprovada.
   - Exibir categorias em ordem alfabetica nos filtros.
   - Se houver contagem por categoria, deixar claro que o numero representa quantidade de cursos.

5. **Implementar carregamento progressivo no catalogo**
   - Trocar a renderizacao inicial de todos os 165 cursos por lote inicial + "Carregar mais" ou scroll progressivo.
   - Evitar paginacao numerada.
   - Manter fallback rastreavel para SEO quando isso for levado ao WordPress.

6. **Limpar elementos visuais sem funcao**
   - Remover ou redesenhar bolas/amarelos decorativos que nao comunicam nada.
   - Ajustar botoes amarelos para nao competirem com o resto da paleta.
   - Conferir contraste e legibilidade em mobile.

### P1 - Importante para fechar a versao 1

7. **Redesenhar cards de curso com selos no rodapé**
   - Manter imagem, titulo, categoria, carga horaria, nivel e CTA.
   - Usar as imagens extraidas dos cursos, pois foram validadas como bom caminho.
   - Consolidado: Libras fica como ribbon no canto superior direito da imagem.
   - Adicionar selos pequenos para idioma, serie/projeto e outros atributos ao lado do botao "Acessar curso".
   - Idiomas: bandeira da Gra-Bretanha para ingles e bandeira da Espanha para espanhol; portugues nao recebe selo.
   - Incluir tooltip ou `aria-label` para selos iconicos.

8. **Revisar secoes da Home**
   - Manter "Cursos em destaque", "Mais cursados" e "Adicionados recentemente".
   - Avaliar grid de 3 versus 4 cards sem travar a entrega.
   - Garantir que as secoes nao empurrem demais o catalogo completo.
   - **DECIDIDO (v1.3):** a secao "Para quem e" / "Comece pelo seu perfil" (`#publicos`) foi **removida** da Home. A escolha por publico permanece como faceta no catalogo.

9. **Reavaliar navegacao por areas**
   - **DECIDIDO (v1.3):** a secao "Navegue por area" (`#areas`) foi **removida** da Home. As areas seguem acessiveis pelo catalogo filtrado (`/cursos/`).
   - Ordem da Home apos "O que e curso MOOC?": **Projetos → Series → Servidor publico (Licenca) → Duvidas**.
   - Registrar como evolucao futura a ideia de nuvem/bolhas proporcionais ao volume da area, caso a navegacao por areas retorne a Home.

10. **Mover avisos de cadastro/e-mail para FAQ**
    - Retirar notas de Hotmail/Outlook ou e-mail nao recebido de secoes explicativas gerais.
    - Colocar essa informacao em "Perguntas frequentes".
    - Se possivel, repetir perto do fluxo real de cadastro no Moodle em fase posterior.

11. **Revisar textos "Como funciona" / "O que e MOOC"**
    - Ajustar titulo e microcopy para explicar: curso aberto, gratuidade, certificado, ritmo proprio e acesso pelo Moodle.
    - Evitar texto que pareca instrucao de cadastro fora de contexto.

### P2 - Evolucoes depois da primeira apresentacao

12. **Planejador de licenca capacitacao**
    - Criar pagina propria ou modulo dedicado.
    - Usar carga horaria dos cursos para somar uma trilha de capacitacao.
    - Nao depender disso para a apresentacao inicial.

13. **Series e projetos parceiros**
    - Manter indicacao de serie/projeto nos cards.
    - Criar hubs especificos para series e projetos quando houver tempo.
    - Considerar serie quando houver dois ou mais cursos relacionados.

14. **Nuvem visual de areas**
    - Evoluir a secao de areas para bolhas proporcionais ao volume de cursos.
    - Clique em cada bolha deve abrir catalogo filtrado.
    - Tratar como melhoria visual/futura, nao como bloqueio.

15. **Automacao de indicadores**
    - Definir se os dados do Power BI serao importados por JSON, planilha ou atualizacao manual.
    - Se for manual, definir periodicidade editorial, por exemplo semestral.
    - Evitar numeros "vivos" sem governanca.

## 3. Sequencia de execucao sugerida

### Passo 1 - Consolidar tokens visuais

Atualizar o CSS do prototipo principal para incorporar os tokens da hero aprovada:

- `--teal` como cor principal de interface;
- `--mint` como fundo claro da primeira dobra;
- `--gold` como CTA pontual;
- `--green-deep` apenas para identidade Ifes e areas institucionais;
- sombras e raios da hero, ajustando radius para nao conflitar com o design system do projeto.

**Pronto quando:** a Home e o Catalogo compartilham a mesma sensacao visual da hero aprovada, sem parecerem duas pecas separadas.

### Passo 2 - Substituir a primeira dobra da Home

Levar para `prototipo-cursos-abertos/index.html` a estrutura da hero aprovada:

- topbar/header simplificado;
- titulo "Cursos Abertos do Ifes";
- subtitulo "aprendizado no seu ritmo";
- texto curto de proposta de valor;
- CTA primario para `cursos.html`;
- CTA secundario coerente;
- imagem hero responsiva;
- faixa de indicadores com numeros sustentaveis.

**Pronto quando:** a primeira tela ja comunica o produto, tem CTA para catalogo e nao depende de rolagem para o usuario entender onde clicar.

### Passo 3 - Ajustar Home abaixo da hero

Reordenar e revisar as secoes:

1. Cursos em destaque.
2. Adicionados recentemente.
3. Mais cursados.
4. O que e / Como funciona.
5. Projetos parceiros.
6. Series.
7. Licenca capacitacao (Servidor publico).
8. Duvidas (FAQ).

> Ordem aplicada na v1.3. Removidos "Para quem e" (`#publicos`) e "Navegar por areas" (`#areas`).

**Pronto quando:** cada secao tem uma funcao clara e todas as chamadas de curso levam ao catalogo ou a um curso.

### Passo 4 - Corrigir catalogo e filtros

Atualizar `cursos.html` e `cursos-dados.js` para:

- categorias alfabeticas;
- filtros coerentes com a taxonomia atual;
- busca com tolerancia a acento;
- ordenacao por relevancia, mais cursados, recentes e A-Z;
- lote inicial de cards;
- botao "Carregar mais" ou scroll progressivo;
- estado vazio claro.

**Pronto quando:** o usuario consegue buscar, filtrar, limpar filtros, ordenar e carregar mais cursos sem paginacao numerada.

### Passo 5 - Melhorar cards e selos

Atualizar componente `.curso`:

- imagem com proporcao estavel;
- titulo legivel com limite de linhas;
- categoria e metadados sem poluicao;
- ribbon de Libras no canto da imagem;
- selos compactos de idioma/serie/projeto ao lado do CTA;
- CTA consistente com aparencia de botao;
- hover/focus acessivel.

**Pronto quando:** cards continuam escaneaveis em desktop e mobile, sem selos quebrando layout.

### Passo 6 - Revisar conteudo operacional

Mover ou ajustar textos:

- cadastro e e-mail nao recebido -> FAQ;
- "o que e MOOC" -> explicacao curta e institucional;
- certificacao -> FAQ ou pagina propria;
- licenca capacitacao -> chamada simples agora, planejador depois.

**Pronto quando:** nenhuma informacao operacional aparece fora do momento de decisao do usuario.

### Passo 7 - QA visual e responsivo

Testar:

- desktop largo;
- notebook;
- tablet;
- celular;
- contraste dos botoes;
- foco por teclado;
- textos longos em cards;
- categorias com nomes extensos;
- carregamento progressivo com filtros ativos.

**Pronto quando:** nao ha sobreposicao, texto cortado, CTA escondido ou lista pesada demais no primeiro carregamento.

## 4. Checklist de aceite

- [ ] Home usa a direcao visual da hero `hero-openlearning-ifes`.
- [ ] CTA para catalogo aparece na primeira dobra.
- [ ] Catalogo tem filtros funcionais.
- [ ] Categorias estao na taxonomia nova e em ordem alfabetica.
- [ ] Catalogo nao carrega todos os cursos de uma vez.
- [ ] Cards usam imagens reais dos cursos.
- [ ] Ribbon de Libras e selos de idioma/serie/projeto nao quebram o card.
- [ ] Numeros de matricula/indicadores estao sustentados ou foram removidos.
- [x] Secao "Para quem e" (`#publicos`) removida da Home (v1.3); publico vira faceta no catalogo.
- [x] Secao "Navegue por area" (`#areas`) removida da Home (v1.3); areas ficam no catalogo.
- [ ] Avisos de cadastro/e-mail foram movidos para FAQ.
- [ ] Mobile foi conferido.
- [ ] Acessibilidade basica foi conferida: contraste, foco, alt e aria-labels.

## 5. Decisoes registradas

| Tema | Decisao |
|------|---------|
| Direcao visual | Usar a versao azul/teal da hero como base da proxima versao |
| Nome publico | Manter "Cursos Abertos do Ifes" |
| Catalogo | Deve ter pagina propria com busca, filtros e ordenacao |
| Todos os cursos | Acesso deve aparecer cedo, idealmente na hero |
| Paginacao | Evitar paginacao numerada; preferir carregamento progressivo |
| Categorias | Usar 15 categorias do formulario/taxonomia aprovada |
| Ordem das categorias | Alfabetica, nao por quantidade |
| Indicadores | Usar como dado editorial se nao houver integracao dinamica |
| Selos | Padrao canonico: Libras no canto da imagem; demais selos ao lado do botao "Acessar curso" |
| Areas na Home | Secao "Navegue por area" removida da Home (v1.3); areas ficam no catalogo |
| Publico na Home | Secao "Comece pelo seu perfil"/"Para quem e" removida da Home (v1.3); publico vira faceta no catalogo |
| Ordem da Home | Apos "O que e curso MOOC?": Projetos → Series → Servidor publico (Licenca) → Duvidas (v1.3) |
| Planejador | Importante, mas nao bloqueia a primeira apresentacao |
| Busca na Home | Barra no hero envia direto para o catalogo pre-filtrado (`/cursos/?q=`) |
| Multilingue | Traduzir a **interface** (PT/EN prontos); titulos de curso ficam em pt-BR; FR/ES depois |

## 6. Riscos e cuidados

- **Risco:** a nova hero parecer desconectada do restante do prototipo verde.  
  **Cuidado:** atualizar tokens globais antes de mexer em secoes isoladas.

- **Risco:** numeros de matriculas serem questionados como dados em tempo real.  
  **Cuidado:** tratar como dado historico/editorial com fonte e periodo.

- **Risco:** catalogo ficar pesado em celular.  
  **Cuidado:** renderizar por lotes e carregar imagens com `loading="lazy"`.

- **Risco:** categorias antigas continuarem aparecendo em cards ou filtros.  
  **Cuidado:** revisar fonte de dados e normalizacao antes da apresentacao.

- **Risco:** selos visuais poluirem os cards.  
  **Cuidado:** manter apenas Libras sobre a imagem; demais selos ficam no rodape, ao lado do botao, com tooltip para detalhe.

## 7. Proxima acao recomendada

Comecar pela Home: migrar a hero aprovada para `prototipo-cursos-abertos/index.html`, ajustar tokens do `estilos.css` e garantir que o botao principal leve para `cursos.html`. Em seguida, atacar catalogo/filtros/lazy loading, que e o bloco funcional mais importante validado na conversa.

## 8. Registro de execucao (posterior a reuniao)

> Protótipo canonico: `stages/03-design-ux/output/canonico/`. Componentes documentados em `design-spec.md`; paginas/idiomas em `mapa-paginas.md`; visao geral em `canonico/README.md`.

### 09/07/2026 — Seletor de idioma, versoes EN e busca na Home

1. **Seletor de idioma no header** (`.lang-switch`) — dropdown acessivel (PT · EN · FR · ES) no canto superior direito, com bandeiras, `role="menu"`/`menuitemradio`, fechar por clique-fora e Esc. Aplicado em `index.html` e `cursos.html`. Spec: `design-spec.md §2.11`.
2. **Versoes em ingles** — `index-en.html` e `cursos-en.html` com a **interface** traduzida (inclui as 34 perguntas do FAQ e a microcopy dinamica do catalogo). **Titulos de curso mantidos em pt-BR** (decisao do cliente). Seletor navega PT ⇄ EN de verdade; FR/ES placeholder. Regra i18n: `design-spec.md §3.6`.
3. **Busca no hero da Home** (`.hero-search`) — `<form method="get">` que leva ao catalogo pre-filtrado (`cursos.html?q=` / `cursos-en.html?q=`). Sem dependencia de JS. Spec: `design-spec.md §2.3`.

**Arquivos tocados:** `index.html`, `cursos.html`, `index-en.html` (novo), `cursos-en.html` (novo), `estilos.css`, `README.md` (novo).

**Pendencias herdadas:** FR/ES sem pagina; troca de idioma por sufixo `-en` deve virar rota/locale no tema WordPress (estagio 05).


