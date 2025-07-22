import pandas as pd
import numpy as np
import dateutil
from tabulate import tabulate

#crear las columnas o cabeceras de la tabla
column_names = ["CÓDIGO", "NOMBRE", "PROGRAMACIÓN", "INGLÉS", "HABILIDADES"]

# Crear un DataFrame de ejemplo
data = {
    "EST01":  {"NOMBRE": "ERNESTO", "PROGRAMACIÓN": 3.0, "INGLÉS": 4.0, "HABILIDADES": 5.0},
    "EST02":  {"NOMBRE": "VALERIA", "PROGRAMACIÓN": 3.1, "INGLÉS": 4.1, "HABILIDADES": 5.0},
    "EST03":  {"NOMBRE": "JOHN",    "PROGRAMACIÓN": 3.2, "INGLÉS": 4.2, "HABILIDADES": 5.0},
    "ESTNN":  {"NOMBRE": "PAOLA",   "PROGRAMACIÓN": 3.3, "INGLÉS": 4.3, "HABILIDADES": 5.0}
}

df = pd.DataFrame.from_dict(data, orient="index")  #convertir diccionario a tabla, con las claves como indice

print(df)

# Imprimir formato tabulado
print(tabulate(df, 
               headers='keys', 
               tablefmt='fancy_grid', 
               numalign='right', 
               stralign='left', 
               floatfmt=".1f"
               )
    )

