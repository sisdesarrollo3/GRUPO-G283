//variables globales
// Espera a que cargue el DOM Document Object Model → Modelo de Objetos del Documento.
window.addEventListener('DOMContentLoaded', () => {
  const form = document.getElementById('formulario');
 
  //addEventListener función de JavaScript que sirve para escuchar eventos en un elemento HTML (Click - submit)
  form.addEventListener('submit', (e) => { //el usuario presiona el boton submit
    e.preventDefault(); // Evita que se recargue
  
    // Captura de datos desde EL FORMULARIO - la mayoría son con .value = 
    const nombre = document.getElementById('nombre').value.trim(); 
    const clave = document.getElementById('clave'); //verificar si chekeado checkbox.checked   
    const email = document.querySelector('input[name="generoenero"]:checked');    
    const edad = document.getElementById('edad').value; 
    const hobbiSeleccionados = document.querySelectorAll("input[name='hobbie']:checked");

    const genero = document.querySelector("input[name='genero']:checked");


  
    // Validación básica
    /*if (nombre === '' || ciudad === '' || ! genero || ! !futbool.checked) {
     alert('Por favor, completa todos los campos.');
     return;
    }*/
  
    // Aquí va tu lógica (guardar, mostrar, enviar, etc.)
    console.log('Datos capturados:', { nombre, clave, email, edad, hobbiSeleccionados, genero });
  
    // Resetear formulario - cuando se requiera limpia todos los campos del formulario del submit
    form.reset();
  });
 });
