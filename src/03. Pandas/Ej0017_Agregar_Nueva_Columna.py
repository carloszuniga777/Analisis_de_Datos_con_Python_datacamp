# Añadir nuevas columnas:
# 
# No te quedes solo con los datos que te dan. 
# En su lugar, puedes añadir nuevas columnas a un DataFrame Esto tiene muchos nombres, 
# como transformación, mutación e ingeniería de características.

# Puedes crear columnas nuevas desde cero, pero también es habitual derivarlas 
# de otras columnas, por ejemplo, sumando columnas o cambiando sus unidades.

# homelessness es un DataFrame que contiene estimaciones de las personas sin hogar 
# en cada estado de EE. UU. en 2018. 
# 
# La columna individual es el número de personas sin hogar que no forman parte 
# de una familia con hijos. 
# 
# La columna family_members es el número de personas sin hogar que sí 
# forman parte de una familia con hijos. 
# 
# La columna state_pop es la población total del estado.


# Import homelessness data
import pandas as pd
import os

# Obtener ruta base del archivo
base_path = os.path.dirname(os.path.abspath(__file__))
ruta_archivo = os.path.join(base_path, "..", "..", "Archivos", "homelessness.csv")

# Importa el excel homelessness.csv
homelessness = pd.read_csv( ruta_archivo)  

# --------------------------------------------------

# Agregando la columna Total como una suma de las columnas individuals y family_members
homelessness['total'] = homelessness['individuals'] + homelessness['family_members']

# Agregando la columna p_homeless
homelessness['p_homeless'] = homelessness['total'] / homelessness['state_pop']

# See the result
print(homelessness)
