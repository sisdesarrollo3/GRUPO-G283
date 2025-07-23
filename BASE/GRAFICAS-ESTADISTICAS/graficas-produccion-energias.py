import matplotlib.pyplot as plt
import pandas as pd
import os

def leer_archivo(archivo):
    try:
        return pd.read_csv(archivo)
    except Exception as e:
        print(f"Error al leer el archivo: {e}")
        return None
    

def graficarPastel ( df ): 
    #df = pd.DataFrame.from_dict(data, orient="index")   # Convertimos el diccionario a DataFrame

    # Creamos gráfico de pastel para Producción
    plt.figure(figsize=(6, 5))                          # Tamaño del gráfico
    plt.pie(df["produccion"],                           # Usamos columna de producción
            labels=df.index,                            # Etiquetas con nombre del país
            autopct='%1.1f%%',                          # Mostrar porcentaje con un decimal
            startangle=90,                              # Empezar desde arriba (90°)
            colors=["#98FB98", "#87CEFA", "#FFB347", "#DDA0DD"],  # Colores por país
            wedgeprops={'edgecolor': 'black'},          # Borde negro en cada porción
            shadow=True)           # Sombra para efecto 3D simulado
    plt.title("Distribución de Producción por País")    # Título del gráfico
    plt.tight_layout()
    plt.show()

    # Creamos gráfico de pastel para Consumo
    plt.figure(figsize=(6, 5))                          # Segundo gráfico con mismo tamaño
    plt.pie(df["consumo"],                              # Usamos columna de consumo
            labels=df.index,                            # Etiquetas con nombre del país
            autopct='%1.1f%%',                          # Mostrar porcentaje con un decimal
            startangle=90,                              # Mismo ángulo inicial
            shadow=True,                                # Sombra para efecto 3D simulado
            colors=["#FFA07A", "#ADD8E6", "#90EE90", "#FFD700"],  # Colores distintos para consumo
            wedgeprops={'edgecolor': 'black'})          # Bordes negros
    plt.title("Distribución de Consumo por País")       # Título del gráfico
    plt.tight_layout()
    plt.show()



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
    if data is not None:
        while True:
            print("\nMenú de Gráficas")
            print("1. Gráfico de Pastel")
            print("2. Histograma")
            print("3. Gráfico de Líneas")
            print("4. Salir")
            opcion = input("Selecciona una opción: ")

            if opcion == '1':
                #graficar_pastel(data, 'PAIS', 'PRODUCCION')
                graficarPastel ( data )
            elif opcion == '2':
                #graficar_histograma(data, 'PRODUCCION')
                graficarHistograma(data)
                input()
            elif opcion == '3':
                graficarLineas(data)
            elif opcion == '4':
                print("Saliendo...")
                break
            else:
                print("Opción no válida. Inténtalo de nuevo.")

if __name__ == "__main__":
    # Diccionario con datos de producción y consumo por país
    '''data = {
        "Colombia": {"produccion": 1200, "consumo": 900},
        "Ecuador": {"produccion": 1300, "consumo": 800},
        "Bolivia": {"produccion": 1400, "consumo": 700},
        "Venezuela": {"produccion": 1500, "consumo": 600}
    }'''
    # Cargar el CSV
    nombreArchivo = os.path.join("DATA", 'energias.csv')
    df = pd.read_csv(nombreArchivo)  # Asegúrate de que el archivo esté en tu ruta de trabajo

    # Convertir a diccionario con países como claves
    data = df.set_index("pais").to_dict(orient="index")

    #archivo = input("Ingresa el nombre del archivo (con extensión .csv): ")
    #data = leer_archivo(archivo)
    main()