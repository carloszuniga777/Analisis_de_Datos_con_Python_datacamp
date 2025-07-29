# Muestreo simple con pandas
# 
# A lo largo de este capítulo, explorarás los datos de canciones de Spotify. 
# Cada fila de este conjunto de datos de población representa una canción, y hay más de 40 000 filas. 
# Las columnas incluyen el nombre de la canción, los artistas que la interpretaron, el año de lanzamiento 
# y atributos de la canción como su duración, tempo y bailabilidad. 
# Empezarás por fijarte en las duraciones.
#
# Tu primera tarea es tomar una muestra del conjunto de datos de Spotify 
# y comparar la duración media de la población con la de la muestra.

import pandas as pd
import os

# Obtener ruta base del archivo
base_path = os.path.dirname(os.path.abspath(__file__))
ruta_archivo = os.path.join(base_path, "..", "..", "Archivos", "spotify_population.csv")


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
spotify_population = pd.read_csv( ruta_archivo, dtype=dtype_dict)  


#-------------------------------------------------
# 1. Toma una muestra de 1000 registros

# Sample 1000 rows from spotify_population
spotify_sample = spotify_population.sample(n=1000)

# Print the sample
print(spotify_sample)

#---------------------------------------------------
# 2. Calcular la media de la muestra vs spotify_population

# Calcula la media de duracion en minutos de spotify_population
mean_dur_pop = spotify_population['duration_minutes'].mean()

#  Calcula la media de duracion en minutos de spotify_population spotify_sample
mean_dur_samp = spotify_sample['duration_minutes'].mean()

# Print the means
print(f'La media de duracion en minutos de las canciones del dataset Spotify es: {mean_dur_pop}')
print(f'La media de duracion en minutos de las canciones de la muestra de Spotify es: {mean_dur_samp}')


# Conclusion
#  Observa que la duración media de las canciones en la muestra es similar, 
# pero no idéntica a la duración media de las canciones en toda la población.