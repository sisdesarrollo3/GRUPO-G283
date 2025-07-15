'''
Realizar un programa que permita leer  N valores positivos por teclado (hasta que se ingrese un número negativo) y posteriormente, nos muestre la suma de los valores ingresados y su promedio.
'''

numero = 0
suma = 0
contador = 0

while numero >= 0: 
    numero = int(input("INGRESE NUMERO (NEGATIVO PARA SALIR): "))
    if numero >= 0:
        suma = suma + numero
        contador += 1

#salida tiempo total
promedio = suma / contador
print(promedio)