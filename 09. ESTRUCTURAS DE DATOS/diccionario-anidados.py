#definir el diccionario
estudiantes = {
    "est01": {"nombre": "Ernesto", "correo": "ernesto@gmail.com", 
              "nacimiento":{"anyo": 1964, "mes": 1, "dia": 31},
               "materias": {"programacion": 4.5, "ingles": 3.5, "habilidades": 5}
             },
    "est02": {"nombre": "Valeria", "correo": "ernesto@gmail.com", 
              "nacimiento":{"anyo": 2000, "mes": 12, "dia": 31},
               "materias": {"programacion": 5, "ingles": 4.5, "habilidades": 5}
             }
}

print(estudiantes)

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