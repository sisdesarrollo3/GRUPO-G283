import os
import time 
import msvcrt
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