from tabulate import tabulate

estudiantes = {
    101: {"Nombre": "Juan Pérez", "Programación": 4.0, "Inglés": 3.5, "Habilidades": 2.8},
    102: {"Nombre": "Ana Gómez", "Programación": 2.9, "Inglés": 3.8, "Habilidades": 3.0}
}

# Convertimos a lista de listas para tabular
tabla = [[id] + list(info.values()) for id, info in estudiantes.items()]
encabezado = ["ID"] + list(next(iter(estudiantes.values())).keys())

print(tabulate(tabla, headers=encabezado, tablefmt='fancy_grid', floatfmt=".1f"))


#persistencia con diccionarios

import pickle

# Lista de diccionarios
datos = [
    {"ID": 101, "Nombre": "Juan", "Nota": 4.0},
    {"ID": 102, "Nombre": "Ana", "Nota": 3.8}
]

# Guardar
with open("datos.pkl", "wb") as archivo:
    pickle.dump(datos, archivo)

# Cargar
with open("datos.pkl", "rb") as archivo:
    cargado = pickle.load(archivo)

print(cargado)

# Aplanamos cada estudiante, cuando se contiene dicciconario de diccionarios
filas = []
for id_est, info in datos.items():
    fila = {
        'ID': id_est,
        'Nombre': info['nombre'],
        'Correo': info['correo'],
        'Nacimiento': f"{info['nacimiento']['dia']:02d}/{info['nacimiento']['mes']:02d}/{info['nacimiento']['anyo']}",
        'Programación': info['materias']['programacion'],
        'Inglés': info['materias']['ingles'],
        'Habilidades': info['materias']['habilidades']
    }
    filas.append(fila)

# Imprimimos la tabla
print(tabulate(filas, headers="keys", tablefmt="double_grid")) #fancy_grid, double_grid, grid
