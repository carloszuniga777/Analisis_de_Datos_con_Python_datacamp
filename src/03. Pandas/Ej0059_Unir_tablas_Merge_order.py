
# Aviso sobre merge_ordered() con varias columnas
# Cuando utilices merge_ordered() para combinar en varias columnas, 
# el orden es importante cuando lo combinas con la función de relleno hacia delante. 
# La función ejecuta la fusión en columnas en el orden proporcionado. 
# 
# En este ejercicio, fusionaremos los datos del PIB 
# y de población del Banco Mundial para Australia y Suecia, 
# invirtiendo el orden de la fusión en las columnas. 
# 
# La frecuencia de las series es diferente, los valores del PIB son trimestrales, 
# y los de la población son anuales. Utiliza la función de relleno 
# hacia delante para rellenar los datos que faltan. 
# 
# Según el orden proporcionado, el avance de relleno utilizará datos no previstos 
# para rellenar los valores que faltan.



import pandas as pd
import matplotlib.pyplot as plt
import os


# Obtener ruta base del archivo
base_path = os.path.dirname(os.path.abspath(__file__))
ruta_archivo_gdp = os.path.join(base_path, "..", "..", "Archivos", "gdp2.csv")
ruta_archivo_pop= os.path.join(base_path, "..", "..", "Archivos", "pop.csv")

# Cargando los archivos CSV
gdp = pd.read_csv(ruta_archivo_gdp)
pop = pd.read_csv(ruta_archivo_pop)

# ------------------------------------------------
# Ejemplo 1: Cruzando por fecha y luego country (Incorrecto)

print("-------------INCORRECTO ---------------")
print('\n\n')

# Fusionar por columnas 'date' y 'country'
ctry_date = pd.merge_ordered(gdp, pop, 
                             on=['date', 'country'],
                             fill_method='ffill'
                             )

print(ctry_date)
print('\n\n')

# Se cruza sin fill_method para validacion visual
ctry_date = pd.merge_ordered(gdp, pop, 
                             on=['date', 'country'],
                             )

print(ctry_date)

# Se puede observar que los valores de la poblacion (pop) y series_coide
# Se autocomplentan tomando los valores de las series de Suecia y Australia
# como valor anterior, y eso es incorrecto

# ------------------------------------------------
# Ejemplo 2: Cruzando por country y luego fecha (Incorrecto)

print('\n\n')
print("-------------CORRECTO ---------------")
print('\n\n')

# Fusionar por columnas 'date' y 'country'
ctry_date = pd.merge_ordered(gdp, pop, 
                             on=['country', 'date'],   #Cambiando el orden de las columnas, primero country y luego date
                             fill_method='ffill'
                             )

# Se puede observar que los valores de la poblacion (pop) y series_coide
# Se autocomplentan tomando los valores correspondientes de su pais,
# Para los de australia se toman los valores anteriores de la poblacion de Australia
# Mientras que para los de Suecia se toman los valores anteriores de la poblacion de Suecia

print(ctry_date)
print('\n\n')

# Cuando combinas primero en date, la tabla se ordena por date y luego por country. 
# Cuando se aplica el relleno hacia adelante, el valor de la población de Suecia en enero 
# se usa para llenar los valores faltantes tanto para Australia como para Suecia 
# durante el resto del año. Esto no es lo que quieres. 
# 
# El relleno hacia adelante está usando datos no deseados para llenar los valores faltantes. 
# Sin embargo, cuando combinas primero en country, la tabla se ordena por country
#  y luego por date, por lo que el relleno hacia adelante se aplica adecuadamente en esta situación.