
import pandas as pd
import matplotlib.pyplot as plt
import os


# Obtener ruta base del archivo
base_path = os.path.dirname(os.path.abspath(__file__))
ruta_archivo_movies = os.path.join(base_path, "..", "..", "Archivos", "movies.csv")
ruta_archivo_scifi_movies = os.path.join(base_path, "..", "..", "Archivos", "scifi_movies.csv")
ruta_archivo_action_movies = os.path.join(base_path, "..", "..", "Archivos", "action_movies.csv")

# Importa el excel sales.csv
movies = pd.read_csv(ruta_archivo_movies)
scifi_movies = pd.read_csv(ruta_archivo_scifi_movies)
action_movies = pd.read_csv(ruta_archivo_action_movies)

# ------------------------------------------------

# Uniendo las tablas action_movies y scifi_movies con un rigth join
action_scifi = action_movies.merge(scifi_movies, 
                                   on='movie_id', 
                                   how='right',
                                   suffixes=('_act','_sci')
                                   )


scifi_only = action_scifi[action_scifi['genre_act'].isnull()]

# Uniendo las tablas movies y scifi_only con un inner join, 
# debido a que las columnas tienen diferentes nombres en ambas tablas, 
# se especifica el nombre de la tabla izquierda como id y el nombre de la tabla derecha como movie_id   
movies_and_scifi_only = movies.merge(scifi_only, left_on='id', right_on='movie_id')

# Print the first few rows and shape of movies_and_scifi_only
print(movies_and_scifi_only.head())
print(movies_and_scifi_only.shape)