/**
 * Exercício 16 — debounce simplificado
 *
 * Escreva uma função `debounce(fn, delay)` que retorna uma versão
 * "debounced" de `fn`: só executa `fn` depois que passar `delay` ms
 * SEM que a função retornada seja chamada de novo (cada nova chamada
 * reinicia o timer).
 *
 * Não precisa ser perfeito, o objetivo é entender o conceito.
 *
 * Exemplo de uso:
 * const log = debounce(() => console.log('executou!'), 300);
 * log(); log(); log(); // só "executou!" uma vez, ~300ms depois da última chamada
 */

function debounce(fn, delay) {
  // implemente aqui
}

const logDebounced = debounce(() => console.log('executou!'), 300);
logDebounced();
logDebounced();
logDebounced();
