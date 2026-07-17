/**
 * Exercício 13 — Verificar se dois arrays têm os mesmos elementos
 *
 * Escreva uma função `mesmosElementos(a, b)` que verifica se dois
 * arrays têm os mesmos elementos, independente da ordem.
 *
 * Exemplo:
 * mesmosElementos([1, 2, 3], [3, 2, 1]) // true
 * mesmosElementos([1, 2, 3], [1, 2, 4]) // false
 * mesmosElementos([1, 2], [1, 2, 3]) // false (tamanhos diferentes)
 */

function mesmosElementos(a, b) {
  // implemente aqui
  if (a.length !== b.length) {
    return false
  } else {
    for (index = 0; index < b.length; index++) {
      if (!a.includes(b[index])) {
        return false
      }
    }
    return true
  }

}

console.log(mesmosElementos([1, 2, 3, ], [3, 2, 1]));
console.log(mesmosElementos([1, 2, 3], [1, 2, 4]));
console.log(mesmosElementos([1, 2], [1, 2, 3]));
