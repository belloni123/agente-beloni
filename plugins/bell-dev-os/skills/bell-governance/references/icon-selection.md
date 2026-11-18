# Seleção de ícones

Use esta referência ao planejar, implementar ou revisar iconografia. Escolha por projeto; não instale bibliotecas em todos os produtos nem faça retrofit sem pedido e benefício claro.

## Critérios de decisão

1. Verifique primeiro a stack, componentes e família já adotada. Preserve uma solução coerente quando ela atende cobertura, licença, acessibilidade e desempenho.
2. Compare linguagem visual, cobertura semântica, pesos disponíveis, grade, consistência, integração real com a stack, importação pontual, manutenção recente, licença e custo total.
3. Escolha uma família principal. Mantenha peso, tamanho óptico, caixa, alinhamento e tratamento de cor consistentes. Use exceções somente para marca oficial ou lacuna real; não misture famílias para criar variedade.
4. Consulte documentação, licença, preço e atividade oficiais no momento da decisão. Não presuma gratuidade, plano, versão, integração nativa ou manutenção futura.
5. Registre a escolha e o motivo quando ela afetar o design system, bundle, licença ou operação.

## Catálogo para avaliar

- [Lucide](https://lucide.dev): linha limpa e ampla integração por framework. A documentação oficial informa licença ISC e, no pacote React, componentes isolados com tree shaking. É um candidato geral, não padrão obrigatório.
- [Phosphor](https://phosphoricons.com): oferece vocabulário expressivo e variações de peso úteis quando a identidade pede mais alcance visual. O repositório oficial publica o core sob MIT; confirme o pacote específico usado.
- [Heroicons](https://heroicons.com): conjunto focado e coerente com bibliotecas oficiais para React e Vue, sob MIT. Considere quando sua cobertura e estilos atendem o produto; não presuma dependência de Tailwind nem integração com outras stacks.
- [Tabler Icons](https://tabler.io/icons): catálogo amplo, grade e traço consistentes, formatos e pacotes para diversas stacks; a licença oficial dos ícones é MIT. Bom candidato quando cobertura extensa é importante, sem obrigar carregar o catálogo inteiro.
- [Iconify](https://icon-sets.iconify.design): agregador para descobrir e consumir muitas coleções. Cada coleção mantém autoria, estilo e licença próprios. Se usado, selecione e documente uma coleção principal; não misture coleções indiscriminadamente nem trate “Iconify” como licença única.
- [Font Awesome](https://fontawesome.com): avalie especialmente em WordPress ou Elementor quando a instalação existente já oferece integração adequada. Free e Pro têm catálogos, termos e custos diferentes; no Free, ícones SVG/JS, fontes e código usam licenças distintas. Não compre plano nem suponha integração nativa sem confirmar o ambiente.

Para motion, avalie apenas quando animação comunicar entrada, clique, progresso, sucesso, erro ou mudança de estado:

- [Lordicon](https://lordicon.com): possui conteúdo gratuito e PRO; o plano gratuito pode exigir atribuição e os termos/preços podem mudar.
- [LottieFiles](https://lottiefiles.com): reúne arquivos públicos e conteúdo premium sob termos distintos. Verifique a licença do asset escolhido, autoria, formato, hospedagem e custo.
- [UseAnimations](https://useanimations.com): coleção React de ícones animados com importação por animação. A licença oficial dos recursos livres exige atribuição e restringe redistribuição; confirme se serve ao produto.

Essas opções não são equivalentes nem uma lista de instalação. Prefira a menor solução mantida que cubra a linguagem e os estados reais do projeto.

## Implementação

- Importe somente ícones usados. Prefira componentes/SVGs pontuais e tree shaking comprovado pela ferramenta e pelo build; evite namespace, fonte ou bundle completo quando isso incluir o catálogo inteiro.
- Ícone decorativo deve ficar oculto da árvore acessível. Controle somente com ícone precisa de nome acessível e alvo de toque adequado; ícone ao lado de texto não deve duplicar anúncio.
- Não dependa de hover. Para motion, use clique, entrada ou mudança de estado quando houver propósito e mantenha a ação funcional com teclado e toque.
- Respeite `prefers-reduced-motion`, ofereça estado estático equivalente e evite autoplay/loop decorativo. Meça bundle, rede, CPU e fluidez no mobile real.
- Para WhatsApp e outras marcas, obtenha o asset em fonte oficial/autorizada, preserve proporções e regras de marca e valide a licença. Uma aproximação desenhada à mão ou ícone genérico não substitui a marca.

## Verificação

- Confirme família principal, exceções justificadas, licença/atribuição e origem dos assets.
- Inspecione consistência de peso, tamanho, alinhamento e semântica em desktop e mobile.
- Teste teclado, leitor de tela quando aplicável, toque, reduced-motion e fallback sem animação.
- Confira o bundle produzido ou a estratégia de carregamento; não aceite “tree-shakable” como evidência se o padrão de importação trouxer a coleção inteira.
