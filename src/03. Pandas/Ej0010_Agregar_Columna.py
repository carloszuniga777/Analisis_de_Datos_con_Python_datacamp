# Creando columna usando bucle:
# No es muy eficiente crear una columna usando bucle por que tiene que crear la columna en cada iteracion

# Import cars data
import pandas as pd
import os

# Obtener ruta base del archivo
base_path = os.path.dirname(os.path.abspath(__file__))
ruta_archivo = os.path.join(base_path, "..", "..", "Archivos", "cars.csv")

# Importa el excel cars.csv
cars = pd.read_csv( ruta_archivo, index_col=0 )  # index_col: Indica que la primer columna se debe utilizar como etiqueta de fila

# Code for loop that adds COUNTRY column
for label, row in cars.iterrows():
    cars.loc[label, "COUNTRY"] = row['country'].upper()


# Print cars
print(cars)