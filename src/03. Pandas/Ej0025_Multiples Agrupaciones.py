# Múltiples resúmenes agrupados
#
# Anteriormente, en este capítulo, has visto que el método .agg() es útil 
# para calcular múltiples estadísticos sobre múltiples variables. 
 


import pandas as pd
import os


# Obtener ruta base del archivo
base_path = os.path.dirname(os.path.abspath(__file__))
ruta_archivo = os.path.join(base_path, "..", "..", "Archivos", "sales.csv")

# Importa el excel sales.csv
sales = pd.read_csv( ruta_archivo)  

#--------------------------------------------------
#Ejemplo 1

# Obteniendo el minimo, maximo,media y mediana de weekly_sales para cada tipo de tienda
sales_stats = sales.groupby('type')['weekly_sales'].agg(['min', 'max', 'mean', 'median'])

# Print sales_stats
print(sales_stats)

print('\n\n')
#-----------------------------------------------------
#Ejemplo 2 

# Obteniendo el minimo, maximo,media y mediana de 
# unemployment y fuel_price_usd_per_l para cada tipo de tienda.
unemp_fuel_stats = sales.groupby('type')[['unemployment', 'fuel_price_usd_per_l']].agg(['min', 'max', 'mean', 'median'])

# Print unemp_fuel_stats
print(unemp_fuel_stats)