/**
 * Exercício 5 — Maior valor de um array
 *
 * Escreva uma função `maiorValor(numeros)` que recebe um array de
 * números e retorna o maior valor, SEM usar `Math.max`.
 *
 * Exemplo:
 * maiorValor([3, 7, 2, 9, 4]) // 9
 * maiorValor([-5, -1, -10]) // -1
 */

function maiorValor(numeros) {
  // implemente aqui
  let maior = numeros[0]

  for (let i = 0; i < numeros.length; i++) {
    if (numeros[i] > maior) {
      maior = numeros[i]
    }
  }

  return maior


}

console.log(maiorValor([53, 117, 2, 19, 4]));
console.log(maiorValor([-5, -1, -10]));
