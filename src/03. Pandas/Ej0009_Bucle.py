# Import cars data
import pandas as pd
import os

# Obtener ruta base del archivo
base_path = os.path.dirname(os.path.abspath(__file__))
ruta_archivo = os.path.join(base_path, "..", "..", "Archivos", "cars.csv")

# Importa el excel cars.csv
cars = pd.read_csv( ruta_archivo, index_col=0 )  # index_col: Indica que la primer columna se debe utilizar como etiqueta de fila


# Iterate over rows of cars
for label, row in cars.iterrows():
    print(f"\nlabel:\n {label}")
    print(f"\nrow:\n {row}")


print("")

# Iterando cars para imprmir los cars_per_cap
for label, row in cars.iterrows():
    print(f'{label}: {row["cars_per_cap"]}')
