#importar librerias de python
import os
import time
import sys
import copy
import math

# Obtener la ruta absoluta de la carpeta raíz del proyecto (PROYECTO) 
base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
# Agregar la carpeta BIBLIOTECA al path
sys.path.append(os.path.join(base_dir, "BIBLIOTECA"))
# Importar libreria
import libreria   #la primera vez muestra error de sintaxis

#FUNCIONES PROPIAS
#Funcion que retorna el perimetro del triangulo con los lados enviados por parametro
def calcularPerimetro(lado1, lado2, lado3):
    return lado1 + lado2 + lado3

#Funcion que retorna el area del triangulo con los lados enviados por parametro
def calcularArea(l1, l2, l3):
    s = (l1 + l2 + l3) / 2
    area = math.sqrt(s * (s - l1) * (s - l2) * (s - l3))
    return area

def hallarTipoTriangulo(l1, l2, l3):
    mensaje= "ISOSCELES"
    if l1 == l2 and l2 == l3:
        mensaje = "EQUILATERO"
    elif (l1 != l2 and l1 != l3 and l2 != l3 ):
        mensaje = "ESCALENO" 
    return mensaje

def valiarTriangulo(lado1, lado2, lado3):
    valido = False
    if(lado1 + lado2 > lado3) and (lado1 + lado3 > lado2) and (lado2 + lado3 > lado1):
        valido = True
    return valido

#LEER LOS DATOS DE LA ESTRUCTURA UNO A UNO, 
#SI ES POSIBLE CONSTRUIR EL TRIANGULO, RETORNA LOS VALORES, SI  NO RETORNA VACIO
def leerDatos():
    valores = {}
    lado1 = libreria.leerFlotante("LADO 1: ", 1, 9999999999)
    lado2 = libreria.leerFlotante("LADO 2: ", 1, 9999999999)
    lado3 = libreria.leerFlotante("LADO 3: ", 1, 9999999999)

    if (valiarTriangulo(lado1, lado2, lado3)):
        #armar la estructura como diccionario
        area = calcularArea( lado1, lado2, lado3)
        perimetro = calcularPerimetro(lado1, lado2, lado3)
        tipoTriangulo = hallarTipoTriangulo(lado1, lado2, lado3)
        valores = {
            "lado1": lado1,
            "lado2": lado2,
            "lado3": lado3,
            "area": area,
            "perimetro": perimetro,
            "tipo": tipoTriangulo
        }
    else:
        libreria.mensajeErrorEsperaSegundos(">>>> NO SE PUEDE CONSTRUIR EL TRIANGULO CON ESTOS LADOS", 1)
    return valores

#RECIBE LA ESTRUCTURA INDIVIDUAL, Y SOBRE LA MISMA SE SOBRESCRIBEN LOS VALORES, 
#SI ES POSIBLE CONSTRUIR EL TRIANGULO, RETORNA LOS VALORES, SI  NO RETORNA VACIO
def actualizar( triangulo ):
    valores = {}
    codigo = next(iter(triangulo))
    while True:
        libreria.limpiarPantalla()
        libreria.listar(triangulo)
        menuActualizar()
        opcion = libreria.leerCaracter('OPCION: ').lower()
        match opcion:
            case '1':
                triangulo[codigo]["lado1"] = libreria.leerFlotante("LADO 1: ", 1, 9999999999)
            case '2':
                triangulo[codigo]["lado2"] = libreria.leerFlotante("LADO 1: ", 1, 9999999999)
            case '3':
                triangulo[codigo]["lado3"] = libreria.leerFlotante("LADO 1: ", 1, 9999999999)
            case '4':   
                if (valiarTriangulo(triangulo[codigo]["lado1"], triangulo[codigo]["lado2"], triangulo[codigo]["lado3"])):             
                    area = calcularArea( triangulo[codigo]["lado1"], triangulo[codigo]["lado2"], triangulo[codigo]["lado3"])
                    perimetro = calcularPerimetro(triangulo[codigo]["lado1"], triangulo[codigo]["lado2"], triangulo[codigo]["lado3"])
                    tipoTriangulo = hallarTipoTriangulo(triangulo[codigo]["lado1"], triangulo[codigo]["lado2"], triangulo[codigo]["lado3"])
                    valores = {
                        "lado1": triangulo[codigo]["lado1"],
                        "lado2": triangulo[codigo]["lado2"],
                        "lado3": triangulo[codigo]["lado3"],
                        "area": area,
                        "perimetro": perimetro,
                        "tipo": tipoTriangulo
                    }
                    return valores
                else:
                    libreria.mensajeErrorEsperaSegundos(">>>> NO SE PUEDE CONSTRUIR EL TRIANGULO CON ESTOS LADOS", 1)
            case '5':
                return valores

def menuActualizar ():
    print ("*** NUEVOS DATOS *** ")
    print ("[1].  LADO 1")
    print ("[2].  LADO 2")
    print ("[3].  LADO 3")
    print ("[4].  ACEPTAR Y REGRESAR")
    print ("[5].  CANCELAR Y REGRESAR")



def menu ():
    os.system("cls")
    print ("*** GESTIONAR LA ENTIDAD *** ")
    print ("[1].  INSERTAR")
    print ("[2].  LISTAR")
    print ("[3].  CONSULTAR")
    print ("[4].  ACTUALIZAR")
    print ("[5].  ELIMINAR")
    print ("[6].  SALIR")

#INICIO DEL PROGRAMA

#VARIABLES GLOBALES 
triangulo = {}    #para la estructura individual
triangulos = {}   #para almacenar todas las estructura individuales

def main():
    while True:
        menu()
        opcion = libreria.leerCaracter("OPCION: ")
        match opcion:
            case '1':
                libreria.limpiarPantalla()
                print("*** INSERTAR ENTIDAD ***")
                codigo = libreria.leerCadena("CODIGO: ", 10).lower()
                if not (codigo in triangulos.keys()):
                    valores = leerDatos()
                    if (valores):
                        triangulos[codigo] = valores
                        libreria.guardar(triangulos, nombreArchivo)
                        libreria.mensajeEsperaSegundos("INSERTADO CORRECTAMENTE", 2)
                else:
                    libreria.mensajeErrorEsperaSegundos(" CODIGO YA EXISTE - NO PERMITO DUPLICADOS", 2)
            case '2':
                libreria.limpiarPantalla()
                print("*** LISTAR ENTIDAD ***")
                #print(triangulos)
                if ( triangulos ):
                    libreria.listar( triangulos )
                    libreria.mensajeEsperaEnter(">>>>>> FIN DE LISTAR <ENTER> CONTINUAR")
                else:
                    libreria.mensajeEsperaSegundos(">>> NADA PARA MOSTRAR ", 1)
                #time.sleep(1)
            case '3':
                libreria.limpiarPantalla()
                print("*** CONSULTAR ENTIDAD ***")
                #print(triangulos)
                if ( triangulos ):
                    codigo = libreria.leerCadena("CODIGO: ", 10).lower()
                    if (codigo in triangulos.keys()):
                        triangulo = {codigo: triangulos[codigo]}
                        libreria.listar(triangulo)
                        libreria.mensajeEsperaEnter(">>>>>> FIN DE CONSULTAR <ENTER> CONTINUAR")
                    else:
                        libreria.mensajeEsperaSegundos(">>> EL CODIGO NO EXISTE ", 1)

            case '4':
                libreria.limpiarPantalla()
                print("*** ACTUALIZAR ENTIDAD ****")
                if (not triangulos):
                    libreria.mensajeEsperaSegundos(">>> LISTA VACIA - NADA PARA ACTUALIZAR", 1)
                else:
                    codigo = libreria.leerCadena("CODIGO: ", 10).lower()
                    if codigo in triangulos.keys():
                        #triangulo = {codigo: triangulos[codigo]}  #extraer el registro ES UN ERROR PORQUE AFECTA TAMBIEN LA LISTA MAYOR
                        triangulo = {codigo: copy.deepcopy(triangulos[codigo])} 
                        valores_actualizados = actualizar( triangulo )
                        if valores_actualizados:
                            triangulos[codigo] = valores_actualizados
                            libreria.guardar(triangulos, nombreArchivo)
                            libreria.mensajeEsperaSegundos(">>> REGISTRO ACTUALIZADO CORRECTAMENTE", 1)
                        #libreria.listar(triangulo)
                        #input()
                    else:
                        libreria.mensajeEsperaSegundos('>>>>> CODIGO NO EXISTE', 1)
            case '5':
                libreria.limpiarPantalla()
                print("*** ELIMINAR ENTIDAD ***")
                #print(triangulos)
                if ( triangulos ):
                    codigo = libreria.leerCadena("CODIGO: ", 10).lower()
                    if (codigo in triangulos.keys()):
                        triangulo = {codigo: triangulos[codigo]}
                        libreria.listar(triangulo)
                        respuesta = libreria.leerCaracter("ESTA SEGURO DE ELIMINAR (Sí / No): ")[0].lower()
                        if (respuesta == 's'):
                            del triangulos[codigo]                            
                            libreria.mensajeErrorEsperaSegundos(">>>>> REGISTRO ELIMINADO", 1)
                            libreria.guardar(triangulos, nombreArchivo)
                    else:
                        libreria.mensajeEsperaSegundos(">>> EL CODIGO NO EXISTE ", 1)
            case '6':
                print("SALE DEL PROGRAMA")
                time.sleep(1)
                break


if __name__ == "__main__":
    nombreArchivo = os.path.join("DATA", 'triangulo.dat')
    triangulos = libreria.cargar(triangulos, nombreArchivo)    
    main()