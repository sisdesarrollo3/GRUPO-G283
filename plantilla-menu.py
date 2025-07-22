import os
import time
import pandas as pd


def menu ():    
    print ("*** GRAFICAS DE CONSUMO Y PRODUCCION DE ENERGIAS RENOVABLES ***")
    print ("[1]. GRAFICAR HISTOGRAMA")
    print ("[2]. GRAFICAR PASTEL O TARTAS")
    print ("[3]. GRÁFICAR LINEAS")
    print ("[4]. SALIR")

def main():    
    while True:
        os.system('cls')
        menu()
        opcion = input("OPCION: ")[0].lower()
        match opcion:
            case '1':
                print ("PROXIMAMENTE HISTOGRAMAS")
                time.sleep(1)
            case '2':
                print ("PROXIMAMENTE PASTEL")
                time.sleep(1)
            case '3':
                print ("PROXIMAMENTE LINEAS")
                time.sleep(1)
            case '4':
                print ("SALIENDO")
                time.sleep(1)
                break
            case _:
                 print ("OPCION NO VALIDA")
                 time.sleep(1)

if __name__ == "__main__":
    # Cargar el CSV
    nombreArchivo = os.path.join("DATA", 'energias.csv')
    df = pd.read_csv(nombreArchivo) # Asegúrate de que el archivo esté en ruta DATA
    # Convertir a diccionario con países como claves
    data = df.set_index("pais").to_dict(orient="index")   #en lugar del indice (0.1.,,,,) trabaja con la clave pais
    main()
