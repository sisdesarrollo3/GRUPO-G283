#[1]. IMPORTAMOS LIBRERÍAS
import pandas as pd                # Pandas permite manejar datos en forma de tabla (DataFrames)
import matplotlib.pyplot as plt    # Matplotlib se usa para generar gráficos, en este caso, de barras

#[2]. DEFINIMOS LOS DATOS EN UN DICCIONARIO DE DICCIONARIOS
# Cada clave principal es el código del estudiante
# Cada valor es otro diccionario con nombre y notas en diferentes componentes
data = {
    "EST01": {"Nombre": "ERNESTO", "PROGRAMACIÓN": 3.0, "INGLES": 4.0, "HABILIDADES": 5.0},
    "EST02": {"Nombre": "VALERIA", "PROGRAMACIÓN": 3.1, "INGLES": 4.1, "HABILIDADES": 5.0},
    "EST03": {"Nombre": "JOHN",    "PROGRAMACIÓN": 3.2, "INGLES": 4.2, "HABILIDADES": 5.0},
    "ESTNN": {"Nombre": "PAOLA",   "PROGRAMACIÓN": 3.3, "INGLES": 4.3, "HABILIDADES": 5.0}
}

#[3]. CONVERTIMOS LOS DATOS EN UN DATAFRAME
# Usamos orient="index" para que los códigos queden como índices del DataFrame
df = pd.DataFrame.from_dict(data, orient="index")

#[4]. CALCULAMOS PROMEDIOS POR COMPONENTE
# Aplicamos .mean() a las columnas numéricas para obtener los promedios generales
promedios = df[["PROGRAMACIÓN", "INGLES", "HABILIDADES"]].mean()

#[5]. CREAMOS GRÁFICO DE BARRAS
plt.figure(figsize=(6, 4))  # Tamaño del gráfico en pulgadas: ancho x alto
bars = plt.bar(promedios.index, promedios.values, color="lightgreen", edgecolor="black")  # Barras en color verde claro

#[6]. AÑADIMOS VALORES ENCIMA DE LAS BARRAS
# Por cada barra, obtenemos su altura (valor) y colocamos texto encima
for bar in bars:
    altura = bar.get_height()  # Altura de la barra
    plt.text(bar.get_x() + bar.get_width()/2, altura + 0.1, f"{altura:.2f}",  # Posición y formato del texto
             ha='center', va='bottom', fontsize=10, fontweight='bold')       # Estética del texto

#[7]. PERSONALIZAMOS LA ESTÉTICA DEL GRÁFICO
plt.title("Promedio por Componente Académico")     # Título del gráfico
plt.xlabel("Componente")                           # Etiqueta del eje X
plt.ylabel("Promedio")                             # Etiqueta del eje Y
plt.ylim(0, 6)                                      # Límites del eje Y (0 a 6, rango típico en notas)
plt.grid(axis='both', linestyle='--', alpha=0.5)    # Cuadrícula punteada en ambos ejes con transparencia

#[8]. AJUSTAMOS DISEÑO Y MOSTRAMOS EL GRÁFICO
plt.tight_layout()  # Ajusta márgenes automáticamente para que nada quede cortado
plt.show()          # Muestra el gráfico en pantalla