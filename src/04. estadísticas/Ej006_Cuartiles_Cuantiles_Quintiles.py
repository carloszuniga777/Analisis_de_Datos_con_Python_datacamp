# Cuartiles, cuantiles y quintiles
# 
# Los cuantiles son una forma estupenda de resumir datos numéricos, 
# ya que pueden utilizarse para medir la tendencia central y la dispersión, 
# así como para hacerse una idea de dónde se sitúa un punto de datos en relación con el resto del conjunto de datos. 
# 
# Por ejemplo, puedes querer ofrecer un descuento al 10 % de los usuarios más activos de un sitio web.

# En este ejercicio, calcularás cuartiles, quintiles y deciles, 
# que dividen un conjunto de datos en 4, 5 y 10 partes, respectivamente.

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os

# Obtener ruta base del archivo
base_path = os.path.dirname(os.path.abspath(__file__))
ruta_archivo = os.path.join(base_path, "..", "..", "Archivos", "food_consumption.csv")

# Importa el excel sales.csv
food_consumption = pd.read_csv( ruta_archivo)  

#-------------------------------------------

# Ejemplo 1: Calcular cuartiles 

print('----------------Ejemplo 1: Calcular cuartiles ----------------')

# Con numpy:

print(f'Con Numpy:\n\n {  np.quantile(food_consumption[['co2_emission']], [0, 0.25, 0.50, 0.75, 1])   }')

print(f'\nCon Pandas:\n\n { food_consumption[['co2_emission']].quantile([0, 0.25, 0.50, 0.75, 1]) }')

print(f'\nCon Pandas Describe:\n\n { food_consumption[['co2_emission']].describe() }')


# Vamos a interpretar esta salida paso a paso. Es un resumen estadístico de las emisiones de CO2 usando cuartiles, 
# que dividen los datos ordenados en partes iguales. Aquí está el análisis:

#        co2_emission
# 0.00         0.000  → Mínimo (0% de los datos)
# 0.25         5.210  → Primer cuartil (Q1)
# 0.50        16.530  → Mediana (Q2)
# 0.75        62.598  → Tercer cuartil (Q3)
# 1.00      1712.000  → Máximo (100% de los datos)

# Interpretación detallada:

# Mínimo (0.00):
#   - Al menos un registro tiene 0 toneladas de emisiones de CO₂.
#   - Ejemplo: Quizás un país que solo consume alimentos con huella de carbono neutra.
# 
# Primer cuartil (Q1 - 0.25):
#   - El 25% inferior de los datos tiene emisiones ≤ 5.210 toneladas.
#   - Traducción: 1 de cada 4 países/registros emite menos de 5.21 toneladas.

# Mediana (Q2 - 0.50):
#   - El valor central cuando los datos están ordenados es 16.53 toneladas.
#   Significado:
#               - 50% de los países emiten ≤ 16.53 toneladas (mitad baja).
#               - 50% de los países emiten ≥ 16.53 toneladas (mitad alta).
# 
# Tercer cuartil (Q3 - 0.75):
#  - El 75% de los datos tiene emisiones ≤ 62.598 toneladas.
#  - Traducción: Solo el 25% de los países supera las 62.6 toneladas.
#
# Máximo (1.00):
#  - El valor más alto es 1,712 toneladas.
#  - Implicación: Hay países con emisiones extremadamente altas (posibles outliers).


#--------------------------------------------

# Ejemplo 2: Calcular 6 cuantiles (Dividir los datos en 5 partes iguales (1 / 5 = 0.2))

print('\n----------------Ejemplo 2: Calcular 6 cuartiles ----------------')

print(f'\n Cuantiles de 6:\n\n { food_consumption[['co2_emission']].quantile([0, 0.2, 0.4, 0.6, 0.8, 1 ])  }')


#---------------------------------------------
# Ejemplo 3: Calcular 11 cuantiles (Dividir los datos en 10 partes iguales (1 / 10 = 0.1))

print('\n----------------Ejemplo 2: Calcular 11 cuartiles ----------------')

print(f'\n Cuantiles de 11:\n\n { food_consumption[['co2_emission']].quantile([0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1]) }')


# Aunque calcular más cuantiles te da una visión más detallada de los datos, 
# también produce más números, haciendo que el resumen sea más difícil de entender rápidamente.

