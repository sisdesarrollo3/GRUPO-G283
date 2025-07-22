import pandas as pd
import numpy as np
import dateutil

# Crear un DataFrame de ejemplo
datos = [
    [1, 'Alice', 85],
    [2, 'Bob', 90],
    [3, 'Charlie', 78],
    [4, 'David', 92]
]

#NOMBRES DE LA CABECERA DE LA TABLA
etiquetas = ['ID', 'Nombre', 'Edad']
tabla     = pd.DataFrame(datos, columns=etiquetas)

print( tabla )
