# Resumo â€” ReuniÃ£o Vitrine MOOC (CGTI e CGTE)

> **Data:** 23/06/2026 Â· **DuraÃ§Ã£o:** 84 min
> **Fonte:** `ReuniÃ£o Vitrine MOOC - CGTI E CGTE.txt`
> **Escopo deste documento:** apenas o que se refere Ã  **Vitrine MOOC**.

**Participantes:**
- Eduardo Moura da Silva (Dudu) â€” CGTI / infraestrutura e servidores
- Elton Vinicius â€” CGTE / desenvolvimento
- Marcos Vinicius Forecchi Accioly â€” CGTE / desenvolvimento

**Ausentes:** Simon e SÃ©rgio (Serginho) â€” responsÃ¡veis por DNS / load balance. DecisÃµes dependentes deles ficaram para a semana seguinte.

---

## DecisÃµes sobre a Vitrine MOOC

**EstratÃ©gia definida:** replicar o modelo que jÃ¡ funcionou na Base de Conhecimento, mas com uma melhoria importante â€” **trabalhar em ambiente de teste de verdade**, e nÃ£o direto em produÃ§Ã£o.

| Tema | DecisÃ£o |
|------|---------|
| **Ambiente** | Eduardo prepara um **ambiente de teste dedicado** (VMs jÃ¡ existem). Nada sobe em produÃ§Ã£o para depois "virar" â€” desenvolve-se em teste, com banco de teste, e sÃ³ depois migra. |
| **VersÃ£o WordPress** | Subir jÃ¡ na **versÃ£o 7.0** (a Vitrine atual estÃ¡ na 5.9). A equipe trabalha local com WP 7 desde jÃ¡. |
| **Banco de dados** | Eduardo disponibiliza um **dump do banco atual** para trabalho local com dados reais. Diferente da Base, a Vitrine **nÃ£o pode ser "travada"** para inserÃ§Ãµes â€” trabalha-se com uma "fotografia de hoje" e refaz-se o dump na hora da migraÃ§Ã£o. |
| **RepositÃ³rio** | Mesmo Git da Vitrine. Copiar a **estrutura de pastas do repositÃ³rio da Base de Conhecimento** (modelo que funcionou). O diretÃ³rio de HTML puro existente foi um rascunho/erro e serÃ¡ descartado. |
| **Fluxo Git** | Branch de trabalho (dev) â†’ PR para a branch indicada por Eduardo â†’ **nunca abrir PR direto para a Master** (Master = produÃ§Ã£o). AtenÃ§Ã£o redobrada porque o GitHub abre PR para Master por padrÃ£o. |
| **CorreÃ§Ã£o anterior** | Eduardo jÃ¡ reverteu commits que tinham ido para a Master por engano (sem impacto, pois nÃ£o havia deploy automÃ¡tico nem atualizaÃ§Ã£o em produÃ§Ã£o). |

**Prazo informal:** ambiente da Vitrine comeÃ§ando por volta de **06/07**; atÃ© lÃ¡ a equipe trabalha localmente.

---

## PrÃ³ximos Passos â€” Vitrine MOOC

### Eduardo / CGTI
1. **Preparar ambiente de teste da Vitrine** (VM + WordPress 7.0 + banco de teste).
2. **Disponibilizar dump do banco atual** da Vitrine para trabalho local.
3. **Subir estrutura do WordPress atualizada** numa branch e informar Ã  equipe **qual branch** Ã© a "Master de produÃ§Ã£o".

### Elton e equipe de desenvolvimento / CGTE
4. **Copiar o modelo (estrutura de pastas) do repositÃ³rio da Base** para a Vitrine.
5. Instalar **WordPress 7 local** (equipe de desenvolvimento na maquina do CEFOR; Elton na dele) e comeÃ§ar o desenvolvimento da Vitrine localmente.
6. Baixar os assets jÃ¡ produzidos (transcriÃ§Ã£o + interfaces feitas no IA/UX Studio) e **organizar/estruturar** o projeto.
7. **Disciplina de Git:** trabalhar via branch e abrir PR sempre para a branch indicada (nunca Master direto).


