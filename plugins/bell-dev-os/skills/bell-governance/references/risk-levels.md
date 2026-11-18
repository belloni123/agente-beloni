# Níveis de risco

| Nível | Exemplos | Rigor esperado |
|---|---|---|
| LOW | Texto, CSS simples, visual reversível | Inspeção localizada e verificação visual ou estática relevante |
| MEDIUM | Feature localizada, componente, API não crítica, fluxo limitado | Requisitos claros, testes do comportamento, revisão focada |
| HIGH | Autenticação, pagamentos, dados importantes, permissões, banco, infraestrutura, regras centrais | SPEC explícita, decisões registradas, testes positivos e negativos, revisão cuidadosa |
| CRITICAL | Ação destrutiva, produção, dados financeiros ou sensíveis, migração irreversível, segurança crítica | Plano de execução e recuperação, validação robusta e autorização quando necessária |

Avalie impacto, reversibilidade, alcance, exposição de dados e incerteza. Aumente o rigor se qualquer dimensão elevar o risco. Prefira mudança localizada, padrão existente, dependência existente e decisão reversível. Não peça autorização por rotina técnica reversível; siga a autorização já dada pelo usuário.
