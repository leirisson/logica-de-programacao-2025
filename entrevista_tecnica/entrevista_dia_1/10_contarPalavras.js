/**
 * Exercício 10 — Contar ocorrências de palavras
 *
 * Escreva uma função `contarPalavras(frase)` que recebe uma frase e
 * retorna um objeto `{ palavra: contagem }` com quantas vezes cada
 * palavra aparece.
 *
 * Exemplo:
 * contarPalavras('o gato e o cachorro e o passaro')
 * // { o: 3, gato: 1, e: 2, cachorro: 1, passaro: 1 }
 */

function contarPalavras(frase) {
  // implemente aqui
  let fraseNova = frase.split(" ")
  const contagem = {}

  for (let index = 0; index < fraseNova.length; index++) {
    const palavra = fraseNova[index]

    if (contagem[palavra]) {
      contagem[palavra] += 1
    } else {
      contagem[palavra] = 1
    }
  }

  return contagem
}

console.log(contarPalavras('o gato e o cachorro e o passaro'));
