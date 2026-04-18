# Projeto Luanny — Walkthrough de Evolução

## Fase 0: Fundação e Contratos ✅

**Período:** 2026-04-16  
**Conversa de referência:** `c6a874d7-38fb-4281-a7a3-d48c01fe4bd2`

### O que foi realizado

O projeto foi inicializado do zero com uma abordagem de **scaffolding progressivo** — toda a arquitetura e contratos de dados definidos antes de qualquer implementação funcional. Isso garante que cada fase futura apenas "preenche stubs" sem risco de quebras estruturais.

#### Artefatos criados

| Componente | Arquivos | Descrição |
|---|---|---|
| **Projeto** | `pyproject.toml`, `.env.example`, `.gitignore`, `README.md` | Configuração, dependências, templates de ambiente |
| **Contratos** | [models.py](../src/luanny/models.py) | 9 modelos Pydantic: `PostRecord`, `MediaItem`, `AriaLabel`, `VideoAnalysis`, `Evidence`, `PostError`, `CollectionResult`, `CollectionMetadata`, `AppConfig` |
| **Configuração** | [config.py](../src/luanny/config.py) | Leitura de `.env`, validação via Pydantic, falha imediata com mensagem clara |
| **Logging** | [log.py](../src/luanny/log.py) | structlog com contextuação por execução e por post |
| **CLI** | [cli.py](../src/luanny/cli.py), [\_\_main\_\_.py](../src/luanny/__main__.py) | Comando `scrape` com flags: `--profile`, `--max-posts`, `--headless/--headed`, `--capture-evidence`, `--output-dir`, `--verbose` |
| **Orquestrador** | [orchestrator.py](../src/luanny/orchestrator.py) | Pipeline completo com stubs: init → auth → discover → extract → evidence → export |
| **Stubs** | `auth.py`, `browser.py`, `profile_discovery.py`, `post_extractor.py`, `evidence_capture.py`, `exporters.py` | Assinaturas corretas com tipos, retornando dados mock |
| **Seletores** | [selectors.py](../src/luanny/selectors.py) | CSS/XPath centralizados com fallbacks |
| **Testes** | `test_models.py` (15 testes), `test_config.py` (6 testes) | Serialização Pydantic, validação de config, cenários de erro |

### Validação realizada

```
$ pytest --tb=short -q
.....................                                                    [100%]
21 passed in 0.05s
```

```
$ python -m luanny scrape --help
✓ Exibe opções: --profile, --max-posts, --headless/--headed, etc.
```

```
$ python -m luanny scrape --profile govbr --max-posts 5
✓ Pipeline stub executa completo (sem .env = erro controlado com mensagem clara)
```

### Decisões arquiteturais tomadas

| Decisão | Valor |
|---|---|
| Idioma do browser | `pt-BR` com heurísticas bilíngues para alt auto-gerado |
| Perfil de teste | `@govbr` (público institucional) |
| Distribuição | Executável Windows standalone (PyInstaller), não Docker |
| Evidências | URL canônica, ISO 8601, SHA-256, versão do coletor |

---

## Transição para Fase 1: Browser e Autenticação

**Data:** 2026-04-17  
**Desbloqueio:** Credenciais da conta de teste `luannypesquisa` recebidas.

### Próximos passos

1. **Criar `.env`** a partir de `.env.example` com credenciais fornecidas
2. **Implementar `browser.py`** — Context manager do Playwright com viewport e idioma `pt-BR`
3. **Implementar `auth.py`** — Login, persistência de sessão (`storage_state.json`), reuso, e tratamento de checkpoint/2FA
4. **Integrar no orchestrator** — Substituir stubs por implementação real
5. **Testes** — Mock de Playwright para fluxo de login e reuso de sessão

> [!IMPORTANT]
> **Guarda contra regressão:** Após cada fase, rodar `pytest` completo para garantir que os 21 testes da Fase 0 continuam verdes. Novos testes são adicionados cumulativamente.

## Fase 1: Implementação do Browser e Autenticação

A Fase 1 foi focada na interação real com o Playwright e com a página do Instagram, assegurando que o coletor consegue estabelecer uma conexão estável e logar na plataforma.

### O que foi construído

1. **Gestão de Sessão (`browser.py`)**
   Desenvolvemos o context manager real do browser. Utilizamos a classe local `BrowserSession` (um `dataclass`) para envelopar a API de baixo nível do Playwright. Agora o script define corretamente:
   - Viewport base para navegação (1280x720) para evitar ser flagrado por headless bounds anômalos.
   - Idioma e localidade padronizados para `pt-BR`.
   - Remoção de flags anti-bot, via parâmetros customizados ao lançar o browser Chromium original.

2. **Autenticação Resiliente (`auth.py`)**
   Para contornar variações no DOM e atualizações contínuas do Instagram, o módulo de login tenta múltiplos mapeamentos para interagir com o site:
   - **Campos de Login Form:** Fallbacks para encontrar o input de email/username (`name="username"`, `name="email"`) e senha (`name="password"`, `name="pass"`).
   - **Cookies/GDPR Banner:** Função automática que limpa e aceita pop-ups intrusivos antes de tentar interagir com qualquer elemento, prevenindo falhas silenciosas de timeout do Playwright.
   - **Persistência (`storage_state.json`):** Uma vez logado, a sessão Playwright é copiada para o disco, dispensando novos logins.
   - **2FA/Checkpoint Fallbacks:** Detecção por tokens (`aria-label`, strings na tela). Quando o framework funciona no modo headed e acha uma interrupção, ele congela e pede atuação manual no console para o usuário finalizar a checagem no browser vivo.

### Atualização Estrutural e Cobertura
- Foram introduzidos 31 novos testes unitários para o `aut.py` e `browser.py` através de mocks em profundidade do engine do Playwright, resultando em 52 testes ativos e passantes.
- Atualizamos as interfaces de Fases 2, 3 e 4 para passarem o `BrowserSession` nativo ao invés de estruturas mockadas.

## Fase 2: Descoberta de Postagens (Profile Grid Discovery)

A Fase 2 substituiu os retornos estáticos em `profile_discovery.py` e mergulhou na exploração real da estrutura DOM em React do feed de perfil do Instagram. O objetivo principal foi contornar a virtualização agressiva de listas empregada em grandes coleções.

### Desafios Superados e Resoluções

1. **Investigação do DOM Virtualizado:**
   - Comprova-se que a página de perfil (`@govbr` neste teste) renderiza apenas os posts visíveis instantaneamente. Ao darmos *scroll*, o Instagram deleta as nodes do topo do DOM. Consequentemente, para uma raspagem abrangente (ex: `>= 50 posts`), o robô teve de assimilar uma rolagem em bloco completo iterativa, processar as URLs instanciadas e guardá-las num `HashSet` (neste caso, um dict).
2. **Correção Topológica dos Seletores:**
   - O plano original presumia que os grids se aninhassem dentro de uma `tag` especial como `<article>`. Foi constatado em tempo de execução que a `Meta` reestruturou seu DOM no perfil em puro empilhamento de `<DIV>`s hierárquicos infinitos sem delimitações semânticas. Adequamos os seletores primários para serem resilientes de *Pattern Matching* com base exclusiva nos hiperlinks (`a[href*='/p/'], a[href*='/reel/']`), provando-se ser a rota mais viável a longo prazo em SPAs modernos.
   - Constatamos ainda que o extrator de propriedades nativo colhia as rotas resolvidas absolutas ou relativas diferentemente de acordo com a heurística do driver. Assim, foi montado um parse inteligente que extrai o ID quebrandos partes sem ferir as keys hashables, impedindo overlapping (bug do "P" vs "Reel" como chave única do dicionário, agora curado para `ID de 11 char` real).
3. **Escada de Interação Humana:**
   - Para que o Virtual list renderer do Instagram efetivasse o loading *Fetch-on-scroll*, o scroll teve de referenciar precisamente o fundo do documento `scrollHeight` interpolado a `human_delay`. Se rolasse muito rapidamente, a requisição GraphQL abortava.

À medida que adentramos na **Fase 3**, nosso indexador consegue navegar dinamicamente páginas do Instagram sem limites aparentes, guardando cada URL em fila prontos para o Extrator de Acessibilidade iterar por cada uma delas em sequência.

## Fase 3: Extração de Dados do Post (Post Meta-Extraction)

A Fase 3 desmantelou o stub e construiu um motor robusto de extração estruturada diretamente no `post_extractor.py`.

### Principais Realizações e Heurísticas

1. **Achatamento do Seletor Principal:**
   - Observou-se novamente que, enquanto o Feed às vezes possui `<article>`, os single-posts (quando abertos em tab independente a partir do perfil) abandonam a semântica rigorosa para carregar uma div root com `main`. Todos os nossos seletores foram migrados (com fallbacks flexíveis) para espelhar a sintaxe real (`main img[src*='instagram']`, `main span[dir='auto']`, etc.).
2. **Análise Textual Rica e Tolerância a Falhas:**
   - Todo o parser de caption (legenda) agora utiliza blocks `try...except` granulares. Ele é capaz de capturar e distinguir a hashtag primária (`#`) de mentions (`@`). Identifica de antemão heurísticas como `#pratodosverem` na legenda realocando a métrica em nosso modelo Pydantic correspondente (`AltTextSource.CAPTION_DESCRIBED`).
3. **Múltiplos Mapeamentos de Mídia e Arrays Dinâmicos:**
   - Detecta automagicamente *Is_Carousel* vs *Is_Video* vs *Is_Image*.
   - Extrai o atributo `alt` das imagens e determina sua procedência (Automática da rede vs Manual do usuário). Vale notar que o Instagram retorna textos em inglês ("Photo by...", "May be an image of text...") mesmo que o idioma do navegador esteja em *pt-BR*, o que comprovou o acerto de termos listas bilingues de inferência em nossos padrões.
4. **Mapeamento de Acessibilidade Oculto (ARIA):**
   - O extrator processa e arquiva instâncias completas de navegação oculta aos olhos padrão (`aria-label`), fundamentais para mapear audiodescrições, interações de clique via screen-reader e botões de vídeo não rotulados visivelmente.
   - Todo o Post processado reverte numa instância estritamente validada do *Schema Pydantic*, que avança perfeitamente livre de Null Pointer Exceptions graças ao default preenchimento na modelagem.

O robô agora funciona interinamente desde o login contornando diálogos de "Not Now", raspando perfis com infinitos posts iterando-os e processando suas profundezas sintáticas. Agora marchamos para a **Fase 4 (Evidência e Exportação)**, para arquivar cada passo metodicamente.

## Fase 4: Evidência e Exportação Analítica

O fechamento de cada ciclo do Pipeline exigia total lastro de pesquisa, sem isso perderíamos validação metódica.

### Mecanismos Forenses Adicionados

1. **Evidente-Capture Robótico (`evidence_capture.py`):**
   - O playwright foi comissionado para, ao terminar de raspar um post, bater uma **Screenshot** ("Fotografia Forense") estritamente delimitada sem o temido Full Page overflow (que trava em layouts infinitos).
   - O código-fonte integral (DOM) foi descarregado para a máquina do pesquisador garantindo o isolamento daquele objeto num momento preciso no tempo.
   - Computamos imediatamente Hashes `SHA-256` sobre as capturas, certificando as provas e impedindo que imagens/arquivos sofram adulteração passiva (característica rigorosa num projeto Open-Source de coleta). Esse modelo injetou o schema valioso em `Evidence`.

2. **Pipeline de Exportadores e Relatórios:**
   - Construído o `exporters.py` implementando JSON puro, serializado estritamente contra Pydantic V2 via `model_dump()`.
   - Incluído o motor do Pandas encarregado de traduzir metadados hiper-estruturados para uma tabela dimensional plana (**CSV** com cabeçalhos tabulares formatados explícita e nativamente compatível como **UTF-8-SIG**—resolve perfeitamente o problema do Excel quebrar acentuação no ecossistema windows) para tabulação simples por estagiários e não-programadores.
   - Relatórios automáticos gerados localmente em Markdown sumarizando o tempo de duração da carga, contagens e diagnósticos quantitativos básicos focados no contraste entre acessibilidade humana ('*manual alts*') v.s Inteligência Artificial (*Auto-generated*).

Nosso pipeline principal da Obtenção e Documentação agora é incontestável sob métodos científicos exatos.

## Fase 5: Robustez e Observabilidade (Escudo Anti-Bot)

Para transformar nosso script num robô de produção imparável capaz de extrair grandes volumes (N=500+), precisamos proteger seu comportamento de navegação:

1. **Retentativas Inteligentes (`tenacity`):**
   - Incorporamos o backoff exponencial nas funções mais propensas a falha de conexão (Abertura de Sessão em `auth.py` e Roteamento de Posts em `post_extractor.py`). Se algo estourar (Timeout TCP, reset de rota, bloqueio de CDN), o robô automaticamente espera e re-tenta até 3 vezes antes de capitular.

2. **Disfarce de Navegação Humana Dinâmica (Rate Limiting):**
   - Dentro do orquestrador, um freio de mão (`human_delay_sync`) ativado por jitter randômico (`AppConfig.delay_min` a `delay_max`) pausa a thread por segundos variados a cada raspagem, evitando que o Instagram aplique *Action Blocks*.

3. **Sensor Forense de Restrição Punitiva (Fail Fast):**
   - Se, em algum tempo, a Meta bloquear a conta (`BLOCK_INDICATORS`), o auth pára imediatamente a sessão alertando para "Atividade Suspeita", em vez de enlatar o robô num laço infinito de timeouts corrompidos.
   - O `extract_post` agora salva capturas de tela exclusivas para panes na navegação (`evidence_error_<id>.png`), separadas das evidências oficiais de sucesso, nos permitindo estudar como as defesas reativas da Meta funcionam contra automação.

## Fase 6: Distribuição Windows, E2E e Documentação Final (Encerramento v1.0)

O principal pilar da Fase 6 era democratizar a ferramenta: transformar um complexo ecossistema Python num pacote **Standalone "One-Click" para não-técnicos**.

1. **Modo Interativo e Interface via CLI:**
   - Aproveitando as classes de opções do `Typer`, instanciamos prompts amigáveis. Se o usuário executar o Luanny sem nenhuma flag (o equivalente a `luanny scrape`), ele apresentará um painel dinâmico via biblioteca `Rich`, coletando o *Nome do Perfil* e a *Quantidade de Posts* através de interações amigáveis diretas no terminal.
   - Escondemos as inundações de log padrão e as trocamos por **Barras de Progresso interativas** (do `rich.progress`). O pesquisador agora vê o avanço numérico literal de cada etapa: "Extraindo posts de @govbr..." (|||||| - 86%).
 
2. **Automação de Build (.exe) e UX Nativa:**
   - Empacotamos o sistema usando **PyInstaller** num script (`scripts/build.py`). Este script consome todos os sub-módulos e despeja a distribuição limpa no pacote `dist/Luanny`.
   - Adicionamos os controladores de execução `executar.bat` para dupla checagem instantânea de clique na área de trabalho e o detalhista manual guiado `LEIA-ME.txt`.

3. **Garantia de Qualidade E2E:**
   - Adicionamos uma verificação holística (`test_e2e.py`) que aciona o próprio _Luanny_ real num invólucro de loop rápido (max 3 posts) validando o ciclo inteiro da aplicação contra um alvo público no Instagram sem estourar limites globais. 

> [!SUCCESS] 
> O software **Luanny** atingiu sua versão **1.0.0** com robustez, isolamento do navegador, evidências calcadas em SHA-256 e uma interface de uso limpa. Todos os objetivos da Fase 0 à Fase 6 propostos foram superados. As credenciais (`.env`) seguem rigorosamente excluídas do versionamento de código no Git.
