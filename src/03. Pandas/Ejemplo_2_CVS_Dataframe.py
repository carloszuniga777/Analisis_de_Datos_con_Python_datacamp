# Cargando los datos a pandas desde un archivo cars.csv

import pandas as pd
import os

# Obtener ruta base del archivo
base_path = os.path.dirname(os.path.abspath(__file__))
ruta_archivo = os.path.join(base_path, '..', '..', 'Archivos', 'cars.csv')

#Importa el excel cars.csv 
cars = pd.read_csv(ruta_archivo, index_col = 0)  # index_col: Indica que la primer columna se debe utilizar como etiqueta de fila


# Print out cars
print(cars)

