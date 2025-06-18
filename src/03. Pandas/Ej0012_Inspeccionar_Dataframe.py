# Inspeccionar un DataFrame:
# Cuando tengas un nuevo DataFrame con el que trabajar,
# lo primero que tienes que hacer es explorarlo y ver qué contiene.
# Hay varios métodos y atributos útiles para ello.

#  -.head() devuelve las primeras filas (el encabezado del DataFrame).
#
#  -.info() muestra información sobre cada una de las columnas,
#        como el tipo de datos y el número de valores que faltan.
#
#  -.shape devuelve el número de filas y columnas del DataFrame.
#
#  -.describe() calcula unas cuantas estadísticas sumarias para cada columna.
#
#  homelessness es un DataFrame que contiene estimaciones de las personas sin hogar
#  en cada estado de EE. UU. en 2018. La columna individual es el número de personas sin hogar que no forman parte de una familia con hijos. La columna family_members es el número de personas sin hogar que sí forman parte de una familia con hijos. La columna state_pop es la población total del estado.

# Import homelessness data
import pandas as pd
import os

# Obtener ruta base del archivo
base_path = os.path.dirname(os.path.abspath(__file__))
ruta_archivo = os.path.join(base_path, "..", "..", "Archivos", "homelessness.csv")

# Importa el excel homelessness.csv
homelessness = pd.read_csv( ruta_archivo) 
# --------------------------------------------------

# Head: Imprime los primeros registros de la tabla
print(homelessness.head())


# info: Muestra la estructura de la tabla
print(homelessness.info())

# Shape: Muestra la cantidad de registros y columnas
print(homelessness.shape)


# Shape: Muestra informacion estadica basica 
print(homelessness.describe())