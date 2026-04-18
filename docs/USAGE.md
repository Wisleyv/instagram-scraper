# Uso

## Execução via Python

```bash
python -m luanny scrape
python -m luanny scrape --profile govbr --max-posts 30
python -m luanny scrape --profile govbr --since 2026-01-01 --until 2026-12-31
python -m luanny scrape --profile govbr --no-resume
```

## Execução interativa

No modo interativo, o CLI solicita o perfil e outros parâmetros de coleta.

Orientações mostradas na preparação da coleta:

- recomendado até `50` posts por rodada para reduzir risco de bloqueio;
- limite técnico máximo de `500` posts por rodada;
- modo do navegador de automação:
	- sem janela (headless) = recomendado para coleta;
	- com janela (headed) = usar em login/checkpoint/diagnóstico.

## Execução pelo pacote Windows

1. Abra `dist/Luanny/`
2. Execute `executar.bat`
3. Escolha no menu:
	- `[1]` iniciar coleta guiada
	- `[2]` mostrar ajuda
	- `[3]` sair
	- `[4]` executar comando avançado

> Recomendação: use sempre `executar.bat` no Windows.
> O `Luanny.exe` aberto por clique duplo pode fechar rápido sem dar tempo de
> leitura da saída.
>
> Esta versão usa terminal (CLI), não uma GUI nativa do Windows.

## Solução de problemas (Windows)

### Sintoma: janela fecha sozinha

- Causa comum: execução direta do `Luanny.exe` sem launcher.
- Ação corretiva: abrir `executar.bat` e usar o menu.

### Sintoma: execução sem mensagem de erro

- O launcher atualizado mostra código de saída quando houver falha.
- Para diagnóstico adicional, rode no terminal:

```bash
dist/Luanny/Luanny.exe --help
dist/Luanny/Luanny.exe scrape
```

### Interrupção manual da coleta

- Durante a coleta, pressione `Ctrl+C` para interromper o comando em execução.
- O Luanny encerra de forma controlada e fecha os recursos do navegador.

## Smoke checks de distribuição (Fase 5)

O build Windows passou a validar automaticamente artefatos críticos do pacote:

- `Luanny.exe --help`;
- execução automatizada de `executar.bat` no fluxo [2] ajuda -> [3] sair.

Comandos:

```bash
# Build com smoke checks (padrão)
python scripts/build.py

# Build com smoke checks + regressão completa
python scripts/build.py --run-regression-tests

# Build sem smoke checks (uso excepcional)
python scripts/build.py --skip-smoke-checks
```

Se algum smoke check falhar, o build retorna erro com stdout/stderr da etapa
que falhou para facilitar o diagnóstico.

## Saídas

- `posts.json`: resultado estruturado da coleta
- `summary.csv`: resumo tabular
- `report.md`: relatório legível da execução
- `manifest.json`: manifesto da execução com trilha de auditoria
- `evidence/`: evidências por post quando ativadas

## Estado incremental (Fases 1 e 2)

- O Luanny persiste estado por perfil em `data/_state/<perfil>.json`.
- IDs já vistos são usados para reduzir duplicidade entre execuções.
- O comportamento pode ser desativado por execução com `--no-resume`.
- Se o arquivo de estado estiver inválido, o sistema reinicia esse estado sem
	interromper a coleta.

## Janela temporal (Fase 2)

- `--since AAAA-MM-DD`: data inicial da janela desejada.
- `--until AAAA-MM-DD`: data final da janela desejada.
- Quando ambas são informadas, somente posts com `published_at` dentro da
	janela são mantidos no resultado final.
- Posts sem `published_at` continuam no resultado nesta fase para evitar perda
	de cobertura.

## Discovery temporal (Fase 3)

- A descoberta agora ignora IDs já vistos durante a própria rolagem quando
	`resume` está ativo, reduzindo retrabalho entre execuções.
- Com `--since`, a discovery interrompe antecipadamente quando os posts
	visíveis já estão consistentemente abaixo da janela temporal.
- O limite `--max-posts` passa a ser aplicado sobre candidatos novos dentro da
	janela, e não apenas sobre os primeiros itens carregados no topo do perfil.

## Manifesto de execução (Fase 4)

- Cada coleta agora gera `manifest.json` no diretório da run.
- O manifesto inclui:
	- metadados da execução e janela temporal aplicada;
	- checkpoint de retomada (`resume`) com estado antes/depois;
	- hashes SHA-256 e tamanho dos artefatos exportados;
	- trilha de auditoria por etapa do pipeline (browser, auth, discovery,
	  extração, filtro temporal, evidências, exportação e persistência de estado).
- O manifesto foi desenhado para facilitar rastreabilidade, auditoria e
	reprodutibilidade entre execuções incrementais.

## Regras de uso atuais

- Perfis públicos apenas
- Fase 7 fora do escopo da v1
- Coletas devem priorizar estabilidade e reprodutibilidade

## Referência para evolução de GUI (versão futura)

- Veja a análise técnica em `docs/ANALISE_GUI_VERSAO_FUTURA.md`.