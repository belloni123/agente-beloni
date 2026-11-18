---
name: bell-init-project
description: Use para configurar ou adaptar a estrutura e as convenções iniciais de um repositório ao Bell Dev OS; inspeciona stack e comandos, sem substituir o planejamento de produto.
---
# Iniciar projeto

Use quando o usuário pedir inicialização, adoção do Bell Dev OS ou organização inicial do repositório. Em projeto novo com pedido de funcionalidade, faça esta preparação se necessária e passe a `bell-plan` para definir o produto. Inspecione repositório e documentação. Identifique stack, arquitetura, banco, autenticação, integrações, scripts, lint, typecheck, testes, build e estratégia de deploy, quando observável. Se houver alvo definido como Coolify ou outro ambiente de containers, registre requisitos reais de runtime, persistência, health check, migração e rollback sem impor uma stack. Separe fatos de inferências e lacunas.

Proponha ou crie, quando apropriado, `AGENTS.md`, `docs/PRD.md`, `docs/PLAN.md`, `docs/adr/` e `docs/specs/`. Mantenha `AGENTS.md` curto, somente com regras permanentes específicas do repositório; não copie as instruções do plugin. Não gere documentos vazios por obrigação. Use os templates em `../bell-governance/assets/` apenas para artefatos necessários. Para projeto novo, encaminhe os requisitos a `bell-plan`.
