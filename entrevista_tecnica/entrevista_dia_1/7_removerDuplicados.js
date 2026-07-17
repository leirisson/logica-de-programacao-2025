/**
 * Exercício 7 — Remover duplicados de um array
 *
 * 1) Escreva `removerDuplicadosManual(array)` que remove elementos
 *    duplicados SEM usar `Set` (implementação manual, ex: com loop
 *    e verificação de existência).
 *
 * 2) Depois, escreva `removerDuplicadosComSet(array)` que faz a
 *    mesma coisa, mas usando `Set`.
 *
 * Exemplo:
 * removerDuplicadosManual([1, 2, 2, 3, 4, 4, 5]) // [1, 2, 3, 4, 5]
 * removerDuplicadosComSet([1, 2, 2, 3, 4, 4, 5]) // [1, 2, 3, 4, 5]
 */

function removerDuplicadosManual(array) {
  // implemente aqui

  let novoArray = []

  for(let index=0; index < array.length; index++){
    if(!novoArray.includes(array[index])){
      novoArray.push(array[index])
    } 
  }

  return novoArray
}

function removerDuplicadosComSet(array) {
  // implemente aqui
  const valores = new Set(array)
  return Array.from(valores)
}

console.log(removerDuplicadosManual([1, 2, 2, 3, 4, 4, 5]));
console.log(removerDuplicadosComSet([1, 2, 2, 3, 4, 4, 5]));
