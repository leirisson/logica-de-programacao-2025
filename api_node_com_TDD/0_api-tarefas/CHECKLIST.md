# Checklist — api-tarefas

## Fase 1 — Setup do Ambiente

- [x] Criar estrutura de pastas (`src/`, `tests/`)
- [x] Criar `package.json`
- [x] Criar `docker-compose.yml`
- [x] Configurar Postgres no `docker-compose.yml`
- [x] Instalar dependências de produção: `fastify`, `@prisma/client`
- [x] Instalar dependências de desenvolvimento: `typescript`, `vitest`, `prisma`, `tsx`
- [x] Configurar scripts no `package.json` (`test`, `dev`)
- [x] Configurar validação de variáveis de ambiente (`src/env/index.ts` com Zod)
- [x] Criar `tsconfig.json`
- [x] Criar `vitest.config.ts`
- [x] Subir o banco com `docker compose up -d` e confirmar que conecta

## Fase 2 — Primeiro teste (sem banco ainda)

- [x] Criar rota `GET /health` em `src/app.ts`
- [x] Escrever teste RED: `tests/health.test.ts`
- [x] Fazer o teste passar (GREEN)
- [x] Refactor: extrair rota para `src/routes/index.ts`

## Fase 3 — Prisma + Banco

- [x] Inicializar Prisma (`npx prisma init`)
- [x] Definir model `Task` no `schema.prisma` com enum `PRIORIDADE`
- [x] Rodar primeira migration
- [x] Corrigir `dataConclusao` para nullable e rodar segunda migration
- [x] Confirmar tabela criada no banco

## Fase 4 — CRUD de Tarefas (TDD)

- [x] `POST /tarefas` — criar tarefa
- [x] Limpar banco após cada teste com `afterEach`
- [x] `GET /tarefas` — listar todas
- [x] `GET /tarefas/:id` — buscar por id (200 encontrado, 404 não encontrado)
- [ ] `PATCH /tarefas/:id` — atualizar
- [ ] `DELETE /tarefas/:id` — deletar

## Fase 5 — Validação e Erros

- [ ] Retornar `400` quando dados obrigatórios estiverem ausentes
- [ ] Retornar `404` quando tarefa não existir
- [ ] Testar todos os casos de erro com TDD

---

> Marque cada item com `[x]` conforme for concluindo.
