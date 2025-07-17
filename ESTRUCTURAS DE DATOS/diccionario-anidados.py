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
