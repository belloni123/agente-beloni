# Geração de vídeo: Magnific primeiro, fal como alternativa

A ferramenta `editor_video` persiste pedidos, recibos e resultados no editor. Ela NÃO chama ferramentas de outro plugin por conta própria: o Codex orquestra os plugins conectados abaixo. Nunca diga que a geração começou apenas porque preparou um pedido.

## Preparar e retomar

1. Liste projetos e abra o escolhido. `editor_video {projectId,action:"list"}` lista pedidos e a política. Continue o ID indicado pelo usuário; não gere de novo um pedido existente.
2. Se necessário prepare: `action:"prepare",input:{key:"UUID gerado uma vez",prompt:"plano",duration:5,start:0,track:0,resolution:"1080p",includeAudio:false}`. De 4 a 30 segundos inteiros, dentro da duração do projeto; formato deriva do projeto. Reutilize a key apenas para recuperar o mesmo pedido com os mesmos parâmetros.
3. Observe status/attempts. `submitting`, `running` e `uncertain` exigem recuperar a tentativa, NÃO uma nova geração. `imported` já tem arquivo local. `ready` só precisa de download/importação. Nunca substitua o vídeo existente por uma nova geração sem pedido do usuário.

## Magnific (primeiro)

1. Leia as skills `magnific-essentials` e `cinematic-shots` e suas referências de prompt; use ferramentas Magnific disponíveis. Consulte `video_models_list` com search `bytedance-seedance-pro-2.5`: catálogo consultado em 13/11/2026 o marca sota/rank 1. Use esse slug para qualidade final, respeitando disponibilidade e campos atuais. Não use modelos privados.
2. Defina o destino pela pasta Magnific escolhida pelo usuário ou `account_defaults_get`. Passe folderReference a cada geração. Não invente referência. Um default `ask` exige a escolha; não troque de provedor para contornar essa preferência.
3. Construa os argumentos exatos `video_generate`: `{slug,prompt,duration,aspectRatio,resolution,folderReference}`. Configure áudio conforme pedido, usando apenas campos suportados. `includeAudio` do editor define a inserção, não garante que o modelo gere ou omita áudio. Sem pedido de trilha, prefira `noMusic:true` para ambiente se o modelo suportar. Não passe fps não suportado. Imagens de referência exigem URLs/identificadores válidos do provedor e contrato atual; não invente assets.
4. Consulte `simulate_cost` com os argumentos exatos antes do gasto e siga limites/preferências do usuário e a skill Magnific. Uma integração instalada não autoriza testes pagos arbitrários. Sem orçamento, acima de aproximadamente 1.000 créditos, a skill Magnific exige informar o plano/preço e esperar a concordância antes de gastar; cite a regra se precisar perguntar. Não use fal para contornar orçamento ou aprovação.
5. Antes da chamada paga salve `action:"update",input:{id,operation:"begin",model:"bytedance-seedance-pro-2.5",arguments:{...argumentos exatos}}`. A tentativa fica `submitting`; existe uma submissionKey de recuperação local, mas Magnific não oferece idempotência por essa chave. Faça UMA chamada `video_generate`.
6. Assim que retornar identifier, registre `operation:"receipt",externalId:"identifier"`. Se o modelo real divergir, registre também actualModel com o slug retornado pelo provedor, informe o usuário e não anuncie o modelo pedido se não foi utilizado.
7. Aguarde o MESMO identifier com `creations_wait`, repetindo long-polls (até 25 segundos por chamada) conforme poll_after_seconds. Lentidão/timeout não é falha terminal. Se a resposta de submit se perder, procure a criação no projeto/provedor; sem certeza registre `failure kind:"unknown"` e recupere, sem outro submit e sem fallback. O recibo pode retomar `uncertain`.
8. Ao completar, leia `creations_get` e use a URL integral do vídeo (`url`), nunca webUrl/thumbnail. Revise com as ferramentas de visualização do provedor. Antes de gravar o arquivo local chame `creations_register_download` com os identificadores, conforme a skill Magnific. Depois registre `operation:"complete",url:"URL HTTPS retornada",downloadRegistered:true`. Só marque true após esse registro realmente passar.

## Fal somente após falha confirmada

- Magnific indisponível/não conectado/modelo incompatível: `operation:"failure",kind:"unavailable",message:"motivo concreto"`.
- Bloqueio de créditos/plano: kind `billing`; fal só dentro do orçamento autorizado, sem comprar créditos nem trocar contas.
- Erro terminal de execução: kind `terminal`, depois de verificar a criação original. Não classifique timeout, fila ou resposta perdida como falha terminal.
- Recusa de conteúdo/política: kind `policy`; não use outro provedor para contornar a recusa. Estado incerto: kind `unknown`; nunca faça fallback.
- Para as três falhas elegíveis, registre `operation:"fallback"`. Isso muda provider para fal e mantém a falha/tentativa Magnific no histórico. Não faça fallback se o resultado Magnific já estiver pronto/importado.
- Leia `fal-media` e `model-routing`. Chame `recommend_model` para o pedido REAL com duração, proporção, resolução e áudio; preserve requisitos, não reduza resolução/duração silenciosamente. Em 13/11/2026 a recomendação para vídeo genérico até 15 s a 768P foi `minimax/h3-max/text-to-video`; não o force para um pedido de 1080p ou 30 s. Copie endpoint e input_contract da resposta atual. Confira preço/orçamento.
- Salve `begin` com model endpoint e argumentos exatos antes de `submit_job`. Use a submissionKey persistida como submission_key: se o journal não estiver disponível e bloquear a chamada antes de cobrar, não remova a chave silenciosamente. Preserve recibos/erros e reporte. Após submit salve receipt com request_id, statusUrl e responseUrl retornados.
- Chame check_job no MESMO request_id até COMPLETED; use get_job_result somente se não veio resultado. Registre complete com URL `video.url` real. Não exige downloadRegistered para fal. Billing block: informe e pare, sem retries automáticos pagos.

## Importar e montar

1. `editor_video {projectId,action:"import",input:{id}}` baixa a URL registrada, limita 256 MB, valida com FFprobe e adiciona à biblioteca. É idempotente: repetir não importa outra cópia. A timeline fica como estava.
2. Se o usuário pediu montagem, releia o estado do projeto e use `action:"place",input:{id,revision:"revisão atual"}`. O mesmo clipe não entra duas vezes. Em 409 releia e reconcilie. A posição/faixa/duração vêm do pedido; os limites da mídia real são respeitados.
3. Inserção participa do histórico do Studio: undo remove da timeline, redo restaura; o arquivo e a proveniência continuam na biblioteca. O clipe aceita edição manual no Studio e via fontes HTML. Nunca reescreva a montagem inteira ao chegar um resultado.
4. Depois de montar rode check/snapshot, olhe os frames, e renderize se solicitado. Mostre endpoint/modelo, provedor utilizado, custo conhecido e limites reais. Não anuncie teste pago de ponta a ponta se só validou a importação com fixture local.
