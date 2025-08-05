console.log("¡Hola desde JavaScript en VS Code!");

const    PI = 3.14159;      
 
console.log(PI)

let colores = ["rojo", "verde", "azul"]; 

console.log(colores[0])

colores = colores.filter(color => color !== "verde");
console.log(colores);

let persona = { nombre: "Juan", edad: 25 };
persona.apellido = "Pérez";
persona["ocupacion"] = "Ingeniero";

console.log(persona)

// Conversión a Número
let num1 = Number("123"); // 123
let num2 = parseInt("123px"); // 123
let num3 = parseFloat("123.45em"); // 123.45

// Conversión a Cadena
let str1 = String(123); // "123"
let str2 = (456).toString(); // "456"

// Conversión a Booleano
let bool1 = Boolean(1); // true
let bool2 = Boolean(0); // false

