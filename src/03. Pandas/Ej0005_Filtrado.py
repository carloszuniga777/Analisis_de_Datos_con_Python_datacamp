# Conducir por la derecha:
#
# El código del ejemplo anterior funcionaba bien, 
# pero en realidad has creado innecesariamente una nueva variable col_drives.
#  
# Puedes conseguir el mismo resultado sin esta variable intermedia. 
# Pon el código que calcula dr directamente en los corchetes 
# que seleccionan las observaciones de cars.

# Cargando los datos a pandas desde un archivo cars.csv
import pandas as pd
import os

# Obtener ruta base del archivo
base_path = os.path.dirname(os.path.abspath(__file__))
ruta_archivo = os.path.join(base_path, "..", "..", "Archivos", "cars.csv")

# Importa el excel cars.csv
cars = pd.read_csv( ruta_archivo, index_col=0 )  # index_col: Indica que la primer columna se debe utilizar como etiqueta de fila

# Filtrando cars
rows = cars[cars["drives_right"]]

# Imprimir
print(rows) #Se obtienen todos los paises que conduncen por la derecha (drives_right: true)
