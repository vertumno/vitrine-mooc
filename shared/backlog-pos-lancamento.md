# Backlog pós-lançamento — Vitrine MOOC

> Ideias levantadas pela comissão e **explicitamente adiadas** para depois do lançamento no
> CONCEFOR (agosto/2026). Origem principal: reunião de 09/07/2026
> (`shared/resumo-reuniao-2026-07-09.md`) e o PRD (`shared/prd-vitrine-mooc-v1.md`).
>
> Nada aqui bloqueia o lançamento. A ordem abaixo é por proximidade de execução, não por prioridade
> — a priorização é da comissão.

---

## 1. Destaques por consulta dinâmica ao banco

**Origem:** Saymon (09/07), com concordância do Elton.

Hoje "Em destaque", "Mais cursados" e "Adicionados recentemente" são listas fixas no HTML.
Deveriam vir de consulta ao banco, com **janela temporal configurável** (todo o período / último
ano / últimos 6 meses), combinando matrículas e número de certificações.

> "É só ajustar a consulta... e aí é legal assim, dinâmico, tá no banco direto. E não precisar de
> alguém ficando trocando ali na mão na vitrine."

**Por que importa:** além de eliminar manutenção manual, a janela temporal permite equilibrar
"cursos populares de sempre" com "descoberta de cursos novos".

**Onde entra:** estágio 05 (tema WordPress). É requisito de implementação, não de design.

**Observação técnica:** o catálogo já tem as ordenações "Mais cursados" e "Recentes" na interface,
mas os campos que as alimentam (`demanda`, `recente`) **não existem** em `cursos-dados.js` — hoje
essas ordenações não funcionam de fato. Precisam vir da mesma fonte dinâmica.

---

## 2. Sugestão de curso pela comunidade, com votação

**Origem:** Saymon (09/07), apoiado por Vanessa.

Um "não encontrou seu curso?" na interface: a pessoa indica a área de conhecimento e descreve o
curso que gostaria. As sugestões viram uma lista pública em que a comunidade vota — o "coraçãozinho".
Os mais votados orientam a priorização da produção.

- **Vanessa:** o valor está no indicador. "É diferente uma pessoa sugerir e de repente a gente
  perceber que tem 300 pessoas interessadas naquele curso."
- **Elton** sugeriu variações do voto: "quero fazer" / "já fiz e adorei".

**Complexidade:** exige moderação (conteúdo público) e provavelmente autenticação ou algum controle
antifraude na votação.

---

## 3. Portal do aluno e recomendação personalizada

**Origem:** Saymon e Elton (09/07). Elton: *"esse aqui é a etapa 2, é um projeto à parte."*

Camada autenticada na vitrine, hoje inexistente — o portal do cursista fica no Moodle. Reuniria
histórico, certificados e registro, e habilitaria recomendação por perfil ("como se fosse Netflix"):
os cursos apareceriam ordenados pelo interesse de cada pessoa, em vez de uma ordem única para todos.

**Ganho adicional apontado pelo Elton:** cruzar dado de conclusão com oferta — saber que quem
concluiu determinado MOOC é público para determinada pós do CEFOR.

**Dependência:** área autenticada. É um projeto próprio, plugável na vitrine depois.

---

## 4. Certificado agregado por série — **bloqueado**

**Origem:** Saymon (09/07).

A ideia: concluir um conjunto de cursos (ex.: HTML + CSS + JavaScript) e receber um certificado
único de carga horária maior. Estimularia a conclusão e atenderia à procura por certificados mais
substanciais.

**Impedimento legal (Vanessa):** não se pode certificar duas vezes a mesma ação. Se a pessoa já
recebeu três certificados, emitir um quarto agregando os mesmos cursos esbarra em legislação.
Precisa de análise jurídica antes de qualquer desenho técnico.

**Impedimento técnico:** o certificado é emitido por plugin do Moodle; a vitrine é outra camada.
Seria preciso um recurso de certificação próprio.

**Status:** não avançar sem parecer jurídico.

---

## 5. Wizard de descoberta ("me ajude a encontrar um curso")

**Origem:** PRD (WIZ-01..06). Elton confirmou na reunião que foi adiado deliberadamente —
optou-se por "simplificar e fazer uma versão mais visual primeiro".

Questionário curto que sugere cursos conforme o interesse declarado. Tem sobreposição clara com
a recomendação personalizada (item 3) e com o chatbot (item 6) — vale decidir se são três coisas
ou uma só antes de implementar qualquer uma.

---

## 6. Chatbot de orientação

**Origem:** Vanessa e Saymon (09/07).

A pessoa descreve o que quer aprender e o sistema sugere o caminho entre os cursos.

**Referências citadas:**
- Equipe do **LEDS**, que colocou algo assim na plataforma deles.
- **Merlin** — `https://tools.gomerlin.com.br/chat/97b57bb1-12b0-4f7e-82b0-a819a090934f` (o chat em
  uso) e `https://app.gomerlin.com.br/users/sign_in` (a página do produto). Saymon relatou que ali
  a conversa é obrigatória na entrada e monta a trilha da pessoa.

**Ressalva da Vanessa:** "já vai para o lado do chatbot, que a gente tem outros desafios
relacionados a ele também".

---

## 7. Planejador de Licença operacional

**Origem:** Saymon perguntou, Vanessa delimitou (09/07).

Hoje o planejador é **instrucional** por decisão da comissão (ver resumo da reunião, §4). A versão
operacional — inscrever nos cursos, emitir as declarações e entregar a documentação comprobatória —
depende da DGP e do fluxo de bloqueio de curso, e exige autenticação.

Saymon resumiu bem o valor da versão operacional: "ele teria ali o planejamento dele já com a
documentação comprobatória". Vanessa: possível no futuro, mas "vai demandar mais tempo do que os
meninos têm no momento para lançar a plataforma".

---

## 8. Páginas ainda sem protótipo

O `stages/03-design-ux/output/mapa-paginas.md` prevê 10 páginas. Só **Home** e **Catálogo** têm
protótipo canônico. Faltam: página do curso, área, série, projeto parceiro, `/qualificacao/`,
certificação, sobre e FAQ. Há versões antigas de algumas em
`stages/03-design-ux/output/_arquivo/prototipo-vitrine-mooc/`, úteis como ponto de partida.

---

## 9. Idiomas FR e ES

O seletor de idioma lista Français e Español como "em breve", desabilitados. Só PT e EN têm página.
A expansão depende da tradução da interface e conecta-se ao Centro Virtual de Idiomas e à parceria
com a Open University, ambos citados na reunião.

---

## 10. Versão em inglês — pendências

Trabalho em inglês pausado a pedido do cliente em 20/07/2026. Ficou faltando, em relação ao que já
foi aplicado no português:

- **`index-en.html`** — retirar o curso "Moodle para Educadores" da lista de mais cursados
  (renumerando os ranks e incluindo "Introdução à Libras" como 8º) e aplicar o novo texto do
  planejador de licença, deixando explícito que ele é instrucional.
- **`cursos-en.html`** — desabilitar FR/ES no seletor de idioma, como já está nas outras três páginas.

Enquanto isso, a home em inglês mostra um curso que sairá do ar e descreve o planejador de um jeito
que a comissão já revisou.
