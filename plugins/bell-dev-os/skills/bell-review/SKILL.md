---
name: bell-review
description: Use após QA ou em pedido explícito de revisão da entrega; avalia aderência, qualidade e riscos no diff com findings objetivos por severidade.
---
# Revisar

Leia PRD, SPEC, ADR, PLAN, diff, testes e relatório de verificação quando disponíveis. Avalie aderência a requisitos e regras de negócio, critérios de aceitação, segurança, performance, arquitetura, manutenção, complexidade, mudanças colaterais, compatibilidade, dependências, dívida técnica e documentação. Em frontend, cobre evidência visual e funcional proporcional, sem transformar preferências genéricas em finding. Para iconografia, avalie coerência, acessibilidade, origem/licença, custo e impacto no bundle segundo `../bell-governance/references/icon-selection.md`; não exija troca de biblioteca sem impacto objetivo. Em backend, verifique se a escolha foi justificada pelo contexto e se controles de servidor, dados e operação correspondem ao risco. Investigue antes de concluir; não invente findings.

Classifique cada problema como BLOCKER, HIGH, MEDIUM ou LOW e informe severidade, problema, impacto, local e recomendação. Use `../bell-governance/assets/REVIEW.template.md` para revisões que justifiquem arquivo; caso contrário, reporte na conversa. Aprove somente sem impeditivos e com critérios relevantes satisfeitos. Se houver BLOCKER ou HIGH, retorne a `bell-build`, depois `bell-verify` e então repita a revisão.
