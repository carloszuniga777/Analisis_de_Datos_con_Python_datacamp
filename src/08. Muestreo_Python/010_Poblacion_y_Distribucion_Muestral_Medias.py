# Población y distribución muestral medias
# 
# Una de las características útiles de las distribuciones muestrales es que puedes cuantificarlas. 
# Concretamente, puedes calcular estadísticas resumidas sobre ellos. 
# Aquí verás la relación entre la media de la distribución muestral y la media del parámetro poblacional.
#
# Se proporcionan tres distribuciones de muestreo. Para cada uno de ellos, se muestreó el conjunto de datos de bajas 
# de empleados mediante un muestreo aleatorio simple y, a continuación, se calculó la media de bajas. 
# 
# Esto se hizo 1000 veces para obtener una distribución muestral de las deserciones medias. 
# Una distribución del muestreo utilizó un tamaño de muestra de 5 para cada réplica, otra utilizó 50 y otra 500.

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os

# Obtener ruta base del archivo
base_path = os.path.dirname(os.path.abspath(__file__))
ruta_archivo = os.path.join(base_path, "..", "..", "Archivos", "attrition_pop.csv")


# Importa el excel
attrition_pop = pd.read_csv( ruta_archivo,  dtype={'RelationshipSatisfaction': 'category'})  


#-----------------------------------------------
# Parte 1: # Media de la poblacion
#-----------------------------------------------

media_poblacion = attrition_pop['Attrition'].mean()

#-----------------------------------------------
#Parte 2:  Tomando muestras de la poblacion
#-----------------------------------------------
# Tomando 5 muestras

# Crea una lista vacia
sampling_distribution_5 = []

# Itera 1000 veces y asigna la medias muestrales a la lista en cada iteracion
for i in range(1000):
	sampling_distribution_5.append(
    	attrition_pop.sample(n=5)['Attrition'].mean()
	)
  
#-----------------------------------------------
# Tomando 50 muestras de la poblacion

# Crea una lista vacia
sampling_distribution_50 = []

# Itera 1000 veces y asigna la medias muestrales a la lista en cada iteracion
for i in range(1000):
	sampling_distribution_50.append(
    	attrition_pop.sample(n=50)['Attrition'].mean()
	)

#-------------------------------------------------
# Tomando 500 muestras de la poblacion

# Crea una lista vacia
sampling_distribution_500 = []

# Itera 1000 veces y asigna la medias muestrales a la lista en cada iteracion
for i in range(1000):
	sampling_distribution_500.append(
    	attrition_pop.sample(n=500)['Attrition'].mean()
	)

#-----------------------------------------------
#Parte 3: Calcular la media de las deserciones medias 
# 		  para cada distribución de muestreo
#-----------------------------------------------

mean_of_means_5 = np.mean(sampling_distribution_5)
mean_of_means_50 = np.mean(sampling_distribution_50)
mean_of_means_500 = np.mean(sampling_distribution_500)



# Print the results
print(f'La media de las 5 muestras es: {mean_of_means_5}')
print(f'La media de las 50 muestras es: {mean_of_means_50}')
print(f'La media de las 500 muestras es: {mean_of_means_500}')
print(f'La media de la poblacion es: {media_poblacion}')


# Conclusion
# - ¿Cómo afecta el tamaño de la muestra a la media de las medias muestrales?
#   Independientemente del tamaño de la muestra, la media de la distribución muestral es una aproximación 
# 	a la media de la población.
# 
# - Incluso para tamaños de muestra pequeños, la media de la distribución de muestreo es una buena aproximación 
# de la media de la población.

#----------------------------------------------------------------
# Parte 4: Errores estándar y el teorema del límite central
#----------------------------------------------------------------
# Variación de la población y de la distribución muestral
# 
# Acabas de calcular la media de la distribución muestral y has visto cómo es una estimación del parámetro poblacional correspondiente. 
# Del mismo modo, como resultado del teorema del límite central, la desviación típica de la distribución muestral 
# tiene una relación interesante con la desviación típica del parámetro poblacional y el tamaño de la muestra.

# Desviacion tipica poblacional
desviacion_tipica_poblacion = attrition_pop['Attrition'].std()

# Desviacion tipica muestral
sd_of_means_5 = np.std(sampling_distribution_5, ddof=1)
sd_of_means_50 = np.std(sampling_distribution_50, ddof=1)
sd_of_means_500 = np.std(sampling_distribution_500, ddof=1)


# Print the results
print('\n\n')
print(f'La desviacion tipica de la poblacion es: {desviacion_tipica_poblacion}')
print(f'La desviacion tipica de las 5 muestras es: {sd_of_means_5}')
print(f'La desviacion tipica de las 50 muestras es: {sd_of_means_50}')
print(f'La desviacion tipica de las 500 muestras es: {sd_of_means_500}')
	  
# Conclusion:
# - ¿Cómo se relacionan las desviaciones típicas de las distribuciones muestrales con la desviación típica de la población 
#   y el tamaño de la muestra?	
# 	
# 		La desviación típica de la distribución muestral es aproximadamente igual a la desviación típica de la población
#   	dividida por la raíz cuadrada del tamaño de la muestra.
#
# -  La cantidad de variación en la distribución de muestreo está relacionada con la cantidad de variación en la población 
# 	 y el tamaño de la muestra. Esta es otra consecuencia del Teorema del Límite Central.

