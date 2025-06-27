# Encontrar valores ausentes
# 
# Los valores ausentes están por todas partes y no quieres que interfieran en tu trabajo.
# Algunas funciones ignoran por defecto los datos que faltan, pero no siempre es ése el 
# comportamiento que puedes desear. Algunas funciones no pueden manejar valores omitidos en absoluto, 
# por lo que hay que ocuparse de estos valores antes de poder utilizarlas. 
# 
# Si no sabes dónde están tus valores ausentes, o si existen, podrías cometer errores en tu análisis. 
# En este ejercicio, determinarás si faltan valores en el conjunto de datos y, en caso afirmativo, cuántos.

import pandas as pd
import matplotlib.pyplot as plt
import os


# Obtener ruta base del archivo
base_path = os.path.dirname(os.path.abspath(__file__))
ruta_archivo = os.path.join(base_path, "..", "..", "Archivos", "avocados_2016.csv")

# Importa el excel sales.csv
avocados_2016 = pd.read_csv(ruta_archivo)

# ------------------------------------------------

# Verificar valores faltantes individuales
print( avocados_2016.isna() )

# Verificar valores faltantes en cada columna (Resumen)
print( avocados_2016.isna().any() )

# Grafico de barras del numero total de valores faltante en cada columna
avocados_2016.isna().sum().plot(kind='bar')

plt.show()