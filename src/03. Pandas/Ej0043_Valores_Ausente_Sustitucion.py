# Sustitución de valores ausentes:
#
# Otra forma de tratar los valores que faltan es sustituirlos todos por el mismo valor. 
# Para las variables numéricas, una opción es sustituir los valores por 0- lo harás aquí. 
# Sin embargo, cuando sustituyes valores ausentes, haces suposiciones sobre lo que significa 
# un valor ausente. En este caso, supondrás que la falta de un número vendido significa 
# que no se realizaron ventas de ese tipo de aguacate esa semana.
#
# En este ejercicio, verás cómo la sustitución de valores ausentes puede afectar a la distribución
# de una variable utilizando histogramas. 
# 
# Puedes trazar histogramas de varias variables a la vez de la siguiente forma:
#
# dogs[["height_cm", "weight_kg"]].hist()

import pandas as pd
import matplotlib.pyplot as plt
import os


# Obtener ruta base del archivo
base_path = os.path.dirname(os.path.abspath(__file__))
ruta_archivo = os.path.join(base_path, "..", "..", "Archivos", "avocados_2016.csv")

# Importa el excel sales.csv
avocados_2016 = pd.read_csv(ruta_archivo)

# ------------------------------------------------

# Lista de columnas con valores faltantes
cols_with_missing = ["small_sold", "large_sold", "xl_sold"]

# Llenando los valores faltantes con 0
avocados_filled = avocados_2016.fillna(0)

# Crear histograma de las columnas con valores faltantes
avocados_filled[cols_with_missing].hist()

plt.show()