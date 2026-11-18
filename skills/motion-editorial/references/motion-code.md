# Continuidade em motion por código

Use apenas as partes relevantes ao motor do projeto.

## Tempo e identidade

- Derive a animação do frame/tempo da composição. Em Remotion, useCurrentFrame + fps e funções determinísticas. Não dependa de timers, animação CSS/SVG autônoma ou aleatoriedade sem semente.
- Compartilhe um relógio para uma explicação que atravessa vários cortes. Recriar o componente com frame zero pode reiniciar pacote, progresso, fundo e estado de ferramenta.
- Se o diagrama se expande mantendo o assunto, prefira uma única instância com parâmetros interpolados. Não remonte um grafo parecido com IDs/estado novos.
- Um token pode fazer ida, chegada, retorno e repouso em intervalos explícitos. Não use `% duração` por conveniência quando o reset puder ser visto.

## Geometria

Defina cada nó com x, y, largura e altura. Portas derivam desses dados: saída direita = x + largura, centro vertical = y + altura/2. Use esses mesmos dados para DOM e SVG. Se o conjunto inteiro muda de escala, transforme também os conectores no mesmo grupo.

Uma linha de progresso pode crescer no caminho. Um pacote pode percorrer ida e volta nesse mesmo caminho; no retorno, inverta o parâmetro de percurso. O estado recebido só muda depois da chegada. Não use uma curva aproximada diferente para o círculo e outra para a linha.

Considere stroke, escala e ordem de pintura: caminho atrás dos nós, pacote visível no espaço livre, endpoint na borda. Uma linha ornamental pode ser livre, mas não deve parecer uma ligação funcional sem destino.

## Layout e texto

- Em trocas entre código e documento, aloque uma viewport estável. Interpole opacity/transform dos conteúdos; preserve altura do painel, portas e status.
- Não anime maxHeight de cada linha de código se o resultado for texto cortado e saltos dos elementos abaixo.
- Troque frases no mesmo invólucro, com entrada/saída coordenadas e altura que comporte ambas. Evite uma condição binária que teletransporte palavras.
- Reflow pode ser intencional, mas precisa ser coreografado, e não um efeito colateral do estado.

## Transições

Uma faixa decorativa fina não esconde a descontinuidade de toda a cena. Escolha entre transformação da entidade, corte editorial ou transição real com origem e destino presentes.

Em uma dissolvência, mantenha a cena anterior durante a entrada da próxima. Se houver vídeo com duração limitada, não leia frames além do take: segure o último quadro para a cauda, quando adequado. Garanta que a camada nova cubra o quadro durante o blend, para não sobrar texto da anterior em áreas transparentes. Marca fixa deve manter posição e relógio.

Preserve timings aprovados e alinhe o relógio da trilha. Uma mudança de duração exige atualizar também áudio, legendas, clips e exportações; não retime silenciosamente a fala do usuário.

## Escala do movimento

Não há um valor de easing universal. Para motion explicativo, entradas curtas com acomodação suave e leitura parada costumam ajudar. Use springs quando houver uma razão material para elasticidade. Eventos de dados geralmente precisam de direção e chegada claras, não de bounce.

Uma pausa legível é uma escolha de movimento. Depois de completar uma cadeia, considere mantê-la concluída em vez de continuar emitindo pacotes decorativos.
