# Seleção e qualidade de backend

Escolha backend e operação pelo problema, não por uma stack favorita.

## Decisão proporcional

Avalie fluxo e regras, carga e crescimento plausíveis, consistência, sensibilidade e residência dos dados, autenticação e autorização, integrações, equipe, orçamento, custo total, observabilidade, manutenção e recursos reais do ambiente. Considere explicitamente:

- nenhum backend ou site estático quando suficiente;
- backend simples com PostgreSQL ou outro armazenamento adequado;
- serviço managed, inclusive Supabase, quando seus recursos e trade-offs forem úteis;
- arquitetura já existente, preservando compatibilidade salvo motivo forte para mudar.

Não empurre Supabase automaticamente nem o descarte por opinião ou vídeo. Não imponha microservices, Kubernetes, Redis, ORM, filas ou qualquer stack universal. Introduza complexidade somente diante de necessidade observável.

## Operação, Git e segurança

- Se Coolify ou containers forem o alvo escolhido, verifique compatibilidade real: imagem/build, processo, portas, variáveis, health checks, volumes, persistência, rede, migrações, backup e rollback conforme aplicável. Não presuma que o alvo foi escolhido.
- Use branches, diff, testes, PR e CI com rigor proporcional ao projeto. Integração GitHub descreve um fluxo possível; não autoriza push, abertura de PR, deploy ou publicação de dados.
- Faça autenticação e autorização efetiva no servidor. Valide entrada e saída nas fronteiras, aplique least privilege e não coloque secrets no Git, cliente, artefatos ou logs.
- Planeje migrations e rollback de acordo com reversibilidade e impacto. Para dados importantes, explicite retenção, restore testado e responsabilidade por backups; não crie exigências operacionais sem necessidade do projeto.

Consulte documentação oficial atual quando comportamento, suporte ou compatibilidade de produto puder ter mudado. Não fixe versões por suposição nem prometa atualização automática.
