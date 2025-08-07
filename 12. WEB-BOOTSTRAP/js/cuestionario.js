//VARIABLES GLOBALES - ARRAYS - OBJETOS
const cuestionario = { // Diccionario con las preguntas
    pregunta1: "¿Qué tan importante crees que es el uso de energías renovables?",
    pregunta2: "¿Qué tanto conoces sobre paneles solares?",
    pregunta3: "¿Qué tan dispuesto estás a cambiar a energías limpias?",
    pregunta4: "¿Qué tanto apoyas iniciativas de energías sostenibles?",
    pregunta5: "¿Qué tan bien informado te sientes sobre el impacto ambiental de energías fósiles?"
};

const respuestas = [1, 2, 3, 4, 5]; // Opciones de respuesta (escala del 1 al 5)

const contenedor = document.getElementById('contenedorCuestionario'); // Selecciona el contenedor del formulario

// Cargar preguntas dinámicamente - 
// Object.entries(cuestionario) convierte ese objeto en un array de pares clave-valor,
Object.entries(cuestionario).forEach(([key, preguntaText], index) => {
    const divPregunta = document.createElement('div'); // Crea un div para cada pregunta
    divPregunta.classList.add('pregunta'); // Le aplica la clase CSS "pregunta"

    //Agrega el HTML de la pregunta y radios
    divPregunta.innerHTML = ` 
            <label class="form-label">${index + 1}. ${preguntaText}</label> <!-- Texto de la pregunta -->
            <div class="btn-group d-flex justify-content-between" role="group"> <!-- Agrupa los radios con Bootstrap -->
            ${respuestas.map(num => ` <!-- Genera dinámicamente los radios -->
                <div class="form-check form-check-inline">
                    <input class="form-check-input" type="radio" name="${key}" value="${num}" id="${key}_${num}" required> <!-- Opción de respuesta -->
                    <label class="form-check-label" for="${key}_${num}">${num}</label> <!-- Etiqueta del número -->
                </div>
            `).join('')}
        </div>
    `;            
    
    contenedor.appendChild(divPregunta); // Añade la pregunta al contenedor
});

// Manejar envío del formulario
document.getElementById('frmCuestionario').addEventListener('submit', function (event) {
    event.preventDefault(); // Evita que la página se recargue

    let total = 0; // Acumulador de las respuestas
    let count = 0; // Contador de respuestas válidas
    for (const key in cuestionario) { // Recorre cada pregunta
        const selected = document.querySelector(`input[name="${key}"]:checked`); // Busca la opción seleccionada
        if (selected) {
            total += parseInt(selected.value); // Suma el valor seleccionado
            count++; // Aumenta el contador
        } else {
            alert("Por favor responder todas las preguntas."); // Alerta si falta una respuesta
            return; // Detiene la función
        }
    }

    const promedio = total / count; // Calcula el promedio de las respuestas
    const divResultado = document.getElementById('divResultado'); // Selecciona el div para mostrar el mensaje
    let message = ""; // Variable para el mensaje motivacional

    // Mensaje motivacional según promedio
    if (promedio >= 4.5) {
        message = "¡Excelente! ¡Eres un verdadero defensor de las energías renovables!";
    } else if (promedio >= 3.5) {
        message = "¡Muy bien! Tienes buena conciencia ambiental.";
    } else if (promedio >= 2.5) {
        message = "¡Vas por buen camino! Infórmate más y verás el impacto.";
    } else {
        message = "¡Es hora de aprender más sobre energías limpias y su importancia!";
        color = "text-danger";
    }

    divResultado.innerHTML = `PROMEDIO OBTENIDO: ${promedio} <br>${message};` // Muestra el resultado final
});