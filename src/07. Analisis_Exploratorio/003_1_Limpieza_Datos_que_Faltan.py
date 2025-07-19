# Tratar los datos que faltan
# Es importante tratar los datos que faltan antes de empezar el análisis.
#
# Un enfoque consiste en descartar los valores que faltan si representan una pequeña proporción, 
# normalmente el 5 %, de tus datos.
#
# Trabajando con un conjunto de datos sobre precios de billetes de avión, 
# almacenado como un DataFrame de pandas llamado planes, tendrás que contar el número de valores perdidos en todas las columnas, 
# calcular el cinco por ciento de todos los valores, utilizar este umbral para eliminar observaciones 
# y comprobar cuántos valores perdidos quedan en el conjunto de datos.

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os

# Obtener ruta base del archivo
base_path = os.path.dirname(os.path.abspath(__file__))
ruta_archivo = os.path.join(base_path, "..", "..", "Archivos", "planes.csv")

# Read in the CSV as a DataFrame
planes = pd.read_csv(ruta_archivo)

#----------------------------------------------------------------
#1. Contar el numero de valores faltantes en cada columna

conteo_inicial =  planes.isna().sum()

print(f'\nAntes: Valores Faltantes en cada columna:\n {conteo_inicial}')
print(f'\nConteo registros inicial: {planes.shape}')

#-------------------------------------------------------------
# 2. Definicion del umbral

# - Calcula el 5% del total de filas del DataFrame
# - Por ejemplo, si hay 1000 filas, el umbral será 50
# - Este será el límite máximo de valores perdidos aceptables por columna

# Find the five percent threshold
threshold = len(planes) * 0.05

# Este umbral se utilizara para filtrar cada columna y encontrar si la columna 
# tiene menos del 5% de datos vacios, se podran eliminar esas filas

#-----------------------------------------------------------
# 3. Creacion del filtro
# Se obtiene una lista de columnas que tienen <= 5% de valores vacios

# Create a filter
cols_to_drop = planes.columns[planes.isna().sum() <= threshold]

print(f'\nColumnas con menos del 5% de valores vacios:\n {cols_to_drop}')

#-----------------------------------------------------------------
# 4. Eliminacion de filas con valores perdidos

# Elimina filas que contiene valores perdidos en las columnas que contienen un umbral de <=5% de valores faltantes
planes.dropna(subset=cols_to_drop, inplace=True)

print(f'\nDespues: Valores faltantes:\n {planes.isna().sum()}')
print(f'\nConteo registros final: {planes.shape}')

# Conclusion:
# Al crear un umbral de valores faltantes y usarlo para filtrar columnas, 
# has logrado eliminar los valores faltantes de todas las columnas excepto "Additional_Info" y "Price".