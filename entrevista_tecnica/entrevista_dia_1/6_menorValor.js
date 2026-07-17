/**
 * Exercício 6 — Menor valor de um array
 *
 * Escreva uma função `menorValor(numeros)` que recebe um array de
 * números e retorna o menor valor, SEM usar `Math.min`.
 *
 * Exemplo:
 * menorValor([3, 7, 2, 9, 4]) // 2
 * menorValor([-5, -1, -10]) // -10
 */

function menorValor(numeros) {
  // implemente aqui
  let menor = numeros[0]
  for(let n =0; n < numeros.length; n++){
    if(numeros[n] < menor){
      menor = numeros[n]
    }
  }

  return menor
}

console.log(menorValor([3, 7, 2, 1, 9, 4]));
console.log(menorValor([-5, -1, -100]));
