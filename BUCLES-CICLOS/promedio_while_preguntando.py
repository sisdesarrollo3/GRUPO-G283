'''
Realizar un programa que permita leer  N valores positivos por teclado (preguntar si desea continuar) y posteriormente, nos muestre la suma de los valores ingresados y su promedio.
'''

numero = 0
suma = 0
contador = 0
respuesta = 's'
while respuesta  == 's': 
    numero = int(input("INGRESE NUMERO (NEGATIVO PARA SALIR): "))
    if numero >= 0:
        suma = suma + numero
        contador += 1
    
    #variable de control debe ser actualizada antes de volver al bucle
    respuesta = input("CONTINUAR (Si/No):")[0].lower()

#salida tiempo total
promedio = suma / contador
print(promedio)
