# Resumir fechas:
#
# Las estadísticas sumarias también pueden calcularse sobre columnas de fecha 
# que tengan valores con el tipo de datos datetime64. 
# 
# Algunas estadísticas sumarias, como la media, no tienen mucho sentido en las fechas, 
# pero otras son extremadamente útiles como, por ejemplo, el mínimo y el máximo, 
# que te permiten ver qué intervalo de tiempo abarcan tus datos.

# Import sales data
import pandas as pd
import os

# Obtener ruta base del archivo
base_path = os.path.dirname(os.path.abspath(__file__))
ruta_archivo = os.path.join(base_path, "..", "..", "Archivos", "sales.csv")

# Importa el excel sales.csv
sales = pd.read_csv( ruta_archivo)  

#-------------------------------------------

# Fecha maxima
print ( sales['date'].max() )

# Fecha minima
print ( sales['date'].min() )

