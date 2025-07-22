import pandas as pd
import matplotlib.pyplot as plt

# [1]. Datos de los estudiantes
triangulos = {
    "tri01": {"lado1": 10, "lado2":10, "lado3":10, "perímetro":30, "área":0, "tipo_triangulo": "EQUILATERO"},
    "tri02": {"lado1": 8, "lado2":8, "lado3":5, "perímetro":21, "área":0, "tipo_triangulo": "ISÓSCELES"},
    "tri03": {"lado1": 7, "lado2":6, "lado3":5, "perímetro":18, "área":0, "tipo_triangulo": "ESCALENO"}
}

# [2]. Convertimos en DataFrame
# Usamos orient="index" para que los códigos queden como índices del DataFrame
df = pd.DataFrame.from_dict(triangulos, orient="index")

# [3]. Calculamos los promedios por componente
cuantos = df["tipo_triangulo"].value_counts()

# [4]. Identificamos la porción de mayor valor para 'explotarla'
max_index = cuantos.idxmax()  # Devuelve el nombre del componente con mayor cantidad
explode = [0.1 if triangulo == max_index else 0 for triangulo in cuantos.index]

# [5]. Creamos el gráfico de pastel con sombra y explosión
plt.figure(figsize=(6, 6))
plt.pie(
    cuantos,
    labels=cuantos.index,
    autopct='%1.2f%%',
    explode=explode,               # Separa la porción con mayor valor
    shadow=True,                   # Sombra para efecto 3D simulado
    startangle=90,
    colors=["#90ee90", "#ffcc99", "#66c2ff"],
    wedgeprops={'edgecolor': 'black'}
)

# [6]. Título y despliegue
plt.title(f"TRIANGULOS X TIPO (Destacado: {max_index})")
plt.tight_layout()
plt.show()

#OTRAS DERIVACIONES
#df[["PROGRAMACIÓN", "INGLES", "HABILIDADES"]].nunique()   - Cuenta cuántos valores diferentes hay en cada columna.