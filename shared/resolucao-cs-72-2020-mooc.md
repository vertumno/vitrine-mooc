# Resolução CS nº 72/2020 — Normatização dos MOOC no Ifes (fonte oficial)

> **O que é:** norma do Conselho Superior do Ifes que normatiza a elaboração, oferta, funcionamento e certificação dos Cursos Online, Abertos e Massivos (MOOC). **11/12/2020.** Revoga a IN 02/2019.
> **Fonte:** [PDF oficial](https://www.ifes.edu.br/images/stories/Resolu%C3%A7%C3%A3o_CS_72_2020_-_Normatiza_cursos_Mooc_no_Ifes.pdf) (extração verbatim dos artigos 1–22; o PDF completo tem mais artigos sobre funcionamento/certificação).
> **Por que importa:** é a **fonte institucional do objetivo** e do **esquema oficial de metadados** — âncora para toda a categorização (não inventar).

---

## 1. Objetivo / definição oficial (o que a plataforma É)

> **Art. 1º.** Consideram-se Cursos Online, Abertos e Massivos (MOOC) os cursos oferecidos a distância e **abertos à comunidade**.

> **Art. 2º.** São características dos MOOC no Ifes: I. Não possuem mediação/tutoria a distância ou presencial. II. Não possuem processo seletivo. III. Para certificação, é necessário ter aproveitamento mínimo de 60%. IV. Possuem carga horária máxima de 60 (sessenta) horas.

> **Art. 3º.** É vedada a oferta de cursos nos níveis técnico, graduação e pós-graduação lato sensu e stricto-sensu em formato MOOC.

**Leitura:** o objetivo institucional é **educação aberta à comunidade** — democratização/inclusão (reforçado pela página do CEFOR: "grande forma de inclusão social... qualquer pessoa, de qualquer lugar e no seu tempo"). **Não é "qualificação profissional"** — este é um *uso/ênfase*, não a definição. MOOC é **extensão/curso livre** (vedado nível formal — Art. 3º).

**Usos previstos** (Art. 4º–5º): podem compor cursos a distância maiores, cumprir carga horária a distância de cursos presenciais e ser contabilizados como **atividades complementares**.

## 2. Esquema OFICIAL de metadados por curso (Art. 14) — âncora da Camada A

> **Art. 14.** Os projetos de cursos no formato MOOC devem conter, no mínimo: I. Nome do curso. II. Dados do proponente. III. Campus responsável. IV. Ano/semestre de início previsto. V. Carga horária (máx. 60h). **VI. Idioma.** **VII. Nível de dificuldade: básico, intermediário ou avançado.** **VIII. Área de conhecimento do curso, de acordo com a tabela do CNPq.** **IX. Eixo Tecnológico.** X. Membros da equipe (docente, técnico-administrativo, aluno, externo). XI. Recursos Materiais. **XII. Público-alvo.** XIII. Requisitos técnicos. XIV. Pré-requisitos. XV. Ementa. **XVI. Objetivos.** XVII. Conteúdos. XVIII. Metodologia. XIX. Resultados esperados. XX. Perfil do egresso. XXI. Avaliação da aprendizagem. XXII. Bibliografia. XXIII. Indicadores.

**Isto confirma oficialmente (não são invenções nossas):**
- **Área de conhecimento = tabela CNPq** (Art. 14 VIII) → você estava certo. É metadado obrigatório.
- **Eixo Tecnológico** (Art. 14 IX) → existe uma **segunda** classificação oficial (Catálogo Nacional — eixos tecnológicos). Cuidado para **não confundir** com nossos "temas de navegação".
- **Idioma** (Art. 14 VI) → o **selo de idioma** é campo oficial.
- **Nível: básico/intermediário/avançado** (Art. 14 VII) → o campo `nivel` é oficial e tem **valores definidos**.
- **Público-alvo** (Art. 14 XII) e **Objetivos** (Art. 14 XVI) → campos oficiais por curso.

## 3. Acessibilidade (obrigatória — âncora dos selos)

> **Art. 13.** Os professores/instrutores devem providenciar a adaptação dos materiais para **garantir a acessibilidade do curso**.
> **Art. 16, § 3º.** Deve-se **priorizar a elaboração de recursos e atividades acessíveis**.
> **Art. 16, § 2º.** Considerar a multiplicidade de recursos... e a **diversidade do público**.

**Leitura:** os selos **Libras / Audiodescrição** e o eixo **Inclusão e Acessibilidade** têm respaldo normativo.

## 4. Matrícula (Art. 17–20)

Sem limite de vagas, sem seleção (Art. 17); matrícula pelo próprio interessado (Art. 18); sem limite de cursos simultâneos (Art. 19); dados mínimos: nome, CPF/documento, cidade/estado/país, etnia, renda per capita, declaração de veracidade (Art. 20). Não há cadastro no Sistema Acadêmico; o Cefor exporta dados (Art. 21).

## 5. Governança da criação (Art. 6–12)

Proponente deve ser servidor do Ifes (Art. 15); formação indicada pelo Cefor + modelos da **Base de Conhecimento** (Art. 6); Cefor verifica conflitos (Art. 7); aprovação pela diretoria de ensino + parecer do NTE (Art. 8); avaliação de qualidade antes do lançamento (Art. 11); turmas conforme cronograma do Cefor (Art. 22).

---

## Implicações para a Vitrine (o que isto ancora)

1. **Objetivo = educação aberta à comunidade / democratização do conhecimento.** A categorização deve refletir isto (amplo), não "qualificação profissional". O ângulo profissional do PRD é ênfase estratégica — a reconciliar com os autores do PRD.
2. **Camada A (metadados oficiais)** = o Art. 14. Nossa arquitetura deve **usar os campos oficiais**: Área CNPq, Eixo Tecnológico, Idioma, Nível (básico/interm./avançado), Público-alvo, Objetivos, Carga horária, etc.
3. **Duas classificações oficiais coexistem:** Área CNPq **e** Eixo Tecnológico. Nossos "temas de navegação" (~10) são uma **terceira camada, de UX**, derivada dessas — e deve ter nome próprio para não colidir com "Eixo Tecnológico".
4. **Selos (Libras, Audiodescrição, Idioma) e nível** deixam de ser proposta nossa: são **campos oficiais/obrigatórios**.
5. **Status "publicado/em produção"** e a exportação de dados (Art. 21) ajudam a modelar o campo `status`.
