# Resúmenes con .groupby() y .agg()
# 
# En este ejercicio, explorarás las medias y desviaciones típicas de los datos anuales de desempleo. 
# En primer lugar, encontrarás las medias y desviaciones típicas independientemente del continente para observar 
# las tendencias mundiales del desempleo. Después, comprobarás las tendencias del desempleo desglosadas por continente.


import pandas as pd
import os


# Obtener ruta base del archivo
base_path = os.path.dirname(os.path.abspath(__file__))
ruta_archivo = os.path.join(base_path, "..", "..", "Archivos", "unemployment.csv")

# Importa el excel sales.csv
unemployment = pd.read_csv( ruta_archivo)  

#--------------------------------------------------
# Ejemplo 1
# Imprime la media y la desviación estándar (en ese orden) de las tasas de desempleo para 2019 y 2020, agrupadas por continente.

resumen =  unemployment[["continent", "2019", "2020"]].groupby('continent').agg(['mean', 'std'])

print(resumen)
print('\n\n')
#--------------------------------------------------
# Ejemplo 2
# Creando nueva columna de resumen

resumen =  unemployment[["continent", "2020"]].groupby('continent').agg(
    mean_rating=("2020", "mean"),    
    std_rating=("2020", "std"),    
    median_year=("2020", "median")
)

print(resumen)
print('\n\n')
#-------------------------------------------
# Especificar agregaciones por columnas, usando diccionario

resumen = unemployment.agg({'2020': ['mean', 'std'], '2021': ['median']})

print(resumen)