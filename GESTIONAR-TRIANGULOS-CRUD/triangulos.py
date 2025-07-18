#importar librerias de python
import os
import time


#FUNCIONES PROPIAS
def menu ():
    os.system("cls")
    print ("*** GESTIONAR LA ENTIDAD *** ")
    print ("[1].  INSERTAR")
    print ("[2].  LISTAR")
    print ("[3].  CONSULTAR")
    print ("[4].  ACTUALIZAR")
    print ("[5].  ELIMINAR")
    print ("[6].  SALIR")



def main():
    while True:
        menu()
        opcion = input("OPCION: ")[0]
        match opcion:
            case '1':
                print("PROXIMAMENTE INSERTAR UNA NUEVA ENTIDAD")
                time.sleep(1)
            case '2':
                print("PROXIMAMENTE LISTAR TODOS LOS REGISTROS DE UNA ENTIDAD")
                input()
                #time.sleep(1)
            case '3':
                print("PROXIMAMENTE CONSULTAR UNA ENTIDAD X EL CODIGO")
                time.sleep(1)
            case '4':
                print("PROXIMAMENTE ACTUALIZAR UNA ENTIDAD POR EL CODIGO")
                time.sleep(1)
            case '5':
                print("PROXIMAMENTE ELIMINAR UNA ENTIDAD X EL CODIGO")
                time.sleep(1)
            case '6':
                print("SALE DEL PROGRAMA")
                time.sleep(1)


if __name__ == "__main__":
    main()