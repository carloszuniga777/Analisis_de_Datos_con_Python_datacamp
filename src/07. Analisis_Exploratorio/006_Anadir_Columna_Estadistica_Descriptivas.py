# Añadir estadísticas descriptivas
# Ahora "Duration" y "Price" contienen valores numéricos en el DataFrame planes, 
# y te gustaría calcular para ellos estadísticas de resumen condicionadas a los valores de otras columnas.

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import os

# Obtener ruta base del archivo
base_path = os.path.dirname(os.path.abspath(__file__))
ruta_archivo = os.path.join(base_path, "..", "..", "Archivos", "planes3.csv")

# Read in the CSV as a DataFrame
planes = pd.read_csv(ruta_archivo)

#----------------------------------------------------------------
# 1. Añade una columna a planes que contenga la desviación típica de "Price" basada en "Airline".

# Se crea una nueva columna y esta columna tendra el valor de la desviacion estandar en funcion del Airline
planes["airline_price_st_dev"] = planes.groupby("Airline")["Price"].transform(lambda x: x.std())

print(f'\n{ planes[["Airline", "airline_price_st_dev"]].value_counts() }')

#--------------------------------------------------------------
# 2. Calcula la mediana de "Duration" en "Airline", almacenándola como una columna llamada "airline_median_duration".

# Se crea una nueva columna y esta columna tendra el valor de la media en funcion del Airline
planes["airline_median_duration"] = planes.groupby("Airline")["Duration"].transform(lambda x: x.median())

print(f'\n{ planes[["Airline","airline_median_duration"]].value_counts() }')

#-----------------------------------------------------------------
# 3. Encuentra la media "Price" por "Destination", guardándola como una columna llamada "price_destination_mean".

# Se crea una nueva columna y esta columna tendra el valor de la media en funcion del Destination
planes["price_destination_mean"] = planes.groupby("Destination")["Price"].transform(lambda x: x.mean())

print(f'\n{ planes[["Destination","price_destination_mean"]].value_counts() }')


#-----------------------------------------------------------------------------
# La diferencia entre encontrar la media o cualquier funcion estadistica 
# Asi:
#         planes.groupby('Airline')['Price'].agg(['mean'])
# 
# 0 asi:
#        planes.groupby("Destination")["Price"].transform(lambda x: x.mean())
# 
# 1. Es que con agg(['std']):   
#
#   - Operación: Agregación - colapsa cada grupo en un solo valor
#   - Resultado: DataFrame/Series con una fila por grupo (8 aerolíneas = 8 filas)
#   - Índice: Los nombres de las aerolíneas como índice
#   - Uso: Para obtener estadísticas resumidas por grupo
#
# 2. transform(lambda x: x.std()):
#  - Operación: Transformación - mantiene la forma original del DataFrame
#  - Resultado: Series con el mismo número de filas que el DataFrame original (10,660 filas)
#  - Valores: Cada fila contiene la media de su grupo correspondiente
#  - Uso: Para asignar estadísticas del grupo a cada observación individual
#
# Ejemplo práctico: Si quieres crear una nueva columna con la desviación estándar 
# de cada aerolínea para cada vuelo, usarías transform(). 
# Si solo quieres ver un resumen estadístico por aerolínea, usarías agg().


