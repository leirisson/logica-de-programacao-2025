

const pares = [1,2,3,4,5,6,7,8,9]

function apenasPares(numeros) {
  return numeros.filter(p => p % 2 === 0 )
}

console.log(apenasPares(pares))