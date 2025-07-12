'''
   aprendiento varibles
   tipo de datos, texto,numericos
'''
import os
import sys

# Obtener la ruta absoluta de la carpeta raíz del proyecto (PROYECTO) 
base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
# Agregar la carpeta BIBLIOTECA al path
sys.path.append(os.path.join(base_dir, "BIBLIOTECA"))
# Importar libreria
import libreria   #la primera vez muestra error de sintaxis


libreria.limpiarPantalla()
#ekjempolo tipo de dato texto
nombre= "JOHN JAIRO"

print("MY NOMBRE ES:", nombre)
print("NOMBRE ES DE TYPO: " , type(nombre))

#ejemplo tipo de dato entero


#ejemplo tipo de dato decimal

