# Dinamizar sobre una variable:

# Las tablas dinámicas son la forma estándar de agregar datos en las hojas de cálculo.

# En pandas, las tablas dinámicas son esencialmente otra forma de realizar cálculos
# agrupados. Es decir, el método .pivot_table() es una alternativa a .groupby().

# En este ejercicio, realizarás cálculos utilizando .pivot_table()
# para reproducir los cálculos que realizaste en la lección anterior utilizando
# .groupby().


import pandas as pd
import os


# Obtener ruta base del archivo
base_path = os.path.dirname(os.path.abspath(__file__))
ruta_archivo = os.path.join(base_path, "..", "..", "Archivos", "sales.csv")

# Importa el excel sales.csv
sales = pd.read_csv(ruta_archivo)

# --------------------------------------------------
# Ejemplo 1

# Obteniendo la media de weekly_sales por tipo
#
# Values = Columna valor numerico a calcular
# Index = Columna de tipo
# Por defecto, si no se especifica pivot_table calcula la media (mean)

mean_sales_by_type = sales.pivot_table(values="weekly_sales", index="type")

print(f"Pivot - Calculando la media:\n\n {mean_sales_by_type}")



print("\n\n")

print( f'Equivalente con Group by: { sales.groupby("type")["weekly_sales"].agg(["mean"]) }')

print("\n\n")
# -----------------------------------
# Ejmplo 2


# Obteniendo la media y mediana de weekly_sales por tipo
#
# Values = Columna valor numerico a calcular
# Index = Columna de tipo
# aggfunc = Se especifica que se quiere calcular la media y mediana

mean_med_sales_by_type = sales.pivot_table(values='weekly_sales', index='type', aggfunc=['mean', 'median'])

# Print mean_med_sales_by_type
print(mean_med_sales_by_type)


print("\n\n")
#-----------------------------------------------------------
# Ejemplo 3

# Obteniendo la media de weekly_sales por tipo y is_holiday
#
# Values = Columna valor numerico a calcular
# Index = Columna vertical de tipo
# columns = Columna horizontal de tipo
# fill_value = Llena lo valores None como 0
mean_sales_by_type_holiday = sales.pivot_table(values='weekly_sales', index='type', columns='is_holiday', fill_value = 0)

# Print mean_sales_by_type_holiday
print(mean_sales_by_type_holiday) 