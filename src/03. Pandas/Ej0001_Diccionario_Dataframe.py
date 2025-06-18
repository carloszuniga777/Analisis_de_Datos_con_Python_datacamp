# De diccionario a DataFrame:

# Pandas es una biblioteca de código abierto que proporciona estructuras de datos 
# y herramientas de análisis de datos de alto rendimiento y fáciles de usar para Python. 
# ¡Suena prometedor!

# El DataFrame es una de las estructuras de datos más importantes de Pandas. 
# Básicamente, es una forma de almacenar datos tabulares en los que puedes 
# etiquetar las filas y las columnas. Una forma de construir un DataFrame 
# es a partir de un diccionario.

# En los ejercicios que siguen trabajarás con datos de vehículos de distintos países. 
# Cada observación corresponde a un país y las columnas dan información sobre el número 
# de vehículos per cápita, si la gente conduce por la izquierda o por la derecha, etc.

# En el script se definen tres listas:

# - names, que contiene los nombres de los países de los que se dispone de datos.
# - dr, una lista con booleanos que indica si la gente conduce por la izquierda 
#   o por la derecha en el país correspondiente.
# - cpc, el número de vehículos de motor por cada 1000 habitantes en el 
#   país correspondiente.
# 
# Cada clave del diccionario es una etiqueta de columna 
# y cada valor es una lista que contiene los elementos de la columna.

# Import pandas as pd
import pandas as pd

# Pre-defined lists
names = ['United States', 'Australia', 'Japan', 'India', 'Russia', 'Morocco', 'Egypt']
dr =  [True, False, False, False, True, True, True]
cpc = [809, 731, 588, 18, 200, 70, 45]


# Creacion de un diccionario
my_dict = {  'country':names, 
             'drives_right':dr, 
             'cars_per_cap':cpc 
            }

# Creacion de un Dataframe apartir del diccionario my_dict
cars = pd.DataFrame(my_dict)

# Print cars
print(cars)

# ¿Te has dado cuenta de que las etiquetas de las filas 
# (es decir, las etiquetas de las distintas observaciones) 
# se han establecido automáticamente en números enteros de 0 a 6?
#
# Para solucionarlo se ha creado una lista row_labels. 
# Puedes utilizarla para especificar las etiquetas de las filas del DataFrame cars

# Definicion de las etiquetas de fila
row_labels = ['US', 'AUS', 'JPN', 'IN', 'RU', 'MOR', 'EG']

# Specify row labels of cars
cars.index = row_labels

# Print cars again
print(cars)