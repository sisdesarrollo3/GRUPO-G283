'''
INDICAR con un mensaje si una persona es mayor de edad o no, segun su edad ingresada por teclado.
ANALISIS:
    ENTRADAS:  edad
    PROCESOS:  mensaje <-- "es mayor de edad" ?  (edad >= 18)
               mensaje <-- "no es mayor de edad" ? (edad < 18)
    SALIDAS:   mensaje
'''
#1. IMPORTAR LIBRERIAS DEL LENGUAJE
import os

#2. FUNCIONES Y PROCEDIMIENTOS PROPIOS - LOS CREAMOS CON DEF
def esMayorDeEdad(edad):
    mensaje = "ES MAYOR DE EDAD"
    if edad < 18:
        mensaje = "ES MENOR DE EDAD"
    return mensaje

#UN PROCEDIMIENTO NO RETORNA NINGUN VALOR
def mostrarMensaje (edad, mensaje):
    os.system("cls")   #limpiar pantalla del terminal
    print("\n***** PUESTO DE VOTACIONES *********")
    print(f"EDAD: {edad} \t MENSAJE: {mensaje}")
    print("=" * 50)

os.system("cls")   #limpiar pantalla del terminal

#3. RESERVAMOS E INICIALIZAMOS VARIABLES
edad = 0
mensaje = ""

#4. ENTRADAS con INPUT
edad = int(input("INGRESE SU EDAD: "))  

#5. PROCESOS - FORMULAS
mensaje = esMayorDeEdad(edad)  #invocar o llamar la funcion

#6. SALIDAS CON PRINT
mostrarMensaje (edad, mensaje)  #invocar el procedimiento
