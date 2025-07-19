#importar librerias de python
import os
import time
import sys

# Obtener la ruta absoluta de la carpeta raíz del proyecto (PROYECTO) 
base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
# Agregar la carpeta BIBLIOTECA al path
sys.path.append(os.path.join(base_dir, "BIBLIOTECA"))
# Importar libreria
import libreria   #la primera vez muestra error de sintaxis

#FUNCIONES PROPIAS
def leerDatos():
    valores = {}
    lado1 = libreria.leerFlotante("LADO 1: ", 1, 9999999999)
    lado2 = libreria.leerFlotante("LADO 1: ", 1, 9999999999)
    lado3 = libreria.leerFlotante("LADO 1: ", 1, 9999999999)

    #armar la estructura como diccionario
    valores = {
        "lado1": lado1,
        "lado2": lado2,
        "lado3": lado3
    }
    return valores

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

nombreArchivo = "triangulos.dat"

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
                    triangulos[codigo] = valores
                    libreria.guardar(triangulos, nombreArchivo)
                    libreria.mensajeErrorEsperaSegundos("INSERTADO CORRECTAMENTE", 2)
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
                print("PROXIMAMENTE ACTUALIZAR UNA ENTIDAD POR EL CODIGO")
                time.sleep(1)
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
                            libreria.guardar(triangulos, nombreArchivo)
                            #libreria.mensajeErrorEsperaSegundos(">>>>> REGISTRO ELIMINADO", 1)
                    else:
                        libreria.mensajeEsperaSegundos(">>> EL CODIGO NO EXISTE ", 1)
            case '6':
                print("SALE DEL PROGRAMA")
                time.sleep(1)
                break


if __name__ == "__main__":
    triangulos = libreria.cargar(triangulos, nombreArchivo)    
    main()