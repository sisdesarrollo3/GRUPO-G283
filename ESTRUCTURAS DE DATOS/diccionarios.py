
#DICCIONARIOS MANEJAN EL CONCEPTO DE CLAVE:VALOR

#CREAR DICCIONARIO

traductor = {
    "amarillo": "yellow",
    "azul": "blue",
    "rojo": "red"
}

#adicionar un registro nuevo con datos del usuario
clave = input("Color en Español: ")
valor = input("Color en Ingles: ")

traductor[clave] = valor

#mostrar el tipo de estructura
print (f"TIPO DEL DICCIONARIO {type(traductor)}")

#listar o imprimir todo el diccionario
print(traductor)

#LISTAR SOLO LAS CLAVES
print("\n CLAVES DEL TRADUCTOR")
for clave in traductor.keys():
    print(clave, end="\t")


#LISTAR SOLO LOS VALORES
print("\n VALORES DEL TRADUCTOR")
for valor in traductor.values():
    print(valor, end="\t")

#LISTAR AMbOS CLAVE Y VALOR EN FORMA DE TUPLAS
print("\n VALORES DEL TRADUCTOR")
for items in traductor.items():
    print(items)

#LISTAR AMbOS CLAVE Y VALOR EN FORMA DE TUPLAS
print("\n VALORES DEL TRADUCTOR")
for clave, valor in traductor.items():
    print(f"CLAVE: {clave}  VALOR: {valor}")
