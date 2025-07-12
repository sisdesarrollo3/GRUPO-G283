import os

def limpiarPantalla ():
    if os.name == 'nt':  # Para sistemas Windows
        os.system('cls')
    else:  # Para sistemas Unix/Linux/Mac
        os.system('clear')