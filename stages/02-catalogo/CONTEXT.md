# Estagio 02: Catalogo

Inventariar os cursos, definir a taxonomia e o esquema de metadados que estrutura a Vitrine.

## Inputs

| Fonte | Arquivo/Local | Escopo | Por que |
|-------|---------------|--------|---------|
| Estagio anterior | `../01-descoberta/output/` | Arquivos completos | Requisitos e analise da Vitrine atual |
| Cursos | `references/cursos-fonte.md` | Arquivo completo | Lista bruta: 165 publicados + 65 em producao |
| Meta | `../../shared/projeto-meta.md` | "Escopo do Catalogo" | Numeros e status dos cursos |
| Indicadores | `output/powerbi-mooc-ifes/` | Planilha, CSVs, manifesto e analise | Demanda, conclusao, distribuicao geografica e priorizacao por dados reais |

## Process

1. Leia `cursos-fonte.md` e separe os cursos por status: publicado e em producao.
2. Normalize os dados (titulos, quebras de linha, duplicidades de famílias como "Lovelace", "Mary Keller", "Educador Maker").
3. Defina a taxonomia: categorias/temas (ex.: Educacao Ambiental, Programacao e TI, Educacao e Pedagogia, Ciencias, Gestao Publica, Idiomas, Saude) e tags transversais (CTSA, Moodle, IA, acessibilidade).
4. Defina o esquema de metadados por curso: titulo, slug, categoria, tags, status, descricao, carga horaria, link, imagem.
5. Classifique cada curso na taxonomia.
6. **[Checkpoint]** Apresente a taxonomia e uma amostra classificada para validacao.
7. Quando houver tarefa de priorizacao, estrategia de catalogo ou UX orientada a dados, consulte `output/powerbi-mooc-ifes/analise-insights-powerbi-mooc-ifes.md`.
8. Para atualizar os indicadores, rode `scripts/extrair_powerbi_mooc.py` e revise `output/powerbi-mooc-ifes/manifest.json`.
9. Rode os checks de Audit. Se algum falhar, revise antes de salvar.
10. Salve o catalogo estruturado em `output/`.

## Checkpoints

| Apos passo | Agente apresenta | Humano decide |
|------------|------------------|---------------|
| 5 | Taxonomia proposta + amostra de cursos classificados | Se categorias e metadados servem para a Vitrine |

## Audit

| Check | Condicao de aprovacao |
|-------|------------------------|
| Cobertura | Todos os cursos da fonte aparecem no catalogo |
| Status | Cada curso marcado como publicado ou em producao |
| Classificacao | Cada curso tem ao menos uma categoria |
| Esquema | Todo curso segue o mesmo esquema de metadados |
| Indicadores | Se usados para decisao, registrar data de extracao, refresh do dataset e limitacoes |

## Outputs

| Artefato | Local | Formato |
|----------|-------|---------|
| Taxonomia | `output/taxonomia.md` | Markdown: categorias, tags e regras |
| Catalogo | `output/catalogo-cursos.md` | Tabela (ou JSON) com metadados de cada curso |
| Catalogo enriquecido | `output/catalogo-cursos-completo.*` | CSV/JSON/Markdown com detalhes extraidos das paginas dos cursos |
| Indicadores Power BI | `output/powerbi-mooc-ifes/painel-indicadores-mooc-ifes.xlsx` | Workbook com abas extraidas do painel |
| Analise de indicadores | `output/powerbi-mooc-ifes/analise-insights-powerbi-mooc-ifes.md` | Markdown executivo com insights e recomendacoes |
| Registro tecnico Power BI | `output/powerbi-mooc-ifes/registro-extracao-powerbi.md` | Markdown com procedimento, limites e reproducibilidade |

## Power BI - Painel de Indicadores

O painel de indicadores da plataforma foi extraido como fonte complementar ao catalogo. Ele nao substitui a lista canonica de cursos, mas adiciona sinais de decisao sobre demanda e conclusao.

### Como atualizar

```powershell
python stages\02-catalogo\scripts\extrair_powerbi_mooc.py
```

### Quando carregar

Carregue `output/powerbi-mooc-ifes/` quando a tarefa envolver:

- priorizacao de cursos;
- destaque na Vitrine;
- filtros/ordenacao por popularidade ou conclusao;
- estrategia de catalogo;
- analise de alcance geografico;
- decisoes de UX baseadas em comportamento real.

### Cuidados

- O ano de 2026 e parcial na extracao atual, feita em 2026-07-01.
- Algumas visualizacoes do Power BI nao retornaram dados pela API publica; ver `manifest.json`.
- A analise quantitativa excluiu linhas incompletas/anomalas, conforme documentado no relatorio.
