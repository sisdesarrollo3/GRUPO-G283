'''
Desarrollar un programa en Lenguaje Python, que permita hallar el área y perímetro de cualquier triángulo, construyendo sus propias funciones, para las entradas, procesos y salidas:

NOTA: NO se conoce la altura, solamente los tres lados (Investigar por AI)

'''

#1. IMPORTAR LIBRERIAS DEL LENGUAJE
import math
import os

#2. FUNCIONES Y PROCEDIMIENTOS PROPIOS - LOS CREAMOS CON DEF
#Funcion que retorna el perimetro del triangulo con los lados enviados por parametro
calcularPerimetro = lambda lado1, lado2, lado3: lado1 + lado2 + lado3

#Funcion que retorna el area del triangulo con los lados enviados por parametro
def calcularArea(l1, l2, l3):
    s = (l1 + l2 + l3) / 2
    area = math.sqrt(s * (s - l1) * (s - l2) * (s - l3))
    return area

#funcion que retorna un numero flotante, se indica la etiqueta enviada por parametro
def leerFlotante(mensaje):
    lado = float(input(mensaje))
    return lado

#UN PROCEDIMIENTO NO RETORNA NINGUN VALOR
def mostrarPerimetro (l1, l2, l3, p):
    print("\n***** PERIMETRO *********")
    print(f"LADO1 LADO2 LAD03 PERIMETRO")
    print("=" * 50)
    print(f"{l1} \t {l2} \t {l3} \t {p}")

def mostrarArea (l1, l2, l3, a):    
    print("\n***** AREA *********")
    print(f"LADO1 LADO2 LAD03 AREA")
    print("=" * 50)
    print(f"{l1} \t {l2} \t {l3} \t {a:.1f}")

#3. RESERVAMOS E INICIALIZAMOS VARIABLES
lado1 = 0
lado2 = 0
lado3 = 0
perimetro = 0
area = 0

#4. ENTRADAS con INPUT
lado1 = leerFlotante("LADO 1: ")
lado2 = leerFlotante("LADO 2: ")
lado3 = leerFlotante("LADO 3: ")

#5. PROCESOS - FORMULAS
#perimetro = lado1 + lado2 + lado3
perimetro = calcularPerimetro(lado1, lado2, lado3)  #invocar o llamar la funcion
area = calcularArea(lado1, lado2, lado3)   #invocar o llamar la funcion

#6. SALIDAS CON PRINT
os.system("cls")   #limpiar pantalla del terminal
mostrarPerimetro (lado1, lado2, lado3, perimetro) #invocar el procedimiento
mostrarArea (lado1, lado2, lado3, area)  #invocar el procedimiento



