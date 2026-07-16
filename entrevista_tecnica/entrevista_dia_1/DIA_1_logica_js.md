# Dia 1 — Lógica, JavaScript/TypeScript e Estruturas de Dados

> Progresso geral: [PROGRESSO.md](PROGRESSO.md)

**Objetivo:** garantir que a base (a parte que mais pesa numa entrevista júnior) está sólida.

---

## Teoria (checklist)

- [✅] Tipos primitivos, coerção, `==` vs `===`, `let/const/var`, escopo (block scope vs function scope), closures.
- [✅] Funções: arrow function vs function declaration, `this`, higher-order functions (`map`, `filter`, `reduce`).
- [✅] Estruturas de dados: array, objeto, `Map`, `Set` — quando usar cada um.
- [✅] Complexidade básica: O(1), O(n), O(n²) — saber reconhecer, não precisa aprofundar.
- [✅] TypeScript básico: tipagem de variáveis, interfaces, `type`, diferença de `interface` vs `type`.

---

## Exercícios (20)

Resolva em `entrevista_tecnica/modelo/` ou em arquivos `.js`/`.ts` novos. Sem copiar solução pronta — o objetivo é treinar o raciocínio para live coding.

1. ✅ Corrigir o bug em `entrevista_tecnica/modelo/pares.js` (a função ignora o parâmetro `numeros` e usa a variável global `pares`).
2. ✅ FizzBuzz de 1 a 100.
3. ✅ Inverter uma string sem usar `.reverse()` ou `.split('').reverse().join('')` prontos — implementar na mão com loop.
4. ✅ Verificar se uma string é palíndromo (ignorando espaços e maiúsculas/minúsculas).
5. ⏳ Encontrar o maior valor de um array sem usar `Math.max`.
6. ⏳ Encontrar o menor valor de um array sem usar `Math.min`.
7. ⏳ Remover elementos duplicados de um array (implementação manual, depois refazer com `Set`).
8. ⏳ Somar todos os números pares de um array usando `reduce`.
9. ⏳ Dado um array de objetos `{ nome, idade }`, retornar só os nomes das pessoas maiores de idade usando `filter` + `map`.
10. ⏳ Contar quantas vezes cada palavra aparece em uma frase (retornar um objeto `{ palavra: contagem }`).
11. ⏳ Implementar uma função `soma(a, b)` e explicar em voz alta a diferença entre declará-la como `function soma(a, b) {}` e `const soma = (a, b) => {}`.
12. ⏳ Escrever uma closure: uma função `criarContador()` que retorna outra função que incrementa e retorna um contador interno a cada chamada.
13. ⏳ Verificar se dois arrays têm os mesmos elementos, independente da ordem.
14. ⏳ Implementar `achatar(array)` que transforma um array de arrays (`[[1,2],[3,4]]`) em um array simples (`[1,2,3,4]`), sem usar `.flat()`.
15. ⏳ Dado um array de números, agrupar em pares e ímpares usando `Map` (`Map<'par'|'impar', number[]>`).
16. ⏳ Escrever uma função `debounce(fn, delay)` simplificada (não precisa ser perfeita, o objetivo é entender o conceito).
17. ⏳ Converter um array de objetos para TypeScript: criar uma `interface Livro { id: number; titulo: string; autor: string; estoque: number }` e tipar uma função `listarComEstoqueBaixo(livros: Livro[], limite: number): Livro[]`.
18. ⏳ Explicar e demonstrar em código a diferença entre cópia rasa (`shallow copy`, ex: spread `{...obj}`) e cópia profunda de um objeto aninhado.
19. ⏳ Implementar uma busca binária simples em um array ordenado (praticar O(log n) e saber explicar por que é mais rápido que busca linear).
20. ⏳ Implementar uma função recursiva de fatorial e outra de Fibonacci; explicar o caso base de cada uma.

---

## Perguntas de entrevista (responda sem consultar)

1. Qual a diferença entre `==` e `===` em JavaScript?
2. O que é uma closure? Dê um exemplo prático.
3. Qual a diferença entre `map`, `filter` e `reduce`?

---

## Dúvidas do dia

| Exercício | Dúvida | Resolvido? |
|-----------|--------|------------|
| | | |
