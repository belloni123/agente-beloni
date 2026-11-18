---
name: bell-plan
description: Use para definir requisitos, critérios de aceitação e plano de features, novos produtos ou mudanças relevantes e ambíguas antes da implementação; não organiza o repositório.
---
# Planejar

Leia `AGENTS.md`, código relacionado e documentação relevante. Entenda objetivo de negócio, usuário afetado, fluxo principal, regras, requisitos ausentes, casos extremos, dependências e riscos. Separe regra de negócio de decisão técnica. Investigue padrões existentes antes de perguntar; pergunte apenas quando a resposta puder alterar significativamente a implementação.

Se o pedido for `Bell iniciar site` ou `Bell iniciar projeto`, leia e siga o modo correspondente em `../bell-governance/references/briefing.md`. Conclua com o briefing para aprovação; não inicie implementação ou deploy automaticamente.

Decida proporcionalmente se precisa de PRD (problema e negócio), SPEC (comportamento e contratos), ADR (decisão arquitetural relevante) e PLAN (tarefas verificáveis). Use os templates em `../bell-governance/assets/`, eliminando seções irrelevantes. Para mudanças relevantes, produza ou atualize um PLAN vivo. Não escreva código de produção durante o planejamento, salvo investigação técnica mínima. Registre decisões abertas como `[?]` e não invente regra de negócio. Entregue critérios de aceitação que possam ser verificados.

Para interface nova ou mudança visual grande, reúna referências concretas e conteúdo real, defina critérios visuais e funcionais e proponha primeiro um trecho representativo, normalmente o hero ou o fluxo principal. Obtenha alinhamento nesse recorte antes de expandir a página, exceto se o usuário pedir outro fluxo; não imponha essa etapa a correções triviais. Planeje mobile-first, estados e acessibilidade. Leia `../bell-governance/references/frontend-quality.md`; se houver iconografia relevante, defina critérios e família principal usando `../bell-governance/references/icon-selection.md`, sem instalar por antecipação.

Quando houver decisão de backend, dados ou hospedagem, compare alternativas pelo caso de uso, carga, sensibilidade, recursos reais, custo total e manutenção. Leia `../bell-governance/references/backend-selection.md`; não escolha fornecedor ou arquitetura por hábito.
