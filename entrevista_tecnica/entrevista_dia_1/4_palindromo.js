/**
 * Exercício 4 — Verificar se uma string é palíndromo
 *
 * Escreva uma função `ehPalindromo(str)` que recebe uma string e
 * retorna `true` se ela for um palíndromo, `false` caso contrário.
 *
 * Regras:
 * - Ignorar espaços
 * - Ignorar diferença entre maiúsculas e minúsculas
 *
 * Exemplo:
 * ehPalindromo('Osso') // true
 * ehPalindromo('A base do teto desaba') // true
 * ehPalindromo('JavaScript') // false
 */

function ehPalindromo(str) {
  // implemente aqui
  const limpa = str.toLowerCase().replaceAll(' ', '')
  let esquerda = 0
  let direita = limpa.length - 1

  while(esquerda < direita){
    if(limpa[esquerda] === limpa[direita]){
      esquerda++
      direita--
    } else {
      return false
    }
  }

  return true

}



console.log(ehPalindromo('Osso'));
console.log(ehPalindromo('A base do teto desaba'));
console.log(ehPalindromo('JavaScript'));

/**
 * Comentários da correção:
 *
 * 1) Lógica correta, mas redundante: você fez DOIS loops separados
 *    (um de trás pra frente, outro de frente pra trás) pra construir
 *    duas strings e comparar. Funciona, mas é O(2n) e código duplicado
 *    (a única diferença entre os loops é a direção do índice).
 *    É possível resolver com um único loop: monte só a versão
 *    "sem espaço e minúscula" (um loop), e depois compare essa string
 *    com ela mesma invertida (reaproveitando a lógica do exercício 3,
 *    inverterString). Ou, ainda mais simples: com dois ponteiros
 *    (início e fim) andando um em direção ao outro, comparando
 *    caractere a caractere — nem precisa montar string nova.
 *
 * 2) `resultado` e `semEspaco` são nomes que não refletem o que cada
 *    variável guarda (as duas guardam a mesma coisa: a string
 *    normalizada, só que em ordens diferentes). Nomes como
 *    `invertida` e `normalizada` deixariam a intenção mais clara.
 *
 * 3) `return resultado === semEspaco ? true : false` — o ternário aqui
 *    é redundante, já que a comparação `===` já retorna um boolean.
 *    Basta `return resultado === semEspaco`.
 *
 * 4) Regra do enunciado só pedia ignorar espaços e maiúsculas/minúsculas,
 *    então não é erro, mas vale lembrar: strings com pontuação
 *    ("Socorram-me, subi no ônibus em Marrocos") não seriam tratadas
 *    corretamente aqui, pois `-`, `,` etc. não são removidos.
 */
