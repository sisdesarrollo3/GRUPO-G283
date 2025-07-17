#inicializar el diccionario
colores = {
    "amarillo": "yellow",
    "azul"    : "blue",
    "rojo"    : "red"
}

#referencia a un elemento clave valor
print(f"COLORES EN INGLES: {colores["amarillo"]} {colores["azul"]} {colores["rojo"]}")

colores["violeta"] = "VIOLET"

#lista las claves
print ("\n\nLISTA CLAVES")
for claves in colores.keys():
    print (claves, end=",")

#lista las claves
print ("\n\nLISTA VALORES")
for valores in colores.values():
    print ( valores, end=",")

print ("\n\nLISTA VALORES EN FORMA DE TUPLAS (clave, valor)")
for items in colores.items():
    print ( items, end=",")

print ("\n\nLISTA CLAVES Y VALORES EN FORMA SEPARADA")
colores['amarillo'] = "AMARILLEISON"
for clave, valor in colores.items():
    print (f"CLAVE: {clave} VALOR: {valor}")