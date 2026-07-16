# Dia 3 — Banco de Dados SQL e Git

> Progresso geral: [PROGRESSO.md](PROGRESSO.md)

**Objetivo:** cobrir os dois requisitos obrigatórios que não são só "programação".

Domínio usado nos exercícios de SQL: tabelas `autores`, `livros`, `vendas` (mesmo domínio de livros/estoque do repo).

```sql
-- Schema de referência para os exercícios
CREATE TABLE autores (
  id SERIAL PRIMARY KEY,
  nome VARCHAR(100) NOT NULL
);

CREATE TABLE livros (
  id SERIAL PRIMARY KEY,
  titulo VARCHAR(200) NOT NULL,
  autor_id INTEGER REFERENCES autores(id),
  estoque INTEGER NOT NULL DEFAULT 0,
  preco NUMERIC(10,2) NOT NULL
);

CREATE TABLE vendas (
  id SERIAL PRIMARY KEY,
  livro_id INTEGER REFERENCES livros(id),
  quantidade INTEGER NOT NULL,
  data_venda DATE NOT NULL
);
```

---

## Teoria SQL (checklist)

- [ ] Modelagem básica: chave primária, chave estrangeira, relacionamento 1:N e N:N.
- [ ] Comandos: `SELECT`, `WHERE`, `JOIN` (INNER, LEFT), `GROUP BY`, `ORDER BY`, `LIMIT`.
- [ ] Diferença entre `JOIN` e subquery.
- [ ] Índices — o que são e por que aceleram consultas (nível conceitual).
- [ ] Normalização básica (1FN, 2FN, 3FN — só o conceito).

## Teoria Git (checklist)

- [ ] Fluxo básico: `clone`, `add`, `commit`, `push`, `pull`, `branch`, `merge`.
- [ ] O que é um conflito de merge e como resolver.
- [ ] Diferença entre `merge` e `rebase` (nível conceitual).
- [ ] GitFlow: branches `main`, `develop`, `feature/*`, `hotfix/*` — a vaga menciona isso explicitamente.
- [ ] `.gitignore`, boas práticas de mensagens de commit.

---

## Exercícios (20)

### SQL (1-12) — escreva a query de próprio punho, sem IDE/autocomplete

1. [ ] Listar todos os livros com seus respectivos autores (`JOIN` simples).
2. [ ] Listar apenas livros do autor "Machado de Assis" (`WHERE` + `JOIN`).
3. [ ] Contar quantos livros cada autor tem (`GROUP BY` + `COUNT`).
4. [ ] Listar autores que têm mais de 3 livros (`GROUP BY` + `HAVING`).
5. [ ] Listar livros com estoque abaixo de 5 unidades, ordenados do menor para o maior estoque.
6. [ ] Listar livros que nunca foram vendidos (`LEFT JOIN` com `vendas` + `IS NULL`).
7. [ ] Calcular a receita total (`quantidade * preco`) por livro.
8. [ ] Top 3 autores com mais livros vendidos no total (`JOIN` livros+vendas, `GROUP BY` autor, `ORDER BY` + `LIMIT`).
9. [ ] Listar vendas feitas no último mês (filtro de data).
10. [ ] Atualizar o estoque de um livro específico após uma venda (`UPDATE ... SET estoque = estoque - X WHERE id = Y`).
11. [ ] Escrever a mesma consulta do exercício 6 usando subquery em vez de `LEFT JOIN`, e explicar em voz alta a diferença de abordagem.
12. [ ] Explicar (por escrito, uma frase) por que colocar um índice em `livros.autor_id` ajudaria a consulta do exercício 1 a performar melhor em uma tabela grande.

### Git (13-20) — executar de verdade no terminal, em um repo de teste

13. [ ] Criar um repositório de teste, fazer o primeiro commit e revisar `git log --oneline`.
14. [ ] Criar uma branch `feature/teste`, fazer uma alteração, commitar, e voltar para `main` sem perder o trabalho.
15. [ ] Simular um conflito de merge: editar a mesma linha de um arquivo em `main` e em `feature/teste`, tentar `git merge feature/teste` e resolver o conflito manualmente.
16. [ ] Praticar `git stash` — alterar um arquivo, guardar com stash, trocar de branch, voltar e recuperar com `git stash pop`.
17. [ ] Fazer um commit "errado" de propósito (mensagem ruim, mistura de assuntos) e depois corrigir com `git commit --amend` (antes de dar push).
18. [ ] Criar uma branch `hotfix/bug-x` a partir de `main`, corrigir algo, mergear de volta — praticando o fluxo GitFlow.
19. [ ] Escrever um `.gitignore` do zero para um projeto Node (ignorar `node_modules`, `.env`, `dist`, etc.).
20. [ ] Explicar em voz alta, sem terminal, a diferença entre `git merge` e `git rebase` e em que cenário você escolheria cada um.

---

## Perguntas de entrevista

1. Qual a diferença entre INNER JOIN e LEFT JOIN?
2. Como você resolve um conflito de merge no Git?
3. O que é uma chave estrangeira e por que ela é importante?

---

## Dúvidas do dia

| Exercício | Dúvida | Resolvido? |
|-----------|--------|------------|
| | | |
