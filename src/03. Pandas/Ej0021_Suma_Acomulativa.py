# Estadísticas acumulativas
# 
# Las estadísticas acumuladas o acumulativas también pueden ser útiles para hacer 
# un seguimiento de las estadísticas resumidas a lo largo del tiempo. 
# 
# En este ejercicio, calcularás la suma acumulada 
# y el máximo acumulado de las ventas semanales de un departamento, 
# lo que te permitirá identificar cuáles han sido las ventas totales hasta el momento, 
# así como cuáles han sido las ventas semanales más elevadas hasta el momento.

import pandas as pd
import os


# Obtener ruta base del archivo
base_path = os.path.dirname(os.path.abspath(__file__))
ruta_archivo = os.path.join(base_path, "..", "..", "Archivos", "sales.csv")

# Importa el excel sales.csv
sales = pd.read_csv( ruta_archivo)  

#--------------------------------------------------

# Ordenando la data por fecha ascendente
sales = sales.sort_values('date', ascending=True)

# Se crea una nueva columna cum_weekly_sales y se obtiene la suma acomulativa de weekly_sales
sales['cum_weekly_sales'] = sales['weekly_sales'].cumsum()

# Se crea nueva columna y calcula la suma acumulativa máxima a lo largo de un eje específico 'weekly_sales'
sales['cum_max_sales'] = sales['weekly_sales'].cummax()

print(sales[["date", "weekly_sales", "cum_weekly_sales", "cum_max_sales"]])