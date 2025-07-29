# ¿Son generalizables las conclusiones de la muestra?
# 
# Acabas de ver cómo el muestreo de conveniencia (recoger datos utilizando el método más fácil) 
# puede dar lugar a muestras que no son representativas de la población. 
# 
# Equivalentemente, esto significa que las conclusiones de la muestra no son generalizables a la población. 
# Visualizar las distribuciones de la población y la muestra puede ayudar a determinar si la muestra 
# es o no representativa de la población.

# El conjunto de datos de Spotify contiene una columna acousticness, que es una medida de confianza de cero a uno 
# de si la canción se hizo con instrumentos que no están enchufados. 
# 
# Compararás la distribución acousticness de la población total de canciones con una muestra de esas canciones.



# Nota: Este tipo de muestre se puede dar cuando las muestras tienen un sesgo, por ejemplo:
#  - Elegir las primeros 100 regitros para una muestra, estos registros pueden tener un sesgo.
#
#  - Realizar una encuesta via telefono de un candidato, cuando solo 30% de la poblacion tiene telefono, es de clase rica 
#    y la mayoria esta a favor de un partido politico, este tipo de muestreo esta sesgado, porque no se toma en consideracion
#    a la poblacion con escasos recursos, que ademas estan a favor de diferentes partidos politicos  
#
# Los datos cuando estan sesgado pueden introducir errores al momento de analisar

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os

# Obtener ruta base del archivo
base_path = os.path.dirname(os.path.abspath(__file__))
ruta_archivo1 = os.path.join(base_path, "..", "..", "Archivos", "spotify_population.csv")
ruta_archivo2 = os.path.join(base_path, "..", "..", "Archivos", "spotify_mysterious_sample.csv")

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

#-------------------------------------------------
# Ejemplo 1. Traza un histograma del acousticness de spotify_population 
# con contenedores con anchura 0.01 de 0 a 1 utilizando pandas .hist().


plt.figure(1)

# Visualize the distribution of acousticness with a histogram

# Definiendo los contenedores: 
# Anchura: 0.01 de de 0 a 1
bins = np.arange(0, 1.01, 0.01)

spotify_population['acousticness'].hist(bins=bins)

plt.title('Poblacion Total de Acousticness')

#--------------------------------------------------------------------
# Ejemplo 2. Actualiza el código del histograma para utilizar el conjunto de datos spotify_mysterious_sample.

plt.figure(2)

spotify_mysterious_sample['acousticness'].hist(bins=bins)

plt.title('Muestra Sesgada')

#--------------------------------------------------------------
plt.show()

#----------------------------------------------------------------

# Compara los dos histogramas que has dibujado. 
#
# ¿Los valores acousticness de la muestra son generalizables a la población general?
# No. Las muestras de acousticness son sistemáticamente superiores a las de la población general.

# Conclusion:  
# Los valores de acousticness en la muestra son todos mayores que 0.95, 
# mientras que en la población completa varían de 0 a 1.