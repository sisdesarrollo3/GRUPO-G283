# pip install pycountry pycountry-convert
import pandas as pd
from pycountry_convert import country_name_to_country_alpha2, country_alpha2_to_continent_code

# Leer el archivo CSV (ajusta la ruta si es necesaria)
df = pd.read_csv(r"C:\Users\J OROZCO\OneDrive\Documents\PROYECTOS-PYTHON-G283\GRUPO-G283\ENERGIAS\02 modern-renewable-energy-consumption.csv")

# Función para obtener continente desde el nombre del país
def get_continent(country_name):
    try:
        code = country_name_to_country_alpha2(country_name)
        continent_code = country_alpha2_to_continent_code(code)
        continents = {
            'AF': 'África',
            'AS': 'Asia',
            'EU': 'Europa',
            'NA': 'América del Norte',
            'SA': 'América del Sur',
            'OC': 'Oceanía',
            'AN': 'Antártida'
        }
        return continents.get(continent_code, 'Desconocido')
    except:
        return 'Desconocido'

# Aplicar la función a la columna 'Entity'
df["Continent"] = df["Entity"].apply(get_continent)

# Guardar el nuevo archivo CSV
df.to_csv("energy_with_continents.csv", index=False)