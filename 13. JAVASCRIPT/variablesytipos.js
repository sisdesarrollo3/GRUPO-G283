//comentarios de una sola linea
/*
 comentarios de bloque varia lineas
*/

//VARIABLES NUMERICAS
let entero = 10;  //varialbe entera
let decimal = 4.5  //variable decimales

const PI = 3.1416;
//PI = PI + 1;  las constantes no permiten modificar su valor inicial
var descontinuada = "valor" // var ya descontinuada

let caracter = '@';
let nombre = "JOHN JAIRO OROZCO";

//SALIDAS POR CONSOLA
console.log("ENTERO ES: " + entero);

//SOLO PARA HTML EN EL NAVEGADOR
//prompt('ingrese valor') similar al input en python
//alert("DECIMAEL ES: ", decimal)  ventana con un mensaje

//ARRAYS  similar a listas en python
let colores = ["rojo", "verde", "azul"];  //Lista en python con indices 0, 1.....N
colores.push("negro")
console.log(colores);
console.log("PRIMER ELEMENTO: " + colores[0]);  //inidicamos el indice

//OBJETOS son diccionarios como en ´python con clave: valor

let persona = { nombre: "Juan", edad: 25 };
persona.apellidos = "Perez Paz";
persona["ocupacion"] = 'Ingeniero';
console.log(persona);

//conversiones
//NOTA la informacion que viene de HTML es de tipo cadena, para procesar hacer la conversión
//let cadena = String(numero)  //convierte a cadena un valor numerico
//let conversion = parseFloat("4.5");

//INTEPOLAR SALIDAS es combinar texto, html, variables

console.log(`
      EL VALOR DE NOMBRES ES: ${nombre}
    `)