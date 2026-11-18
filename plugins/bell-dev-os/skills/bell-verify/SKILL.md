---
name: bell-verify
description: Use após implementação ou em pedidos de checagem funcional; executa QA com evidências e relata PASS, FAIL ou PARTIAL, sem substituir a revisão de aderência.
---
# Verificar

Leia SPEC e critérios de aceitação quando existirem. Examine o diff e execute verificações relevantes: testes, lint, typecheck, build, caminho principal, falhas esperadas, casos extremos e regressões. Para interface, use navegador real quando disponível, percorra fluxos e registre screenshots representativos em desktop e mobile; verifique toque, foco por teclado, ações visíveis sem hover, acessibilidade, reduced-motion e desempenho proporcional. Quando houver ícones, confira família e alinhamento consistentes, semântica, marcas legítimas, licença/atribuição, imports pontuais e fallback estático de motion conforme `../bell-governance/references/icon-selection.md`. Compare com referências e critérios definidos, não apenas com gosto pessoal. Compilação isolada não valida interface. Escolha verificações proporcionais ao risco; não execute comandos irrelevantes só para completar lista. Não confie apenas no relato de implementação.

Produza um relatório usando `../bell-governance/assets/VERIFICATION.template.md` quando a tarefa justificar arquivo; em tarefas simples, reporte na conversa. Status: PASS, FAIL ou PARTIAL. Liste verificações, comandos, resultados, bugs, evidências, pontos não testados e riscos restantes. Diferencie código escrito, compilação, testes, fluxo funcional e validação completa. Registre falhas recorrentes e acrescente teste de regressão quando ele for estável e útil. Se FAIL, retorne a `bell-build` e verifique novamente. Nunca afirme “funcionando” ou “design validado” sem evidência suficiente nos alvos realmente inspecionados.
