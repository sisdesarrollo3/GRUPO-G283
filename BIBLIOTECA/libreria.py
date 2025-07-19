import os
import time 
import msvcrt
import pickle

from tabulate import tabulate
from colorama import Fore, Back, Style, init
init()

###################################################################
#función que limpia la pantalla dependiendo del sistema operativo #
###################################################################
def limpiarPantalla ():
    if os.name == 'nt':  # Para sistemas Windows
        os.system('cls')
    else:  # Para sistemas Unix/Linux/Mac
        os.system('clear')

###############################################
#función lee un solo carácter NO espera ENTER #
###############################################
def leerCaracter (mensaje):
  print(mensaje, end="", flush=True)
  return msvcrt.getch().lower().decode('utf-8')  #getch captura un solo caracter No hay que dar enter

#############################################################
#función que muestra un mensaje enviado y espera N segundos #
#############################################################
def mensajeErrorEsperaSegundos( mensaje, segundos ):
    print(Fore.RED + Style.BRIGHT + mensaje + Style.RESET_ALL)
    time.sleep( segundos )

##############################################################################################
# Función que valida el ingreso de una cadena que no sea vacia y limitar un maximo caracteres#
# SI se quiere que retorne recortado usar return cadena[:maximoCaracteres]
##############################################################################################
def leerCadena( mensaje, maximoCaracteres ):
    while True:
        #print(f"{mensaje}", end="", flush=True)
        cadena = input( f"{mensaje} (Máx. {maximoCaracteres} caracteres): ").strip()
        if 0 < len(cadena) <= maximoCaracteres:  #Retorna la cadena válida
           return cadena[:maximoCaracteres] #cadena
        else:
            print(f"❌ Error: La cadena no debe estar vacía y debe tener máximo {maximoCaracteres} caracteres.", end="", flush=True)
            time.sleep(1)                 # Pausa breve de 1 segundo)
            print("\r\033[K", end="")     # \r Mueve cursor al inicio de la línea y limpia la línea con \033[K
            print("\033[F\033[K", end="") # Mueve cursor al final de la línea de arriba y limpia la línea
            continue

############################################################################
# Función que valida el ingreso de un decimal en un rango minimo y maximo  #
############################################################################
def  leerFlotante (mensaje, minimo, maximo):
  while True:
    print(f"{mensaje} ({minimo}-{maximo}): ", end="", flush=True)
    valor = input().strip().replace(",", ".")
    # Verificar que no esté vacío ni tenga espacios intermedios
    if not valor or " " in valor:
      print(f"❌Error: {mensaje} no debe estar vacío ni contener espacios.", end="", flush=True)
      time.sleep(1)                 # Pausa breve de 1 segundo)
      print("\r\033[K", end="")     # \r Mueve cursor al inicio de la línea y limpia la línea con \033[K
      print("\033[F\033[K", end="") # Mueve cursor al final de la línea de arriba y limpia la línea
      continue
      # Verificar si es un número decimal válido
    try:
      numero = float(valor)
      if minimo <= numero <= maximo:  # numero >= minimo and numero <= maximo
        return numero
      else:
        print(f"❌Error: {mensaje} debe estar entre {minimo} y {maximo}.", end="", flush=True)
        time.sleep(1)                 # Pausa breve de 1 segundo
        print("\r\033[K", end="")     # Mueve cursor al inicio de la línea y limpia la línea
        print("\033[F\033[K", end="") # Mueve cursor al final de la línea de arriba y limpia la línea
    except ValueError:
      print("❌Error: {mensaje} inválida. ", end="", flush=True)
      time.sleep(1)                 # Pausa breve de 1 segundo
      print("\r\033[K", end="")     # Mueve cursor al inicio de la línea y limpia la línea
      print("\033[F\033[K", end="") # Mueve cursor al final de la línea de arriba y limpia la línea

def mensajeEsperaSegundos( mensaje, segundos ):
    print(Fore.GREEN + Style.BRIGHT + mensaje + Style.RESET_ALL)
    time.sleep( segundos )

##################################################################
# Procedimiento que espera que el usuario presione Enter         #
##################################################################
def mensajeEsperaEnter( mensaje ):
    print("\n" + Fore.GREEN + Style.BRIGHT + mensaje + Style.RESET_ALL, end="")
    input()

#----------------------------------------------------------------------------#
#Función para listar cualquier lista, le debo enviar la lista y el encezado  #
#----------------------------------------------------------------------------#
def listar( listas ):
    # Códigos ANSI para color verde
    verde = '\033[92m'
    reset = '\033[0m'

    # Construir encabezado con color
    encabezado = ["ID"] + list(next(iter(listas.values())).keys())
    encabezado = [verde + col.upper() + reset for col in encabezado]

    # Construir la tabla
    tabla = [[id] + list(info.values()) for id, info in listas.items()]

    # Imprimir tabla con encabezado colorido
    print(tabulate(tabla, headers=encabezado, tablefmt='fancy_grid', floatfmt=".1f"))


#-------------------------------------------------------------------#
#recibe un diccionario lo muestra y validad la opcion del usuario   #
#VALIDA que sea un valor numerio en el rango enviado por parametro  #
#-------------------------------------------------------------------#
def leerDiccionario (diccionario, mensaje):            
      #tabla = [[clave, descripcion] for clave, descripcion in diccionario.items()]
      #print(tabulate(tabla, headers=["Clave", "Descripción"], tablefmt="fancy_grid"))
      while True:
        #   opcion = LeerCaracter( mensaje ).upper()
          opcion = leerCaracter(mensaje)
          if opcion in diccionario:
                return opcion
          else:
            print("❌  " + Fore.RED + Style.BRIGHT + "OPCION NO VALIDA" + Style.RESET_ALL, end="", flush=True)
            time.sleep(1) # Pausa breve de 1 segundo
            print(end="\r\033[K") # Mueve el cursor al inicio de la linea y limpia la línea

#---------------------------------------------------------#
# Función para guardar Información en Archivos - MODO  w, # 
# si existe lo borra, si no existe lo crea                #
#---------------------------------------------------------#
def guardar(lista, filename):
    archivo = open( filename, 'wb') #W se abre solo para escritua y si existe lo borra y crea uno nuevo y B indica que un archivo binario
    pickle.dump(lista, archivo)
    archivo.close()
    print(""+Fore.LIGHTYELLOW_EX+"\n\n>>> Guardando Información en los archivos correspondientes <<< " + Style.RESET_ALL)
    time.sleep(2)

#----------------------------------------------------------------------#
# Función para cargar Información en Archivos, MODO R, de solo lectura #
#----------------------------------------------------------------------#
def cargar(lista, filename):
    try:
        archivo = open(filename, 'rb')   #R se abre solo para lectura y B indica que un archivo binario
        lista = pickle.load(archivo)
        archivo.close()
        print("" + Fore.RED+"\n>>> Cargando Información : "+filename + '' + Style.RESET_ALL)
        time.sleep(1)
        return lista
    except:
        print("" + Fore.RED+"\n>>> Error al cargar el archivo o no se ha creado: " + filename + '' + Style.RESET_ALL)
        time.sleep(1)
    return lista