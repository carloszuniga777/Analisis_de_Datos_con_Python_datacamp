# Cortar series temporales
# La segmentación es especialmente útil para las series temporales, 
# ya que es habitual querer filtrar los datos dentro de un intervalo de fechas. 
# 
# Añade la columna date al índice y utiliza .loc[] para realizar el subconjunto. 
# Lo importante es recordar que debes mantener tus fechas en formato ISO 8601, 
# es decir, "yyyy-mm-dd" para año-mes-día, "yyyy-mm" para año-mes y "yyyy" para año.

# Recuerda del Capítulo 1 que puedes combinar varias condiciones booleanas utilizando operadores lógicos,
#  como &. Para hacerlo en una línea de código, tendrás que añadir paréntesis () alrededor de cada condición.

import pandas as pd
import os


# Obtener ruta base del archivo
base_path = os.path.dirname(os.path.abspath(__file__))
ruta_archivo = os.path.join(base_path, "..", "..", "Archivos", "temperatures.csv")

# Importa el excel sales.csv
temperatures = pd.read_csv(ruta_archivo)

# ------------------------------------------------

# Obteniendo el registro 5 y columna 1
print( temperatures.iloc[5, 1] )


print('\n\n')

# Ejemplo 1: Obteniendo los 5 primeros registros 
print( temperatures.iloc[:5] )

print('\n\n')

# Ejemplo 2: Obteniendo todos registros y seleccionando las columnas 3 y 4
print( temperatures.iloc[:, 2:4]  )

print('\n\n')

# Ejemplo 3: convinando ejemplo 1 y 2
# Obteniendo las primeros 5 registros y las columnas 3 y 4
print( temperatures.iloc[:5, 2:4])