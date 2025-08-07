// Variables globales
let datosOriginales = []; // Almacena los datos cargados del CSV
let graficoTop = null;    // Referencia al gráfico actual para poder destruirlo si se actualiza

// Cabeceras columnas
const columnas = [ // Nombres de columnas que se esperan en el CSV
  'Continent',
  'Entity',
  'Code',
  'Year',
  'Geo Biomass Other - TWh',
  'Solar Generation - TWh',
  'Wind Generation - TWh',
  'Hydro Generation - TWh'
];

const colores = [ // Colores para las barras del gráfico
  'rgba(255, 99, 132, 0.6)',   // rojo
  'rgba(54, 162, 235, 0.6)',   // azul
  'rgba(255, 206, 86, 0.6)',   // amarillo
  'rgba(75, 192, 192, 0.6)',   // verde
  'rgba(153, 102, 255, 0.6)',  // morado
  'rgba(255, 159, 64, 0.6)'    // naranja
];

//NOTA con  array.map  se recorre uno a uno los elementos; map trabaja con pareja (valor, indice)

// Cargar archivo CSV
document.getElementById('inputArchivo').addEventListener('change', function (e) { // Detecta cuando se selecciona un archivo
  const archivo = e.target.files[0]; // Obtiene el archivo seleccionado
  if (!archivo) return; // Si no hay archivo, no hace nada

  const lector = new FileReader(); // Crea un lector de archivos
  lector.onload = function (event) { // Cuando se haya leído el archivo...
    const contenido = event.target.result; // Obtiene el contenido del archivo
    procesarCSV(contenido); // Llama a la función para procesar el contenido
  };
  lector.readAsText(archivo); // Lee el archivo como texto
});

// Procesar CSV y validar cabeceras
function procesarCSV(texto) {
  const lineas = texto.split(/\r?\n/).filter(l => l.trim() !== ''); // Divide el contenido en líneas, eliminando vacías
  const delimitador = texto.includes(';') ? ';' : ','; // Detecta si el separador es ; o ,
  const cabeceras = lineas[0].split(delimitador).map(c => c.trim()); // Obtiene las cabeceras y las limpia

  const validas = columnas.every(c => cabeceras.includes(c)); // Verifica si todas las cabeceras columnas están presentes
  if (!validas) {
    alert('❌ Cabeceras inválidas. Se esperaban: ' + columnas.join(', ')); // Muestra alerta si faltan cabeceras
    return;
  }

  datosOriginales = lineas.slice(1).map(linea => { // Procesa las líneas de datos
    const partes = linea.split(delimitador); // Divide cada línea en columnas
    const obj = {}; // Objeto para almacenar una fila
    cabeceras.forEach((c, i) => obj[c] = partes[i]?.trim()); // Asigna cada valor a su cabecera
    return obj; // Devuelve el objeto fila
  });

  actualizarCabecerasTabla(); // Inserta cabeceras en la tabla HTML
  poblarFiltros(); // Llena los combos (filtros)
  aplicarFiltros(); // Aplica los filtros y muestra tabla/gráfico
}

// Poblar filtros dinámicos
function poblarFiltros() {
  const continentes = [...new Set(datosOriginales.map(d => d['Continent']))].sort(); // Extrae continentes únicos
  const años = [...new Set(datosOriginales.map(d => d['Year']))].sort(); // Extrae años únicos
  const entidades = [...new Set(datosOriginales.map(d => d['Entity']))].sort(); // Extrae entidades (paises) únicas

  llenarSelect('comboContinente', continentes); // Llena combo de continentes
  llenarSelect('comboAnio', años); // Llena combo de años
  llenarSelect('comboPais', entidades); // Llena combo de países
  llenarSelect('comboFuente', columnas.slice(4)); // Llena combo de fuentes (últimas columnas)
}

// Llenar un <select> con opciones
function llenarSelect(id, opciones) {
  const select = document.getElementById(id); // Obtiene el <select> por ID
  select.innerHTML = '<option value="">-- Todos --</option>'; // Opción por defecto
  opciones.forEach(op => {
    const opt = document.createElement('option'); // Crea una opción
    opt.value = op; // Valor de la opción
    opt.textContent = op.replace(' - TWh', ''); // Texto visible sin " - TWh"
    select.appendChild(opt); // Agrega la opción al <select>
  });
}

// Aplicar filtros y actualizar tabla + gráfico
function aplicarFiltros() {
  const continente = document.getElementById('comboContinente').value; // Valor seleccionado en comboContinente
  const año = document.getElementById('comboAnio').value; // Valor seleccionado en comboAnio
  const entidad = document.getElementById('comboPais').value; // Valor seleccionado en comboPais
  const fuente = document.getElementById('comboFuente').value || 'Solar Generation - TWh'; // Fuente seleccionada o valor por defecto
  const topN = parseInt(document.getElementById('comboTop').value) || 10; // Cantidad top seleccionada o 10

  let filtrados = datosOriginales.filter(d => { // Filtra los datos según los filtros aplicados
    return (!continente || d['Continent'] === continente) &&
           (!año || d['Year'] === año) &&
           (!entidad || d['Entity'] === entidad);
  });

  filtrados.sort((a, b) => { // Ordena por la fuente energética de mayor a menor
    const valA = parseFloat((a[fuente] ?? '').replace(',', '.')) || 0;
    const valB = parseFloat((b[fuente] ?? '').replace(',', '.')) || 0;
    return valB - valA;
  });

  const datosTop = filtrados.slice(0, topN); // Toma los primeros N resultados

  actualizarTabla(datosTop); // Muestra la tabla
  actualizarGrafico(datosTop, fuente); // Muestra el gráfico
}

// Actualizar tabla HTML con todas las columnas
function actualizarTabla(datos) {
  const cuerpo = document.getElementById('tablaDatos'); // Obtiene el <tbody> de la tabla
  cuerpo.innerHTML = ''; // Limpia el contenido anterior

  datos.forEach(d => { // Recorre cada dato (fila)
    const fila = document.createElement('tr'); // Crea una fila
    fila.innerHTML = columnas.map(c => `<td style="text-align: right;">${d[c]}</td>`).join(''); // Agrega celdas por cada columna, con join se une todas las celdas como una sola cadena que se asigna a la fila
    cuerpo.appendChild(fila); // Añade la fila a la tabla
  });
}

function actualizarCabecerasTabla() {
  const cabecera = document.getElementById('cabeceraTabla'); // Obtiene la fila de cabecera
  cabecera.innerHTML = columnas.map(c => `<th style="color:green;">${c}</th>`).join(''); // Agrega las cabeceras con estilo
}

// Actualizar gráfico con Chart.js según fuente seleccionada - fuente es el tipo de energia del combo
function actualizarGrafico(datos, fuente) {
  const canvas = document.getElementById('graficoTop'); // Obtiene el <canvas> del gráfico
  if (!canvas) return; // Si no existe, no hace nada
  const ctx = canvas.getContext('2d'); // Obtiene el contexto 2D para dibujar

  const entidades = datos.map(d => d['Entity']); // Extrae las entidades (paises)
  const valores = datos.map(d => { // Extrae los valores numéricos de la fuente
    const raw = d[fuente] ?? '';  //raw significa sin refinar - crudo
    const limpio = typeof raw === 'string' ? raw.replace(',', '.') : raw; //verifica si es cadena para cambiar coma por punto en numeros
    return parseFloat(limpio) || 0;  //si es valor numerico válido, sino lo deja como 0
  });

  if (graficoTop) graficoTop.destroy(); // Si ya hay un gráfico, lo destruye

  const backgroundColors = valores.map((_, i) => colores[i % colores.length]); // Asigna colores a cada barra con '_' omitimos el valor del color no se requiere, solo el índice; 

  graficoTop = new Chart(ctx, { // Crea el gráfico con Chart.js
    type: 'bar', // Tipo de gráfico: barras
    data: {
      labels: entidades, // Nombres de entidades (paises)
      datasets: [{
        label: fuente.replace(' - TWh', '') + ' (TWh)', // Etiqueta del dataset
        data: valores, // Datos de las barras
        backgroundColor: backgroundColors, // Colores de fondo
        borderColor: backgroundColors.map(color => color.replace('0.6', '1')), // Bordes opacos
        borderWidth: 1 // Grosor del borde
      }]
    },
    options: {
      responsive: true, // Se adapta al tamaño de la pantalla
      plugins: {
        legend: { display: false }, // Oculta la leyenda
        title: {
          display: true,
          text: `Top Países por ${fuente.replace(' - TWh', '')}` // Título del gráfico
        }
      },
      scales: {
        x: {
          title: {
            display: true,
            text: 'Paises', // Etiqueta del eje X
            font: {
              size: 14,
              weight: 'bold'
            }
          }
        },
        y: {
          title: {
            display: true,
            text: 'Tera Vatios Hora (TWh)', // Etiqueta del eje Y
            font: {
              size: 14,
              weight: 'bold'
            }
          },
          beginAtZero: true // Comienza en 0
        }
      }
    }
  });
}

// Escuchar cambios en filtros
['comboContinente', 'comboAnio', 'comboPais', 'comboTop', 'comboFuente'].forEach(id => {
  document.getElementById(id).addEventListener('change', aplicarFiltros); // Aplica filtros cuando cambie un select
});
