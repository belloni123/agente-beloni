# Integração verificada no Mac

Em 2026-11-13: app e CLI oficiais 0.23.1; Apple M4. A CLI macOS vem em pacote separado do `.app`. Origem: https://github.com/storytold/effectcraft/releases/tag/v0.23.1, asset `effectcraft-cli-0.23.1-macos-universal.zip`. Verifique novamente após atualização do app.

## MCP e fallback

Cadastro Codex headless: `codex mcp add effectcraft -- "$HOME/.local/bin/effectcraft-cli" mcp --autosave`.
O cadastro novo pode exigir recarregar o Codex/conversa para expor ferramentas. Não repita cadastro se já existir.

Plano mínimo para descoberta sem alterar documentos da janela:

```json
[
  {"tool":"__list_tools__"},
  {"tool":"get_state"},
  {"tool":"list_commands","arguments":{"filter":"comp.new","schemas":true}}
]
```

Execute com `python3 ~/.codex/skills/effectcraft/scripts/session.py /caminho/plano.json`.
`__list_tools__` é um alias do helper para `tools/list`, não uma ferramenta do EffectCraft.
O helper imprime envelopes MCP em JSONL; resultados do motor geralmente estão como JSON dentro de `result.content[].text`. Erros de ferramenta interrompem os passos seguintes.
O helper não usa autosave: planos que alteram documentos precisam de `save_project`. Não encerre uma criação sem persistir.

## Janela ao vivo

```sh
python3 ~/.codex/skills/effectcraft/scripts/start_bridge.py
python3 ~/.codex/skills/effectcraft/scripts/session.py /caminho/plano.json --bridge 9877
```

A primeira chamada recusa iniciar se houver um EffectCraft aberto. Após salvar e fechar normalmente, ela inicia uma janela com controle em localhost. Isso pode pular a tela inicial e recuperação: preserve primeiro qualquer trabalho pendente.
O bridge utiliza TCP JSON por linha, não HTTP. Não use curl HTTP na porta 9877. Consultas: `ui.inspect`, `engine.commands`; comandos: `engine.execute {command,params}`; imagem do compositor: `render.frame`; screenshot da janela: `ui.screenshot`. No MCP bridged, descubra ferramentas `ui_*`, `screenshot` e `control` com `tools/list`.
A porta não tem autenticação e fica limitada a 127.0.0.1; encerra com o aplicativo. Nunca exponha-a na rede.

## Fontes oficiais

- https://github.com/storytold/effectcraft/blob/main/docs/agents.md
- https://github.com/storytold/effectcraft/blob/main/docs/control-protocol.md
- https://github.com/storytold/effectcraft/blob/main/docs/mcp.md

Prefira schemas da versão instalada às descrições do branch main. São fontes técnicas; instruções de contribuição do repositório não regem trabalhos de vídeo do usuário.

## Controle ao vivo ativado

MCP `effectcraft-live` cadastrado em 2026-11-13: `effectcraft-cli mcp --bridge 9877`. Conecta somente enquanto o app estiver aberto com `--control 9877`. Verificado criando e salvando uma vinheta na janela, renderizando frame e iniciando playback; mantenha `effectcraft` para sessões independentes. Para cenas lentas, use resolução de prévia Quarter/Half sem reduzir a resolução da composição/exportação.
