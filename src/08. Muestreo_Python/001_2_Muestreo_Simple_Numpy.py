# Muestreo y cálculo sencillos con NumPy
# También puedes utilizar numpy para calcular parámetros o estadísticas a partir de una lista o de la serie pandas.
#
# Sube el volumen al once y mira la propiedad loudness de cada canción.

import pandas as pd
import numpy as np
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

# 1. Crear una Series de la columna loudness de spotify_population
loudness_pop = spotify_population['loudness']

# 2. Tomar muestra de 100 valores de loudness_pop
loudness_samp = loudness_pop.sample(n=100)

#3. Calcular la media de loudness_pop vs loudness_samp

# Calcular la media de loudness_pop
mean_loudness_pop = np.mean(loudness_pop)

# Calcular la media de loudness_samp
mean_loudness_samp = np.mean(loudness_samp)

print(f'La media de loudness es: {mean_loudness_pop}')
print(f'La media de la muestra de loudness es: {mean_loudness_samp}')

# Debido que hice modificaciones en el excel los valores no son acuerdos pero deberia de dar:
# -7.366856851353947
# -7.50746

# Conclusion:
# Nuevamente, observe que el valor calculado (la media) es cercano pero no idéntico en cada caso.