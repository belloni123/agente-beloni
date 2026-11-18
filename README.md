# Agente Beloni

Coleção de plugins e skills de Felipe Belloni para usar com o Codex e adaptar aos seus fluxos de trabalho.

**[Baixar o pacote ZIP](https://github.com/belloni123/agente-beloni/releases/latest/download/agente-beloni.zip)**

| Skill | Uso |
| --- | --- |
| [After Effects](skills/after-effects/) | Composição, títulos, expressões, JSX e MOGRT |
| [B16 Immersive Frontend](skills/b16-immersive-frontend/) | Interfaces com movimento, interação e 3D |
| [CopyMoney Copywriter](skills/copymoney-copywriter/) | Copy para campanhas, páginas e conteúdo |
| [EffectCraft](skills/effectcraft/) | Composições, keyframes, efeitos e render no EffectCraft |
| [Motion Editorial](skills/motion-editorial/) | Motion graphics explicativos, ritmo e revisão |
| [Perguntas da Semana](skills/perguntas-da-semana/) | FAQ, post e roteiro a partir de perguntas do público |
| [Pridias](skills/pridias/) | Inventário e seleção de skills disponíveis |
| [Resolve AI Editing](skills/resolve-ai-editing/) | Edição no DaVinci Resolve via Resolve AI Bridge |
| [Resumo da Manhã](skills/resumo-da-manha/) | Boletim de IA com fontes e aplicação prática |
| [Vídeo em 3 Posts](skills/video-em-3-posts/) | Rascunhos para LinkedIn, Instagram e X |
| [Zé Marreta Vendedor](skills/ze-marreta-vendedor/) | Diagnóstico e condução de vendas high ticket |

## Plugins do Codex

| Plugin | Uso e dependências |
| --- | --- |
| [Bell Dev OS](plugins/bell-dev-os/) | Planejamento, implementação e revisão de projetos de software |
| [IMOB ADV](plugins/imob-adv/) | Fluxos e referências para direito imobiliário |
| [Editor de Vídeo](plugins/editor-video/) | Edição via MCP em uma instalação do Editor de Vídeo local |

Cada pasta em `plugins/` é um plugin separado com seu manifesto. A skill de cada plugin também pode ser usada separadamente, copiando sua pasta de `skills/` dentro do plugin.

O plugin Editor de Vídeo exige Node.js e o Editor de Vídeo local instalado. Configure a variável `EDITOR_VIDEO_ROOT` para o caminho absoluto da instalação que contém `scripts/mcp.mjs`. A variável precisa estar disponível ao processo do servidor MCP. EffectCraft e Resolve AI Editing dependem de seus respectivos editores e conexões locais.

## Como usar as skills

1. Baixe e extraia o ZIP.
2. Copie a pasta da skill desejada, com seu `SKILL.md` e as referências, para `~/.agents/skills/` ou para `.agents/skills/` no seu projeto.
3. Se já houver uma skill com o mesmo nome, compare as versões antes de substituir. Abra uma nova sessão e invoque a skill pelo nome.

As três skills de conteúdo BellOS usam uma estrutura local em `~/cofre`. Ajuste os caminhos descritos no `SKILL.md` para seus arquivos e forneça as fontes da tarefa. Para Vídeo em 3 Posts, você pode fornecer a transcrição diretamente.

## Fontes e créditos

- [B16 Immersive Frontend](https://github.com/belloni123/b16-immersive-frontend)
- [CopyMoney Skills](https://github.com/belloni123/copymoney-skills)
- [Zé Marreta Vendedor](https://github.com/belloni123/ze-marreta-vendedor) e seus [créditos](credits/ze-marreta-vendedor.md)
- Pridias e as três skills de conteúdo vêm da coleção local de Felipe Belloni.

- [IMOB ADV](https://github.com/belloni123/imob-adv)

Os direitos dos materiais de terceiros permanecem com seus titulares.
