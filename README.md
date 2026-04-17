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
```

## Uso

```bash
# Modo interativo (guiado)
python -m luanny scrape

# Modo direto
python -m luanny scrape --profile govbr --max-posts 30
```

## Documentação

- [Guia de Instalação](docs/INSTALL.md)
- [Guia de Uso](docs/USAGE.md)

## Licença

MIT
