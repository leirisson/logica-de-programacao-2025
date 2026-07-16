


function criarContador(){
    let contator = 0;
    return function () {
        contator++
        return contator
    }
}

const contador = criarContador()
console.log(contador())
console.log(contador())
console.log(contador())