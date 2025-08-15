# Cálculo de intervalos de confianza
# 
# Has conocido dos métodos para calcular los intervalos de confianza: el método de los cuantiles 
# y el método del error típico. El método del error típico consiste en utilizar la función de distribución 
# acumulativa inversa (inversa CDF) de la distribución normal para calcular los intervalos de confianza. 
# 
# En este ejercicio, realizarás estos dos métodos con los datos de Spotify.

import pandas as pd
import numpy as np
from scipy.stats import norm
import os

# Obtener ruta base del archivo
base_path = os.path.dirname(os.path.abspath(__file__))
ruta_archivo = os.path.join(base_path, "..", "..", "Archivos", "spotify_population.csv")


# Importa el excel
spotify_population = pd.read_csv( ruta_archivo)  

#----------------------------------------------
# Parte 1: Obteniendo las Muestras 
#---------------------------------------------
# Muestra Simple:

spotify_sample = spotify_population.sample(n=5000, replace=False)


#--------------------------------
# Distribucion Bootstrap

# 1️⃣ Tomar una muestra inicial de la población, con remplazo es decir los registros no se repiten
spotify_sample_bootstrap = spotify_population.sample(n=5000, replace=False)

# 2️⃣ Construir la distribución bootstrap
bootstrap_distribution = []

for i in range(2000):
    bootstrap_distribution.append(
    	spotify_sample_bootstrap.sample(n=5000, replace=True)['popularity'].mean()
    )

#----------------------------------
# Parte 2: Calcular el intervalo de confianza 
#--------------------------------
# Ejemplo 1: 
# Genera un intervalo de confianza del 95 % utilizando el método de cuantiles en la distribución bootstrap, 
# estableciendo el cuantil 0.025 como lower_quant y el cuantil 0.975 como upper_quant.

# Generate a 95% confidence interval using the quantile method
lower_quant = np.quantile(bootstrap_distribution, 0.025)
upper_quant = np.quantile(bootstrap_distribution, 0.975)

# Print quantile method confidence interval
print([x.item() for x in [lower_quant, upper_quant]])

#----------------------------------
# Ejemplo 2:
# Genera un intervalo de confianza del 95 % utilizando el método del error estándar a partir de la distribución bootstrap.
#
# Calcula point_estimate como la media de bootstrap_distribution, y standard_error como la desviación típica de bootstrap_distribution.
# Calcula lower_se como el cuantil 0.025 de una inv. CDF de una distribución normal con media point_estimate y desviación típica standard_error.
# Calcula upper_se como el cuantil 0.975 de ese mismo inv. CDF.


# Find the mean and std dev of the bootstrap distribution
point_estimate = np.mean(bootstrap_distribution)
standard_error = np.std(bootstrap_distribution, ddof=1)

# Find the lower limit of the confidence interval
lower_se = norm.ppf(0.025, loc=point_estimate, scale=standard_error)
# Find the upper limit of the confidence interval
upper_se = norm.ppf(0.975, loc=point_estimate, scale=standard_error)

# Print standard error method confidence interval
print([x.item() for x in [lower_se, upper_se]])

#------------------------------------------------------------------
# Pregunta:
# ¿Qué información proporciona ese intervalo de confianza?
# Un intervalo de valores plausibles para una cantidad desconocida.

# Conclusion:
#  - Los intervalos de confianza tienen en cuenta la incertidumbre en nuestra estimación de un parámetro poblacional, 
#    proporcionando un rango de valores posibles. Estamos seguros de que el valor verdadero se encuentra 
#    en algún lugar del intervalo especificado por ese rango.
#
#  - El método de error estándar para calcular el intervalo de confianza asume que la distribución bootstrap es normal. 
#    Esta suposición debería mantenerse si el tamaño de la muestra y el número de réplicas son suficientemente grandes.