# ¿Son generalizables estos resultados?
#
# Veamos otra muestra para ver si es representativa de la población. 
# Esta vez, examinarás la columna duration_minutes del conjunto de datos de Spotify, 
# que contiene la duración de la canción en minutos.


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os

# Obtener ruta base del archivo
base_path = os.path.dirname(os.path.abspath(__file__))
ruta_archivo1 = os.path.join(base_path, "..", "..", "Archivos", "spotify_population.csv")
ruta_archivo2 = os.path.join(base_path, "..", "..", "Archivos", "spotify_mysterious_sample2.csv")

# Define los tipos deseados para las columnas
dtype_dict = {
    'acousticness': 'float64',
    'danceability': 'float64',
    'duration_ms': 'float64',
    'duration_minutes': 'float64',
    'energy': 'float64',
    'explicit': 'float64',
    'instrumentalness': 'float64',
    'key': 'float64',
    'liveness': 'float64',
    'loudness': 'float64',
    'mode': 'float64',
    'popularity': 'float64',
     'speechiness': 'float64',
}

# Importa el excel
spotify_population = pd.read_csv( ruta_archivo1, dtype=dtype_dict)  
spotify_mysterious_sample = pd.read_csv( ruta_archivo2)  

print(spotify_mysterious_sample.shape)

#-------------------------------------------------
# Ejemplo 1. Traza un histograma del acousticness de spotify_population 
# con contenedores con anchura 0.01 de 0 a 1 utilizando pandas .hist().


plt.figure(1)

# Visualize the distribution of acousticness with a histogram

# Definiendo los contenedores: 
# Anchura: 0.5 de de 0 a 15
bins = np.arange(0, 15.5, 0.5)

spotify_population['duration_minutes'].hist(bins=bins)

plt.title('Poblacion Total de Duration_minutes')

#--------------------------------------------------------------------
# Ejemplo 2. Actualiza el código del histograma para utilizar el conjunto de datos spotify_mysterious_sample.

plt.figure(2)

spotify_mysterious_sample['duration_minutes'].hist(bins=bins)

plt.title('Muestra Sin Sesgo')

#--------------------------------------------------------------
plt.show()

#----------------------------------------------------------------

# Compara los dos histogramas que has dibujado. 
# 
# ¿Los valores de duración de la muestra son generalizables a la población general?
# Sí. Es probable que la muestra seleccionada sea una muestra aleatoria de todas las canciones de la población.

# Conclusion:
# Los valores de duración en la muestra muestran una distribución similar a los de toda la población, 
# por lo que los resultados son generalizables.