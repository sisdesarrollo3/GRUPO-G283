import pandas as pd
import matplotlib.pyplot as plt

# Diccionario original con códigos como claves
data = {
    "EST01": {"Nombre": "ERNESTO", "PROGRAMACIÓN": 3.0, "INGLES": 4.0, "HABILIDADES": 5.0},
    "EST02": {"Nombre": "VALERIA", "PROGRAMACIÓN": 3.1, "INGLES": 4.1, "HABILIDADES": 5.0},
    "EST03": {"Nombre": "JOHN",    "PROGRAMACIÓN": 3.2, "INGLES": 4.2, "HABILIDADES": 5.0},
    "ESTNN": {"Nombre": "PAOLA",   "PROGRAMACIÓN": 3.3, "INGLES": 4.3, "HABILIDADES": 5.0}
}

# Crear DataFrame
df = pd.DataFrame.from_dict(data, orient="index")

# Calcular promedio por estudiante (excluyendo la columna "Nombre")
df["Promedio"] = df[["PROGRAMACIÓN", "INGLES", "HABILIDADES"]].mean( axis=1 )

# Crear gráfica de barras con código y nombre
etiquetas = [f"{codigo} - {df.loc[codigo, 'Nombre']}" for codigo in df.index]   # df.loc[filas, columnas]
promedios = df["Promedio"].values

plt.figure(figsize=(7, 4))
bars = plt.bar(etiquetas, promedios, color="salmon", edgecolor="black")

# Añadir etiquetas encima de cada barra
for bar in bars:
    altura = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, altura + 0.05, f"{altura:.2f}",
             ha='center', va='bottom', fontsize=9, fontweight='bold')

# Estilo del gráfico
plt.title("Promedio por Estudiante")
plt.xlabel("Código - Nombre")
plt.ylabel("Promedio")
plt.ylim(0, 6)
plt.xticks(rotation=45)   #grados de rotación de la etiqueta X
plt.grid(axis='y', linestyle='--', alpha=0.3)

plt.tight_layout()
plt.show()