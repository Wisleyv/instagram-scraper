# Instalação

## Pré-requisitos

- Python 3.10 ou superior
- Conta operacional do Instagram configurada em `.env`
- Chromium do Playwright instalado localmente

## Instalação para desenvolvimento

```bash
git clone <url-do-repositorio>
cd Luanny
python -m venv .venv
.venv\Scripts\activate
pip install -e ".[dev]"
playwright install chromium
```

## Variáveis de ambiente

Crie um arquivo `.env` na raiz do projeto com pelo menos:

```env
INSTAGRAM_USERNAME=sua_conta
INSTAGRAM_PASSWORD=sua_senha
```

## Build do executável

```bash
python scripts/build.py
```

O build gera `dist/Luanny/` e cria os atalhos `executar.bat` e `LEIA-ME.txt`.

Na Fase 5, o build passou a executar smoke checks automaticamente ao final:

1. `Luanny.exe --help`
2. fluxo automatizado de `executar.bat` ([2] ajuda, [3] sair)

Opções adicionais:

```bash
# Também executa regressão completa
python scripts/build.py --run-regression-tests

# Ignora smoke checks (uso excepcional)
python scripts/build.py --skip-smoke-checks
```

## Verificação pós-build (Windows)

Após gerar o executável, valide:

1. Confirmar no log do build que os smoke checks finalizaram com sucesso.
2. Abrir `dist/Luanny/executar.bat` e validar o menu manualmente (opcional).
3. Executar `dist/Luanny/Luanny.exe --help` no terminal (opcional).
4. Para regressão completa no mesmo fluxo, usar `--run-regression-tests`.

## Problema conhecido corrigido

Ocorrência registrada:

- Clique duplo em `Luanny.exe` podia abrir e fechar rapidamente (flash).
- `executar.bat` antigo apenas chamava o exe e pausava, sem menu de ação.

Correções implementadas:

- launcher com menu, checagem de executável e retorno de código de erro;
- modo interativo no CLI empacotado quando executado sem subcomando.

## Observações

- O `Luanny.spec` é versionado e serve como base do empacotamento.
- O projeto está focado na v1; o módulo de áudio segue fora do escopo.