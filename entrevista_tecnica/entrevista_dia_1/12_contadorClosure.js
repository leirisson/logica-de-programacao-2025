/**
 * Exercício 12 — Closure: criarContador
 *
 * Escreva uma função `criarContador()` que retorna outra função.
 * Cada vez que a função retornada é chamada, ela incrementa e
 * retorna um contador interno.
 *
 * Exemplo:
 * const contar = criarContador();
 * contar(); // 1
 * contar(); // 2
 * contar(); // 3
 *
 * const outroContador = criarContador();
 * outroContador(); // 1 (independente do primeiro)
 */

function criarContador() {
  // implemente aqui
}

const contar = criarContador();
console.log(contar());
console.log(contar());
console.log(contar());
