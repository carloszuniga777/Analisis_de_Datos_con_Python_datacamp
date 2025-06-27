# Unir las tablas por INNER JOIN

import pandas as pd
import matplotlib.pyplot as plt
import os


# Obtener ruta base del archivo
base_path = os.path.dirname(os.path.abspath(__file__))
ruta_archivo_taxi_owners = os.path.join(base_path, "..", "..", "Archivos", "taxi_owners.csv")
ruta_archivo_taxi_veh = os.path.join(base_path, "..", "..", "Archivos", "taxi_veh.csv")

# Importa el excel sales.csv
taxi_owners = pd.read_csv(ruta_archivo_taxi_owners)
taxi_veh = pd.read_csv(ruta_archivo_taxi_veh)
# ------------------------------------------------
# Unir la tabla axi_owners y taxi_veh y configurar el sufijo
taxi_own_veh = taxi_owners.merge(taxi_veh, on='vid', suffixes=('_own','_veh'))

# Print the value_counts to find the most popular fuel_type
print(taxi_own_veh['fuel_type'].value_counts())