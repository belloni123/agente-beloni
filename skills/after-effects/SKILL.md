---
name: after-effects
description: Cria e revisa motion graphics no Adobe After Effects. Use para títulos, lower thirds, vinhetas, composição, keyframes, expressões, scripts JSX e templates MOGRT.
---

# After Effects

## Preparar a composição

- Confirme dimensões, proporção, FPS e duração com a referência ou projeto. Se for editar um AEP existente, salve uma cópia versionada e identifique as comps que o pedido afeta.
- Organize os elementos reutilizáveis em pré-comps. Separe mídia, composição de entrega e controles editáveis. Para peças que mudam de proporção, teste o enquadramento e a legibilidade em cada comp de saída.
- Marque as entradas, pontos de leitura e saídas. Revise a animação em velocidade normal antes de ajustar curvas no Graph Editor. Use controles compartilhados para propriedades que precisam variar em conjunto.

## Escolher a automação

- Use expressões para calcular o valor de uma propriedade ou vinculá-la a um controle. Confira o tipo esperado pela propriedade, especialmente valores 2D e 3D. Para caixas que acompanham texto, teste a expressão baseada em `sourceRectAtTime()` com texto curto, longo e multilinha.
- Use um script ExtendScript (`.jsx`) para criar comps, inserir camadas ou automatizar tarefas do projeto. Valide a comp e a seleção antes de alterar o AEP. Agrupe operações em um undo group e feche-o em `finally`. Use match names para propriedades internas quando o script precisar funcionar em instalações com idiomas diferentes.
- Para MOGRT, publique no Essential Graphics apenas os controles que o editor precisa alterar. Confira fontes, mídia e pré-comps, exporte o `.mogrt` e teste no Premiere com dados diferentes dos padrões.

## Entregar e conferir

- Entregue AEP editável, MOGRT, render ou código conforme o pedido. Preserve o áudio original em mudanças apenas visuais. Em entrega com transparência, confira um quadro sobre fundos claro e escuro.
- Abra o projeto salvo, confira fontes e arquivos vinculados. Revise primeiro e último quadro, transições, legibilidade e dimensões do arquivo exportado. Se o aplicativo não estiver disponível, entregue o código ou procedimento solicitado e informe quais verificações dependem do After Effects.

## Documentação Adobe

- [Scripts em After Effects](https://helpx.adobe.com/after-effects/desktop/automate-in-after-effects/automate-animation/scripts.html)
- [Expressões](https://helpx.adobe.com/after-effects/using/expression-basics.html)
- [Motion Graphics Templates](https://helpx.adobe.com/after-effects/using/editable-text-templates.html)
