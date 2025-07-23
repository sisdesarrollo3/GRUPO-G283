import os
import time
import pandas as pd
import matplotlib.pyplot as plt


def menu ():    
    print ("*** GRAFICAS DE CONSUMO Y PRODUCCION DE ENERGIAS RENOVABLES ***")
    print ("[1]. GRAFICAR HISTOGRAMA")
    print ("[2]. GRAFICAR PASTEL O TARTAS")
    print ("[3]. GRÁFICAR LINEAS")
    print ("[4]. SALIR")

def graficar_pastel( data ):
    df = pd.DataFrame.from_dict(data, orient='index')  #convertimos el diccionario a dataframe - tabla

    # Crear figura compartida
    # AXS->Lista de Ejes(1 fila, 2) columnas, fig->Objeto figura completa
    fig, axs = plt.subplots(1, 2, figsize=(12, 5), facecolor='orange')  
    fig.suptitle("Energías Renovables - Comparativo", fontsize=14, fontweight='bold')

    #crear el gráfico de produccion
    #plt.figure(figsize=(6,5))     #tamaño del grafico en pulgadas
    
    axs[0].pie (
        df["produccion"],          #nombramos la columna de produccion
        labels  = df.index,        #Etiquetas con el nombrre del pais
        autopct = '%1.1f%%',       #mostrar porcentaje con un decimal
        startangle = 90,            #empezar desde arriba 90 grado
        colors = ["#98FB98", "#87CEFA", "#FFB347", "#DDA0DD"],  # Colores por país
        wedgeprops = {'edgecolor': 'black'},  #Borde negro por cada porcion
        shadow = True              #sombra para el efecto 3D
    ) 

    axs[0].set_title("DISTRIBUCIÓN DE PRODUCCIÓN X PAIS")
    #axs[0]..tight_layout()
    #plt.show()

    #crear el gráfico de consumo
    #plt.figure(figsize=(6,5))     #tamaño del grafico en pulgadas
    axs[1].pie (
        df["consumo"],          #nombramos la columna de consumo
        labels  = df.index,        #Etiquetas con el nombrre del pais
        autopct = '%1.1f%%',       #mostrar porcentaje con un decimal
        startangle = 90,            #empezar desde arriba 90 grado
        colors = ["#98FB98", "#87CEFA", "#FFB347", "#DDA0DD"],  # Colores por país
        wedgeprops = {'edgecolor': 'black'},  #Borde negro por cada porcion
        shadow = True              #sombra para el efecto 3D
    ) 

    axs[1].set_title("DISTRIBUCIÓN DEL CONSUMO X PAIS")
    plt.tight_layout()
    plt.show()


def main():    
    while True:
        os.system('cls')
        menu()
        opcion = input("OPCION: ")[0].lower()
        match opcion:
            case '1':
                graficar_pastel( data )
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
    data = df.set_index("pais").to_dict(orient="index")
    main()
