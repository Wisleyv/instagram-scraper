# Projeto Luanny — Planejamento e Acompanhamento

## Fase 1: Browser e Autenticação (CONCLUÍDA)

### Configuração e Infraestrutura
- [x] Configurar Chromium no ambiente (`playwright install chromium`)
- [x] Criar arquivo `.env` a partir do template com credenciais da conta de teste

### Implementação de `browser.py`
- [x] Desenvolver `BrowserSession` dataclass (encapsula contexto, página, etc.)
- [x] Implementar `create_browser_context` (viewport fixo 1280x720, idioma `pt-BR`)
- [x] Implementar `close_browser_context` (fechamento ordenado para não deixar processos zumbis)
- [x] Implementar helpers de delay humano e `storage_state`

### Implementação de `auth.py`
- [x] Implementar fluxo de login principal com fallbacks para múltiplos seletores (tratando mudanças de DOM do Instagram)
- [x] Implementar persistência e reuso de sessão (`storage_state.json`)
- [x] Implementar detecção e fallback interativo para Checkpoints/2FA (modo `--headed`)
- [x] Implementar dispensa preventiva de banners de cookies e GDPR

### Integração e Testes
- [x] Substituir stubs no `orchestrator.py` pelas implementações reais
- [x] Atualizar stubs das Fases 2-4 para aceitar `BrowserSession` em vez de tipos genéricos
- [x] Escrever testes unitários com mocks de Playwright para Fases 0 e 1 (>50 testes passando)
- [x] Executar testes holísticos (Login Real + Reuso de Sessão)

---

## Fase 2: Descoberta de Postagens (CONCLUÍDA)
- [x] Analisar DOM e comportamento do Instagram no carregamento do grid de posts.
- [x] Implementar `profile_discovery.py` com rolagem (scroll) progressiva até o final do virtual grid.
- [x] Identificar e extrair URLs validas de postagens do grid, limitadas por `--max-posts`, parseando as slugs corretas das rotas absolutas do React Router.
- [x] Atualizar os seletores do grid (`main a[href*="/p/"]` testado, revertendo para o simples `a[href*="/p/"]` que reflete a árvore DOM correta para o list-renderer atual da meta).
- [x] Desenvolver testes unitários completos para o `profile_discovery`.

---

## Fase 3: Extração de Dados (CONCLUÍDA)
- [x] Implementar a navegação sequencial por IDs recebidas e parse real do DOM na postagem interna individual.
- [x] Extrair Caption, hashtags, mentions e expandir tag "more/mais".
- [x] Extrair metadados e heurísticas bilíngues para determinar automaticamente Alt Text (Auto-generated pt-BR/en-US ou manual).
- [x] Detectar tipo de mídia corretamente (imagem, vídeo, carrossel).
- [x] Extrair ARIA labels estruturados.

---

## Fase 4: Evidência e Exportação (CONCLUÍDA)
- [x] Mapear o schema `Evidence` para capturar as informações na etapa de persistência.
- [x] Implementar mecanismo de Printscreen (`screenshot` nativo do playwright) salvando como `.png`.
- [x] Salvar código-fonte estrutural (HTML) do DOM individual e extrair Hashes (SHA-256).
- [x] Formatar o dicionário Python final consolidado.
- [x] Exportar toda a saída padronizada.

---

## Fase 5: Robustez e Observabilidade (CONCLUÍDA)
- [x] **(5.1) Retries com backoff:** Adicionar decoradores `tenacity` em chamadas de rede no `browser.py`, `auth.py` e `post_extractor.py`.
- [x] **(5.2) Timeouts:** Consolidar uso dos timeouts globais via `AppConfig`.
- [x] **(5.3) Rate limiting:** Implementar sleep com jitter configurável no `orchestrator.py` para não violar os limites do Meta.
- [x] **(5.4) Evidência de Erro:** Capturar screenshot e HTML de falhas operacionais não tratadas (crash log visual).
- [x] **(5.5) Detecção de bloqueios da Meta:** Identificar "Action Blocks", "Challenge Required" no frontend para pausar graciosamente ao invés de estourar timeout na view do Playwright.
- [x] **(5.6) Contextualized Logs:** Enriquecer `structlog` com meta_info e traceback amigável.
- [x] **(5.7) Testes de Robustez:** Validar resiliência com timeouts e exceções injetadas.

---

## Fase 6: Distribuição Windows, Testes E2E e Documentação (CONCLUÍDA)
- [x] **(6.1) Modo interativo:** Criar prompts em pt-BR via Typer (Rich) em `cli.py`.
- [x] **(6.2) Barra de Progresso:** Implementar bar na main loop do orchestrator.
- [x] **(6.3) Teste E2E:** Criar `tests/test_e2e.py` que aponta para um perfil fixo validando todos os layers até o output.
- [x] **(6.4) Build:** Script PyInstaller `build.py` lidando com o empacotamento do Playwright e Chromium num folder distribuível.
- [x] **(6.5) UX para o usuário final:** Criar os atalhos ou scripts `executar.bat` e manual `LEIA-ME.txt`.
