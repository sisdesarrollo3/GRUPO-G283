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



def menu ():
    libreria.limpiarPantalla()
    print(Fore.GREEN + "*****  GESTION DE LA ENTIDAD **** " + Style.RESET_ALL)
    print(Fore.RED + "[1]." +  Style.RESET_ALL  + "LLAMADA A FUNCION UNO ")
    print("[2]. LLALMADA A FUNCION DOS ")
    print("[3]. LLALMADA A FUNCION TRES ")
    print("[4]. Salir")    
    print(Style.RESET_ALL)


def main():
    while True:
        menu()
        opcion = libreria.leerCaracter("SU OPCION: ")
        match opcion:
            case '1':
                print("ACA LLAMO A LA FUNCION UNO")
                time.sleep(1)
            case '2':
                print("ACA LLAMO A LA FUNCION DOS")
                time.sleep(1)
            case '3':
                print("ACA LLAMO A LA FUNCION TRES")
                time.sleep(1)
            case '4':
                print("GRACIAS POR UTILIZAR NUESTRO PROGRAMA")
                time.sleep(1)
                break
            case _:                
                print("❌  " + Fore.RED + Style.BRIGHT + "OPCION NO VALIDA [1....4]" + Style.RESET_ALL)
                time.sleep(2)

if __name__ == "__main__":
    main()