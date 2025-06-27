# Eliminar valores ausentes
# 
# Ahora que sabes que hay algunos valores ausentes en tu DataFrame, 
# tienes algunas opciones para tratarlos. Una forma es eliminarlos completamente del conjunto de datos. 
# En este ejercicio, eliminarás los valores ausentes eliminando todas las filas que contengan valores ausentes.

import pandas as pd
import matplotlib.pyplot as plt
import os


# Obtener ruta base del archivo
base_path = os.path.dirname(os.path.abspath(__file__))
ruta_archivo = os.path.join(base_path, "..", "..", "Archivos", "avocados_2016.csv")

# Importa el excel sales.csv
avocados_2016 = pd.read_csv(ruta_archivo)

# ------------------------------------------------

# Eliminar las filas con valores faltantes
avocados_complete = avocados_2016.dropna()

# Verificar si alguna columna contiene valores faltantes
print(avocados_complete.isna().any())