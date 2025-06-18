# ¿Recuerdas np.logical_and(), np.logical_or() y np.logical_not(), 
# las variantes NumPy de los operadores and, or y not? 
# 
# También puedes utilizarlos en la serie de pandas para realizar 
# operaciones de filtrado más avanzadas.


# Obtener los piases que cuyo cars_per_cap sea superior a 500

import pandas as pd
import numpy as np
import os

# Obtener ruta base del archivo
base_path = os.path.dirname(os.path.abspath(__file__))
ruta_archivo = os.path.join(base_path, "..", "..", "Archivos", "cars.csv")

# Importa el excel cars.csv
cars = pd.read_csv( ruta_archivo, index_col=0 )  # index_col: Indica que la primer columna se debe utilizar como etiqueta de fila

#1. Obteniendo la columna cars_per_cap
cpc = cars['cars_per_cap']

#2. Filtrando cars_per_cap para obtener los registros 
#   que esten entre los rangos 100 a 500
filter = np.logical_and(cpc > 100, cpc < 500)    #Se contruye una serie boleana [US: true, RU: false ...]

#3.Filtrando la tabla cars con los rangos
result = cars[filter]


print(result)
