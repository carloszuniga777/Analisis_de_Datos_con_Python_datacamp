# Eliminar valores atípicos
# Aunque eliminar los valores atípicos no siempre es el camino a seguir, 
# para tu análisis has decidido que solo incluirás los vuelos en los que el "Price" no sea un valor atípico.
#
# Por lo tanto, tienes que encontrar el umbral superior y utilizarlo para eliminar los valores que lo superen del DataFrame planes.

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import os

# Obtener ruta base del archivo
base_path = os.path.dirname(os.path.abspath(__file__))
ruta_archivo = os.path.join(base_path, "..", "..", "Archivos", "planes3.csv")

# Read in the CSV as a DataFrame
planes = pd.read_csv(ruta_archivo)

#---------------------------------------------------------------

print(f'Antes:\n  { planes["Price"].describe() }')

plt.figure(1)
sns.histplot(data=planes, x="Price").figure.suptitle("Antes", y=0.95)

#----------------------------------------------------------------
# 1. Encontrar los percentiles 75 y 25

# Find the 75th and 25th percentiles
price_percentil_75 = planes["Price"].quantile(0.75)
price_percentil_25 = planes["Price"].quantile(0.25)

#-------------------------------------------------------------
# 2. Calculando el IQR

# Calculate iqr
prices_iqr = price_percentil_75 - price_percentil_25

#--------------------------------------------------------------
# 3. Calcula los umbrales superior e inferior de valores atípicos.

upper = price_percentil_75 + (1.5 * prices_iqr)
lower = price_percentil_25 - (1.5 * prices_iqr)


#----------------------------------------------------------------
# 4. Elimina los valores atípicos de planes.

planes = planes[(planes["Price"] > lower) & (planes["Price"] < upper)]

print(f'\ndespues:\n  { planes["Price"].describe() }')


plt.figure(2)
sns.histplot(data=planes, x="Price").figure.suptitle("Despues", y=0.95)
plt.show()


# Conclusion:
# 
# Lograste crear umbrales basados en el IQR y los usaste para filtrar el conjunto 
# de datos planes para eliminar precios extremos. Originalmente, el conjunto de datos
# tenía un precio máximo de casi 55000, pero la salida de planes.describe() muestra que el máximo 
# se ha reducido a alrededor de 23000, ¡reflejando una distribución menos sesgada para el análisis!