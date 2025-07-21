import os
import sys
import time

from colorama import init, Fore, Back, Style, Cursor
init()

# Obtener la ruta absoluta de la carpeta raíz del proyecto (PROYECTO) 
base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
# Agregar la carpeta BIBLIOTECA al path
sys.path.append(os.path.join(base_dir, "BIBLIOTECA"))
# Importar libreria
import libreria   #la primera vez muestra error de sintaxis

def menu():
    print("*** GESTIONAR ENTIDAD ****")
    print(Style.DIM + Fore.GREEN  + "[1]. llamar la función uno")
    print("[2]. llamar la función dos")
    print("[3]. llamar la función tres")
    print("[4]. Salir")
    print(Style.RESET_ALL)

def main():   
    while True:
        libreria.limpiarPantalla()
        menu()
        opcion = libreria.LeerCaracter("OPCIÓN: ")
        match opcion:
            case '1':
                print("llamando a la funcion UNO donde se encuentre")
                time.sleep(2)
            case '2':
                print("llamando a la funcion DOS donde se encuentre")
                time.sleep(2)
            case '3':
                print("llamando a la funcion TRES donde se encuentre")
                time.sleep(2)
            case '4':
                print("saliendo del programa")
                time.sleep(2)
                break    #sale del bucle y regresa desde donde fué llamado
                #si es salir por completo del programa entonces sys.exit()
            case _:            
                #print("Opción NO válida [1....4]")
                libreria.mensajeErrorEsperaSegundos("Opción NO válida [1....4]", 2)
                

if __name__ == "__main__":
    main()