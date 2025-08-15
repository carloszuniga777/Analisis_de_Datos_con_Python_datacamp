# Compara las medias muestrales y bootstrap
# Para facilitar el cálculo, se han incluido distribuciones similares a las calculadas en el ejercicio anterior, 
# esta vez utilizando un tamaño de muestra de 5000.

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
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

#-------------------------------------------
# Distribucion Muestral:

sampling_distribution = []

for i in range(2000):
    sampling_distribution.append(
    	spotify_population.sample(n=5000, replace=False)['popularity'].mean()
    )

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
# Parte 2: Calcular la media 
#--------------------------------
# Calcula la media popularity de 4 formas:
# 
# Población: a partir de spotify_population, toma la media de popularity.
# Muestra: de spotify_sample, toma la media de popularity.
# Distribución muestral: de sampling_distribution, toma su media.
# Distribución Bootstrap: a partir de bootstrap_distribution, toma su media.


# Calculate the population mean popularity
pop_mean = spotify_population['popularity'].mean()

# Calculate the original sample mean popularity
samp_mean = spotify_sample['popularity'].mean()

# Calculate the sampling dist'n estimate of mean popularity
samp_distn_mean = np.mean(sampling_distribution)

# Calculate the bootstrap dist'n estimate of mean popularity
boot_distn_mean = np.mean(bootstrap_distribution)


# Print the means
print([x.item() for x in [pop_mean, samp_mean, samp_distn_mean, boot_distn_mean]])


#----------------------------------------
# Pregunta: 
# 
# Basándote en las cuatro medias que acabas de calcular  (pop_mean, samp_mean, samp_distn_mean y boot_distn_mean),
# ¿qué afirmación es cierta?
# 
# La media de la distribución muestral es la mejor estimación de la verdadera media poblacional; 
# la media de la distribución bootstrap es la más cercana a la media muestral original

# Conclusion:
# La media de la distribución de muestreo se puede usar para estimar la media de la población, 
# pero ese no es el caso con la distribución bootstrap.

#---------------------------------------------
# Parte 3: Comparar desviaciones típicas de muestreo y bootstrap
#--------------------------------------------
# Del mismo modo que has visto cómo se pueden utilizar la distribución muestral y 
# la distribución bootstrap para estimar la media de la población, ahora verás cómo se pueden 
# utilizar para estimar la variación, o más concretamente, la desviación típica, de la población.
# 
# Recuerda que el tamaño de la muestra es 5000.

# Ejercicio:
# Calcula la desviación típica de popularity de 4 formas.

# Población: a partir de spotify_population, toma la desviación típica de popularity.
# 
# Muestra original: a partir de spotify_sample, toma la desviación típica de popularity.
# 
# Distribución muestral: a partir de sampling_distribution, toma su desviación típica 
# y multiplícala por la raíz cuadrada del tamaño de la muestra (5000).
# 
# Distribución Bootstrap: a partir de bootstrap_distribution, toma su desviación típica 
# y multiplícala por la raíz cuadrada del tamaño de la muestra.


# Calculate the population std dev popularity
pop_sd = spotify_population['popularity'].std(ddof=0)

# Calculate the original sample std dev popularity
samp_sd = spotify_sample['popularity'].std(ddof=1)

# Calculate the sampling dist'n estimate of std dev popularity

standard_error = np.std(sampling_distribution, ddof=1)
samp_distn_sd = standard_error * np.sqrt(5000)

# Calculate the bootstrap dist'n estimate of std dev popularity
standard_error = np.std(bootstrap_distribution, ddof=1)
boot_distn_sd = standard_error * np.sqrt(5000)

# Print the standard deviations
print('\n\n')
print([x.item() for x in [pop_sd, samp_sd, samp_distn_sd, boot_distn_sd]])

#------------------------
# Pregunta:
# Según los cuatro resultados que acabas de calcular (pop_sd, samp_sd, samp_distn_sd, y boot_distn_sd), 
# ¿qué afirmación es cierta?
#
# El cálculo a partir de la distribución bootstrap es la mejor estimación de la desviación típica de la población.

# Conclusion:
# Esta es una propiedad importante de la distribución bootstrap. Cuando no tienes todos los valores de la población 
# o la capacidad de muestrear múltiples veces, puedes usar el bootstrapping para obtener una buena estimación de la 
# desviación estándar de la población.


# Resumen capitulo:
# Aprendiste sobre el concepto de bootstrapping y cómo se usa para estimar la variación en una población desconocida. 
# Específicamente, descubriste:
#
#   - El bootstrapping implica remuestreo: Usar un conjunto de datos para generar múltiples muestras 
#     y calcular estadísticas para cada una. Por ejemplo, generar una distribución bootstrap de puntuaciones medias 
#     sabor de café a partir de una muestra implica remuestrear y calcular la media para cada remuestreo.
#   
#   - Comparación de distribuciones bootstrap y de muestreo: Viste cómo una distribución bootstrap, 
#     creada a partir del remuestreo de un conjunto de datos, se compara con una distribución de muestreo que teóricamente se obtendría al tomar muchas muestras de la población. Esta comparación ayuda a entender la variabilidad y el sesgo en las estimaciones de parámetros poblacionales.
# 
#   - Estimación de parámetros poblacionales: La lección destacó que, aunque la media de una distribución bootstrap 
#     coincide estrechamente con la media de la muestra, puede no representar con precisión la media poblacional si la muestra está sesgada. Sin embargo, el bootstrapping es efectivo para estimar la desviación estándar de la población. Esto se hace calculando la desviación estándar de las medias bootstrap y ajustándola por la raíz cuadrada del tamaño de la muestra.
# 
# Aquí tienes un fragmento de código que ilustra cómo generar una distribución bootstrap y calcular su media y desviación estándar:
#
#       bootstrap_means = [np.mean(np.random.choice(sample, replace=True, size=len(sample))) for _ in range(1000)]
#       mean_of_bootstrap_means = np.mean(bootstrap_means)
#       std_dev_of_bootstrap_means = np.std(bootstrap_means, ddof=1)
# 
# - Errores estándar y desviación estándar poblacional: Aprendiste que la desviación estándar de las medias bootstrap, 
#   también conocida como error estándar, puede usarse para estimar la variabilidad de la estadística de la muestra. Multiplicar el error estándar por la raíz cuadrada del tamaño de la muestra da una buena estimación de la desviación estándar poblacional.
#   
# Esta lección te equipó con habilidades prácticas para usar el bootstrapping para entender conceptos estadísticos 
# y estimar parámetros poblacionales, enfatizando las limitaciones y fortalezas de este método.
#
# El objetivo de la próxima lección es aprender cómo estimar el rango de valores posibles para una cantidad desconocida 
# usando intervalos de confianza, que ayudan a tener en cuenta la incertidumbre en las previsiones.