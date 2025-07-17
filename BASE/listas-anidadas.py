#definir el diccionario
estudiantes = [
        ["est01", "Ernesto", "ernesto@gmail.com", [1964, 1, 31], [4.5, 3.5, 5]],
        ["est02", "Valeria", "valeria@gmail.com", [2000, 12, 1], [5, 4.5, 5]]
]
estudiantes.append(["est03", "Eduardo"])  
print(estudiantes)

for registro in estudiantes:    
    print(registro)

for registro in estudiantes:    
    for elemento in registro:
        print(elemento)
#print(f"ESTUDIANTE est01: {estudiantes[0]}")
#print(f"ESTUDIANTE est01 : {estudiantes[0]} NOTA DE PROGRMACION: {estudiantes[0][4][0]}")
#print(f"ESTUDIANTE est01 : {estudiantes[0]} NOTA DE INBLES: {estudiantes[0][4][1]}")
'''
#mostrar el cumpleaños de ernesto  MES 1 - DIA 31
print(f"CUMPLEAÑOS EL MES {estudiantes["est01"]["nacimiento"]["mes"]}   DIA {estudiantes["est01"]["nacimiento"]["dia"]}")

#MEJORAR MOSTRANDO EL NOMBRE DEL MES
meses = {
    "1": "Enero",
    "2": "Febrero",
    "3": "Marzo",
    "4": "Abril",
    "5": "Mayo",
    "6": "Junio",
    "7": "Julio",
    "8": "Agosto",
    "9": "Septiembre",
    "10": "Ocubre",
    "11": "Noviembre",
    "12": "Diciembre"
}

#mostrar el cumpleaños de ernesto  MES Enero - DIA 31
nombreMes = meses[str(estudiantes["est01"]["nacimiento"]["mes"])]
print(f"CUMPLEAÑOS EL MES {nombreMes}   DIA {estudiantes["est01"]["nacimiento"]["dia"]}")

#MOSTRAR EL PROMEDIO DE NOTAS DE VALERIA
promedio = (estudiantes["est02"]["materias"]["programacion"] + estudiantes["est02"]["materias"]["ingles"] + estudiantes["est02"]["materias"]["habilidades"]) / 3

print(f"PROMEDIO DE VALERIA {promedio}")

#NOTAS DE TODOS
for clave in estudiantes.keys():
    promedio = (estudiantes[clave]["materias"]["programacion"] + estudiantes[clave]["materias"]["ingles"] + estudiantes[clave]["materias"]["habilidades"]) / 3
    print(f"PROMEDIO {promedio}")

# Convertimos a lista de listas para tabular
tabla = [[id] + list(info.values()) for id, info in estudiantes.items()]
encabezado = ["ID"] + list(next(iter(estudiantes.values())).keys())

from tabulate import tabulate
print(tabulate(tabla, headers=encabezado, tablefmt='fancy_grid', floatfmt=".1f"))

'''