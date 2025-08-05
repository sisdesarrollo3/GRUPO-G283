// Bucle for...in  para recorrer  Objetos, clave: valor

const objeto = { a: 1, b: 2, c: 3 };
for (let key in objeto) {
    console.log(`for...in: ${key} = ${objeto[key]}`);
}

//salidas for...in: a = 1  for...in: b =21  for...in: c = 3
