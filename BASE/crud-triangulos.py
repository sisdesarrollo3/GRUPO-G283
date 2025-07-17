import pickle
import os

print(__name__)
FILENAME = "triangulos.pkl"

# 🧩 Cargar datos si existen
def cargar_datos():
    if os.path.exists(FILENAME):
        with open(FILENAME, "rb") as file:
            return pickle.load(file)
    return {}

# 💾 Guardar datos
def guardar_datos(data):
    with open(FILENAME, "wb") as file:
        pickle.dump(data, file)

# 🔨 Crear triángulo
def crear(triangulos, id, lado1, lado2, lado3):
    if id in triangulos:
        print(f"⚠️ El ID {id} ya existe.")
    else:
        triangulos[id] = {"lado1": lado1, "lado2": lado2, "lado3": lado3}
        guardar_datos(triangulos)
        print(f"✅ Triángulo {id} creado.")

# 🔍 Leer triángulo
def leer(triangulos, id=None):
    if id:
        tri = triangulos.get(id)
        if tri:
            print(f"📐 Triángulo {id}: {tri}")
        else:
            print(f"❌ El ID {id} no existe.")
    else:
        for tid, datos in triangulos.items():
            print(f"{tid}: {datos}")

# ✏️ Actualizar triángulo
def actualizar(triangulos, id, lado1=None, lado2=None, lado3=None):
    if id in triangulos:
        if lado1: triangulos[id]["lado1"] = lado1
        if lado2: triangulos[id]["lado2"] = lado2
        if lado3: triangulos[id]["lado3"] = lado3
        guardar_datos(triangulos)
        print(f"🔄 Triángulo {id} actualizado.")
    else:
        print(f"❌ No se encontró el ID {id}.")

# ❌ Eliminar triángulo
def eliminar(triangulos, id):
    if id in triangulos:
        del triangulos[id]
        guardar_datos(triangulos)
        print(f"🗑️ Triángulo {id} eliminado.")
    else:
        print(f"❌ No se puede eliminar. El ID {id} no existe.")

# 🏁 Ejemplo de uso
if __name__ == "__main__":
    triangulos = cargar_datos()

    crear(triangulos, 1, 3, 4, 5)
    crear(triangulos, 2, 6, 6, 6)
    leer(triangulos)
    actualizar(triangulos, 1, lado3=8)
    leer(triangulos, 1)
    eliminar(triangulos, 2)
    leer(triangulos)