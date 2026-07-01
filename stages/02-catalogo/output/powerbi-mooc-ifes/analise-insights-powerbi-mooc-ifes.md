# Análise do Painel de Indicadores MOOC Ifes

Fonte: extração do Power BI público em 2026-07-01. Dataset com último refresh em 2026-06-29T11:15:54.177.

Observação metodológica: a análise usa a aba `Indicadores por curso` e abas auxiliares extraídas para CSV/XLSX. Foram excluídas dos cálculos 7 linhas incompletas/anômalas da resposta compactada do Power BI; a base quantitativa principal ficou com 164 cursos válidos.

## Sumário executivo

- A operação é altamente concentrada: 50 cursos geram 74,0% das matrículas e 75,2% dos certificados.
- A taxa média global de certificação é 33,3%, mas a mediana por curso é 32,2%. O primeiro quartil fica em 24,7%; cursos abaixo disso merecem intervenção.
- O maior curso, `Inglês Comunicativo – Aprenda o Básico Essencial`, concentra 7,5% das matrículas, mas só 2,8% dos certificados, com conversão de 12,5%.
- Se apenas os cursos de alta demanda e baixa conversão alcançassem a mediana de certificação, haveria potencial estimado de +7.281 certificados.
- O Campus Vila Velha tem baixa escala relativa, mas excelente conversão: 42,6%, a maior entre unidades com mais de 1.000 matrículas.
- O CEFOR responde por 60,4% das matrículas e 36,1% de conversão: é o motor de escala e também o principal ponto de alavancagem.
- A expansão nacional é real: 65,1% das matrículas por UF estão fora do Espírito Santo.
- A presença internacional ainda é pequena: 0,5% das matrículas por país estão fora do Brasil.
- 2025 foi o maior ano fechado em matrículas: 68.720. Em 2026 há 30.675 matrículas até a extração, portanto não deve ser comparado como ano fechado.

## Decisões sugeridas

1. Priorizar melhoria de conclusão nos cursos com alta demanda e baixa conversão.
   - Esses cursos já têm tração; mexer neles tende a gerar mais certificados do que lançar novos cursos.
   - O caso mais relevante é `Inglês Comunicativo – Aprenda o Básico Essencial`: levar sua conversão de 12,5% para a mediana de 32,2% geraria cerca de +4.417 certificados.

2. Criar uma rotina de “otimização de curso campeão”.
   - Cursos com grande matrícula e baixa conversão devem receber revisão de carga, atividades, comunicação inicial, critérios de certificação e pontos de abandono.
   - A meta não precisa ser agressiva: aproximar os piores cursos da mediana já gera impacto grande.

3. Usar o Campus Vila Velha como laboratório de boas práticas.
   - A unidade tem 34 cursos, 12.775 matrículas e 42,6% de conversão.
   - Vários cursos ambientais e de saúde ambiental aparecem com conversão elevada mesmo sem grande escala.
   - A pergunta estratégica: o que há no desenho desses cursos que aumenta conclusão?

4. Separar estratégia de catálogo em dois portfólios.
   - Portfólio de escala: cursos com grande demanda, mesmo que conversão média. Objetivo: alcance.
   - Portfólio de eficiência: cursos com alta conversão, mesmo que pequena demanda. Objetivo: formação efetiva e reputação.

5. Reforçar distribuição fora do Espírito Santo.
   - O Espírito Santo soma 34,9% das matrículas por UF; São Paulo, Rio de Janeiro, Minas Gerais e Bahia já formam um bloco nacional relevante.
   - A Vitrine deve comunicar melhor busca, filtros e temas de interesse nacional, não apenas institucional/local.

6. Tratar internacionalização como oportunidade específica, não como resultado espontâneo.
   - O Brasil concentra 99,5% das matrículas por país.
   - Moçambique e Portugal aparecem no topo internacional, sugerindo potencial lusófono.
   - Se internacionalização for meta, recomenda-se curadoria de cursos com linguagem mais universal, páginas com SEO em português internacional e sinalização para público externo.

## Cursos que merecem intervenção imediata

Cursos com alta demanda e conversão abaixo do primeiro quartil:

| Curso | Unidade | Matrículas | Conversão | Potencial até mediana |
|---|---:|---:|---:|---:|
| Inglês Comunicativo – Aprenda o Básico Essencial | Campus Linhares | 22.384 | 12,5% | +4.417 certificados |
| Mooc de Lovelace: Programação Python e C | CEFOR | 6.310 | 21,5% | +675 certificados |
| ProgramaKids: Apresentando a programação para as crianças | CEFOR | 2.871 | 12,7% | +561 certificados |
| Estatística com o R | Campus Linhares | 2.713 | 16,8% | +419 certificados |
| Como criar um MOOC? | CEFOR | 3.428 | 20,7% | +395 certificados |
| GAMIFICAÇÃO NO MOODLE | CEFOR | 3.081 | 21,4% | +334 certificados |
| Mooc de Lovelace: Robótica Educacional | CEFOR | 3.273 | 24,1% | +264 certificados |
| Ensino de astronomia: Reconhecimento do Céu noturno | CEFOR | 2.710 | 24,2% | +216 certificados |

Insight menos óbvio: o problema não é falta de procura. Esses cursos já atraem público; o gargalo é permanência/conclusão. Para decisão, isso é uma fila de otimização, não uma fila de divulgação.

## Cursos pequenos que parecem eficientes

Cursos com conversão alta e escala ainda modesta:

| Curso | Matrículas | Conversão | Certificados |
|---|---:|---:|---:|
| Plantando um Rio mais Doce – Preparando a terra | 681 | 81,9% | 558 |
| Avaliação da Aprendizagem no Contexto da Educação Ambiental | 805 | 67,2% | 541 |
| Moodle 4 para Estudantes | 685 | 57,4% | 393 |
| Educação em Saúde Ambiental | 149 | 53,7% | 80 |
| Catadores como Ecoeducadores Ambientais | 171 | 49,1% | 84 |
| Explorando Estilos de Aprendizagem | 716 | 45,3% | 324 |
| Saberes Populares e Educação Ambiental | 769 | 44,6% | 343 |
| Comunidades Quilombolas e os Saberes Sócioambientais | 972 | 44,1% | 429 |
| Resíduos Sólidos e a Educação Ambiental | 880 | 43,9% | 386 |

Insight menos óbvio: há cursos “pequenos bons” que podem estar subpromovidos. Dobrar a matrícula dos 10 cursos mais eficientes, mantendo a mesma conversão, adicionaria cerca de +3.207 certificados.

## Unidades

| Unidade | Cursos | Matrículas | Participação | Conversão |
|---|---:|---:|---:|---:|
| CEFOR | 71 | 179.239 | 60,4% | 36,1% |
| Campus Linhares | 5 | 28.290 | 9,5% | 14,8% |
| Campus Vila Velha | 34 | 12.775 | 4,3% | 42,6% |
| Campus Aracruz | 6 | 11.473 | 3,9% | 36,2% |
| Campus Ibatiba | 5 | 10.482 | 3,5% | 36,5% |
| Campus Venda Nova do Imigrante | 2 | 10.201 | 3,4% | 30,4% |
| Campus Viana | 7 | 10.008 | 3,4% | 33,5% |
| Campus Nova Venécia | 8 | 9.945 | 3,4% | 30,4% |
| Campus Colatina | 8 | 8.201 | 2,8% | 33,8% |

Insight menos óbvio: Campus Linhares tem grande escala por causa de poucos cursos, mas baixa conversão. Campus Vila Velha tem o comportamento inverso: menor escala por curso, mas excelente conclusão. Uma decisão madura combinaria os dois aprendizados: escala de Linhares + desenho de permanência de Vila Velha.

## Tipos de curso

| Tipo | Cursos | Matrículas | Conversão | Horas de formação |
|---|---:|---:|---:|---:|
| Ensino | 135 | 94,2% | 33,0% | 94,3% |
| Pesquisa | 28 | 5,6% | 37,4% | 5,3% |
| Desenvolvimento Institucional | 1 | 0,2% | 43,8% | 0,4% |

Insight menos óbvio: Pesquisa tem participação pequena, mas conversão superior a Ensino. Pode ser um nicho de catálogo com público mais qualificado/motivado, útil para cursos de aprofundamento e trilhas avançadas.

## Geografia

Top UFs por matrícula:

| UF | Matrículas | Participação |
|---|---:|---:|
| Espírito Santo | 104.249 | 34,9% |
| São Paulo | 35.073 | 11,8% |
| Rio de Janeiro | 20.876 | 7,0% |
| Minas Gerais | 20.484 | 6,9% |
| Bahia | 12.712 | 4,3% |
| Rio Grande do Sul | 10.574 | 3,5% |
| Pernambuco | 8.694 | 2,9% |
| Pará | 8.163 | 2,7% |

Insight menos óbvio: a Vitrine é uma porta nacional. O design e a taxonomia devem favorecer descoberta por tema, nível, carga horária e objetivo profissional, porque a maioria das matrículas por UF já vem de fora do ES.

## Tendência anual

| Ano | Matrículas | Cresc. matrículas | Certificados | Cresc. certificados |
|---|---:|---:|---:|---:|
| 2020 | 26.233 | 1125,3% | 11.616 | 3564,4% |
| 2021 | 25.889 | -1,3% | 8.992 | -22,6% |
| 2022 | 41.029 | 58,5% | 11.716 | 30,3% |
| 2023 | 53.462 | 30,3% | 14.850 | 26,7% |
| 2024 | 50.663 | -5,2% | 20.694 | 39,4% |
| 2025 | 68.720 | 35,6% | 22.258 | 7,6% |
| 2026 parcial | 30.675 | -55,4% | 8.967 | -59,7% |

2026 é parcial, pois a extração foi feita em 2026-07-01. Não deve ser interpretado como queda anual consolidada.

Insight menos óbvio: 2024 teve menos matrículas que 2023, mas muito mais certificados. Isso sugere que a qualidade/conclusão pode melhorar mesmo sem crescimento bruto de entrada. Métrica de sucesso da Vitrine não deve ser só matrícula; precisa incluir certificados e taxa de conclusão.

## Implicações para a nova Vitrine

- O catálogo deve destacar cursos de alta conversão, não apenas mais acessados.
- A busca precisa permitir filtros por carga horária, tema, unidade, nível/esforço e popularidade.
- Cursos de alta demanda e baixa conclusão devem receber sinalização interna de “revisar experiência”.
- Cursos com conversão alta e baixa escala devem entrar em campanhas, vitrines temáticas e recomendações.
- A Vitrine deve ajudar o usuário a escolher melhor; escolha ruim provavelmente vira abandono.
- Métricas de decisão recomendadas para cada curso: matrículas, certificados, taxa de certificação, tempo médio de conclusão, carga horária, unidade, tipo, popularidade e tendência recente.

