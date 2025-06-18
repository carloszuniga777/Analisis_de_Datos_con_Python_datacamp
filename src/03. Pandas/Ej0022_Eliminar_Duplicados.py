# Eliminar duplicados
# Eliminar duplicados es una habilidad esencial para obtener recuentos precisos, 
# porque a menudo no quieres contar lo mismo varias veces. 
# En este ejercicio, crearás algunos DataFrames nuevos utilizando valores únicos de sales.

import pandas as pd
import os

# Obtener ruta base del archivo
base_path = os.path.dirname(os.path.abspath(__file__))
ruta_archivo = os.path.join(base_path, "..", "..", "Archivos", "sales.csv")

# Importa el excel sales.csv
sales = pd.read_csv( ruta_archivo)  

#--------------------------------------------------

# Elimnar los duplicados combinacion store/type 
store_types = sales.drop_duplicates(subset=['store', 'type'])
print(store_types.head())

# Elimnar los duplicados combinacion store/department 
store_depts = sales.drop_duplicates(subset=['store', 'department'])
print(store_depts.head())

# Elimnar las fechas duplicadas donde las filas de del subset is_holiday sean true
holiday_dates = sales[sales['is_holiday']].drop_duplicates(subset=['date'])

# Print date col of holiday_dates
print(holiday_dates['date'])