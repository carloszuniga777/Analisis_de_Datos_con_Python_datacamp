# Subconjunto con .loc[]
#
# La función clave de los índices es .loc[]: 
# un método de subconjunto que acepta valores de índice. 
# Si le pasas un único argumento, tomará un subconjunto de filas.
#
# El código para el subconjunto que utiliza .loc[] 
# puede ser más fácil de leer que el subconjunto estándar de corchetes,
# lo que puede hacer que tu código sea menos pesado de mantener.

import pandas as pd
import os


# Obtener ruta base del archivo
base_path = os.path.dirname(os.path.abspath(__file__))
ruta_archivo = os.path.join(base_path, "..", "..", "Archivos", "temperatures.csv")

# Importa el excel sales.csv
temperatures = pd.read_csv(ruta_archivo)

# --------------------------------------------------

# Estableciendo el indice de temperatures en city
temperatures_ind = temperatures.set_index('city')

#print(temperatures_ind)

#-----------------------------------------------

# Ejemplo: En este ejemplo se establece 
# que teniendo city como indice se hace mas facil el filtrado 
# que no teniendolo como indice
  
# Para filtrar city siendo este una columna normal 
# Es necesario hacer lo siguiente:  
 
 # Lista de ciudades a filtrar
cities = ["Salvador", "Belo Horizonte"]

cityfilter = temperatures[ temperatures['city'].isin(cities) ]

print(cityfilter)

#------------------------------------
# Filtrando las ciudades por medio de loc,
# En este caso las ciudades estan definidas como indices, 
# por lo que es mas facil el filtrado, que el anterior ejemplo

result = temperatures_ind.loc[cities]

print(result)