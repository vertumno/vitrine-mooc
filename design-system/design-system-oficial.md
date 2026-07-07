# Design System Oficial — Cursos Abertos do Ifes

> **Status:** OFICIAL (decisão do usuário em 07/07/2026).
> **Fonte principal:** `stages/03-design-ux/output/_arquivo/proposta-home-vitrine.html` (proposta aprovada como direção visual, hoje arquivada),
> combinada com `palette.md`, `typography.md` e `design-logo-cefor/design-logo-cefor.md`.
> Este arquivo é a referência canônica para todo protótipo novo e para o tema WordPress (estágio 05).

---

## 1. Nome da plataforma

| Regra | Valor |
|-------|-------|
| Nome público (páginas, títulos, SEO, footer) | **Cursos Abertos do Ifes** |
| "Vitrine" / "Vitrine MOOC" | **Apenas referência interna** do projeto — **NUNCA** aparece em página |
| Assinatura institucional | Ifes · Cefor |

---

## 2. Tokens de cor

```css
:root{
  /* Superfícies e texto */
  --paper:#f8f9fa;        /* fundo da página */
  --paper-2:#f1f6f2;      /* fundo alternado de seção */
  --ink:#212529;          /* texto */
  --ink-soft:#6c757d;     /* texto secundário / metadados */
  --line:#dee2e6;         /* bordas e divisores */

  /* Marca — verde institucional Ifes */
  --green:#147a02;        /* primária: botões, links de marca, foco */
  --green-mid:#066017;    /* hover, links, eyebrow */
  --green-deep:#195128;   /* hero, blocos imersivos, footer, topbar gov */
  --green-mist:#dcefd3;   /* badges, chips, hover suave */

  /* Marca CEFOR/IF (somente logo e badge NOVO) */
  --cefor-green:#3da63d;  /* quadrados do pixel-mark */
  --cefor-red:#e2211c;    /* círculo do pixel-mark */

  /* Apoio e acento */
  --teal:#008080;         /* apoio/categoria (herança) */
  --red:#dc3545;          /* badge NOVO, erro */
  --amber:#ffbc00;        /* dourado — acento pontual (SEMPRE texto escuro por cima) */

  /* Estrutura */
  --radius:10px;
  --maxw:1160px;
}
```

**Tons derivados usados sobre verde-profundo** (texto/detalhe em seções `--green-deep`):
`#F2F7F0` (título), `#C9DECB` (lead), `#9FD8A6` (destaque/em/link), `#8FC996` (eyebrow), `#CFE3CF` (topbar), `#A9C4AC` (footer).

## 3. Tipografia

```css
:root{
  --font-display:"Poppins","Segoe UI",sans-serif;             /* h1–h3, títulos */
  --font-body:"Open Sans",system-ui,-apple-system,sans-serif; /* corpo + dados (16px, lh 1.6) */
  --font-cond:"Oswald","Arial Narrow",sans-serif;             /* eyebrow/kicker uppercase */
  --font-mono:var(--font-body); /* mono DESATIVADA (07/07/2026) — ver nota abaixo */
}
```

- **Sem fonte monoespaçada (decisão 07/07/2026).** O usuário não gosta de mono. Números, carga horária, matrículas, selos e contagens usam a **fonte de corpo (Open Sans)**. Para neutralizar usos herdados sem reescrever tudo, `--font-mono` aponta para `--font-body`; a JetBrains Mono foi removida do `@import`.
- Escala e pesos: ver `typography.md` (base 16px, h1 `clamp(2rem,4.4vw,3.3rem)` na hero, seção h2 `clamp(1.5rem,2.6vw,2.1rem)`).

## 4. Marca CEFOR (logo)

Usar o **pixel-mark oficial** (grade 3×4: círculo vermelho `#e2211c` + 10 quadrados verdes `#3da63d` + 2 células vazias nas colunas 3 das linhas 2 e 4) conforme `design-logo-cefor/design-logo-cefor.md` — Implementação A (CSS puro) nos protótipos; PNGs oficiais (`cefor-horizontal-cor.png`, `icone_cefor-horizontal-cor.png`) quando fidelidade total for exigida.

Lockup do header da plataforma: pixel-mark + texto **"Cursos Abertos"** / **"Ifes · Cefor"**.

## 5. Componentes canônicos (da proposta aprovada)

| Componente | Especificação |
|------------|--------------|
| **Topbar gov** | Faixa `--green-deep`, texto `#CFE3CF` 0.78rem: "Instituto Federal do Espírito Santo · Cefor" + links utilitários (Validar certificado, Suporte) |
| **Header** | Sticky, fundo `--paper`, 68px, logo à esquerda, nav com underline verde no hover, CTA `btn-primary` |
| **Hero** | Fundo `--green-deep`, eyebrow Oswald, h1 com `em` verde-claro `#9FD8A6`, busca com botão `btn-light`. **REGRA: hero COMPACTA** — nas páginas internas, apenas título + lead + busca (padding vertical ≤ 40px); na home, sem mosaico gigante nem stats de 4 colunas |
| **Botões** | `--radius` 10px (não pill), padding 12px 22px, peso 700; variantes: `primary` (verde), `outline` (borda), `light` (branco sobre verde) |
| **Eyebrow** | Oswald 0.9rem, uppercase, tracking .1em, `--green-mid` (ou `#8FC996` sobre verde) |
| **Card de curso** | Fundo branco, borda `--line`, radius 10px, hover eleva (`translateY(-2px)` + sombra). **Capa = imagem original do curso** preenchendo o card **inteiro, sem faixa branca, sem espaço lateral e sem corte perceptível**. As thumbs têm todas a **mesma proporção** (~274×188 ≈ 1.456), então a moldura usa `aspect-ratio:274/188` + `object-fit:cover` — ratio da moldura = ratio da imagem, logo cobre 100% sem cortar. Cards com a mesma altura. **Sem nada sobreposto.** (Se o formato das thumbs mudar no futuro, ajustar o `aspect-ratio` da `.capa` para o novo ratio.) Corpo branco na ordem: **categoria (topo)** → **nome** → **meta** → **selos** → botão compacto **"Acessar curso"** (reordenado via flex `order`; botão em verde-profundo `--green-deep`, mais escuro). Categoria como kicker `--green-mid` semibold |
| **Selos** | Chips **sutis na área branca** (nunca sobre a imagem): fundo `--paper-2`, texto `--ink-soft`, borda `--line`, radius 4px, .66rem. Rótulos legíveis (`Libras`, `Novo`, `Mais cursado`, `UnAC`, `Inglês`). **Idioma: português é o padrão implícito — NÃO exibir selo "Português"**; só mostrar selo de idioma quando o curso for em inglês (`Inglês`/`EN`). `Novo` = tom dourado suave (bg `#fff6e0`, texto `#8a5a00`); `Mais cursado` (`.pop`) = verde suave (`--green-mist`/`--green-mid`). `.selos:empty` colapsa para não deixar espaço vazio |
| **Meta do curso** | 0.72rem `--green-mid` (fonte de corpo): carga horária · inscritos/nível |
| **Filtros/chips** | 0.75rem, pill, borda `--line`; ativo = fundo `--green-deep` texto branco |
| **Página Cursos** | Hero compacta (sem busca) → catálogo direto (filtros + grade). **Sem seção "Em destaque"** — os destaques vivem só na home |
| **Ranking (mais cursados)** | Lista com posição grande, nome Poppins, matrículas à direita |
| **Seções imersivas** | Licença/projetos: fundo `--green-deep` com grid-pattern sutil de linhas brancas a 7–9% |
| **FAQ** | `<details>/<summary>` com `+`/`−` mono |
| **Motion** | `.reveal` (fade+rise 0.6s) via IntersectionObserver; tudo desligado sob `prefers-reduced-motion` |
| **Container** | `max-width:1160px`, padding lateral 24px |

## 6. Regras de conteúdo (do's & don'ts)

**Faça ✅**
- Dizer "**gratuito**" em texto corrido ("gratuito, com certificado do Ifes").
- Usar imagens **originais** de cada curso (thumbs de `mooc.cefor.ifes.edu.br`) nas capas.
- Números reais dos indicadores (matrículas Power BI) nos rankings e selos de prova social.
- Acessibilidade: skip-link, `:focus-visible` verde, `aria-*` em carrossel/filtros, contraste AA.

**Não faça ❌**
- ~~"Vitrine"~~ em qualquer texto visível de página.
- ~~Estatística "R$ 0 — gratuito, do início ao certificado"~~ (decisão 07/07/2026: não usar "R$ 0" como número; gratuidade é mensagem de texto, não métrica).
- Hero gigante (2 colunas + mosaico + 4 stats) em páginas internas. Na página **Cursos**, a hero não tem busca (a busca vive no catálogo).
- **Fonte monoespaçada** em qualquer lugar (decisão 07/07/2026).
- **Selos sobre a imagem** do curso — sempre na área branca do card.
- ~~"Certificado Ifes"~~ como rótulo dentro do card; ~~dois botões~~ no card (só "Acessar curso").
- Dourado `--amber` com texto branco (usar texto `--ink`).
- Capas com gradiente + iniciais quando existir thumb real do curso.

---

## Rastreabilidade

- Proposta-fonte: `stages/03-design-ux/output/_arquivo/proposta-home-vitrine.html` (arquivada como referência histórica — ainda usa o nome antigo e a hero grande; **este documento prevalece**).
- Protótipos oficiais novos: `stages/03-design-ux/output/prototipo-cursos-abertos/`.
- Tokens detalhados: `palette.md` (cores) · `typography.md` (tipografia) · `design-logo-cefor/` (marca CEFOR).
