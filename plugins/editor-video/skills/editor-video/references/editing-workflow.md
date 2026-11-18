# Procedimento de edição

Aplique estas decisões conforme a operação solicitada. Continue revisões do mesmo vídeo; para vídeos independentes, prefira contexto separado com fontes e guia explícitos, sem criar chats automaticamente.

## Preparar

Leia o guia de estilo aprovado do projeto, quando existir, e reúna bruto, assets e pedido antes de montar. Confira metadados, áudio, sincronismo e decodificação do bruto com ferramentas locais disponíveis; use amostras proporcionais e investigue falhas encontradas. Texto ausente na transcrição pode ser voz baixa ou falha de microfone, não silêncio removível. Não diga que conferiu áudio apenas por ler metadados.

Escolha o motor pela operação: código para motion, áudio/texto para cortes, integração nativa para efeitos e entrega manual editável, geração para transformar conteúdo visual. Preserve o fluxo de provedores de `generation.md`. Não reinstale bibliotecas já disponíveis. Transcrição, tracking e segmentação exigem ferramentas concretas; estes procedimentos não acrescentam essas capacidades ao editor.

## Montar e revisar

Para cortes por fala, reutilize transcrição com timestamps e plano de cortes quando disponíveis. Preserve palavras baixas, negações e atribuições. Em retakes ambíguos, examine os segmentos/ilhas de fala; escolher sempre a última tomada e remover todos os respiros dependem de estilo aprovado. Confira ataques e finais no áudio.

Estabilize cortes antes de legendas e processamento caro. Legendas usam o tempo da saída final; mudança de corte invalida alinhamentos afetados, inclusive inserts e áudio. Limite máscaras aos trechos e regiões que exigem oclusão. Reutilize tracking/matte enquanto fonte e parâmetros forem compatíveis; invalide quando mudarem. Não copie limiares de outro microfone ou enquadramento.

Agrupe alterações conhecidas sem ignorar dependências e revisões. Registre versão, intervalo, objeto e resultado esperado; distinga tempo do bruto e da saída. Localize falas pela transcrição antes de buscar visualmente. Faça prévia leve para decisão de composição e trecho animado para decisão de movimento. Uma correção pequena ainda requer conferência proporcional; não substitua check/snapshot por mera leitura do código.

## Reutilizar e entregar

Quando o usuário aprovar um estilo, crie ou atualize `GUIA_<ESTILO>.md` no projeto, vinculando vídeo aprovado, código/componentes e comando de render. Registre somente parâmetros medidos ou aprovados (formato, fontes, cores, margens, ritmo, camadas, legendas, som e zona do rosto), feedback → regra e valores “a confirmar”. Não crie guia novo se o existente já cobre o estilo; não confunda prévia entregue com aprovação. Nos próximos pedidos, leia esse guia diretamente.

Registre tempo decorrido e etapas relevantes, duração bruta/final e refações quando houver dados. Tokens/cache e gasto de provedores só com telemetria atribuível e preço identificado; caso contrário informe “não medido”. Não converta porcentagem do limite semanal em custo faturado nem invente tokens. Render/transcrição locais consomem máquina e tempo; a orquestração ainda pode consumir tokens.

Preserve o modelo escolhido; não troque modelo/esforço automaticamente. Guia pronto pode reduzir trabalho de planejamento, mas não garante economia fixa. Não adote o estilo visual do autor da referência como preferência do usuário.
