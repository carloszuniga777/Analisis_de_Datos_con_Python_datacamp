# Distribución muestral vs. distribución bootstrap
# 
# La distribución muestral y la distribución bootstrap están estrechamente relacionadas. 
# En situaciones en las que puedes muestrear repetidamente de una población 
# (estas ocasiones son raras), es útil generar tanto la distribución de muestreo como la distribución bootstrap, 
# una tras otra, para ver cómo se relacionan.

# Aquí, la estadística que te interesa es la puntuación media popularity de las canciones.

# spotify_population (todo el conjunto de datos) y spotify_sample (500 filas muestreadas aleatoriamente 
# de spotify_population) están disponibles

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
# Ejercicio 1: Distribucion Muestral
# 
# Genera una distribución muestral de 2000 réplicas utilizando un bucle for.
# Toma una muestra de 500 filas de la población sin reemplazo y calcula la media popularity.

mean_popularity_2000_samp = []

# Generate a sampling distribution of 2000 replicates
for i in range(2000):
    mean_popularity_2000_samp.append(
    	# Sample 500 rows and calculate the mean popularity 
    	spotify_population.sample(n=500)['popularity'].mean()
    )

# Print the sampling distribution results
print(mean_popularity_2000_samp)

plt.figure(1)

plt.hist(x=mean_popularity_2000_samp, bins=30, edgecolor='black')

# Añadimos título y etiquetas para facilitar la interpretación
plt.title("Distribución Muestral")
plt.xlabel("Media popularity")
plt.ylabel("Frecuencia")

#-----------------------------------------------------------------
# Ejercicio 2: Distribucion Botstrap
# 
# Muestrea 500 filas de la muestra con reemplazo y calcula la media popularity para generar una distribución bootstrap de 2000 réplicas.


# Muestra sin replazo de la poblacion original
spotify_sample = spotify_population.sample(n=500, replace=False)


mean_popularity_2000_boot = []

# Generate a bootstrap distribution of 2000 replicates
for i in range(2000):
    mean_popularity_2000_boot.append(
    	# Resample 500 rows and calculate the mean popularity     
    	spotify_sample.sample(n=500, replace=True)['popularity'].mean()
    )

# Print the bootstrap distribution results
print('\n\n')
print(mean_popularity_2000_boot)


plt.figure(2)

# Dibujamos un histograma para visualizar la distribución de esas 1000 medias
plt.hist(x=mean_popularity_2000_boot, bins=30, edgecolor='black')

# Añadimos título y etiquetas para facilitar la interpretación
plt.title("Distribución Bootstrap")
plt.xlabel("Media de danceability")
plt.ylabel("Frecuencia")

#------------------------------------------------------
# Mostramos el gráfico en pantalla
plt.show()

# Conclusion:
#  La distribución de muestreo y la distribución bootstrap están estrechamente relacionadas, 
# y también lo está el código para generarlas.