'''
Desarrollar un programa en Lenguaje Python, que permita hallar el área y perímetro de cualquier triángulo, construyendo sus propias funciones, para las entradas, procesos y salidas:

NOTA: NO se conoce la altura, solamente los tres lados (Investigar por AI)

'''

#1. IMPORTAR LIBRERIAS DEL LENGUAJE
import math
import os

#2. FUNCIONES Y PROCEDIMIENTOS PROPIOS - LOS CREAMOS CON DEF
#Funcion que retorna el perimetro del triangulo con los lados enviados por parametro
def calcularPerimetro(lado1, lado2, lado3):
    return lado1 + lado2 + lado3

#Funcion que retorna el area del triangulo con los lados enviados por parametro
def calcularArea(l1, l2, l3):
    s = (l1 + l2 + l3) / 2
    area = math.sqrt(s * (s - l1) * (s - l2) * (s - l3))
    return area

#porque la raiza de un numero negativo no es posible, se valida si el area es posible
def validarSiArea(l1, l2, l3):
    s = (l1 + l2 + l3) / 2
    resultado = s * (s - l1) * (s - l2) * (s - l3)
    return resultado

#funcion que retorna un numero flotante, se indica la etiqueta enviada por parametro
def leerFlotante(mensaje):
    lado = float(input(mensaje))
    return lado

#UN PROCEDIMIENTO NO RETORNA NINGUN VALOR
def generarSalida (l1, l2, l3, p, a, mensajeTipo):
    print("\n***** PROGRAMA DEL TRIÁNGULO *********")
    print("LADO1 LADO2 LADO3 PERIMETRO AREA TIPO")
    print("=" * 50)
    print(f"{l1} \t {l2} \t {l3} \t {p} \t {a:.1f} \t {mensajeTipo}")

def generarSalidaTotal (contadorEquilateros, contadorEscalenos, contadorIsosceles):
    print("\n***** TOTALE POR TIPO DE TRIANGULO *********")
    print("EQUILATEROS   ESCALENOS   ISOSCELES")
    print("=" * 50)
    print(f"{contadorEquilateros} \t {contadorEscalenos} \t {contadorIsosceles}")


def hallarTipoTriangulo(l1, l2, l3):
    global contadorEquilateros
    mensaje= "ISOSCELES"
    if l1 == l2 and l2 == l3:
        mensaje = "EQUILATERO"
        contadorEquilateros = contadorEquilateros + 1
    elif (l1 != l2 and l1 != l3 and l2 != l3 ):
        mensaje = "ESCALENO"    
        contadorEscalenos += 1
    else:
        contadorIsosceles += 1
    return mensaje

def valiarTriangulo(lado1, lado2, lado3):
    valido = False
    if (lado1 + lado2 > lado3) and (lado1 + lado3 > lado2) and (lado2 + lado3 > lado1):
        valido = True
    return valido

#3. RESERVAMOS E INICIALIZAMOS VARIABLES
lado1 = 0
lado2 = 0
lado3 = 0
perimetro = 0
area = 0
mensajeTipo = ""

contadorEquilateros = 0
contadorEscalenos = 0
contadorIsosceles = 0



#ENCERRAMOS EN UN BUCLE PARA REPETIR EL MISMO PROCESO VARIAS VECES
respuesta = 's'   #MI VARIABLE DE CONTROL RESPUESTA INICIA EN UN VALOR PARA INGRESAR POR PRIMERA VEZ AL BUCLE
while (respuesta ==  's'):   #MI VARIABLE DE CONTROL ES COMPARADA CON UN VALOR, PARA QUE SE EJECUTE POR VERDADERO Y SALGA POR FALSO
    #4. ENTRADAS con INPUT
    lado1 = leerFlotante("LADO 1: ")
    lado2 = leerFlotante("LADO 2: ")
    lado3 = leerFlotante("LADO 3: ")

    # Validar si los lados forman un triángulo
    if (lado1 + lado2 > lado3) or (lado1 + lado3 > lado2) or (lado2 + lado3 > lado1):
        #5. PROCESOS - FORMULAS
        #perimetro = lado1 + lado2 + lado3
        perimetro = calcularPerimetro(lado1, lado2, lado3)  #invocar o llamar la funcion
        os.system("cls")   #limpiar pantalla del terminal
        #validamos si el area es posible
        if validarSiArea(lado1, lado2, lado3) >= 0:
            area = calcularArea(lado1, lado2, lado3)   #invocar o llamar la funcion
        else:
            mensajeTipo = "Error NO se puede calcular el área"
            #print("el area no es posible, por la raiz de un numero negativo")
        #6. SALIDAS CON PRINT
        
        
        mensajeTipo = hallarTipoTriangulo(lado1, lado2, lado3)
    else:
        mensajeTipo = "Error"

    
    generarSalida (lado1, lado2, lado3, perimetro, area, mensajeTipo) #invocar el procedimiento    

    respuesta = input("DESEA CONTINUAR (sI/NO)")[0].lower()  #MI VARIABLE DE CONTROL ES ACTUALIZA PARA REGRESAR AL INICIO DEL BUCLE

#SALIDA EN TIEMPO DE TOTAL 
generarSalidaTotal (contadorEquilateros, contadorEscalenos, contadorIsosceles)



