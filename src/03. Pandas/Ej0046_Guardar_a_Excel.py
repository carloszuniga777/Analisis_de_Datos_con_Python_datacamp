# Diccionario de listas
#
# ¡Acaban de llegar más datos! Esta vez, utilizarás el método del diccionario de listas,
#  analizando los datos columna por columna.

#    date	       small_sold	large_sold
#  "2019-11-17"	    10859987	7674135
#  "2019-12-01"	    9291631	    6238096


import pandas as pd
import matplotlib.pyplot as plt
import os

# Obtener ruta base del archivo
base_path = os.path.dirname(os.path.abspath(__file__))
ruta_archivo = os.path.join(base_path, "..", "..", "Archivos", "airline_bumping.csv")

# Importa el excel sales.csv
airline_bumping = pd.read_csv(ruta_archivo)

#---------------------------------------------------

print(airline_bumping.head())

# Para cada grupo de aerolíneas, selecciona las columnas nb_bumped y total_passengers, y calcula la suma 
airline_totals = airline_bumping.groupby("airline")[["nb_bumped", "total_passengers"]].sum()

# Crea una nueva columna de airline_totals llamada bumps_per_10k, 
# que es el número de pasajeros accidentados por cada 10 000 pasajeros en 2016 y 2017.
airline_totals["bumps_per_10k"] = airline_totals["nb_bumped"] / airline_totals["total_passengers"] * 10000

# Ordena airline_totals por los valores de bumps_per_10k de mayor a menor 
airline_totals_sorted = airline_totals.sort_values('bumps_per_10k', ascending=False)

print('\n\n')
print(airline_totals_sorted)

# Guardando el Dataframe a Excel
ruta_guardado = os.path.join(base_path, "..", "..", "Archivos", "airline_totals_sorted.csv")

airline_totals_sorted.to_csv(ruta_guardado, index=False)  # Sin columna de índices