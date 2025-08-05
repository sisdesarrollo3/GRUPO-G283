let mes = 2
//EL BREAK ES OBLIGADO PARA SALIR DE CASE RESPECTIVO, SI NO TOMA TAMBIEN EL SIGUIENE CASE

switch (mes){
  case 1: mensaje = "ENERO";
      break;
  case 2: mensaje = "FEBRERO";
      break;
  case 3: mensaje = "MARZO";
      break;
  case 4: mensaje = "ABRIL";
      break; 
  default: mensaje = "NO EXISTE EL MES"
}
console.log(mes, "CORRESPONDE AL MES DE ", mensaje)

//salida  2 CORRESPONDE AL MES DE  FEBRERO