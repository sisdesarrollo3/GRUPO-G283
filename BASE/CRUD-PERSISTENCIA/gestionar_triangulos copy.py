import os
import sys
import time
import copy
from tabulate import tabulate
from colorama import init, Fore, Back, Style, Cursor
init()

# Obtener la ruta absoluta de la carpeta raíz del proyecto (PROYECTO) 
base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
# Agregar la carpeta BIBLIOTECA al path
sys.path.append(os.path.join(base_dir, "BIBLIOTECA"))
# Importar libreria
import libreria   #la primera vez muestra error de sintaxis

def valiarTriangulo(valoresLados):
    valido = False
    if (valoresLados["lado1"] + valoresLados["lado2"] > valoresLados["lado3"]) and (valoresLados["lado1"] + valoresLados["lado3"] > valoresLados["lado2"]) and (valoresLados["lado2"] + valoresLados["lado3"] > valoresLados["lado1"]):
        valido = True
    return valido

def leerDatos():
    lado1 = libreria.leerFlotante ("LADO 1: ", 0, 9999999)
    lado2 = libreria.leerFlotante ("LADO 2: ", 0, 9999999)
    lado3 = libreria.leerFlotante ("LADO 3: ", 0, 9999999)
    valores = {
        "lado1": lado1, 
        "lado2": lado2, 
        "lado3": lado3
    }
    return valores

def actualizar( triangulo_unico ):
    # Extraemos la única clave y datos
    codigo = next(iter(triangulo_unico))
    #datos = triangulo_unico[codigo]
    while True:
        libreria.limpiarPantalla()
        libreria.listar( triangulo_unico )
        menuActualizar()
        opcion = libreria.leerCaracter("SU OPCION: ")
        match opcion:
            case '1': triangulo_unico[codigo]['lado1'] = libreria.leerFlotante ("LADO 1: ", 0, 9999999)
            case '2': triangulo_unico[codigo]['lado2'] = libreria.leerFlotante ("LADO 2: ", 0, 9999999)
            case '3': triangulo_unico[codigo]['lado3'] = libreria.leerFlotante ("LADO 3: ", 0, 9999999)
            case '4': break
            case _:                
                print("❌  " + Fore.RED + Style.BRIGHT + "OPCION NO VALIDA [1....4]" + Style.RESET_ALL)
                time.sleep(2)   
    return triangulo_unico

def menuActualizar ():
    print(Fore.GREEN + "*****  ACTUALIZANDO DATOS **** " + Style.RESET_ALL)
    print(Fore.RED + "[1]." +  Style.RESET_ALL  + "LADO 1 ")
    print("[2]. LADO 2 ")
    print("[3]. LADO 3 ")
    print("[4]. SALIR")    
    print(Style.RESET_ALL)

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

confirmaciones = {
    's': "Sí",
    'n': "No"
}

triangulos = {}
triangulo  = {}

#filename = 'triangulos.dat'
# Ruta del archivo binario para los productos

def main():
    while True:
        menu()
        opcion = libreria.leerCaracter("SU OPCION: ")
        match opcion:
            case '1':
                libreria.limpiarPantalla()
                print("*** INSERTANDO NUEVA ENTIDAD ***")
                codigo = libreria.leerCadena("CÓDIGO: ", 5).lower()
                if (codigo in triangulos.keys()):
                    libreria.mensajeErrorEsperaSegundos("El Código de la Entidad ya existe NO se permiten duplicados", 2)
                else:
                    valores = leerDatos()
                    if (valiarTriangulo(valores)):
                        triangulos[codigo] = valores
                        libreria.guardar(triangulos, TRIANGULOS_FILE_PATH)
                        libreria.mensajeEsperaSegundos('*** INSERTADO CORRECTAMENTE ***', 1)
                    else:
                        libreria.mensajeErrorEsperaSegundos("ERROR: NO se puede construir un triangulo, la suma de dos lados debe ser mayor al tercer lado", 2)
            case '2':
                libreria.limpiarPantalla()
                print("*** LISTADO DE LA ENTIDAD ***")
                if (not triangulos):
                    libreria.mensajeEsperaSegundos("*** SIN ENTIDADES PARA LISTAR - LISTA VACIA", 2)
                else:
                    #print(triangulos)          
                    libreria.listar(triangulos)          
                    libreria.mensajeEsperaEnter('*** FIN DE LISTAR - <ENTER> CONTINUAR ***')
            case '3':
                libreria.limpiarPantalla()
                print("** CONSULAR ENTIDAD X SU CODIGO ***")
                if (not triangulos):
                    libreria.mensajeEsperaSegundos("*** SIN ENTIDADES PARA LISTAR - LISTA VACIA", 2)
                else:
                    codigo = libreria.leerCadena("CÓDIGO: ", 5).lower()
                    if (codigo in triangulos.keys()):
                        #print(triangulos[codigo])
                        triangulo_unico = {codigo: triangulos[codigo]}
                        libreria.listar(triangulo_unico)   
                        libreria.mensajeEsperaEnter("FIN DE CONSULTAR <ENTER> CONTINUAR***")
                    else:
                        libreria.mensajeEsperaSegundos('*** EL CODIGO A CONSULTAR NO EXISTE  ***', 2)

            case '4':
                libreria.limpiarPantalla()
                print("** ACTUALIZAR ENTIDAD X SU CODIGO ***")
                if (not triangulos):
                    libreria.mensajeEsperaSegundos("*** SIN ENTIDADES PARA LISTAR - LISTA VACIA", 2)
                else:
                    codigo = libreria.leerCadena("CÓDIGO: ", 5).lower()
                    if (codigo in triangulos.keys()):
                        #print(triangulos[codigo])
                        copia =  {codigo: copy.deepcopy(triangulos[codigo])}
                        #triangulo_unico ={codigo: triangulos[codigo]}
                        triangulo_unico = actualizar(copia)  
                        if (valiarTriangulo(triangulo_unico[codigo])):
                            triangulos[codigo] = copia[codigo]                            
                            libreria.guardar(triangulos, TRIANGULOS_FILE_PATH)
                            libreria.mensajeEsperaEnter("FIN DE ACTUALIZAR <ENTER> CONTINUAR***")
                        else:
                            libreria.mensajeErrorEsperaSegundos("ERROR: NO se puede construir un triangulo, la suma de dos lados debe ser mayor al tercer lado", 2)
                    else:
                        libreria.mensajeEsperaSegundos('*** EL CODIGO A CONSULTAR NO EXISTE  ***', 2)
            case '5':
                libreria.limpiarPantalla()
                print("** ELIMINAR ENTIDAD X SU CODIGO ***")
                if (not triangulos):
                    libreria.mensajeEsperaSegundos("*** SIN ENTIDADES PARA LISTAR - LISTA VACIA", 2)
                else:
                    codigo = libreria.leerCadena("CÓDIGO: ", 5).lower()
                    if (codigo in triangulos.keys()):
                        #print(triangulos[codigo])
                        triangulo_unico = {codigo: triangulos[codigo]}
                        libreria.listar(triangulo_unico)   
                        respuesta = libreria.leerDiccionario (confirmaciones, "ESTA SEGURO DE ELIMINAR (Sí / No):  ").lower()
                        if respuesta == 's':
                            del triangulos[codigo]   #borrado logico
                            libreria.guardar(triangulos, TRIANGULOS_FILE_PATH)  #borrado fisico
                            libreria.mensajeEsperaSegundos('*** EL TRIANGULO HA SIDO ELIMINADO  ***', 2)
                        libreria.mensajeEsperaEnter("FIN DE ELIMINAR <ENTER> CONTINUAR***")
                    else:
                        libreria.mensajeEsperaSegundos('*** EL CODIGO A ELIMINAR NO EXISTE  ***', 2)
            case '6':
                libreria.mensajeEsperaSegundos('*** SALIENDO - FIN DEL PROGRAMA  ***', 2)
                break
            case _:                
                print("❌  " + Fore.RED + Style.BRIGHT + "OPCION NO VALIDA [1....4]" + Style.RESET_ALL)
                time.sleep(2)

if __name__ == "__main__":    
    TRIANGULOS_FILE_PATH = os.path.join('PERSISTENCIA', 'triangulos.dat')
    triangulos = libreria.cargar(triangulos, TRIANGULOS_FILE_PATH)
    main()