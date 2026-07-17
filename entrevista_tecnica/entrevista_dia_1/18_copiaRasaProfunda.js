/**
 * Exercício 18 — Cópia rasa vs cópia profunda
 *
 * Demonstre em código a diferença entre cópia rasa (shallow copy,
 * ex: spread `{...obj}`) e cópia profunda de um objeto ANINHADO.
 *
 * Dica: crie um objeto com uma propriedade que seja outro objeto
 * (ou array), faça as duas cópias, altere a propriedade aninhada na
 * cópia, e mostre no console o que acontece com o original em cada
 * caso.
 */

const original = {
  nome: 'Ana',
  endereco: {
    cidade: 'São Paulo',
    cep: '00000-000',
  },
};

// 1) cópia rasa
const copiaRasa = { ...original };
// altere copiaRasa.endereco.cidade e veja o que acontece com original

// 2) cópia profunda
// implemente uma forma de copiar `original` sem compartilhar a
// referência do objeto aninhado `endereco`
const copiaProfunda = {
  ...copiaRasa,
  endereco: {...original.endereco}
}

console.log(original);
