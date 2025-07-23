import os
import time
import pandas as pd
import matplotlib.pyplot as plt


def menu ():    
    print ("*** GRAFICAS DE CONSUMO Y PRODUCCION DE ENERGIAS RENOVABLES ***")
    print ("[1]. GRAFICAR PASTEL O TARTAS")
    print ("[2]. GRAFICAR HISTOGRAMA")
    print ("[3]. GRÁFICAR LINEAS")
    print ("[4]. SALIR")

def graficar_pastel( data ):
    df = pd.DataFrame.from_dict(data, orient='index')  #convertimos el diccionario a dataframe - tabla

    #crear el gráfico de produccion
    plt.figure(figsize=(6,5))     #tamaño del grafico en pulgadas
    plt.pie (
        df["produccion"],          #nombramos la columna de produccion
        labels  = df.index,        #Etiquetas con el nombrre del pais
        autopct = '%1.1f%%',       #mostrar porcentaje con un decimal
        startangle = 90,            #empezar desde arriba 90 grado
        colors = ["#98FB98", "#87CEFA", "#FFB347", "#DDA0DD"],  # Colores por país
        wedgeprops = {'edgecolor': 'black'},  #Borde negro por cada porcion
        shadow = True              #sombra para el efecto 3D
    ) 

    plt.title("Distribución Producción - Energías Renovables x País")
    plt.tight_layout()
    plt.show()

    #crear el gráfico de consumo
    plt.figure(figsize=(6,5))     #tamaño del grafico en pulgadas
    plt.pie (
        df["consumo"],          #nombramos la columna de produccion
        labels  = df.index,        #Etiquetas con el nombrre del pais
        autopct = '%1.1f%%',       #mostrar porcentaje con un decimal
        startangle = 90,            #empezar desde arriba 90 grado
        colors = ["#98FB98", "#87CEFA", "#FFB347", "#DDA0DD"],  # Colores por país
        wedgeprops = {'edgecolor': 'black'},  #Borde negro por cada porcion
        shadow = True              #sombra para el efecto 3D
    ) 

    plt.title("Distribución Consumo - Energías Renovables x País")
    plt.tight_layout()
    plt.show()

#GRAFICAS HISTOGRAMA
def graficarHistograma ( data ):
    df = pd.DataFrame.from_dict(data, orient="index")   # Convertimos el diccionario en un DataFrame con países como índices

    import numpy as np        # Usamos numpy para manejar posiciones y desplazamientos de las barras
    x = np.arange(len(df))    # Creamos un arreglo con posiciones numéricas para cada país
                              # genera [0, 1, 2, ...] según el número de filas del DataFrame

    ancho = 0.35              # Definimos el ancho de cada barra

    plt.figure(figsize=(8, 5))     # Tamaño del gráfico: ancho de 8 y alto de 5 pulgadas

    # Dibujamos las barras de producción desplazadas hacia la izquierda
    barras_produccion = plt.bar(x - ancho/2, df["produccion"], width=ancho,
            label="Producción", color="green", edgecolor="black")

    # Dibujamos las barras de consumo desplazadas hacia la derecha
    barras_consumo = plt.bar(x + ancho/2, df["consumo"], width=ancho,
            label="Consumo", color="orange", edgecolor="black")

    plt.xticks(x, df.index)                     # Etiquetas del eje X usando los nombres de los países
    plt.title("Producción y Consumo por País")  # Título del gráfico
    plt.xlabel("País")                          # Etiqueta del eje X
    plt.ylabel("Kilovatios")                      # Etiqueta del eje Y
    plt.grid(axis='y', linestyle='--', alpha=0.4) # Cuadrícula horizontal punteada con transparencia
    plt.legend(title="Indicador")                 # Leyenda del gráfico con título

    # COLOCAMOS VALORES ENCIMA DE CADA BARRA
    for barra in barras_produccion:
        altura = barra.get_height()
        plt.text(barra.get_x() + barra.get_width()/2, altura + 20,  # Posición del texto
                f"{int(altura)}", ha='center', va='bottom', fontsize=9, fontweight='bold', color="green")

    for barra in barras_consumo:
        altura = barra.get_height()
        plt.text(barra.get_x() + barra.get_width()/2, altura + 20,
                f"{int(altura)}", ha='center', va='bottom', fontsize=9, fontweight='bold', color="orange")

    plt.tight_layout()    # Ajusta los márgenes para que todo encaje
    plt.show()            # Muestra el gráfico en pantalla

def graficarLineas( data ):
    df = pd.DataFrame.from_dict(data, orient="index")   # Convierte el diccionario en un DataFrame usando los países como índice

    plt.figure(figsize=(8, 5))                          # Define el tamaño del gráfico (ancho=8, alto=5 pulgadas)

    plt.plot(df.index, df["produccion"],              # Traza la línea de producción con etiquetas del eje X basadas en los países
            marker='o',                               # Estilo: marca circular en cada punto
            label="Producción",                       # Etiqueta para la leyenda
            color="green")                            # Color verde para la línea de producción

    plt.plot(df.index, df["consumo"],                  # Traza la línea de consumo por país
            marker='o',                               # Misma marca circular
            label="Consumo",                          # Etiqueta para la leyenda
            color="orange")                           # Color naranja para la línea de consumo

    # Mostrar valores encima de cada punto de producción
    for i, valor in enumerate(df["produccion"]):
        plt.text(df.index[i], valor + 3, str(valor),
                 ha='center', va='bottom', fontsize=9, color="black", fontweight='bold')


    plt.title("Producción vs. Consumo por País")       # Título principal del gráfico
    plt.xlabel("País")                                 # Etiqueta del eje X
    plt.ylabel("Kilovatios")                            # Etiqueta del eje Y
    plt.grid(True, linestyle='--', alpha=0.4)          # Cuadrícula horizontal con líneas punteadas y transparencia
    plt.legend(title="Indicador")                      # Muestra la leyenda con título
    plt.tight_layout()                                 # Ajusta el diseño para evitar que se corten etiquetas
    plt.show()                                         # Muestra el gráfico en pantalla



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
