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
    print(Fore.GREEN + "*****  GESTION DE TRIANGULOS **** " + Style.RESET_ALL)
    print(Fore.RED + "[1]." +  Style.RESET_ALL  + "INSERTAR ")
    print("[2]. LISTAR ")
    print("[3]. CONSULTAR ")
    print("[4]. ACTUALIZAR ")
    print("[5]. ELIMINAR ")
    print("[6]. SALIR")    
    print(Style.RESET_ALL)


def main():
    while True:
        menu()
        opcion = libreria.leerCaracter("SU OPCION: ")
        match opcion:
            case '1':
                print("ACA COMO INSERTAR UNO NUEVO")
                time.sleep(1)
            case '2':
                print("ACA COMO LISTAR TODAS LAS ENTIDADES")
                time.sleep(1)
            case '3':
                print("ACA COMO CONSULTAR UNA SOLA ENTIDAD X SU CODIGO")
                time.sleep(1)
            case '4':
                print("ACA COMO ACTUALIZAR UNA SOLA ENTIDAD X SU CODIGO, SUS DATOS")
                time.sleep(1)
                break
            case '5':
                print("ACA COMO ELIMINAR UNA ENTIDAD")
                time.sleep(1)
            case '6':
                print("ACA SALIR")
                time.sleep(1)
                break
            case _:                
                print("❌  " + Fore.RED + Style.BRIGHT + "OPCION NO VALIDA [1....4]" + Style.RESET_ALL)
                time.sleep(2)

if __name__ == "__main__":
    main()