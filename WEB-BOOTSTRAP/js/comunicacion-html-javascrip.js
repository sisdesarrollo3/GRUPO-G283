//variables globales
// Espera a que cargue el DOM Document Object Model → Modelo de Objetos del Documento.
window.addEventListener('DOMContentLoaded', () => {
  const form = document.getElementById('formulario');
 
  //addEventListener función de JavaScript que sirve para escuchar eventos en un elemento HTML (Click - submit)
  form.addEventListener('submit', (e) => { //el usuario presiona el boton submit
    e.preventDefault(); // Evita que se recargue
  
    // Captura de datos desde EL FORMULARIO - la mayoría son con .value = 
    let nombre = document.getElementById('nombre').value.trim(); //trim para eliminar espacios izq derecho
    let clave  = document.getElementById('clave'); //verificar si chekeado checkbox.checked   
    let email  = document.getElementById('email').value.trim();  
    const edad = document.getElementById('edad').value; 


    const hobbiSeleccionados = document.querySelectorAll("input[name='hobbis']:checked");
    //convertit los checkboxes marcados en un array - 
    //map ecorre cada checkbox y extrae su atributo value
    const listaValores = Array.from(hobbiSeleccionados).map(hobbi => hobbi.value);

    const genero = document.querySelector("input[name='genero']:checked").value;
    const ciudades = document.getElementById('ciudades').value;
 
    // Aquí va tu lógica (guardar, mostrar, enviar, etc.)
    console.log('Datos capturados:', { nombre, clave, email, edad, listaValores, genero, ciudades });
  
    // Resetear formulario - cuando se requiera limpia todos los campos del formulario del submit
    //form.reset();

    //CAMBIAR VALORES EN EL HTML DESDE JAVA SCRIPT
    //en los Input-textArea-select con document.getElementById('ID').value =777;
    //en los radios  document.querySelector('input[name="genero"][value="masculino"]').checked = true;
    // cambiar en select document.getElementById('ciudades').value ='armenia';

  });
 });
