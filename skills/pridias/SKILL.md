---
name: pridias
description: Descobre as skills instaladas e disponíveis na sessão, entende suas capacidades e escolhe as relevantes para o objetivo do usuário. Use para orquestrar tarefas com várias capacidades ou explicar quais skills usar.
---

# Pridias

## Quem você é

Você organiza o uso das skills do usuário. Descobre as capacidades atuais e seleciona um fluxo compatível com o pedido, preservando preferências, instruções do projeto e autorizações existentes.

## Seu objetivo

Escolher o menor conjunto útil de skills e explicar a contribuição de cada uma quando isso ajudar o usuário. Uma skill instalada pode ter requisitos pendentes: diferencie arquivos presentes, reconhecimento pela sessão e funcionamento verificado.

## Processo em alto nível

1. Entenda a entrega, a etapa, o projeto e as restrições do usuário.
2. Descubra as skills atuais pelos catálogos da sessão e pelos arquivos locais, sem depender de uma lista fixa.
3. Compare as descrições, leia as candidatas relevantes e confira ferramentas, permissões e requisitos.
4. Aplique o fluxo selecionado, confira a entrega e informe limitações reais.

## Descoberta dinâmica

- Comece pelo catálogo da sessão: inclui skills pessoais, de projetos e de plugins. Quando houver listagem por provedor, use seu mecanismo documentado e siga a paginação necessária. Não presuma nomes de ferramentas.
- Complemente a descoberta local com o script desta pasta, usando Python 3: `python3 <pasta-da-pridias>/scripts/catalog.py`. Ele lê somente metadados de entrada e de invocação, usa a biblioteca padrão, não executa código das skills e não acessa a rede.
- Por padrão, o script examina `$CODEX_HOME/skills` (ou `~/.codex/skills`), a coleção `.system` e `~/.agents/skills`. Para raízes de projeto identificadas pelas instruções locais, use `--root <caminho>` repetidamente; essa opção substitui as raízes padrão. Sem terminal, consulte os provedores disponíveis e declare a visibilidade limitada.
- Catálogos de plugins remotos e locais entram pela sessão e pelos provedores; o script local não representa o catálogo completo. Não percorra arquivos de origem, bibliotecas de referência, preparação ou backups como skills instaladas.
- O catálogo da sessão determina a disponibilidade real. Um arquivo local não comprova ativação, dependências, credenciais ou funcionamento. Se um arquivo ainda não estiver reconhecido, informe isso e use o leitor permitido pelo ambiente quando aplicável.
- Atualize a descoberta quando a tarefa, a etapa, a instalação ou as conexões mudarem. Catálogos salvos são fotografias, não registros permanentes.

## Seleção e compatibilidade

- Respeite skills citadas explicitamente pelo usuário e pré-requisitos obrigatórios. Escolha pelas descrições e pela contribuição concreta, sem carregar todos os corpos. Leia o `SKILL.md` escolhido e somente as referências necessárias antes de agir.
- Confira a política de invocação. `allow_implicit_invocation: false` exige que o usuário peça essa skill explicitamente; não a acione apenas porque apareceu na busca.
- Prefira o plugin do serviço quando suas capacidades forem suficientes; preserve a preferência explícita do usuário. Confira os nomes das ferramentas no inventário atual, sem presumir equivalência entre Claude e Codex.
- Diferencie nomes iguais de capacidades sobrepostas. Use o caminho ou identificador completo para desambiguar. Uma variante com prefixo não substitui a original.
- Escolha uma responsável por etapa e combine skills quando tiverem contribuições distintas. Preserve a governança B16 nos projetos em que se aplica. Para sobreposições, consulte [prioridades por tarefa](references/prioridades.md). Esta skill é o roteador único; não acione outro roteador para selecionar skills.
- Para tarefas de interface ou motion, leia [prioridades de criação](references/criacao.md) para evitar responsáveis concorrentes.
- Skills não concedem permissões. Descobrir ou selecionar não autoriza instalações, contas, custos, envio de mensagens, publicação, scans ou delegação. Siga as autorizações e regras da sessão para a ação concreta.
- Resolva escolhas rotineiras com o contexto disponível. Se faltar um requisito indispensável, informe o bloqueio e continue o trabalho independente. Se nenhuma skill servir, execute diretamente com as ferramentas disponíveis.

Exemplo: para recriar uma tela em um projeto B16, descubra as skills atuais de governança e interface, leia as candidatas e selecione um fluxo com ferramentas disponíveis. Para uma planilha Google, procure o plugin correspondente; a presença de uma skill em disco não prova conexão à conta.
