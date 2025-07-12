'''
Dado un número del 1 al 7, imprime el día de la semana correspondiente.
ANALISIS:
   ENTRADAS: numeroDia
   PROCESOS: nombreDia <--  "lunes"        ???  numeroDia == 1     
             nombreDia <--  "Martes"
             nombreDia <--  "Miercoles"    ???  numeroDia == 3


             nombreDia <--  "Domingo"      ???  numeroDia == 7
   SALIDAS:  nombreDia
'''
#2. FUNCIONES Y PROCEDIMIENTOS PROPIOS - LOS CREAMOS CON DEF
def hallarNombreDia(numeroDia):
    match numeroDia:
        case 1:
            nombreDia = "Lunes"
        case 2:
            nombreDia = "Martes"
        case 3:
            nombreDia = "Miércoles"
        case 4:
            nombreDia = "Jueves"
        case 5:
            nombreDia = "Viernes"
        case 6:
            nombreDia = "Sábado"
        case 7:
            nombreDia = "Domingo"
        case _:
            nombreDia =  "Número no válido, debe ser del 1 al 7"
    return nombreDia


#3. RESERVAMOS E INICIALIZAMOS VARIABLES
numeroDia = 0
nombreDia = ""

#4. ENTRADAS con INPUT
numeroDia = int(input("Ingrese un número del 1 al 7: "))

#5. PROCESOS - FORMULAS
nombreDia = hallarNombreDia(numeroDia)

#6. SALIDAS CON PRINT
print(f"El día de la semana correspondiente al número {numeroDia} es: {nombreDia}")

