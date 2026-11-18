# Investigar bugs

Para falha de causa desconhecida, reúna evidências antes de alterar código:

1. Leia o erro completo, identifique ambiente e mudanças recentes e reproduza o problema. Se for intermitente, registre as condições e observe o estado nas fronteiras dos componentes.
2. Rastreie o valor ou evento incorreto até a origem e compare com um caso que funciona. Verifique handlers concorrentes, ordem de respostas e estado compartilhado quando os sintomas indicarem disputa.
3. Formule uma hipótese específica e teste uma variável por vez. Não empilhe correções sem saber qual hipótese foi confirmada.
4. Corrija a causa no fluxo do projeto. Quando útil e proporcional, preserve uma reprodução ou teste de regressão que falhe antes e passe depois.
5. Confira o comportamento afetado e os checks exigidos pelo projeto. Relate o que foi observado, o que foi corrigido e as limitações reais.

Se as tentativas repetidas não sustentarem a hipótese, volte às evidências e reavalie a arquitetura ou a dependência externa. Não declarar causa conhecida sem prova.
