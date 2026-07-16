
/**
 * Correção aplicada: antes havia dois blocos `if` separados, então
 * múltiplos de 3 e 5 ao mesmo tempo (ex: 15) caíam nos dois blocos e
 * imprimiam "FizzBuzz" e "Fizz". Agora é um único if/else if/else if/else
 * encadeado, então só um caminho executa por número.
 * Loop também corrigido para começar em i = 1 (não 0), e todas as
 * comparações padronizadas com === em vez de misturar com ==.
 */


for (let i = 1; i <= 100; i++) {
    if (i % 3 === 0 && i % 5 === 0) {
        console.log('FizzBuzz')
    }
    else if (i % 3 === 0) {
        console.log('Fizz')
    } 
    else if (i % 5 === 0) {
        console.log('Buzz')
    } 
    else {
        console.log(i)
    }
}
