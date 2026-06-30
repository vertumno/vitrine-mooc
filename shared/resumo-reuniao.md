# Resumo — Reunião Vitrine MOOC (CGTI e CGTE)

> **Data:** 23/06/2026 · **Duração:** 84 min
> **Fonte:** `Reunião Vitrine MOOC - CGTI E CGTE.txt`
> **Escopo deste documento:** apenas o que se refere à **Vitrine MOOC**.

**Participantes:**
- Eduardo Moura da Silva (Dudu) — CGTI / infraestrutura e servidores
- Elton Vinicius — CGTE / desenvolvimento
- Marcos Vinícius "Marquito" Forecchi Accioly — CGTE / desenvolvimento

**Ausentes:** Simon e Sérgio (Serginho) — responsáveis por DNS / load balance. Decisões dependentes deles ficaram para a semana seguinte.

---

## Decisões sobre a Vitrine MOOC

**Estratégia definida:** replicar o modelo que já funcionou na Base de Conhecimento, mas com uma melhoria importante — **trabalhar em ambiente de teste de verdade**, e não direto em produção.

| Tema | Decisão |
|------|---------|
| **Ambiente** | Eduardo prepara um **ambiente de teste dedicado** (VMs já existem). Nada sobe em produção para depois "virar" — desenvolve-se em teste, com banco de teste, e só depois migra. |
| **Versão WordPress** | Subir já na **versão 7.0** (a Vitrine atual está na 5.9). A equipe trabalha local com WP 7 desde já. |
| **Banco de dados** | Eduardo disponibiliza um **dump do banco atual** para trabalho local com dados reais. Diferente da Base, a Vitrine **não pode ser "travada"** para inserções — trabalha-se com uma "fotografia de hoje" e refaz-se o dump na hora da migração. |
| **Repositório** | Mesmo Git da Vitrine. Copiar a **estrutura de pastas do repositório da Base de Conhecimento** (modelo que funcionou). O diretório de HTML puro existente foi um rascunho/erro e será descartado. |
| **Fluxo Git** | Branch de trabalho (dev) → PR para a branch indicada por Eduardo → **nunca abrir PR direto para a Master** (Master = produção). Atenção redobrada porque o GitHub abre PR para Master por padrão. |
| **Correção anterior** | Eduardo já reverteu commits que tinham ido para a Master por engano (sem impacto, pois não havia deploy automático nem atualização em produção). |

**Prazo informal:** ambiente da Vitrine começando por volta de **06/07**; até lá a equipe trabalha localmente.

---

## Próximos Passos — Vitrine MOOC

### Eduardo / CGTI
1. **Preparar ambiente de teste da Vitrine** (VM + WordPress 7.0 + banco de teste).
2. **Disponibilizar dump do banco atual** da Vitrine para trabalho local.
3. **Subir estrutura do WordPress atualizada** numa branch e informar à equipe **qual branch** é a "Master de produção".

### Elton e Marquito / CGTE
4. **Copiar o modelo (estrutura de pastas) do repositório da Base** para a Vitrine.
5. Instalar **WordPress 7 local** (Marquito na máquina do CEFOR; Elton na dele) e começar o desenvolvimento da Vitrine localmente.
6. Baixar os assets já produzidos (transcrição + interfaces feitas no IA/UX Studio) e **organizar/estruturar** o projeto.
7. **Disciplina de Git:** trabalhar via branch e abrir PR sempre para a branch indicada (nunca Master direto).
