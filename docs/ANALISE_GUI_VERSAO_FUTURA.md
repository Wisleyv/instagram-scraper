# Analise de Viabilidade de GUI Windows (Versao Futura)

## Objetivo

Registrar a avaliacao tecnica para futura integracao de uma interface grafica
no Luanny, voltada para usuario nao tecnico, com foco em:

- visibilidade da evolucao da coleta;
- comando de interrupcao segura;
- sensacao de controle operacional.

## Resumo Executivo

A viabilidade para GUI no Windows e **alta**.

Motivos principais:

1. O pipeline principal esta concentrado no orquestrador, o que reduz
   retrabalho para adicionar eventos de progresso.
2. Ja existe rastreabilidade por manifesto e trilha de auditoria por etapa.
3. O encerramento do browser ja e feito em bloco final, favorecendo stop seguro.

## Base Atual Reaproveitavel

- Pipeline consolidado de coleta em uma funcao unica de orquestracao.
- Metricas e estados por etapa ja existentes (discovery, extraction,
  evidence, export, state, manifest).
- Manifesto por execucao com trilha auditavel.
- Build Windows estabelecido com PyInstaller.

## Lacunas para GUI

1. Progresso hoje e emitido para terminal, nao para um canal de eventos.
2. Fluxo de checkpoint/2FA ainda usa input bloqueante em console.
3. Nao existe token de cancelamento cooperativo entre etapas.
4. Empacotamento atual foi desenhado para launcher em terminal.

## Proposta Tecnica Recomendada

### 1) Camada de Eventos no Orquestrador

Adicionar callback opcional de progresso, sem quebrar API existente, por
exemplo:

- `on_event(step, status, details)`.

Com isso, CLI e GUI passam a compartilhar o mesmo backend.

### 2) Cancelamento Cooperativo

Adicionar um cancel token consultado em pontos seguros:

- antes de iniciar cada post;
- antes de captura de evidencia;
- antes de exportacao final.

Semantica de parada segura:

- finalizar unidade atual em andamento;
- fechar browser;
- exportar resultado parcial;
- salvar estado incremental (quando habilitado);
- gerar manifesto com status de cancelamento.

### 3) GUI Windows Minimalista

Primeira entrega recomendada: `tkinter` com worker thread + fila de eventos.

Elementos minimos:

- formulario de parametros (perfil, max-posts, janela temporal, resume);
- barra de progresso global e log de etapas;
- botao `Iniciar`;
- botao `Parar com seguranca`;
- estado final com link para pasta de saida.

### 4) Build para GUI

Criar opcao de empacotamento GUI em paralelo ao modo atual de console,
preservando fallback CLI para suporte e diagnostico.

## Roadmap Sugerido (vNext)

1. **M1 - Instrumentacao**: eventos de progresso + cancel token no backend.
2. **M2 - Interface**: shell GUI com tela unica e parametros basicos.
3. **M3 - Stop Seguro**: fluxo completo de cancelamento com manifesto.
4. **M4 - Distribuicao**: build dedicado GUI + smoke checks de interface.

## Criterios de Aceite da GUI (vNext)

- Usuario inicia coleta sem linha de comando.
- Usuario visualiza etapa atual e progresso.
- Usuario pode interromper com stop seguro sem corromper estado.
- Execucao interrompida gera manifesto indicando cancelamento.
- Build GUI inicia em Windows limpo e retorna mensagens claras em falha.

## Riscos e Mitigacoes

- **Risco**: bloqueio em checkpoint/2FA.
  - Mitigacao: substituir input de console por notificacao/evento para GUI.
- **Risco**: concorrencia (thread/UI).
  - Mitigacao: worker isolado e comunicacao por fila thread-safe.
- **Risco**: regressao no fluxo atual CLI.
  - Mitigacao: manter callback opcional e suite de testes com cobertura dual.

## Conclusao

GUI Windows e uma evolucao natural e recomendada para o perfil de usuario
nao tecnico do projeto. A implementacao pode ser incremental, com baixo risco
arquitetural se iniciar pela instrumentacao de eventos e cancelamento no
orquestrador.
