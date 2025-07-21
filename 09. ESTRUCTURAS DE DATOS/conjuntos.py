#CONJUNTOS

#DECLARACION DE UN CONJUNTO

#pares = set()
pares = {2, 4, 6, 8}
impares = {1, 3, 5, 7, 9}
print (f"IMPARES: {type(impares)}")
#LISTAR
print (f"IMPARES: {impares}")
print (f"PARES: {pares}")

#adicionar elmento
pares.add(0)
impares.add(9)

print (f"PARES: {pares}")

#eliminar elemnto
print("\nELIMINANDO EL 9")
impares.discard(9)
print (f"IMPARES: {impares}")

#maximos y minimos
print("\nMAXIMOS Y MINIMOS")
print(f"MAXIMO PAR: {max(pares)}")
print(f"MINIMO IMPAR: {min(impares)}")

print("\nUNION INTERSECCION DIFERENCIA")
print (f"UNION: {impares.union(pares)}")
print (f"INTERSECCION: {impares.intersection(pares)}")
print (f"DIFERENCIA: {impares.difference(pares)}")