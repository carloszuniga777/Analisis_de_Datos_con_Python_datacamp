
# La función merge_asof() puede utilizarse para crear conjuntos de datos en los que tienes una tabla de fechas de inicio y fin,
# y quieres utilizarlas para crear una bandera en otra tabla. Te han dado gdp, 
# que es una tabla de valores trimestrales del PIB de EEUU durante la década de 1980. 
# 
# Además, se te ha entregado la tabla recession. Contiene la fecha de inicio de cada recesión en EEUU desde 1980, 
# y la fecha en que se declaró que la recesión había terminado. 
# 
# Utiliza merge_asof() para fusionar las tablas y crear una bandera de estado si un trimestre fue durante una recesión. 
# Por último, para comprobar tu trabajo, representa los datos en un diagrama de barras.

import pandas as pd
import matplotlib.pyplot as plt
import os


# Obtener ruta base del archivo
base_path = os.path.dirname(os.path.abspath(__file__))
ruta_archivo_gdp = os.path.join(base_path, "..", "..", "Archivos", "gdp3.csv")
ruta_archivo_recession= os.path.join(base_path, "..", "..", "Archivos", "recession.csv")


# Cargando los archivos CSV
gdp = pd.read_csv(ruta_archivo_gdp)
recession = pd.read_csv(ruta_archivo_recession)



# # ------------------------------------------------
# Formtenado la columna de fecha y hora
gdp['date'] = pd.to_datetime(gdp['date'], format='%d/%m/%Y', errors='coerce')
recession['date'] = pd.to_datetime(recession['date'], format='%d/%m/%Y', errors='coerce')

#-------------------------------------------------------------------

# Uniendo las tablas gdp y recession utilizando merge_asof con la coincidencia de fecha mas cercana hacia atras
gdp_recession = pd.merge_asof(gdp, recession, on='date')

# Crea una lista basada en el valor de fila de gdp_recession['econ_status']
# Si es recession = r, si es normal = g 
is_recession = ['r' if s == 'recession' else 'g' for s in gdp_recession['econ_status']]

# Plot a bar chart of gdp_recession
gdp_recession.plot(kind='bar', y='gdp', x='date', color=is_recession, rot=90, figsize=(12, 6))
plt.show()

# Puedes ver en el gráfico que hubo varios trimestres a principios de los años 80 donde la recesión fue un problema. 
# merge_asof() te permitió agregar rápidamente una bandera al conjunto de datos gdp al hacer coincidir entre dos fechas diferentes, 
# ¡en una sola línea de código! Si realizaras la misma tarea usando subsetting, habría tomado mucho más código.