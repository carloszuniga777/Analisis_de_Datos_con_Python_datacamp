# Cálculos con .groupby()
# 
# El método .groupby() te facilita mucho la vida. 
# En este ejercicio, realizarás los mismos cálculos que la última vez, 
# excepto que utilizarás el método .groupby(). 
# 
# También realizarás cálculos sobre datos agrupados por dos variables 
# para ver si las ventas difieren por tipo de tienda dependiendo de si es una semana 
# festiva o no.


import pandas as pd
import os

# Obtener ruta base del archivo
base_path = os.path.dirname(os.path.abspath(__file__))
ruta_archivo = os.path.join(base_path, "..", "..", "Archivos", "sales.csv")

# Importa el excel sales.csv
sales = pd.read_csv( ruta_archivo)  

#--------------------------------------------------
#Ejemplo 1

# Agrupando por typo y obteniendo la sumatoria de ventas semanales por tipo
sales_by_type = sales.groupby("type")["weekly_sales"].sum()

# Obteniendo la proporción de ventas en cada tipo de tienda 
sales_propn_by_type = sales_by_type / sum(sales['weekly_sales'])

print(sales_propn_by_type)

#---------------------------------------------------
# Ejemplo 2

# Agrupando por typo y obteniendo la sumatoria de ventas semanales por tipo
sales_by_type = sales.groupby("type")["weekly_sales"].sum()

# Agrupando por tipo y is_holiday, 
# obteniendo la sumatoria ventas semanales por tipo y is_holiday
sales_by_type_is_holiday = sales.groupby(['type', 'is_holiday'])['weekly_sales'].sum()

print(sales_by_type_is_holiday)