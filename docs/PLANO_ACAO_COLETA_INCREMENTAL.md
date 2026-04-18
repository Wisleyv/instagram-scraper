# Plano Tecnico - Coleta Incremental

## Contexto

O modelo atual de coleta por lote curto precisa evoluir para um fluxo
incremental, com deduplicacao persistente e cobertura temporal ampla.

Este plano divide a evolucao em fases pequenas para reduzir retrabalho e
preservar estabilidade.

## Fases do plano

1. Fase 1 - Estado persistente da coleta
2. Fase 2 - Parametros de janela temporal (since/until/resume)
3. Fase 3 - Discovery orientada por tempo + parada por janela
4. Fase 4 - Manifesto de execucao e trilha de auditoria
5. Fase 5 - Integracao com build Windows e smoke checks de distribuicao

## Fase 1 (implementada)

### Objetivo

Introduzir estado persistente por perfil para:

- guardar IDs de posts ja coletados;
- reduzir risco de coleta duplicada entre execucoes;
- registrar checkpoint temporal mais antigo coletado.

### Alteracoes implementadas

- Modelo novo `CollectionState` no modulo de modelos.
- Modulo novo `collection_state.py` com:
  - resolucao de path de estado;
  - carga resiliente (fallback em caso de arquivo ausente ou invalido);
  - persistencia em JSON;
  - merge deduplicado de IDs e atualizacao do post mais antigo coletado.
- Integracao no orquestrador:
  - carrega estado antes da discovery;
  - filtra IDs ja vistos antes da extracao;
  - salva estado atualizado ao final da execucao.

### Arquivo de estado

- Local: `data/_state/<perfil>.json`
- Campos principais:
  - `profile`
  - `collection_id`
  - `seen_post_ids`
  - `last_published_at`
  - `last_post_id`
  - `updated_at`

## Salvaguardas anti-regressao

- Cobertura de testes unitarios para carga, persistencia e merge de estado.
- Sem alteracao de comportamento de credenciais/autenticacao.
- Sem alteracao do fluxo de exportacao existente (`posts.json`, `summary.csv`,
  `report.md`).
- Deduplicacao aplicada somente sobre IDs ja persistidos no estado.

## Criterios de aceite da fase 1

- Reexecucao de coleta no mesmo perfil ignora posts com IDs ja vistos.
- Estado e atualizado com novos IDs ao fim da execucao.
- Caso o arquivo de estado esteja corrompido, a coleta nao quebra.

## Acoes executadas nesta entrega

- Implementacao do modelo `CollectionState`.
- Implementacao do modulo `collection_state.py` com load/save/update.
- Integracao no `orchestrator.py` para deduplicacao entre execucoes.
- Inclusao da bateria de testes `tests/test_collection_state.py`.
- Atualizacao de documentacao no `README.md` e `docs/USAGE.md`.

Validacao executada:

- `pytest tests/test_collection_state.py -q` -> 4 passed.
- `pytest -q` -> 70 passed.

## Fase 2 (implementada)

### Objetivo

Adicionar controle operacional de janela temporal e retomada por execucao para:

- permitir recortes temporais sem alterar codigo;
- manter deduplicacao como comportamento padrao, com opcao de desligar;
- registrar parametros de janela no metadata exportado.

### Alteracoes implementadas

- Modelo `AppConfig` com campos `since`, `until` e `resume` + validacao
  `since <= until`.
- `load_config` atualizado para ler `SINCE`, `UNTIL` e `RESUME` via `.env`
  e por overrides da CLI.
- CLI `scrape` atualizada com:
  - `--since AAAA-MM-DD`
  - `--until AAAA-MM-DD`
  - `--resume/--no-resume`
  - prompts interativos para janela temporal e retomada.
- `orchestrator.py` atualizado para:
  - carregar/salvar estado incremental somente quando `resume=True`;
  - filtrar posts por `published_at` dentro da janela quando configurada;
  - preservar posts sem `published_at` nesta fase.
- `CollectionMetadata` atualizado para registrar `since`, `until` e
  `resume_enabled`.

### Criterios de aceite da fase 2

- Parametros temporais podem ser configurados por `.env` e por CLI.
- Execucao com `--no-resume` nao reutiliza nem atualiza estado persistido.
- `since > until` falha cedo por validacao.
- Resultado final respeita janela para posts com data conhecida.

## Fase 3 (implementada)

### Objetivo

Tornar a discovery orientada por tempo e por estado incremental para:

- evitar repetir apenas os posts do topo a cada execucao;
- aplicar janela temporal ja na descoberta quando houver sinal de data;
- parar rolagem cedo quando a fronteira `since` foi claramente ultrapassada.

### Alteracoes implementadas

- `discover_posts` agora aceita `seen_post_ids` e ignora IDs previamente
  coletados durante a rolagem.
- A meta `max_posts` passa a contar posts novos candidatos (nao vistos),
  permitindo avancar historicamente entre execucoes.
- Discovery tenta ler `time[datetime]` no grid como hint temporal e aplica:
  - descarte precoce de posts fora de `since`/`until` quando a data e visivel;
  - parada antecipada quando a tela corrente permanece abaixo de `since` em
    repetidas iteracoes.
- `orchestrator.py` passa os IDs vistos diretamente para `discover_posts`.

### Criterios de aceite da fase 3

- Com `resume=True`, a discovery retorna preferencialmente posts ainda nao
  vistos, mesmo com IDs antigos no topo do perfil.
- Com `since` configurado, discovery interrompe quando os itens visiveis ja
  sao consistentemente mais antigos que o limite inferior.
- Fluxo permanece compativel quando nao ha `datetime` disponivel no grid.

## Fase 4 (implementada)

### Objetivo

Adicionar manifesto de execucao por run com trilha de auditoria para:

- ampliar rastreabilidade operacional da coleta;
- registrar checkpoint incremental before/after na mesma run;
- vincular artefatos exportados a hashes verificaveis.

### Alteracoes implementadas

- Modulo novo `execution_manifest.py` para gerar `manifest.json` por run.
- Manifesto inclui:
  - metadados principais da execucao;
  - configuracao temporal (`since`/`until`) e status de `resume`;
  - snapshot de checkpoint incremental antes/depois do update de estado;
  - trilha de auditoria de etapas com timestamp e detalhes;
  - hashes SHA-256 e tamanho de `posts.json`, `summary.csv`, `report.md`
    e do arquivo de estado (quando disponivel).
- `orchestrator.py` atualizado para:
  - registrar eventos de auditoria durante o pipeline;
  - persistir `manifest.json` ao final da execucao bem-sucedida.

### Criterios de aceite da fase 4

- Toda run concluida gera `manifest.json` no diretorio de saida da execucao.
- Manifesto registra checkpoint incremental com contagem de IDs before/after.
- Manifesto inclui hashes dos artefatos exportados quando presentes.
- Trilha de auditoria cobre etapas principais do pipeline.

## Fase 5 (implementada)

### Objetivo

Integrar smoke checks ao build Windows de distribuicao para:

- validar artefatos criticos logo apos o empacotamento;
- reduzir risco de regressao no launcher e no executavel final;
- tornar o build mais confiavel para uso por equipe nao tecnica.

### Alteracoes implementadas

- Modulo novo `build_smoke.py` com validacao automatizada de distribuicao.
- `scripts/build.py` atualizado para executar smoke checks por padrao ao final:
  - `Luanny.exe --help`;
  - fluxo automatizado de `executar.bat` ([2] ajuda -> [3] sair).
- Build ganhou parametros operacionais:
  - `--skip-smoke-checks`
  - `--run-regression-tests`
  - `--smoke-timeout`
  - `--regression-timeout`

### Criterios de aceite da fase 5

- Build falha cedo se `Luanny.exe` ou `executar.bat` estiverem ausentes.
- Build falha se `Luanny.exe --help` falhar.
- Build falha se fluxo automatizado de `executar.bat` falhar.
- Build expõe stderr/stdout da etapa com problema para diagnostico rapido.

## Proximos passos (fase 6 em diante)

- Expandir smoke checks para cenarios adicionais de runtime.
- Evolucao futura: GUI Windows para usuario nao tecnico.
  - referencia: `docs/ANALISE_GUI_VERSAO_FUTURA.md`.
