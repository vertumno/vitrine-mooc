/**
 * Gera canonico/cursos-dados.js a partir de duas entradas:
 *
 *   1. stages/02-catalogo/output/catalogo-cursos-completo.json  (extração da vitrine atual)
 *   2. canonico/curadoria.json                                   (curadoria manual)
 *
 * Séries, projetos parceiros, idiomas adicionais e sinalização de curso obsoleto NÃO existem
 * na fonte — são decisões do CEFOR e vivem em curadoria.json.
 *
 * Uso:  node gerar-dados.mjs
 *
 * A saída é determinística: rodar duas vezes produz arquivos idênticos.
 */

import { readFileSync, writeFileSync } from "node:fs";
import { dirname, join } from "node:path";
import { fileURLToPath } from "node:url";

const AQUI = dirname(fileURLToPath(import.meta.url));
const FONTE = join(AQUI, "..", "..", "..", "02-catalogo", "output", "catalogo-cursos-completo.json");
const CURADORIA = join(AQUI, "curadoria.json");
const SAIDA = join(AQUI, "cursos-dados.js");

// ---------------------------------------------------------------- normalização

/** Remove acentos e caixa, para comparar texto livre vindo da extração. */
const chave = (s) =>
  String(s ?? "")
    .normalize("NFD")
    .replace(/[̀-ͯ]/g, "")
    .toLowerCase()
    .trim();

/**
 * Carga horária: a fonte tem 25+ grafias para o mesmo dado — "60h", "60 horas",
 * "60 Horas", "60 horas.", "20 h", "20H", "30h." etc. Pedido do Marquito na
 * reunião de 09/07/2026: padronizar. Regra: primeiro inteiro do texto -> "NNh".
 */
function normalizarCarga(bruto) {
  const texto = String(bruto ?? "").trim();
  // "Carga horária" é vazamento do cabeçalho da tabela na extração, não um valor.
  if (!texto || chave(texto) === "carga horaria") {
    return { carga: "nao-informada", cargaLabel: "Não informada" };
  }
  const achado = texto.match(/\d+/);
  if (!achado) return { carga: "nao-informada", cargaLabel: "Não informada" };

  const horas = Number(achado[0]);
  const faixa =
    horas <= 10 ? "ate-10" :
    horas <= 20 ? "10-20" :
    horas <= 40 ? "20-40" :
    horas <= 60 ? "40-60" : "mais-60";

  return { carga: faixa, cargaLabel: `${horas}h` };
}

/**
 * Nível: além das grafias com ponto final e caixa variada, alguns registros
 * trazem o bloco de professores colado ("Básico\nInstrutora:..."). Corta na
 * primeira quebra de linha e compara sem acento.
 */
function normalizarNivel(bruto) {
  const primeira = String(bruto ?? "").split("\n")[0];
  const k = chave(primeira).replace(/\.$/, "");
  if (k.startsWith("basico")) return { nivel: "basico", nivelLabel: "Básico" };
  if (k.startsWith("intermediari")) return { nivel: "intermediario", nivelLabel: "Intermediário" };
  if (k.startsWith("avancad")) return { nivel: "avancado", nivelLabel: "Avançado" };
  return { nivel: "nao-informado", nivelLabel: "Não informado" };
}

/**
 * Idioma: habilita o filtro pedido pela Vanessa na reunião de 09/07/2026.
 * A fonte tem 13 grafias de "Português" ("Português.", "português",
 * "Português (Brasil)", "Português - BR", "língua portuguesa"...) e alguns
 * registros multilíngues ("Inglês e Português", "Pomerano/Português").
 *
 * Retorna códigos (pt/en/es/pom) — não rótulos — porque o card já usa esse
 * campo para desenhar os selos de bandeira (LANGUAGE_BADGES em cursos.html).
 */
const IDIOMAS = [
  { codigo: "pt", nome: "Português", padrao: /portugu|lingua portuguesa/ },
  { codigo: "en", nome: "Inglês", padrao: /ingles|english/ },
  { codigo: "es", nome: "Espanhol", padrao: /espanhol|espanol|spanish/ },
  { codigo: "pom", nome: "Pomerano", padrao: /pomerano/ }
];

function normalizarIdiomas(bruto) {
  const k = chave(bruto);
  // "Idioma" é vazamento do cabeçalho, mesmo caso da carga horária.
  if (!k || k === "idioma") return [];

  // A faceta é sobre a língua em que o curso é ministrado, não sobre a língua
  // ensinada. "Português (língua de instrução) e inglês (língua alvo)" é um
  // curso em português — marcá-lo como inglês daria falso positivo na busca.
  const trechos = k.split(/[,;/]| e /).filter((t) => !/alvo/.test(t));

  return IDIOMAS.filter((i) => trechos.some((t) => i.padrao.test(t))).map((i) => i.codigo);
}

// ---------------------------------------------------------------- geração

const fonte = JSON.parse(readFileSync(FONTE, "utf8"));
const curadoria = JSON.parse(readFileSync(CURADORIA, "utf8"));

// Índices da curadoria, por número do curso.
const serieDoCurso = new Map();
for (const s of curadoria.series) {
  for (const n of s.cursos) {
    if (!serieDoCurso.has(n)) serieDoCurso.set(n, []);
    serieDoCurso.get(n).push(s);
  }
}
const projetoDoCurso = new Map();
for (const p of curadoria.projetos) {
  for (const n of p.cursos) {
    if (!projetoDoCurso.has(n)) projetoDoCurso.set(n, []);
    projetoDoCurso.get(n).push(p);
  }
}
const idiomasCurados = new Map(curadoria.idiomas_curados.map((i) => [i.n, i.idiomas]));
const obsoletos = new Map(curadoria.obsoletos.map((o) => [o.n, o]));

const cursos = fonte.cursos.map((bruto) => {
  const campos = bruto.campos ?? {};

  const categoria = String(bruto.categorias_slugs ?? "").split(",").map((s) => s.trim()).filter(Boolean);
  const categoriaNomes = String(bruto.categorias_nomes ?? "").split(",").map((s) => s.trim()).filter(Boolean);
  const tags = String(bruto.tags ?? "").split(",").map((s) => s.trim()).filter(Boolean);

  const series = serieDoCurso.get(bruto.n) ?? [];
  const projetos = projetoDoCurso.get(bruto.n) ?? [];

  // Idioma da fonte + idiomas adicionais da curadoria (ex.: série Embrace, com
  // versões em inglês e espanhol). Curso sem idioma legível na extração assume
  // Português: a plataforma é brasileira e a ausência é falha de extração, não
  // ausência real do metadado (Art. 14 VI da Resolução CS 72/2020).
  const idiomas = [...new Set([
    ...(normalizarIdiomas(campos.idioma).length ? normalizarIdiomas(campos.idioma) : ["pt"]),
    ...(idiomasCurados.get(bruto.n) ?? [])
  ])];
  // Mantém a ordem canônica pt · en · es · pom.
  idiomas.sort((a, b) => IDIOMAS.findIndex((i) => i.codigo === a) - IDIOMAS.findIndex((i) => i.codigo === b));

  const curso = {
    n: bruto.n,
    titulo: bruto.titulo_catalogo,
    categoria,
    categoriaNomes,
    ...normalizarCarga(campos.carga_horaria),
    ...normalizarNivel(campos.nivel_dificuldade),
    libras: Boolean(bruto.libras),
    idiomas,
    projeto: projetos.map((p) => p.slug),
    projetoNomes: projetos.map((p) => p.nome),
    serie: series.map((s) => s.slug),
    serieNomes: series.map((s) => s.nome),
    link: bruto.link_curso,
    thumb: bruto.link_thumb,
    search: [
      bruto.titulo_catalogo,
      ...categoriaNomes,
      ...tags,
      campos.descricao_curso ?? "",
      campos.publico_alvo ?? "",
      ...projetos.map((p) => p.nome),
      ...series.map((s) => s.nome)
    ].join(" ")
  };

  // Curso substituído por versão mais recente — some das vitrines da Home e
  // ganha aviso no catálogo, até a extinção formal (reunião de 09/07/2026).
  const obsoleto = obsoletos.get(bruto.n);
  if (obsoleto) {
    curso.obsoleto = true;
    curso.obsoletoNota = obsoleto.nota;
    curso.obsoletoNotaEn = obsoleto.nota_en;
  }

  return curso;
});

// Facetas: só entram valores que realmente ocorrem, para não exibir filtro vazio.
const usados = (extrair) => new Set(cursos.flatMap(extrair));

const catUsadas = usados((c) => c.categoria);
const categoriasVistas = new Map();
for (const c of cursos) {
  c.categoria.forEach((slug, i) => {
    if (!categoriasVistas.has(slug)) categoriasVistas.set(slug, c.categoriaNomes[i] ?? slug);
  });
}

const cargasUsadas = usados((c) => [c.carga]);
const niveisUsados = usados((c) => [c.nivel]);
const idiomasUsados = usados((c) => c.idiomas);

const filtros = {
  categoria: [...categoriasVistas.entries()]
    .filter(([slug]) => catUsadas.has(slug))
    .map(([slug, nome]) => ({ slug, nome })),
  carga: [
    { slug: "ate-10", nome: "Até 10h" },
    { slug: "10-20", nome: "10 a 20h" },
    { slug: "20-40", nome: "20 a 40h" },
    { slug: "40-60", nome: "40 a 60h" },
    { slug: "mais-60", nome: "Mais de 60h" },
    { slug: "nao-informada", nome: "Não informada" }
  ].filter((f) => cargasUsadas.has(f.slug)),
  nivel: [
    { slug: "basico", nome: "Básico" },
    { slug: "intermediario", nome: "Intermediário" },
    { slug: "avancado", nome: "Avançado" },
    { slug: "nao-informado", nome: "Não informado" }
  ].filter((f) => niveisUsados.has(f.slug)),
  idioma: IDIOMAS.filter((i) => idiomasUsados.has(i.codigo)).map((i) => ({ slug: i.codigo, nome: i.nome })),
  projeto: curadoria.projetos.map((p) => ({ slug: p.slug, nome: p.nome })),
  serie: curadoria.series.map((s) => ({ slug: s.slug, nome: s.nome }))
};

const saida =
  `// Dados gerados por gerar-dados.mjs a partir de\n` +
  `// stages/02-catalogo/output/catalogo-cursos-completo.json + canonico/curadoria.json.\n` +
  `// NÃO editar à mão — rode "node gerar-dados.mjs" para regerar.\n` +
  `window.CURSOS_FILTROS = ${JSON.stringify(filtros, null, 2)};\n\n` +
  `window.CURSOS_MOOC = ${JSON.stringify(cursos, null, 2)};\n`;

writeFileSync(SAIDA, saida);

// ---------------------------------------------------------------- resumo

const conta = (lista, campo) => {
  const m = {};
  for (const c of cursos) for (const v of [].concat(c[campo] ?? [])) m[v] = (m[v] ?? 0) + 1;
  return lista.map((f) => `${f.nome}: ${m[f.slug] ?? 0}`).join(" · ");
};

console.log(`cursos-dados.js gerado — ${cursos.length} cursos`);
console.log(`  carga:   ${conta(filtros.carga, "carga")}`);
console.log(`  nível:   ${conta(filtros.nivel, "nivel")}`);
console.log(`  idioma:  ${conta(filtros.idioma, "idiomas")}`);
console.log(`  séries:  ${conta(filtros.serie, "serie")}`);
console.log(`  projetos:${conta(filtros.projeto, "projeto")}`);
console.log(`  obsoletos: ${cursos.filter((c) => c.obsoleto).length}`);
