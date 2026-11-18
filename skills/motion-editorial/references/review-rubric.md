# Revisão observável de uma animação

## O que avaliar

| Critério | Pergunta observável | Exemplo de defeito |
| --- | --- | --- |
| Causalidade | A chegada produz a mudança de estado? | Ferramenta marca concluído antes da resposta voltar. |
| Continuidade espacial | Sei onde o elemento foi parar? | Grafo some e outro equivalente reaparece em posição nova. |
| Conexão | A linha chega às portas certas em movimento? | Nó muda de escala e o conector fica parado. |
| Leitura | Há tempo de entender a informação principal? | Texto entra enquanto a altura do painel comprime as linhas. |
| Hierarquia | Uma ação principal conduz o olhar? | Título, fundo, brilho e cards competem continuamente. |
| Ritmo | O movimento muda conforme a intenção? | Todas as cenas têm a mesma subida, stagger e wipe. |
| Estado estável | O movimento repousa quando termina? | Progresso volta a zero ou pacote reaparece sem nova ação. |
| Integração | A pessoa e a arte compartilham espaço e ênfase? | Sobreposição cruza o rosto ou ignora a fala. |

Classifique defeitos concretos pela consequência. Evite inventar uma nota numérica para gosto. Distingua algo demonstrável (salto, corte de texto, porta incorreta) de uma proposta editorial.

## Evidência proporcional

- Ajuste localizado de curva/posição: amostras antes, durante e depois, mais reprodução do trecho se disponível.
- Passagem entre cenas: amostre também a fronteira, não só o meio de cada cena. Uma janela de 1–2 segundos de cada lado costuma revelar resets.
- Cena com várias etapas: confira chegada, feedback e repouso de cada etapa; não basta o quadro final.
- Revisão geral: avalie trechos representativos em movimento e todas as fronteiras afetadas. Renderize a saída e confira o arquivo completo tecnicamente.
- Voz ausente: informe que os tempos são provisórios. Voz presente: observe pausas, ênfases e manutenção do espaço de câmera.

O script de amostragem ajuda a localizar defeitos. Ele não substitui percepção em reprodução normal, avaliação auditiva ou validação com a gravação real. Identifique qual evidência foi realmente obtida.

## Encerramento da revisão

Corrija defeitos demonstrados e confira novamente os mesmos intervalos. Pare quando não houver quebras observadas no escopo, a sequência puder ser acompanhada e a leitura estiver preservada; não adicione efeitos só para mostrar trabalho. Registre o que permanece como decisão criativa ou depende de mídia futura.

## Falhas intermitentes na exportação

Decodificar sem erro e revisar poucos stills não comprova integridade visual. Quadros com mosaicos, partes da viewport ou marcas repetidas podem estar codificados normalmente no MP4. Quando houver esse sintoma, preserve um intervalo defeituoso e valide nele uma mudança de backend de captura/renderização antes da exportação completa. Em Remotion/Chromium, teste também a captura intermediária em PNG quando JPEG produzir mosaicos, além de alternativas de backend gráfico. Alterar somente o backend pode passar num trecho curto e falhar no vídeo completo. Nenhuma configuração é uma exigência universal.

Depois da correção, examine amostras densas dos intervalos relatados e varra todos os quadros com verificações adequadas à composição (por exemplo, saltos isolados e presença de elementos fixos). Calibre os detectores contra o defeito conhecido e inspecione seus alertas. Ausência de alerta não comprova ausência de todo defeito. Registre separadamente checagem automatizada, amostragem visual e reprodução audiovisual efetivamente realizada.
