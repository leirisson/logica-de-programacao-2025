# Dia 2 — Node.js, APIs REST e TDD

> Progresso geral: [PROGRESSO.md](PROGRESSO.md)

**Objetivo:** dominar o back-end pedido na vaga (Node.js + REST + testes).

Use `api_node_com_TDD/regras_TDD_Estudos.md` como referência de ciclo RED → GREEN → REFACTOR — não precisa reler tudo, mas volte lá quando travar em alguma fase.

---

## Teoria (checklist)

- [ ] O que é Node.js, event loop (não precisa aprofundar internals, mas saber explicar que é single-threaded com I/O não-bloqueante).
- [ ] REST: verbos HTTP (GET/POST/PUT/PATCH/DELETE), status codes (200, 201, 400, 401, 403, 404, 500), idempotência.
- [ ] Estrutura de uma API Express: rotas, middlewares, tratamento de erros.
- [ ] Validação de entrada (ex: `zod`, `joi`, ou validação manual).
- [ ] TDD: ciclo RED → GREEN → REFACTOR.

---

## Exercícios (20)

Domínio sugerido para todos os exercícios de API: **livros e estoque** (mesmo domínio já usado no repo). Sempre que possível, escreva o teste antes (RED → GREEN → REFACTOR).

1. [ ] Montar a estrutura `src/app.js` (sem `listen()`) + `src/server.js` (com `listen()`) e explicar por que essa separação existe.
2. [ ] Escrever teste + implementação de `GET /health` retornando `{ status: 'ok' }`.
3. [ ] Escrever teste + implementação de `GET /livros` retornando uma lista fixa (array em memória).
4. [ ] Escrever teste + implementação de `GET /livros/:id` retornando 404 quando o id não existe.
5. [ ] Escrever teste + implementação de `POST /livros` criando um livro e retornando 201 com o objeto criado (incluindo `id`).
6. [ ] Escrever teste garantindo que `POST /livros` retorna 400 se `titulo` estiver ausente.
7. [ ] Escrever teste garantindo que `POST /livros` retorna 400 se `estoque` for negativo.
8. [ ] Escrever teste + implementação de `PUT /livros/:id` substituindo todos os campos do livro.
9. [ ] Escrever teste + implementação de `PATCH /livros/:id/estoque` atualizando só o campo estoque.
10. [ ] Escrever teste + implementação de `DELETE /livros/:id` retornando 204.
11. [ ] Implementar um middleware de log simples (loga método + rota + tempo de resposta) e testar que ele não quebra as rotas existentes.
12. [ ] Implementar um middleware de tratamento de erro centralizado (`app.use((err, req, res, next) => ...)`) e testar que erros lançados nas rotas caem nele.
13. [ ] Refatorar a validação manual de `POST /livros` para usar uma lib de schema (`zod` ou `joi`) — comparar antes/depois.
14. [ ] Escrever um teste que mocka uma "camada de repositório" (`livroRepository`) para isolar a lógica de negócio do acesso a dados (usar `jest.mock`).
15. [ ] Implementar a rota `GET /livros?estoqueMin=5` filtrando por query param, com teste cobrindo o filtro.
16. [ ] Explicar e demonstrar em teste a diferença de comportamento entre `PUT` (substitui tudo) e `PATCH` (atualiza parcialmente) na mesma rota de livro.
17. [ ] Escrever um teste de integração que cria um livro (`POST`) e depois busca ele (`GET /livros/:id`) na sequência, validando que os dados batem.
18. [ ] Adicionar paginação simples em `GET /livros` (`?page=1&limit=10`) com teste garantindo que o tamanho da página é respeitado.
19. [ ] Rodar `npm run test:coverage` (ou equivalente) sobre o que foi construído e identificar uma linha sem cobertura — escrever o teste que falta.
20. [ ] Documentar as rotas construídas em um pequeno `README.md` da API (rota, verbo, body esperado, respostas possíveis) — praticar comunicação técnica escrita.

---

## Perguntas de entrevista

1. Qual a diferença entre PUT e PATCH?
2. Como você estruturaria uma API REST para um recurso de "produtos"? Quais rotas e verbos?
3. O que é TDD e por que você escreveria o teste antes do código?

---

## Dúvidas do dia

| Exercício | Dúvida | Resolvido? |
|-----------|--------|------------|
| | | |
