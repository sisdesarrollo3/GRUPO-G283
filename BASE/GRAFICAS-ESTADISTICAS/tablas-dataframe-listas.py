# [1] IMPORTAR LIBRERÍAS
import pandas as pd                # Para manejo de datos en forma tabular (DataFrame)
import numpy as np                 # (No usado aquí, puede eliminarse si no se necesita)
import dateutil                   # (No usado aquí, puede eliminarse también)

from tabulate import tabulate      # Permite imprimir tablas con formato visual en consola

# [2] DEFINIR LAS CABECERAS DE LA TABLA
column_names = ["CÓDIGO", "Nombre", "PROGRAMACIÓN", "INGLES", "HABILIDADES"]
# Lista con los nombres de las columnas que tendrá el DataFrame

# [3] DEFINIR LOS DATOS COMO LISTAS DE LISTAS
data = [
    ["EST01", "ERNESTO", 3.0, 4.0, 5.0],
    ["EST02", "VALERIA", 3.1, 4.1, 5.0],
    ["EST03", "JOHN",    3.2, 4.2, 5.0],
    ["EST04", "PAOLA",   3.3, 4.3, 5.0]
]
# Cada sublista representa una fila en la tabla: código, nombre y notas

# [4] CREAR EL DATAFRAME USANDO LOS DATOS Y CABECERAS
df = pd.DataFrame(data, columns=column_names)
# Crea una tabla con columnas nombradas y los datos organizados por filas

# [5] IMPRIMIR EL DATAFRAME EN FORMATO NORMAL
print(df)
# Muestra la tabla directamente usando el método básico, sin formato especial

# [6] IMPRIMIR LA TABLA CON FORMATO USANDO TABULATE
print(tabulate(df,
               headers='keys',         # Usa los nombres de columna como cabecera
               tablefmt='fancy_grid',  # Formato visual tipo cuadrícula elegante
               numalign='right',       # Alinea los números a la derecha
               stralign='left',        # Alinea texto a la izquierda
               floatfmt=".1f"          # Muestra los decimales con una cifra (ej: 3.0 → 3.0)
              ))
# Tabulate toma el DataFrame y lo transforma en una tabla visualmente clara