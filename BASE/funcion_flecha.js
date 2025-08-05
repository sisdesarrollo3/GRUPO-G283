let myGlobal = 4
//tradicional
function dividir (a, b) {
    console.log('Global' + myGlobal);
    
    myGlobal = 555
    return a / b;
}

//expresada
const dividir2 = function (a, b) {
    return a / b;
}

//funcion flecha
const dividir3 = (a, b) => {
    return a / b;
}

const dividir4 = (a, b) => a / b;


//flecha compacta
console.log(dividir4(10, 2))

console.log(typeof(Number("777")))
console.log(typeof(parseFloat("4.5")))
console.log(typeof(parseInt("88")))

for (let i=0; i<5; i++){
    console.log('hola');
}
