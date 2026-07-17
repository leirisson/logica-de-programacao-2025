/**
 * Exercício 14 — Achatar um array de arrays
 *
 * Escreva uma função `achatar(array)` que transforma um array de
 * arrays em um array simples, SEM usar `.flat()`.
 *
 * Exemplo:
 * achatar([[1, 2], [3, 4]]) // [1, 2, 3, 4]
 * achatar([[1], [2, 3], [4, 5, 6]]) // [1, 2, 3, 4, 5, 6]
 */

function achatar(array) {
  // implemente aqui
  const arrayCompleto = []
  for(i=0; i < array.length; i++){
    for(j=0; j < array[i].length; j++){
        arrayCompleto.push(array[i][j])
    }
  }

  return arrayCompleto
}

console.log(achatar([[1, 2], [2, 3, 4]]));
console.log(achatar([[1], [2, 3], [4, 5, 6]]));
