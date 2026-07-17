/**
 * Exercício 9 — filter + map em array de objetos
 *
 * Dado um array de objetos `{ nome, idade }`, escreva uma função
 * `nomesMaioresDeIdade(pessoas)` que retorna só os NOMES das pessoas
 * com 18 anos ou mais, usando `filter` + `map`.
 *
 * Exemplo:
 * nomesMaioresDeIdade([
 *   { nome: 'Ana', idade: 17 },
 *   { nome: 'Bruno', idade: 20 },
 *   { nome: 'Carla', idade: 18 },
 * ])
 * // ['Bruno', 'Carla']
 */

function nomesMaioresDeIdade(pessoas) {
  // implemente aqui
  return pessoas
  .filter(pessoa => pessoa.idade >= 18)
  .map(pessoa => pessoa.nome)
  

}

console.log(nomesMaioresDeIdade([
  { nome: 'Ana', idade: 17 },
  { nome: 'Bruno', idade: 20 },
  { nome: 'Carla', idade: 18 },
]));
