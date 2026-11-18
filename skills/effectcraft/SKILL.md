---
name: effectcraft
description: Crie e edite motion graphics no EffectCraft do Mac por MCP nativo, CLI ou controle da janela. Use para títulos animados, vinhetas, lower thirds, keyframes, efeitos, composições editáveis e renders solicitados nesse aplicativo.
---

# EffectCraft

Entregue motion editável em `.ecproj`, com assets identificáveis e render no formato solicitado. Preserve textos, marca e direção visual do pedido. EffectCraft tem motor próprio: compatibilidade com After Effects é parcial; não suponha importação de `.aep`, plugins ou presets Adobe.

## Acesso

- No Mac configurado, o app está em `/Applications/EffectCraft.app` e a CLI oficial em `~/.local/bin/effectcraft-cli`. Confirme a versão com `get_state` e a sintaxe com `--help`. A referência local é [references/integration.md](references/integration.md).
- Prefira as ferramentas MCP `effectcraft` quando oferecidas. O servidor cadastrado é **headless**: seu estado é independente da janela aberta. Salve explicitamente antes de terminar ou trocar de projeto.
- Se o MCP não estiver carregado na conversa, use [scripts/session.py](scripts/session.py): executa um plano JSON de chamadas na mesma sessão MCP, preservando estado entre passos. Cada execução cria uma sessão nova, portanto inclua `open_project` ao continuar um arquivo e `save_project` após alterações. Uma falha interrompe o plano; não há rollback do plano inteiro. Os argumentos não interpolam resultados: use IDs descobertos, nomes únicos ou `batch` nativo com referências documentadas.
- Para editar a janela ao vivo, use o canal TCP local de uma instância iniciada com `--control 9877`; a CLI aceita `mcp --bridge 9877`. [scripts/start_bridge.py](scripts/start_bridge.py) abre o app controlável somente se nenhum EffectCraft estiver rodando. Se a janela atual não tiver controle, preserve-a: salve o trabalho e feche normalmente antes de reabrir. Não mate processos nem descarte recuperação/alterações. O script não reinicia a sessão atual.
- `session.py plano.json --bridge 9877` dirige a sessão visível. Verifique identidade e estado com `ui_inspect`/`get_project` antes de editar. Headless não comprova que algo foi aberto na janela.

## Trabalho de motion

1. Extraia duração, proporção, FPS, destino, textos, assets e referências. Leia o guia de estilo aprovado do projeto, se existir, e reúna as alterações conhecidas antes de montar. Se houver gravação, confira metadados, áudio e sincronismo com evidência proporcional antes de investir na composição; lacuna na transcrição não comprova silêncio. Resolva escolhas comuns pelo contexto, declarando as suposições relevantes. Não imponha uma estética ou formato universal.
2. Descubra os schemas instalados com `list_commands`/`describe_command`, ferramentas com `tools/list`, efeitos com `list_effects` e fontes com `list_fonts`. Use os IDs retornados: nomes, parâmetros e versões da documentação online podem divergir.
3. Organize composições e camadas por função; mantenha textos vivos, formas e assets separados. Inspecione `get_comp` e `get_layer` antes de modificar propriedades; use seus caminhos reais. Reutilize composições e animações aprovadas para variações de texto/asset. Estabilize cortes antes de alinhar legendas e executar tracking/máscaras caros, quando suportados. Mudanças de corte exigem recalcular alinhamentos afetados na saída. Limite máscaras aos intervalos/regiões necessários e reaproveite tracking/matte somente enquanto fonte e parâmetros forem compatíveis.
4. Construa keyframes com aceleração/desaceleração adequada ao movimento, hierarquia temporal e leitura dos títulos. Especifique `timeBase: "comp"` quando os tempos se referirem à timeline: o padrão é tempo da camada, que muda com offset/stretch. Use `batch` atômico para conjuntos de comandos compatíveis ou `run_script` para construção procedural após conferir a API suportada.
5. Salve uma nova versão ao editar um original, salvo substituição pedida. Inclua o salvamento no mesmo plano headless que cria a composição. Não substitua o projeto atual da janela antes de preservar mudanças existentes.
6. Renderize frames no começo, durante movimentos, no pico de leitura e no final. Veja as imagens e confira acentos, alinhamento, recortes, contraste, composição e alpha. Confirme a animação com uma prévia em vídeo quando o movimento importar. Use resolução reduzida para decisões de composição e trechos curtos para movimento; confirme detalhes de texto/alpha na resolução final quando necessário. Em revisão, identifique versão, composição/camada, intervalo e resultado esperado; distinga tempo da composição, da camada e do bruto. Confira também as fronteiras alteradas, mesmo em ajustes pequenos.
7. Consulte schemas de `renderQueue.*` ou `effectcraft-cli render --help`/ajuda geral antes de exportar. Escolha codec, resolução, áudio e alpha conforme o destino; H.264 não preserva transparência. Templates e Lottie requerem verificação de suporte aos efeitos usados.
8. Reabra o `.ecproj` salvo em sessão isolada e confira composição, camadas, textos e keyframes. Verifique duração, FPS, dimensões e render final. Entregue links absolutos para a matriz, render e assets necessários, com uma descrição curta da editabilidade.

Em timeout ou desconexão de uma mutação, o resultado é desconhecido: inspecione antes de repetir. Para renders longos no canal de controle, prefira fila sem espera e consultas de estado conforme o schema instalado; o transporte do app tem limite de espera.

## Estilo reutilizável e métricas

Após aprovação real do usuário, atualize o guia de estilo existente ou crie `GUIA_<ESTILO>.md` junto ao projeto. Vincule o `.ecproj`, render aprovado, assets e procedimento de exportação; registre parâmetros medidos/aprovados (fontes, cores, margens, timings, curvas, camadas, legendas, som e área do apresentador), feedback → regra e valores “a confirmar”. Não confunda prévia entregue com aprovação nem transforme o estilo de uma referência em preferência global. Leia esse guia nas próximas edições, sem depender de localizar chats antigos.

Registre tempo e refações quando disponíveis. Tokens/cache e custos de provedores exigem telemetria atribuível e preço identificado; sem dados, informe “não medido”. Não converta percentual de assinatura em gasto faturado. Render local consome máquina e tempo; chamadas de orquestração ainda podem consumir tokens. Estas instruções não acrescentam ao EffectCraft recursos que seus schemas não ofereçam.
