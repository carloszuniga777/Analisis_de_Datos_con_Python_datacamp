# # Creando columna usando Apply:
# Utilizar para iterar por cada observación de un DataFrame Pandas es fácil de entender, pero no muy eficiente. 
# En cada iteración, creas una nueva serie de pandas.iterrows()
#
# Si quieres añadir una columna a un DataFrame mediante una llamada a una función de otra columna, 
# el método en combinación con un bucle no es la mejor forma de hacerlo.
#  En su lugar, deberás utilizar apply()

# Import cars data
import pandas as pd
import os

# Obtener ruta base del archivo
base_path = os.path.dirname(os.path.abspath(__file__))
ruta_archivo = os.path.join(base_path, "..", "..", "Archivos", "cars.csv")

# Importa el excel cars.csv
cars = pd.read_csv( ruta_archivo, index_col=0 )  # index_col: Indica que la primer columna se debe utilizar como etiqueta de fila

# Agregar la columna usando apply
cars["COUNTRY"] = cars["country"].apply(str.upper) 


# Print cars
print(cars)