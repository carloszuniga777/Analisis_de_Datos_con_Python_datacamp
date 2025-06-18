# Rellenar los valores que faltan y sumar valores con tablas dinámicas:
# 
# El método .pivot_table() tiene varios argumentos útiles, 
# como fill_value y margins.

#  - fill_value: sustituye los valores que faltan por un valor 
# real (lo que se conoce como imputación). Con qué sustituir los valores ausentes
# pero lo más sencillo es sustituirlos por un valor ficticio.
# 
# - margins: es un atajo para cuando dinamizas por dos variables, 
# pero también quieres dinamizar por cada una de esas variables por separado: 
# da los totales de fila y columna del contenido de la tabla dinámica.
# En este ejercicio, practicarás el uso de estos argumentos para mejorar 
# tus habilidades con las tablas dinámicas, ¡lo que te ayudará a hacer números 
# de forma más eficiente!


import pandas as pd
import os


# Obtener ruta base del archivo
base_path = os.path.dirname(os.path.abspath(__file__))
ruta_archivo = os.path.join(base_path, "..", "..", "Archivos", "sales.csv")

# Importa el excel sales.csv
sales = pd.read_csv(ruta_archivo)

# --------------------------------------------------
# Ejemplo 1

# Obteniendo la media de weekly_sales por tipo y is_holiday
#
# Values = Columna valor numerico a calcular
# Index = Columna vertical de tipo
# columns = Columna horizontal de tipo
# fill_value = Llena lo valores None como 0
# margins = crea una columna nueva y una fila nueva nueva, sacando la media total
# margins_name = Nombre de la columna magins
result = sales.pivot_table(values="weekly_sales", 
                           index="department", 
                           columns="type", 
                           fill_value=0, 
                           margins=True,
                           margins_name = 'Media Total'
                          )

print(result)