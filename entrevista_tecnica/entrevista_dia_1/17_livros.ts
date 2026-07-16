/**
 * Exercício 17 — TypeScript básico
 *
 * 1) Crie uma interface `Livro` com: id (number), titulo (string),
 *    autor (string), estoque (number).
 *
 * 2) Tipe uma função `listarComEstoqueBaixo(livros: Livro[], limite: number): Livro[]`
 *    que retorna os livros com estoque menor ou igual ao limite.
 *
 * Exemplo:
 * listarComEstoqueBaixo(livros, 5)
 * // retorna só os livros com estoque <= 5
 */

interface Livro {
  // implemente aqui
}

function listarComEstoqueBaixo(livros: Livro[], limite: number): Livro[] {
  // implemente aqui
}

const livros: Livro[] = [
  { id: 1, titulo: 'Clean Code', autor: 'Robert C. Martin', estoque: 3 },
  { id: 2, titulo: 'O Hobbit', autor: 'J.R.R. Tolkien', estoque: 12 },
  { id: 3, titulo: 'Refactoring', autor: 'Martin Fowler', estoque: 5 },
];

console.log(listarComEstoqueBaixo(livros, 5));
