/**
 * Exercício 19 — Busca binária
 *
 * Escreva uma função `buscaBinaria(array, alvo)` que busca `alvo`
 * em um array JÁ ORDENADO, retornando o índice se encontrar, ou -1
 * se não encontrar.
 *
 * Depois, explique por que é O(log n) e por que é mais rápido que
 * busca linear (O(n)).
 *
 * Exemplo:
 * buscaBinaria([1, 3, 5, 7, 9, 11], 7) // 3
 * buscaBinaria([1, 3, 5, 7, 9, 11], 4) // -1
 */

function buscaBinaria(array, alvo) {
  // implemente aqui
  let inicio = 0
  let fim = array.length - 1

  while (inicio <= fim) {
    let meio = Math.floor((inicio + fim) / 2)
    if (array[meio] === alvo) {
      return meio
    } else if (array[meio] < alvo) {
      inicio = meio + 1
    } else if (array[meio] > alvo) {
      fim = meio - 1
    }


  }

  return -1
}

console.log(buscaBinaria([1, 3, 5, 7, 9, 11], 5));
console.log(buscaBinaria([1, 3, 5, 7, 9, 11], 9));

/**
 * Explicação (escreva aqui com suas palavras):
 * sempre verifica se o valor procurado é maior ou menor do que a metade do array 
 * assim reduzindo o tempo de busca do valor
 *
 */
