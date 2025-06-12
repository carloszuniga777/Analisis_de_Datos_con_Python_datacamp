#Generar un array numpy bidimensional con datos aleatorios

import numpy as np

# Media: Es el valor central alrededor del cual se agrupan los datos

# Desviación estándar: Mide qué tan dispersos están los datos respecto a la media
# Un valor de 0.20 significa que la mayoría de los datos (≈68%) estarán entre:
# 1.75 ± 0.20 → entre 1.55 y 1.95 metros

height = np.round(np.random.normal(1.75, 0.20, 5000), 2)  #Parametros: Media: 1.75, Desviacion Estandar: 0.20, Cantidad: 5000

weight = np.round(np.random.normal(60.32, 15, 5000), 2)   #Parametros: Media: 60.32, Desviacion Estandar: 15, Cantidad: 5000

np_city = np.column_stack((height, weight))

print(np_city)