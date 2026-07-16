/**
 * Exercício 3 — Inverter uma string
 *
 * Escreva uma função `inverterString(str)` que recebe uma string e
 * retorna ela invertida.
 *
 * Regras:
 * - Não pode usar `.reverse()`
 * - Não pode usar `.split('').reverse().join('')`
 * - Implementar na mão, usando um loop (for/while)
 *
 * Exemplo:
 * inverterString('hello') // 'olleh'
 * inverterString('JavaScript') // 'tpircSavaJ'
 */

function inverterString(str) {
  let tamanho = str.length -1
  let resultado = ''
  
  for(tamanho; tamanho >= 0; tamanho--){
    resultado += str[tamanho]
  }

  return resultado
}

console.log(inverterString('JavaScript'));
