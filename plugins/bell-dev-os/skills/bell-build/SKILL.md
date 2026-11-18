---
name: bell-build
description: Use quando o usuário pedir implementação ou o plano estiver pronto e os requisitos forem suficientes; altera código, testes e documentação seguindo padrões existentes.
---
# Implementar

Leia `AGENTS.md` e, quando relevantes, PRD, SPEC, ADR e PLAN. Inspecione o código e siga sua arquitetura. Faça a menor alteração correta; evite refatoração lateral. Crie ou atualize testes significativos e documentação relevante. Atualize o PLAN conforme avança. Distinga implementação de validação.

Não invente regra de negócio, altere requisito silenciosamente, remova funcionalidade para facilitar, esconda erros ou apague dados para contornar problemas. Justifique dependência estrutural e registre mudança arquitetural importante. Mantenha código enxuto, componentes e abstrações proporcionais; evite overengineering, frameworks pesados e dependências sem benefício demonstrável. Não faça alteração destrutiva de banco nem modifique autenticação silenciosamente. Para decisão técnica pequena e reversível, siga o padrão existente e registre quando útil. Para decisão relevante de produto, dinheiro, dados, segurança, autenticação, arquitetura, integração ou UX crítica, apresente opções e peça decisão humana se o contexto não a resolver.

Em interface, siga `../bell-governance/references/frontend-quality.md`: preserve a personalidade definida para o projeto, construa mobile-first e não dependa de hover. Em backend, siga `../bell-governance/references/backend-selection.md`, inclusive limites de segurança, dados e deploy. Ao terminar, encaminhe a `bell-verify`.
