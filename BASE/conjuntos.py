#inicializamos los conjuntos
pares = {2, 4, 6, 8}
impares = {1, 3, 5, 7, 9}

print(f"IMPARES: {impares}")
print(f"PARES: {pares}")

pares.add(0)
print(f"PARES: {pares}")


import random


impares.discard(5)
print(f"IMPARES: {impares}")

impares.add(5) 
pares.add(5)
union = impares.union(pares) 
interseccion = impares.intersection(pares)
diferencia = impares.difference(pares)

print(f"UNION: {union}")
print(f"INTERSECCIÓN: {interseccion}")
print(f"DIFERENCIA: {diferencia}")

#recorrerlos
for elemento in pares:
	print(elemento)

aleatorios = {0} #minimo un elemento sino  myConjunto = set()
for i in range(5):
	aleatorios.add(random.randint(18, 100))

print(f"ALEATORIOS: {aleatorios}")

print(f"MAXIMO: {max(aleatorios)}")
print(f"MINMO: {min(aleatorios)}")

copia = impares.copy()
print(f"COPIA: {copia}")

impares.clear()
print(f"IMPARES LIMPIO: {impares}")