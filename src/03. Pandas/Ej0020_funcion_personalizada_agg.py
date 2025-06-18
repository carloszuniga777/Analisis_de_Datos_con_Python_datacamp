# Resúmenes eficaces
# Aunque pandas y NumPy tienen muchas funciones, 
# a veces puedes necesitar una función diferente para resumir tus datos.

# El método .agg() te permite aplicar tus propias funciones personalizadas a un DataFrame,
# así como aplicar funciones a más de una columna de un DataFrame a la vez, 
# haciendo que tus agregaciones sean muy eficientes. Por ejemplo:

# df['column'].agg(function)
# 
# En la función personalizada para este ejercicio, 
# "IQR" es la abreviatura de rango intercuartílico, 
# que es el percentil 75 menos el percentil 25. Es una alternativa 
# a la desviación típica que resulta útil si tus datos contienen valores atípicos.


import pandas as pd
import os
import numpy as np


# Obtener ruta base del archivo
base_path = os.path.dirname(os.path.abspath(__file__))
ruta_archivo = os.path.join(base_path, "..", "..", "Archivos", "sales.csv")

# Importa el excel sales.csv
sales = pd.read_csv( ruta_archivo)  

#-------------------------------------------------

# Funcion personalizada IQR
def iqr(column):
    return column.quantile(0.75) - column.quantile(0.25)


#----------------------------------
#Ejemplo 1:

# Print IQR of the temperature_c column
print( sales['temperature_c'].agg(iqr))

#-----------------------------------
#Ejemplo 2

print('')

# Se agregaron las columnas: fuel_price_usd_per_l y unemployment
print(sales[["temperature_c", 'fuel_price_usd_per_l', 'unemployment']]
            .agg(iqr)
      )

#-----------------------------------------
# Ejemplo 3

print('')


# Incluyendo la mediana de numpy
print(
       sales[["temperature_c", "fuel_price_usd_per_l", "unemployment"]]
            .agg([iqr, 'median'])
    )