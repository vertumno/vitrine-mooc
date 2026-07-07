# Design System - Logo CEFOR / Ifes

Este arquivo e a especificacao de origem da logo do CEFOR usada na Vitrine MOOC.

Regra principal: a logo final deve ser aplicada a partir dos PNGs oficiais nesta pasta. Nao recriar a marca em CSS, SVG manual, texto editavel ou composicao aproximada quando o objetivo for fechamento visual da interface.

## Fonte canonica

| Uso | Arquivo canonico | Dimensoes do canvas | Area opaca | SHA-256 |
| --- | --- | ---: | ---: | --- |
| Marca horizontal completa | `cefor-horizontal-cor.png` | `2835 x 1135 px` | `2495 x 585 px` | `BF57DC6700F06C9F3D8F839D8CDD2C7BCD94639F2AB8D75833E17AB4EE633276` |
| Icone isolado | `icone_cefor-horizontal-cor.png` | `435 x 575 px` | `403 x 543 px` | `17D12DE5188AFA696206D4D9C14737640F609ED78F4F2DBA2441FD8F41F42AD2` |

Arquivos:

```text
design-system/design-logo-cefor/cefor-horizontal-cor.png
design-system/design-logo-cefor/icone_cefor-horizontal-cor.png
```

## Conteudo visual obrigatorio

### Marca horizontal completa

A marca horizontal deve ser exatamente o arquivo `cefor-horizontal-cor.png`.

Ela contem:

- simbolo dos Institutos Federais a esquerda;
- texto `INSTITUTO FEDERAL` em caixa alta;
- texto `Espirito Santo`;
- assinatura `Centro de Referencia em Formacao`;
- assinatura `e em Educacao a Distancia`.

O texto, a quebra de linha, o peso visual, as proporcoes e os espacamentos devem vir do PNG oficial. Nao substituir por texto HTML/CSS.

### Icone

O icone deve ser exatamente o arquivo `icone_cefor-horizontal-cor.png`.

Ele contem:

- grade visual do Instituto Federal;
- circulo vermelho no canto superior esquerdo;
- blocos verdes com cantos arredondados;
- celulas vazias na terceira coluna da segunda e quarta linhas.

Nao redesenhar o icone em CSS para producao, porque pequenas diferencas de raio, cor, espacamento e antialiasing deixam de ser identicas ao PNG oficial.

## Cores extraidas dos PNGs

Estas cores existem apenas como referencia de auditoria visual. Elas nao autorizam recriacao manual da marca para uso final.

| Elemento | Cor dominante extraida |
| --- | --- |
| Verde do simbolo | `#359830` |
| Vermelho do circulo | `#C90C0F` |
| Texto da marca horizontal | `#000000` |

## Regras de aplicacao em HTML

Use sempre `img` apontando para o PNG oficial.

Os exemplos abaixo usam o caminho relativo correto a partir de:

```text
stages/03-design-ux/output/prototipo-cursos-abertos/cursos.html
```

### Marca horizontal

```html
<img
  class="cefor-logo cefor-logo--horizontal"
  src="../../../../design-system/design-logo-cefor/cefor-horizontal-cor.png"
  alt="Instituto Federal do Espirito Santo - Centro de Referencia em Formacao e em Educacao a Distancia"
>
```

### Icone isolado

```html
<img
  class="cefor-logo cefor-logo--icon"
  src="../../../../design-system/design-logo-cefor/icone_cefor-horizontal-cor.png"
  alt="Instituto Federal do Espirito Santo"
>
```

### CSS recomendado

```css
.cefor-logo {
  display: block;
  width: auto;
  max-width: 100%;
  object-fit: contain;
  object-position: left center;
}

.cefor-logo--horizontal {
  aspect-ratio: 2835 / 1135;
}

.cefor-logo--icon {
  aspect-ratio: 435 / 575;
}
```

Defina a altura pelo contexto da interface e preserve `width: auto`. Nunca force largura e altura simultaneamente se isso alterar a proporcao natural do PNG.

## Tamanhos de referencia

| Contexto | Asset | Altura sugerida |
| --- | --- | ---: |
| Header desktop | `cefor-horizontal-cor.png` | `56px` a `72px` |
| Header compacto | `cefor-horizontal-cor.png` | `44px` a `56px` |
| Rodape | `cefor-horizontal-cor.png` | `56px` a `80px` |
| Favicon/app icon interno | `icone_cefor-horizontal-cor.png` | conforme exportacao necessaria |
| Marca auxiliar pequena | `icone_cefor-horizontal-cor.png` | `36px` a `52px` |

## Fundos e contraste

Os PNGs tem transparencia. A marca horizontal usa texto preto; portanto:

- aplicar preferencialmente sobre fundo branco ou muito claro;
- nao aplicar a marca horizontal sobre fundo escuro, verde saturado, imagem carregada ou gradiente;
- se o fundo nao for claro, criar uma faixa clara solida para receber a marca;
- nao adicionar sombra, contorno, brilho, filtro, blur ou recoloracao.

## Proibido

- Recriar o logotipo final com CSS grid, SVG manual ou texto HTML.
- Trocar o arquivo por uma versao recortada, comprimida, convertida ou redesenhada.
- Alterar cor, contraste, saturacao, opacidade ou aplicar filtros.
- Distorcer a proporcao natural dos PNGs.
- Separar o simbolo do texto na marca horizontal completa.
- Substituir `Centro de Referencia em Formacao e em Educacao a Distancia` por `CEFOR` no lockup oficial.

## Checklist de auditoria

Antes de fechar qualquer tela:

1. O elemento visual usa `cefor-horizontal-cor.png` para marca completa?
2. O icone usa `icone_cefor-horizontal-cor.png` quando aparece sozinho?
3. O `src` aponta para a pasta `design-system/design-logo-cefor/` ou para copia byte-a-byte desses arquivos?
4. A proporcao natural foi preservada?
5. A marca esta sobre fundo claro e limpo?
6. Nao ha CSS recriando quadrados, circulo ou texto da marca?
7. O `alt` descreve a instituicao sem duplicar texto vizinho desnecessariamente?

Se qualquer resposta for "nao", a aplicacao da logo ainda nao esta correta.
