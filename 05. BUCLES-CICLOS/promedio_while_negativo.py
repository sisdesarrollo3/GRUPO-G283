'''
Realizar un programa que permita leer  N valores positivos por teclado (hasta que se ingrese un número negativo) y posteriormente, nos muestre la suma de los valores ingresados y su promedio.
'''

#BUCLE    variable control inicia en un valor  NUMERO
#         variable control es comparada con el valor final NUMERO
#         variable control debe ser incrementada  NUMERO
# todo bucle se ejecuta mientras la condicion sea VERDADERO, sale por FALSO


numero = 0
suma = 0
contador = 0

#El bucle se ejecuta mientra el numero sea
while numero >= 0: 
    numero = int(input("INGRESE NUMERO (NEGATIVO PARA SALIR): "))
    if numero >= 0:
        suma = suma + numero
        contador += 1

#salida tiempo total
promedio = suma / contador
print(promedio)