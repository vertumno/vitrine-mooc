# Estagio 02: Catalogo

Inventariar os cursos, definir a taxonomia e o esquema de metadados que estrutura a Vitrine.

## Inputs

| Fonte | Arquivo/Local | Escopo | Por que |
|-------|---------------|--------|---------|
| Estagio anterior | `../01-descoberta/output/` | Arquivos completos | Requisitos e analise da Vitrine atual |
| Cursos | `references/cursos-fonte.md` | Arquivo completo | Lista bruta: 165 publicados + 65 em producao |
| Meta | `../../shared/projeto-meta.md` | "Escopo do Catalogo" | Numeros e status dos cursos |

## Process

1. Leia `cursos-fonte.md` e separe os cursos por status: publicado e em producao.
2. Normalize os dados (titulos, quebras de linha, duplicidades de famílias como "Lovelace", "Mary Keller", "Educador Maker").
3. Defina a taxonomia: categorias/temas (ex.: Educacao Ambiental, Programacao e TI, Educacao e Pedagogia, Ciencias, Gestao Publica, Idiomas, Saude) e tags transversais (CTSA, Moodle, IA, acessibilidade).
4. Defina o esquema de metadados por curso: titulo, slug, categoria, tags, status, descricao, carga horaria, link, imagem.
5. Classifique cada curso na taxonomia.
6. **[Checkpoint]** Apresente a taxonomia e uma amostra classificada para validacao.
7. Rode os checks de Audit. Se algum falhar, revise antes de salvar.
8. Salve o catalogo estruturado em `output/`.

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

## Outputs

| Artefato | Local | Formato |
|----------|-------|---------|
| Taxonomia | `output/taxonomia.md` | Markdown: categorias, tags e regras |
| Catalogo | `output/catalogo-cursos.md` | Tabela (ou JSON) com metadados de cada curso |
