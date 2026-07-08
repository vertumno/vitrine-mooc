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

7. **Redesenhar cards de curso com selos laterais**
   - Manter imagem, titulo, categoria, carga horaria, nivel e CTA.
   - Usar as imagens extraidas dos cursos, pois foram validadas como bom caminho.
   - Adicionar selos pequenos para Libras, idioma, serie/projeto e outros atributos.
   - Testar a composicao dos selos na lateral direita do card, aproveitando o espaco em branco citado na conversa.
   - Incluir tooltip ou `aria-label` para selos iconicos.

8. **Revisar secoes da Home**
   - Manter "Cursos em destaque", "Mais cursados" e "Adicionados recentemente".
   - Avaliar grid de 3 versus 4 cards sem travar a entrega.
   - Garantir que as secoes nao empurrem demais o catalogo completo.
   - Reposicionar ou simplificar "Para quem e" se os cards nao levarem a filtros reais.

9. **Reavaliar navegacao por areas**
   - Para a primeira versao, pode permanecer como lista/grade simples.
   - Cada area deve levar ao catalogo filtrado.
   - Evitar dar peso visual excessivo a uma secao que a equipe percebeu como menos funcional.
   - Registrar como evolucao futura a ideia de nuvem/bolhas proporcionais ao volume da area.

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
2. Mais cursados.
3. Adicionados recentemente.
4. Para quem e, somente se apontar para filtros reais.
5. Navegar por areas.
6. Projetos parceiros.
7. Licenca capacitacao.
8. O que e / Como funciona / FAQ.

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
- selos compactos de acessibilidade/idioma/serie;
- CTA consistente;
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
- [ ] Selos de Libras/idioma/serie/projeto nao quebram o card.
- [ ] Numeros de matricula/indicadores estao sustentados ou foram removidos.
- [ ] Secao "Para quem e" leva a filtros reais ou foi simplificada.
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
| Selos | Explorar selos pequenos/laterais nos cards |
| Areas na Home | Pode ficar simples na v1; nuvem/bolhas fica para evolucao |
| Planejador | Importante, mas nao bloqueia a primeira apresentacao |

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
  **Cuidado:** testar primeiro com 2 ou 3 tipos de selo e usar tooltip para detalhe.

## 7. Proxima acao recomendada

Comecar pela Home: migrar a hero aprovada para `prototipo-cursos-abertos/index.html`, ajustar tokens do `estilos.css` e garantir que o botao principal leve para `cursos.html`. Em seguida, atacar catalogo/filtros/lazy loading, que e o bloco funcional mais importante validado na conversa.


