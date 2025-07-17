#las tuplas son inmutables

#declarar
tupla = (1, 'a', "veronica", 4.5)
tupla[4] = "otro valor"


# tupla.add("otro valor")  la tupla no permite adicionar ni eliminar es INMUTABLE
#salidas
print(type(tupla))

#salida completa entre parentesis y separados por coma
print(tupla)

#salida de un solo elemento hago referencia al indice de 0 a ....
print(tupla[2])

impares = {0}
pares = {0}
for i in range(1,10,2):
	impares.add(i)

for i in range(5):
	pares.add(i*2)
    
#para hacer referencia a sus índices, el conjunto se convierte a tupla
tuplaImpares = tuple(impares)
tuplaPares   = tuple(pares)
print('TUPLA DE IMPARES', tuplaImpares)
print('TUPLA DE PARES', tuplaPares)
print(str(len(tuplaImpares)))
print('PRIMER ELEMENTO',  str(tuplaImpares[0]))
print('ULTIMO ELEMENTO',  tuplaPares[3])
