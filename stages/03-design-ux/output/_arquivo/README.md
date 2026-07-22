# Arquivo — protótipos antigos (estágio 03)

**Não usar como referência de trabalho.** O protótipo vigente é a família **v3** em
`stages/03-design-ux/output/canonico/` — `index-v3.html`, `cursos-v3.html`, `projeto-v3.html` e
`licenca-v3.html`. Ver `canonico/README.md`.

| Item | O que era | Por que foi arquivado |
|------|-----------|----------------------|
| `index-v3-centralizado.html` | Home v3 com o texto do hero **centralizado** | Em 22/07/2026 a versão com texto à esquerda foi eleita padrão e virou `canonico/index-v3.html` |
| `canonico-en/` | Home e catálogo em **inglês** (`index-en.html`, `cursos-en.html`) | Trabalho em inglês pausado a pedido do cliente em 20/07/2026, e já desatualizado em relação ao PT. O seletor de idioma das páginas v3 passou a marcar **EN como "em breve"**, junto de FR/ES |
| `proposta-refino/` | Protótipo alternativo completo (home + catálogo) com superfamília IBM Plex e estrutura reorganizada | Proposta de redesenho radical. A direção adotada foi o refino tipográfico sobre o canônico (v3). Dela sobreviveram o hero com máscara teal e o texto à esquerda, incorporados ao v3 |
| `proposta-home-vitrine.html` | Proposta de home aprovada como **direção visual** | O design system foi extraído dela e oficializado; o HTML usa o nome antigo ("Vitrine MOOC"), hero grande e a estatística "R$ 0" — tudo revogado |
| `prototipo-vitrine-mooc.html` | Home do primeiro protótipo navegável | Substituída |
| `prototipo-vitrine-mooc/` | Páginas internas do primeiro protótipo (cursos, curso, área, público, qualificação, sobre, FAQ) | Continuam sendo o **único** ponto de partida existente para essas páginas — nenhuma delas tem versão canônica ainda |
| `prototipo-cursos-abertos/` | Home + catálogo com a marca "Cursos Abertos do Ifes" | Substituído por `canonico/` |
| `prototipo-vitrine-hero/`, `hero-openlearning-ifes/` | Estudos isolados de hero | Direção incorporada ao canônico |

## Caminhos relativos

Os arquivos movidos em 22/07/2026 tiveram os caminhos **corrigidos** para continuarem abrindo
daqui: apontam para `../canonico/` (ou `../../canonico/`) em vez de irmãos locais. Nenhum deles
duplica CSS, dados ou imagens — todos leem do `canonico/` vigente.

> **Ressalva no `index-v3-centralizado.html`:** ele carrega o `estilos-v3.css` atual, onde as
> regras de hero à esquerda deixaram de ser condicionais. Abrir esse arquivo hoje **não** reproduz
> a versão centralizada fielmente — ele serve como registro do HTML, não do resultado visual.

## Histórico

- **07/07/2026** — primeira leva arquivada, após a consolidação do design system oficial.
- **09/07/2026** — `prototipo-cursos-abertos/` arquivado quando `canonico/` passou a ser o protótipo vivo.
- **20/07/2026** — este README corrigido: apontava `prototipo-cursos-abertos/` como vigente, mas
  aquela pasta já estava arquivada aqui dentro.
- **22/07/2026** — a família **v3** passou a ser o protótipo vivo. Arquivados: a home v3
  centralizada, as versões em inglês e a `proposta-refino/` inteira. O canônico PT
  (`canonico/index.html` e `canonico/cursos.html`) **continua no lugar** como referência de
  comparação "antes/depois", e o `canonico/estilos.css` permanece porque o v3 o usa como camada
  base.

> As páginas internas (curso, área, série, projeto, qualificação, certificação, sobre, FAQ) seguem
> sem versão canônica. Ver `../mapa-paginas.md` e `shared/backlog-pos-lancamento.md` §8.
