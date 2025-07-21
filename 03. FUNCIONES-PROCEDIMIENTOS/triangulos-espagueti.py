'''
Desarrollar un programa en Lenguaje Python, que permita hallar el área y perímetro de cualquier triángulo, construyendo sus propias funciones, para las entradas, procesos y salidas:
NOTA: NO se conoce la altura, solamente los tres lados (Investigar por AI)

ANALISIS: Comprender y detectar todas las variables
   ENTRADAS (INPUT)   : lado1, lado2, lado3
   PROCESOS (FORMULAS): perimetro <-- lado1 + lado2 + lado3
                        s <= (lado1 + lado2 + lado3) / 2
                        area <= math.sqrt(s * (s - lado1) * (s - lado2) * (s - lado3))                        
   SALIDAS : (PRINT)  : perimetro, area
'''

#1. IMPORTAR LIBRERIAS DEL LENGUAJE
import math

#2. FUNCIONES Y PROCEDIMIENTOS PROPIOS


#3. RESERVAR E INICIALIZAR VARIBLES
lado1 = 0
lado2 = 0
lado3 = 0
perimetro = 0
area = 0

#4. ENTRADAS con INPUT
lado1 = float(input("LADO 1: "))
lado2 = float(input("LADO 2: "))
lado3 = float(input("LADO 3: "))

#5. PROCESOS - FORMULAS
perimetro = lado1 + lado2 + lado3

s = (lado1 + lado2 + lado3) / 2
area = math.sqrt(s * (s - lado1) * (s - lado2) * (s - lado3))

#6. SALIDAS CON PRINT
print(perimetro)
print(area)



