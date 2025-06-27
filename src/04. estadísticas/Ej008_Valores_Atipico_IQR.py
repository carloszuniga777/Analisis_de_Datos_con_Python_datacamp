# Metodo 2: Usando libreria scipy para calcular el IQR
# 
# Encontrar valores atípicos mediante IQR
# 
# Los valores atípicos pueden tener grandes efectos en estadísticas como la media, 
# así como en estadísticas que se basan en la media, como la varianza y la desviación típica. 
# 
# El rango intercuartílico, o IQR, es otra forma de medir la dispersión que está menos influida por los valores atípicos. 
# El IQR también se utiliza a menudo para encontrar valores atípicos. Si un valor es menor que Q1 - 1.5 x IQR 
# o mayor que Q3 + 1.5 x IQR, se considera un valor atípico. 
# 
# De hecho, así es como se calculan las longitudes de los bigotes en un diagrama de caja matplotlib.
#
#
#                                         Interquartile Range
#                                                (IQR)
#                                      <--------------------->         
#                  <---- 1.5*IQR ---->  _____________________  <---- 1.5*IQR ----> 
#                                      |         |           |
#                                      |         |           | 
#         Outliers |-------------------|         |           |--------------------|  Outliers  
#                                      |_________|___________|      
#                                      Q1       Median       Q3
#                             (25ht percentile)             (75ht percentile)
#    
# En este ejercicio, calcularás el IQR y lo utilizarás para encontrar algunos valores atípicos


# Los valores Atipicos son valores en un conjunto de datos que 
# se desvian significativamente del resto de datos 
# y el método IQR (Rango Intercuartílico) es una técnica robusta para identificarlos

import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import iqr             # pip install scipy
import os

# Obtener ruta base del archivo
base_path = os.path.dirname(os.path.abspath(__file__))
ruta_archivo = os.path.join(base_path, "..", "..", "Archivos", "food_consumption.csv")

# Importa el excel sales.csv
food_consumption = pd.read_csv( ruta_archivo)  

#-------------------------------------------
# Metodo 2:

# Calculamos el total co2_emission por pais
emissions_by_country = food_consumption.groupby('country')['co2_emission'].sum()


# Calculamos el primer y tercer Cuartil y el valor atipico IQR
iqr = iqr(emissions_by_country)
q1 = emissions_by_country.quantile(0.25)
q3 = emissions_by_country.quantile(0.75)

# Calcular los puntos de corte inferior y superior para valores atípicos
lower = q1 - 1.5 * iqr
upper = q3 + 1.5 * iqr

# Encontrando el valor atipico
outliers = emissions_by_country[ (emissions_by_country < lower) | (emissions_by_country > upper)] 
print(outliers)

#¡Detección de valores atípicos sobresaliente! 
# Parece que Argentina tiene una cantidad sustancialmente mayor de emisiones de CO2 
# por persona que otros países del mundo.

