'''
Programa que permita mostrar la conocida serie de FIBONACCI de los primeros N terminos, crear una función que la invoque y la muestre, por ejemplo: myFibbonacci (n).
La siguiente es la serie FIBONACCI de los primeros 9 terminos
“0 - 1 - 1 - 2 - 3 - 5 - 8 - 13  - 21 …….”
'''

veces = int(input("Cuantos terminos de la seria: "))

anterior = 0
actual = 1

print(f"{anterior} , {actual} ,", end="")


for i in range(veces):
    resultado = anterior + actual
    print (f"{resultado} ,", end="")
    anterior = actual
    actual = resultado