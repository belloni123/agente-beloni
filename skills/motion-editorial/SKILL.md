---
name: motion-editorial
description: Criar, revisar e refinar motion graphics explicativos para vídeo, com continuidade entre elementos, conexões corretas, ritmo de leitura e integração com apresentador. Use para diagramas animados, sobreposições e sequências que pareçam rígidas ou desconectadas; não para pedidos apenas de roteiro ou imagem estática.
---

# Motion editorial

Produza movimento que faça o espectador acompanhar uma ideia, e não apenas perceber que elementos se mexem. Preserve o roteiro e a identidade do projeto. Fluidez não equivale a mais efeitos, molas em tudo ou oscilação aleatória.

## Direção a partir do material real

Antes de montar sobre gravação, confira o bruto e o áudio com evidência proporcional; lacuna na transcrição não comprova silêncio. Leia o guia de estilo aprovado e os assets explícitos do projeto. Fixe a montagem antes de alinhar legendas e executar tracking/máscaras caros; mudança de cortes exige recalcular os alinhamentos afetados na saída.

Em oclusão por pessoa, processe só os trechos/regiões necessários e reutilize tracking/matte enquanto fonte e parâmetros forem compatíveis. Confira cabelo, halos e mãos cruzando a máscara. Ao revisar, identifique versão, intervalo e resultado esperado, distinguindo tempo do bruto e da saída; preserve a conferência temporal abaixo.

Em revisão, examine o vídeo entregue, a timeline e o código quando existir. Registre problemas com intervalos de tempo e causa observável. Separe defeito de conexão/layout, problema de atenção/ritmo e preferência estética. Um frame isolado não comprova fluidez.

Para cada passagem relevante, identifique:

- Qual entidade o espectador está acompanhando: pedido, cliente, resposta, ferramenta, pessoa ou resultado.
- A origem, o destino e a consequência da ação. Uma resposta deve chegar antes de o estado mudar para recebido.
- O que permanece e o que realmente precisa mudar na próxima composição.
- O foco principal e a janela de leitura. Informação secundária pode esperar.

Se a voz ainda não existir, use marcações provisórias explícitas. Preserve os espaços de câmera; não invente sincronização com gravação ausente. Leia a direção visual existente antes de escolher cores e fontes. Preferências de uma marca não viram regra global desta skill.

## Continuidade e composição

Quando duas cenas continuam a mesma explicação, prefira manter a entidade e transformar sua posição, escala ou função. Abrir o diagrama para tela inteira deve preservar nós, caminhos e estado. Cortes diretos também são válidos quando marcam uma mudança editorial real; não precisam de uma vinheta para justificá-los.

Conexões pertencem aos objetos: derive portas e trajetórias das mesmas coordenadas usadas para os nós. Faça a linha acompanhar a transformação do conjunto, chegar à borda correta e ficar na camada adequada. Se uma linha desaparecer ou surgir, sua origem/destino deve continuar claro. Uma faixa luminosa solta não substitui uma ligação.

O resultado deve nascer do processo visível: por exemplo, seleção vira ferramenta e execução vira resposta. Evite trocar todo o quadro por outro conjunto de cards quando o assunto ainda é o mesmo.

## Coreografia

Escolha o movimento pelo papel do objeto. Use trajetórias estáveis para dados, acomodação curta para componentes e pausas para títulos e conclusões. Pode haver antecipação ou sobreposição discreta quando ajudar a perceber causa e efeito.

Varie o ritmo com intenção, sem repetir a mesma entrada vertical e o mesmo atraso em todos os elementos. Início, viagem, chegada e leitura são momentos distintos. O movimento pode parar depois de cumprir sua função.

Evite teletransporte de palavras, reset de progresso e laços que saltam da ponta ao início. Em um ciclo necessário, torne o retorno legível ou esconda a emenda de modo intencional. Oscilações e brilhos contínuos precisam de função editorial.

Reserve uma área estável para texto e resultados. Não comprima linhas legíveis para fazer um documento aparecer: faça a transição no mesmo espaço ou transforme um invólucro, preservando a leitura do conteúdo. Não desloque o restante da cena por reflow acidental.

Em vídeo com apresentador, proteja rosto e gestos; use sobreposições abaixo ou ao lado conforme o enquadramento real. Nos espaços provisórios, mantenha a função de cada área clara. A gravação é que confirma corte, ênfase e tempo final.

## Implementação

Ao trabalhar com Remotion ou outro motor por código, leia [references/motion-code.md](references/motion-code.md). Não imponha Remotion a uma montagem que já tenha outro fluxo válido.

Preserve a versão anterior quando fizer uma revisão material. Primeiro corrija o trecho que evidencia o problema; depois propague o princípio aos demais trechos afetados. Mídia gerada pode fornecer assets, mas não corrige uma timeline desconexa por si só.

## Conferência temporal

Revise os intervalos afetados em movimento, quando houver reprodução disponível, e também em amostras próximas às mudanças. Inclua antes/durante/depois de transições, trocas de texto, chegada de dados e mudanças de layout. Um storyboard de cenas prontas é insuficiente.

O helper [scripts/sample_motion.py](scripts/sample_motion.py) extrai uma sequência temporal com rótulos de tempo a partir de um vídeo já renderizado. Leia [references/review-rubric.md](references/review-rubric.md) para calibrar os critérios de revisão e a evidência mínima por tipo de alteração.

Confira em tamanho próximo ao celular: legibilidade, limites do quadro, portas conectadas, hierarquia e tempo de leitura. Verifique exportação, frames/duração e decodificação. No fluxo por código, valide também mudanças de estado e determinismo.

Entregue uma prévia revisada e um diagnóstico curto: onde quebrava, o que mudou e o que ainda depende da gravação. Diferencie revisão por amostras de reprodução integral com áudio. Não declare percepção humana, sincronização ou audição que não tenha ocorrido.

Depois de aprovação real de um estilo, atualize o guia existente ou crie `GUIA_<ESTILO>.md` junto ao projeto, com vídeo/código de referência, parâmetros medidos ou aprovados, feedback → regra e valores “a confirmar”. Leia-o diretamente nas próximas edições. Registre tempo e refações quando disponíveis; custos e tokens somente com dados atribuíveis, sem transformar percentual de assinatura em gasto faturado. Não imponha respiros removidos, zoom constante ou movimento contínuo como estilo universal.
