# Conducir por la derecha:
#
# Empecemos de forma sencilla e intentemos encontrar todas las
# observaciones en cars en las que drives_right sea True.
#
# drives_right es una columna booleana, por lo que tendrás que extraerla
# como serie y luego utilizar esta serie booleana
# para seleccionar observaciones de cars.


# Cargando los datos a pandas desde un archivo cars.csv
import pandas as pd
import os

# Obtener ruta base del archivo
base_path = os.path.dirname(os.path.abspath(__file__))
ruta_archivo = os.path.join(base_path, "..", "..", "Archivos", "cars.csv")

# Importa el excel cars.csv
cars = pd.read_csv( ruta_archivo, index_col=0 )  # index_col: Indica que la primer columna se debe utilizar como etiqueta de fila

# Extrayendo la columna drives_right como serie
# Esta columna contiene valores: true o false
col_drives = cars["drives_right"]  # [[US, true], [AUS, false], [JPN, true], [RU, false]]


# Filtrando cars
rows = cars[col_drives]


# Imprimir
print(rows) #Se obtienen todos los paises que conduncen por la derecha (drives_right: true)
