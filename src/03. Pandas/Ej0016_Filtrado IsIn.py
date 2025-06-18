# Subconjunto de filas por variables categóricas:
# El subconjunto de datos basado en una variable categórica suele implicar 
# el uso del operador or (|) para seleccionar filas de varias categorías. 
# 
# Esto puede resultar tedioso cuando quieres todos los estados de una de las tres 
# regiones diferentes, por ejemplo. 
# 
# En su lugar, utiliza el método .isin(), que te permitirá abordar este problema 
# escribiendo una sola condición en lugar de tres distintas.
# 
#  colors = ["brown", "black", "tan"]
#  condition = dogs["color"].isin(colors)
#  dogs[condition]

# Import homelessness data
import pandas as pd
import os

# Obtener ruta base del archivo
base_path = os.path.dirname(os.path.abspath(__file__))
ruta_archivo = os.path.join(base_path, "..", "..", "Archivos", "homelessness.csv")

# Importa el excel homelessness.csv
homelessness = pd.read_csv( ruta_archivo)  

# --------------------------------------------------

# Filtrando homelessness por los estados California, arizona, nevada y utah
filtroEstados = ["California", "Arizona", "Nevada", "Utah"]
estados = homelessness[homelessness['state'].isin(filtroEstados)]

print(estados)

