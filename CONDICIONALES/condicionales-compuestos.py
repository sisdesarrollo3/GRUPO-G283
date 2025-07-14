'''
Un almacén desea aplicar un descuento de acuerdo al valor de la compra.
si el valor es mayor o igual a 100, se aplica un descuento del 10%. 
si el valor es menor a 100 y mayor a 50, se aplica un descuento del 5%.
si el valor es menor o igual a 50, no se aplica descuento.

ANALISIS:
    ENTRADAS:  valorCompra
    PROCESOS:  porcentaje <-- 0  ???          valorCompra < 50
               porcentaje  <-- 10%   ???      valorCompra >= 100
               porcentaje  <-- 5%   ???       valorCompra < 100 and valorCompra >= 50
               descuento <-- valorCompra * porcentaje   
               valorFinal <-- valorCompra - descuento                                
    SALIDAS:   valorCompra, descuento, valorFinal
'''
#1. IMPORTAR LIBRERIAS DEL LENGUAJE
import os

#2. FUNCIONES Y PROCEDIMIENTOS PROPIOS - LOS CREAMOS CON DEF
def calcularPorcentaje(valorCompra):
    porcentaje = 0
    if (valorCompra >= 100):
        porcentaje = 0.10
    elif (valorCompra >= 50):
        porcentaje = 0.05
    return porcentaje

def calcularDescuento(valorCompra, porcentaje):
    return valorCompra * porcentaje

def calcularValorFinal(valorCompra, descuento):
    return valorCompra - descuento

def generarSalida(valorCompra, porcentaje, descuento, valorFinal):
    os.system("cls")   #limpiar pantalla del terminal
    print("\n***** DETALLES DE LA COMPRA *********")
    print("VALOR COMPRA PORCENTAJE  DESCUENTO  VALOR FINAL")    
    print("=" * 50)
    print(f"{valorCompra} \t {porcentaje}% \t {descuento} \t {valorFinal}")
    

#3. RESERVAMOS E INICIALIZAMOS VARIABLES
valorCompra = 0
porcentaje = 0
descuento = 0
valorFinal = 0

#4. ENTRADAS con INPUT
valorCompra = float(input("INGRESE EL VALOR DE LA COMPRA: "))

#5. PROCESOS - FORMULAS - LLAMAO a FUNCIONES Y PROCEDIMIENTOS
porcentaje = calcularPorcentaje(valorCompra)
descuento = calcularDescuento(valorCompra, porcentaje)
valorFinal = calcularValorFinal(valorCompra, descuento)

#6. SALIDAS CON PRINT - LLAMADO a PROCEDIMIENTOS
generarSalida(valorCompra, porcentaje, descuento, valorFinal)