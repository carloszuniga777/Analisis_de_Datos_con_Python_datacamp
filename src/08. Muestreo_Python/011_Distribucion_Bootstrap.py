# Generar una distribución bootstrap
# 
# El proceso para generar una distribución bootstrap es similar al proceso para generar 
# una distribución muestral; solo el primer paso es diferente.
#
# Para hacer una distribución muestral, se parte de la población y se muestrea sin reemplazo. 
# Para hacer una distribución bootstrap, empiezas con una muestra y la muestreas con reemplazo. 
# Después, los pasos son los mismos: calcula la estadística de resumen que te interese en esa muestra/remuestra y, 
# a continuación, repite el proceso muchas veces. En cada caso, puedes visualizar la distribución con un histograma.
#
# Aquí, spotify_sample es un subconjunto del conjunto de datos spotify_population. 
# Para que sea más fácil ver cómo funciona el remuestreo, se ha añadido una columna de índice de fila llamada 
# 'index', y solo se han incluido las columnas de nombre de artista, nombre de canción y danceability.

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os

# Obtener ruta base del archivo
base_path = os.path.dirname(os.path.abspath(__file__))
ruta_archivo = os.path.join(base_path, "..", "..", "Archivos", "spotify_population.csv")


# Importa el excel
spotify_population = pd.read_csv( ruta_archivo)  

#-----------------------------------------------

# Simplificando la data
spotify_sample = spotify_population[['artists', 'name', 'danceability']]
spotify_sample = spotify_sample.reset_index()

#----------------------------------------------
# 1. Crea una distribución bootstrap dibujando un histograma de mean_danceability_1000.

# 1️⃣ Tomar una muestra inicial de la población sin remplazo, es decir, las registros no se repiten
spotify_sample = spotify_sample.sample(n=500, replace=False)


# 2️⃣ Construir la distribución bootstrap

# Preparamos una lista vacía donde almacenaremos las 1000 medias bootstrap
mean_danceability_1000 = []

# Iteramos 1000 veces para generar 1000 réplicas bootstrap
for i in range(1000):
    # 1) spotify_sample.sample(frac=1, replace=True)
    #    - frac=1 indica que el tamaño de la muestra bootstrap es igual
    #      al tamaño original de spotify_sample.
    #    - replace=True activa el remuestreo con reemplazo.
    #    Esto crea una "nueva muestra" de la misma longitud donde
    #    algunos registros pueden repetirse y otros quedar fuera.
    
    # 2) ['danceability']
    #    Seleccionamos únicamente la columna numérica de interés.
    
    # 3) np.mean(...)
    #    Calculamos la media de danceability en esa réplica.
    
    # 4) .append(...)
    #    Añadimos el resultado a nuestra lista de medias.
    mean_danceability_1000.append(
        np.mean(
            spotify_sample
            .sample(frac=1, replace=True)['danceability']
        )
    )

# Al terminar el bucle, mean_danceability_1000 contiene 1000 valores,
# cada uno representando la media de danceability en una réplica bootstrap.

# Dibujamos un histograma para visualizar la distribución de esas 1000 medias
plt.hist(x=mean_danceability_1000, bins=30, edgecolor='black')

# Añadimos título y etiquetas para facilitar la interpretación
plt.title("Distribución Bootstrap de la Media de Danceability (1000 réplicas)")
plt.xlabel("Media de danceability")
plt.ylabel("Frecuencia")

# Mostramos el gráfico en pantalla
plt.show()

#------------------------------------------------------
# A partir de la muestra más pequeña de canciones de Spotify, podemos estimar la media de la estadística 
# de bailabilidad en la población. Dado que tenemos una distribución de estadísticas, incluso podemos cuantificar 
# cuán precisa es nuestra estimación.


# Resumen Capitulos:
# Has aprendido sobre el concepto de bootstrapping, un método estadístico usado para estimar 
# la distribución de una población basada en una muestra. Los puntos clave incluyen:
#
# - Re-muestreo: Descubriste que el re-muestreo implica muestrear con reemplazo de un conjunto de datos, 
#                permitiendo que el mismo ítem sea seleccionado varias veces. Esto contrasta con el muestreo 
#                sin reemplazo, donde cada ítem solo puede ser seleccionado una vez.
# 
# - Bootstrapping vs. Muestreo: Exploraste cómo el bootstrapping es esencialmente lo inverso del muestreo tradicional. 
#                               Mientras que el muestreo extrae un subconjunto menor de una población para análisis, 
#                               el bootstrapping usa una muestra para simular una población mayor.
# 
# - Distribución Bootstrap: Aprendiste que una distribución bootstrap se crea re-muestreando repetidamente un conjunto de datos, 
#                           calculando una estadística (como la media) para cada re-muestra, y luego analizando la distribución 
#                           de esas estadísticas. Este proceso ayuda a estimar la variabilidad de la estadística 
#                           en diferentes muestras de la población.
# 
# - Aplicación Práctica: A través de ejercicios, practicaste la generación de una distribución bootstrap usando Python. 
#                        Por ejemplo, para re-muestrear un conjunto de datos y calcular la media de una columna, usaste:
# 
#       import numpy as np
#       
#       # Suponiendo que 'data' sea un DataFrame y 'column_name' sea la columna de interés
#       bootstrap_means = []
#       
#       for _ in range(1000):  # Número de muestras bootstrap
#           resample = data.sample(frac=1, replace=True)
#           mean = resample['column_name'].mean()
#           bootstrap_means.append(mean)
#
#  - Visualización: Finalmente, aprendiste a visualizar la distribución bootstrap, 
#   típicamente usando un histograma, para entender la variabilidad de la estadística y su potencial distribución en la población.
# 
#  Esta lección te ha equipado con el conocimiento y habilidades fundamentales para aplicar 
#  el bootstrapping en varios escenarios de análisis de datos, mejorando tu capacidad de hacer inferencias 
#  sobre poblaciones a partir de muestras.
#
#  El objetivo de la próxima lección es enseñar cómo usar el bootstrapping para estimar la variabilidad 
#  y el sesgo en las estimaciones de parámetros poblacionales, enfatizando sus fortalezas y limitaciones.