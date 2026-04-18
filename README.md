# Luanny

**Coletor de dados de acessibilidade do Instagram para pesquisa acadêmica.**

Luanny é uma ferramenta que coleta e estrutura informações de acessibilidade
de publicações públicas do Instagram, gerando dados prontos para análise
acadêmica e auditoria de práticas de acessibilidade digital.

## Funcionalidades

- Coleta automatizada de posts públicos do Instagram
- Extração de texto alternativo, ARIA labels e sinais de acessibilidade
- Detecção de hashtags como `#PraTodosVerem` e `#PraCegoVer`
- Geração de JSON detalhado e CSV resumido
- Captura de evidências técnicas para reprodutibilidade científica
- Tolerância a falhas parciais

## Instalação Rápida

```bash
# Clonar o repositório
git clone <url-do-repositorio>
cd Luanny

# Criar ambiente virtual e instalar
python -m venv .venv
.venv\Scripts\activate   # Windows
pip install -e ".[dev]"
playwright install chromium
```

## Build Windows

```bash
python scripts/build.py
```

O build usa [Luanny.spec](Luanny.spec) como fonte única de verdade e gera
o pacote final em `dist/Luanny/`.

Por padrão, o build também executa smoke checks de distribuição (Fase 5):

- valida `Luanny.exe --help`;
- valida o fluxo automatizado do launcher `executar.bat` ([2] ajuda, [3] sair).

Opções úteis:

```bash
# Inclui regressão completa no final (pytest -q)
python scripts/build.py --run-regression-tests

# Pula smoke checks (uso excepcional)
python scripts/build.py --skip-smoke-checks
```

### Execução no Windows

- Use `dist/Luanny/executar.bat` como ponto de entrada padrão.
- Evite abrir `Luanny.exe` com clique duplo direto.
- O launcher `.bat` agora apresenta menu, mantém o terminal aberto e exibe
	código de saída quando houver erro.
- Esta versão roda em terminal (CLI), sem GUI nativa do Windows.
- Para interromper uma coleta em andamento, use `Ctrl+C`.

### Ocorrência Registrada e Correção

Foi registrada ocorrência de encerramento silencioso no Windows:

- Sintoma 1: clique duplo em `Luanny.exe` causava "flash" no terminal.
- Sintoma 2: `executar.bat` encerrava sem contexto após a tecla de pausa.

Procedimento corretivo aplicado:

- launcher `.bat` com menu e verificação explícita de `Luanny.exe`.
- tratamento de erro com exibição de `EXIT_CODE` após execução.
- fallback interativo no CLI empacotado quando aberto sem argumentos.

Salvaguarda contra regressão:

- smoke checks do build validam automaticamente:
	- `dist/Luanny/executar.bat` abre menu e executa opção [2] (help);
	- `dist/Luanny/Luanny.exe --help` retorna sem falha.
- regressão completa pode ser executada no mesmo comando com:
	- `python scripts/build.py --run-regression-tests`.

## Status Atual

- Fase 0 a Fase 6 estão concluídas no histórico do projeto.
- A versão inicial mantém a Fase 7 fora do escopo.
- A prioridade atual é estabilização do executável e previsibilidade de runtime.

## Uso

```bash
# Modo interativo (guiado)
python -m luanny scrape

# Modo direto
python -m luanny scrape --profile govbr --max-posts 30
```

Regras práticas para evitar bloqueio da plataforma:

- Recomendado: até `50` posts por rodada.
- Limite técnico máximo: `500` posts por rodada.
- Prefira rodadas menores e sucessivas em vez de coletas muito longas.

## Documentação

- [Guia de Instalação](docs/INSTALL.md)
- [Guia de Uso](docs/USAGE.md)
- [Plano Técnico de Coleta Incremental](docs/PLANO_ACAO_COLETA_INCREMENTAL.md)
- [Análise de Viabilidade da GUI (versão futura)](docs/ANALISE_GUI_VERSAO_FUTURA.md)

## Licença

MIT
