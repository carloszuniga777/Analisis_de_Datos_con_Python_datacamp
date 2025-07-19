# Identificar valores atípicos
# Has demostrado que reconoces qué hacer cuando se te presentan valores atípicos, 
# pero ¿puedes identificarlos utilizando visualizaciones?
#
# Intenta averiguar si hay valores atípicos en las columnas "Price" o "Duration" del DataFrame planes.

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

#----------------------------------------------------------------
# 1. Trazando la distribucion de los precios 
plt.figure(1)
sns.histplot(data=planes, x='Price')


# Valores atípicos identificados:
#
# 1. Cola larga hacia la derecha: La distribución muestra una cola extendida que se extiende 
#    hasta aproximadamente 50,000 en el eje de precio, mientras que la mayoría de los datos 
#    se concentran entre 0-20,000.
#
# 2. Observaciones aisladas: Hay barras muy pequeñas y separadas en el rango de 25,000-50,000 
#    que representan observaciones poco frecuentes y alejadas del grupo principal.
#
# 3. Distribución sesgada: La forma general sugiere una distribución con sesgo positivo extremo, 
#    donde los valores atípicos "estiran" la cola hacia valores más altos.


#----------------------------------------------------------------
# 2. Muestra las estadísticas descriptivas de la duración del vuelo.

print( planes['Duration'].describe() )


# Valores atípicos identificados:
# 
# count    10446.000000
# mean        10.723798
# std          8.472321
# min          0.083000
# 25%          2.833000
# 50%          8.667000
# 75%         15.500000
# max         47.667000
#
#   - Valor mínimo (0.083): Este valor está extremadamente alejado del primer cuartil (2.833) (Q1: 25%). 
#     La diferencia es de aproximadamente 2.75 unidades, lo que representa una distancia considerable 
#     considerando que el rango intercuartílico (IQR) es de 12.667 (IQR: 75%: 15.500000 - 25%: 2.833000).
#  
#  - Valor máximo (47.667): Este es claramente un valor atípico severo. Está muy por encima del tercer cuartil (15.5) (Q3: 75%), 
#    con una diferencia de 32.167 unidades, que es más de 2.5 veces el rango intercuartílico.

plt.figure(2)
sns.histplot(data=planes, x='Duration')


# Valores atípicos identificados:
# 1. Valores extremos en la cola derecha: Hay observaciones dispersas que se extienden hasta aproximadamente duración = 40, 
#    mientras que la mayoría de los datos se concentran entre 0-30.
#
# 2. Observaciones aisladas: Las barras más allá de duración 30 tienen 
#    frecuencias muy bajas (prácticamente 0) y están claramente separadas del grupo principal de datos.

#--------------------------------------------------------------
plt.show()


# Conclusion:
# Los histogramas, diagramas de caja y estadísticas descriptivas también son métodos 
# útiles para identificar valores extremos. ¡Ahora vamos a tratarlos!
