# [1] IMPORTAMOS LAS LIBRERÍAS NECESARIAS
import pandas as pd                # Para manipular datos en forma de tablas (DataFrames)
import matplotlib.pyplot as plt    # Para crear gráficos personalizados

# [2] DEFINIMOS LOS DATOS COMO UN DICCIONARIO DE DICCIONARIOS
# Cada clave representa un estudiante con su información académica
data = {
    "EST01": {"Nombre": "ERNESTO", "PROGRAMACIÓN": 3.0, "INGLÉS": 4.0, "HABILIDADES": 5.0},
    "EST02": {"Nombre": "VALERIA", "PROGRAMACIÓN": 3.1, "INGLÉS": 4.1, "HABILIDADES": 5.0},
    "EST03": {"Nombre": "JOHN",    "PROGRAMACIÓN": 3.2, "INGLÉS": 4.2, "HABILIDADES": 5.0},
    "EST04": {"Nombre": "PAOLA",   "PROGRAMACIÓN": 3.3, "INGLÉS": 4.3, "HABILIDADES": 5.0}
}

# [3] CONVERTIMOS EL DICCIONARIO EN UN DATAFRAME
df = pd.DataFrame.from_dict(data, orient='index')

# [4] DEFINIMOS LAS COMPONENTES QUE VAMOS A GRAFICAR
componentes = ["PROGRAMACIÓN", "INGLÉS", "HABILIDADES"]

# [5] PREPARAMOS LAS ETIQUETAS DEL EJE X (CÓDIGO Y NOMBRE DEL ESTUDIANTE)
etiquetas = [f"{codigo} - {df.loc[codigo, 'Nombre']}" for codigo in df.index]

# [6] ESTABLECEMOS LA POSICIÓN DE CADA GRUPO DE BARRAS EN EL EJE X
import numpy as np
x = np.arange(len(df))  # Posición de cada estudiante en el eje X - función de NumPy que genera un array de valores numéricos
ancho = 0.25            # Ancho de cada barra individual

# [7] CREAR EL GRÁFICO DE COLUMNAS AGRUPADAS
plt.figure(figsize=(8, 5))

# Creamos una barra por cada componente, desplazada horizontalmente
for i, comp in enumerate(componentes):
    plt.bar(x + i*ancho, df[comp], width=ancho, label=comp)

# [8] CONFIGURAMOS LOS ELEMENTOS DEL GRÁFICO
plt.title("Componentes Académicos por Estudiante")
plt.xlabel("Estudiantes")
plt.ylabel("Nota")
plt.xticks(x + ancho, etiquetas, rotation=45)  # Alinea las etiquetas centradas entre las barras
plt.ylim(0, 6)                                 # Rango de notas típico
plt.legend(title="Componente")                # Leyenda identificando cada barra
plt.grid(axis='y', linestyle='--', alpha=0.3)  # Cuadrícula horizontal punteada

plt.tight_layout()
plt.show()