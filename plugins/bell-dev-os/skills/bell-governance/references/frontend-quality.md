# Qualidade frontend

Use estas diretrizes em produtos com interface. Preserve requisitos mais específicos do usuário e os padrões válidos do projeto.

## Direção antes da expansão

- Comece pelo conteúdo real, usuário e tarefa principal. Reúna referências concretas e extraia delas critérios observáveis, sem copiar identidade alheia.
- Defina personalidade visual própria para o projeto. Evite a combinação automática de gradientes, cards translúcidos, brilho e texto genérico que produz uma aparência intercambiável de “IA”.
- Em projeto novo ou mudança visual ampla, implemente e alinhe um recorte representativo antes da página inteira. Normalmente será o hero ou fluxo principal. Não imponha essa aprovação a ajustes triviais nem contrarie um fluxo explícito do usuário.
- Escreva copy humana, direta e tecnicamente correta. Não use travessão como vício estilístico.

## Composição e interação

- Projete mobile-first e amplie de forma coerente para telas maiores. Priorize toque, alvos adequados, foco visível por teclado e estados `focus`, `active` e selecionado acessíveis. Não use hover, inclusive como efeito decorativo, salvo pedido explícito do usuário para aquele projeto; mesmo nessa exceção, nenhuma ação ou informação pode depender dele.
- Tipografia serifada, contraste entre famílias e palavras partidas no hero não são receitas automáticas. Escolha tipografia e hierarquia pelo conteúdo, marca, idioma, legibilidade e desempenho; não imponha uma única fonte a todos os projetos.
- Use ícones reais de bibliotecas confiáveis e adequadas ao projeto. Não improvise glifos, emojis, desenhos CSS ou substitutos inventados. Escolha uma família principal coerente e leia [seleção de ícones](icon-selection.md) ao definir ou revisar iconografia. Para marcas, como WhatsApp, use asset oficial ou fonte autorizada e respeite licença e diretrizes da marca.
- Motion, 3D, entradas e saídas podem fortalecer sobretudo o hero quando explicam, orientam ou expressam a identidade. Defina propósito, fallback mobile, comportamento com `prefers-reduced-motion`, acessibilidade e orçamento de CPU, GPU, rede e bundle. Não adote framework pesado apenas por disponibilidade.
- Termos ambíguos, como “dragons, 3DS”, exigem confirmação pelo contexto; não inferir uma biblioteca específica.

## Implementação e evidência

- Reuse padrões existentes quando bons. Faça componentes e abstrações proporcionais à repetição e à mudança prevista. Evite dependências e camadas sem ganho concreto.
- Verifique estados de carregamento, vazio, erro, sucesso, conteúdo longo e tamanhos relevantes. Em navegador real, percorra o fluxo em desktop e mobile e capture evidências representativas. Teste teclado, toque, contraste e reduced-motion conforme o escopo.
- Registre problemas recorrentes e adicione testes de regressão quando estáveis. Diferencie compilação, fluxo funcional e validação visual; limite alegações aos navegadores, viewports e fluxos de fato avaliados.
