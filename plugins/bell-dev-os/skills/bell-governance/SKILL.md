---
name: bell-governance
description: Roteia pedidos de desenvolvimento em linguagem natural entre inicialização, PLAN, IMPLEMENT, VERIFY e REVIEW; coordena transições com rigor proporcional ao risco.
---
# Bell Dev OS — governança

Interprete o pedido e classifique internamente: ajuste trivial, bug localizado, melhoria pequena, feature, alteração relevante, mudança arquitetural ou novo projeto. Consulte [workflow](references/workflow.md) e [níveis de risco](references/risk-levels.md). Para trabalho de interface, consulte [qualidade frontend](references/frontend-quality.md); para decisões de backend, dados ou deploy, consulte [seleção de backend](references/backend-selection.md). Use o mínimo de etapas e artefatos que permita uma entrega segura; preserve as quatro fases para mudanças relevantes. Não imponha formulários ou aprovações intermediárias para ajustes triviais.

Quando o usuário disser `Bell iniciar site` ou `Bell iniciar projeto`, conduza o modo correspondente do [briefing guiado](references/briefing.md). São gatilhos em linguagem natural, não comandos de interface. O usuário pode enviar texto, emails, briefings, anexos e áudios antes deles; o gatilho sinaliza que terminou o envio inicial. Ambos iniciam consolidação, entrevista e síntese dentro de `bell-plan`, nunca build automático. `bell-init-project` continua reservado à preparação de um repositório e só entra depois, se o briefing aprovado indicar essa necessidade e a execução estiver no escopo.

Antes de implementar, esclareça ambiguidades de produto que afetem o resultado. Entenda problema, requisitos e usuário; separe regras de negócio de decisões técnicas; registre decisões relevantes. Investigue o repositório antes de perguntar. Faça perguntas apenas quando a resposta mudar materialmente a implementação. Siga instruções do usuário e do projeto quando forem mais específicas.

Use a [tabela de decisão](references/workflow.md) para escolher a primeira fase. Respeite pedidos explícitos de planejar, implementar, conferir ou revisar; quando o pedido for amplo, percorra as fases necessárias até entregar o resultado solicitado. Inicializar o repositório prepara o projeto, enquanto planejar define o produto e a mudança. Um pedido simples pode atravessar as fases de modo leve sem criar arquivos. Não trate uma implementação como concluída antes de evidência proporcional. GitHub, branch, PR e CI são opções de fluxo, não autorização para publicar código, dados ou segredos.
