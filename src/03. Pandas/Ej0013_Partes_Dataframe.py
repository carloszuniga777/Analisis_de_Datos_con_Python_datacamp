# Partes de un DataFrame

# Para comprender mejor los objetos DataFrame, es útil saber que constan
# de tres componentes, almacenados como atributos:
#
#  -.values: una matriz NumPy bidimensional de valores.
#
#  -.columns: un índice de columnas, con los nombres de las columnas.
#
#  -.index: un índice de las filas, con los números o nombres de fila.
#
# Resulta habitual pensar en los índices como una lista de cadenas o números,
# aunque el tipo de datos Index de pandas permite opciones más sofisticadas,
# que se tratarán más adelante en el curso.

# Import homelessness data
import pandas as pd
import os

# Obtener ruta base del archivo
base_path = os.path.dirname(os.path.abspath(__file__))
ruta_archivo = os.path.join(base_path, "..", "..", "Archivos", "homelessness.csv")

# Importa el excel homelessness.csv
homelessness = pd.read_csv(ruta_archivo)  

# --------------------------------------------------

# values: Imprime los valores de la tabla
print(homelessness.values)

# columns: Muestra las columnas de la tabla
print(homelessness.columns)

# index: Muestra los indices de las filas
print(homelessness.index)
