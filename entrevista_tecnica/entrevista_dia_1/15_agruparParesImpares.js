/**
 * Exercício 15 — Agrupar pares e ímpares usando Map
 *
 * Escreva uma função `agruparParesImpares(numeros)` que recebe um
 * array de números e retorna um `Map<'par'|'impar', number[]>`
 * agrupando os números em pares e ímpares.
 *
 * Exemplo:
 * agruparParesImpares([1, 2, 3, 4, 5])
 * // Map(2) { 'impar' => [1, 3, 5], 'par' => [2, 4] }
 */

function agruparParesImpares(numeros) {
  // implemente aqui
  const mapa = new Map()
  mapa.set('par', [])
  mapa.set('impar', [])

  for(let index = 0; index < numeros.length; index++){
    if(numeros[index] % 2 == 0){
       mapa.get('par').push(numeros[index])
    } else {
      mapa.get('impar').push(numeros[index])
    }
  }

  return mapa

}

console.log(agruparParesImpares([1, 2, 3, 4, 5]));
