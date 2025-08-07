function calcular ( operacion ) {
    //RECIBIMOS LA INFORMACION QUE VIENE DESDE EL FORMULARIO
    let numero1 = Number(document.getElementById("txtNumero1").value);
    let numero2 = parseFloat(document.getElementById("txtNumero2").value);

    let resultado = 0

    if (isNaN(numero1) || isNaN(numero2)) {
        alert("Favor ingresar los Números");
        return 
    }

    switch (operacion){
        case '+': resultado = numero1 + numero2; break;
        case '-': resultado = numero1 - numero2; break;
        case '*': resultado = numero1 * numero2; break;
        case '/': if (numero2 === 0){
                    resultado = "ERRROR division x cero"
                  }
                  else resultado = numero1 / numero2; 
                  break;
        default: resultado = "NaN";
    }

    //ENVIAR VALORES AL HTML
    document.getElementById("txtResultado").value = resultado;
    console.log(`FORMULA ${numero1} ${operacion} ${numero2}  =  ${resultado}`)
}