# Media y mediana:
# 
# Las estadísticas sumarias son exactamente lo que parecen: 
# resumen muchos números en una sola estadística. 
# Por ejemplo, la media, la mediana, el mínimo, el máximo y la desviación típica 
# son estadísticas sumarias. 
# 
# Calcular estadísticas sumarias te permite
#  hacerte una mejor idea de tus datos, aunque sean muchos.

# Import sales data
import pandas as pd
import numpy as np
import os

# Obtener ruta base del archivo
base_path = os.path.dirname(os.path.abspath(__file__))
ruta_archivo = os.path.join(base_path, "..", "..", "Archivos", "sales.csv")

# Importa el excel sales.csv
sales = pd.read_csv( ruta_archivo)  

#-------------------------------------------

# Media
print(sales['weekly_sales'].mean())

# Mediana
print(sales['weekly_sales'].median())

#------------------------------------------

print("\n\nCalcular la media, mediana usando agg")

print( sales.agg( { 'weekly_sales': ['mean', 'median'] } ) ) 

#------------------------------------------
print("\n\notra manera de calcular la media, mediana con numpy")

print(  np.mean(sales["weekly_sales"])  )
print(  np.median(sales["weekly_sales"]) )