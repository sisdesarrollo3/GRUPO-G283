import pandas as pd
import matplotlib.pyplot as plt

# [1]. Datos de los estudiantes
data = {
    "EST01": {"Nombre": "ERNESTO", "PROGRAMACIÓN": 3.0, "INGLES": 4.0, "HABILIDADES": 5.0},
    "EST02": {"Nombre": "VALERIA", "PROGRAMACIÓN": 3.1, "INGLES": 4.1, "HABILIDADES": 5.0},
    "EST03": {"Nombre": "JOHN",    "PROGRAMACIÓN": 3.2, "INGLES": 4.2, "HABILIDADES": 5.0},
    "ESTNN": {"Nombre": "PAOLA",   "PROGRAMACIÓN": 3.3, "INGLES": 4.3, "HABILIDADES": 5.0}
}

# [2]. Convertimos en DataFrame
# Usamos orient="index" para que los códigos queden como índices del DataFrame
df = pd.DataFrame.from_dict(data, orient="index")

# [3]. Calculamos los promedios por componente
promedios = df[["PROGRAMACIÓN", "INGLES", "HABILIDADES"]].mean()

# [4]. Identificamos la porción de mayor valor para 'explotarla'
max_index = promedios.idxmax()  # Devuelve el nombre del componente con mayor promedio
explode = [0.1 if componente == max_index else 0 for componente in promedios.index]

# [5]. Creamos el gráfico de pastel con sombra y explosión
plt.figure(figsize=(6, 6))
plt.pie(
    promedios,
    labels=promedios.index,
    autopct='%1.2f%%',
    explode=explode,               # Separa la porción con mayor valor
    shadow=True,                   # Sombra para efecto 3D simulado
    startangle=90,
    colors=["#90ee90", "#ffcc99", "#66c2ff"],
    wedgeprops={'edgecolor': 'black'}
)

# [6]. Título y despliegue
plt.title(f"Promedios por Componente (Destacado: {max_index})")
plt.tight_layout()
plt.show()

#OTRAS DERIVACIONES
#df[["PROGRAMACIÓN", "INGLES", "HABILIDADES"]].nunique()   - Cuenta cuántos valores diferentes hay en cada columna.