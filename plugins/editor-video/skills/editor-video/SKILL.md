---
name: editor-video
description: Use para criar, abrir, editar, revisar e exportar vídeos no Editor de Vídeo local pelo Codex.
---

# Editor de Vídeo
Em toda criação ou revisão, leia [references/editing-workflow.md](references/editing-workflow.md): preparação do bruto, guia aprovado, cortes/legendas, reaproveitamento de processamento e métricas verificáveis. Aplique apenas as etapas pertinentes; não trate instruções como capacidades implementadas.
Use editor_help primeiro para descobrir contratos. O servidor inicia o editor automaticamente. URL: http://127.0.0.1:3110.
Liste projetos antes de criar outro quando a intenção for continuar um existente. Leia estado e fontes para entender a timeline HTML. Preserve intervenções manuais e use revision retornada; em conflito releia e reconcilie.
Use editor_import para mídias solicitadas pelo usuário; depois add-media. Use rotas de legendas, áudio e relink para operações específicas. Para edição ampla (cenas, cortes, animação, texto, aparência), leia sources e salve source: só arquivos de composição existentes, pelo histórico compartilhado com o Studio. Crie cenas dentro dessas composições. Não modifique os manifests diretamente.
Siga o contrato HyperFrames: timed elements com data-start/data-duration, timeline GSAP pausada registrada em window.__timelines, seek determinístico. Depois de mudar HTML use produce check e snapshot e inspecione as imagens antes de concluir. Produza render quando solicitado. Não anuncie sucesso se check ou render falhar. Undo/redo pela rota history.
Astra dirige e edita código. Para gerar footage use o fluxo completo em [references/generation.md](references/generation.md): Magnific PRIMEIRO, Seedance 2.5 como padrão de qualidade; fal SOMENTE após falha confirmada elegível. Use editor_video para persistir pedidos, tentativas, recibos, resultados e inserção com histórico. As chamadas pagas são feitas pelo Codex nas ferramentas do provedor conectado. Nunca afirme geração iniciada sem recibo nem repita submit incerto. Não afirme que um storyboard proposto já foi materializado. Não publique projetos automaticamente.
