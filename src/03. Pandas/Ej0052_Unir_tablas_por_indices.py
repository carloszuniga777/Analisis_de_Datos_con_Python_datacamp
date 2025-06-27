# Ejercicios de unir dos tablas por sus indices
import pandas as pd
import matplotlib.pyplot as plt
import os


# Obtener ruta base del archivo
base_path = os.path.dirname(os.path.abspath(__file__))
ruta_archivo_movies = os.path.join(base_path, "..", "..", "Archivos", "movies.csv")
ruta_archivo_ratings = os.path.join(base_path, "..", "..", "Archivos", "ratings.csv")

# Importa el excel sales.csv y se establece como indice la columna 'id'
movies = pd.read_csv(ruta_archivo_movies, index_col=['id'])
ratings = pd.read_csv(ruta_archivo_ratings, index_col=['id'])

# ------------------------------------------------
# Uniendo la tabla movies y ratings por indices por medio de left join
movies_ratings = movies.merge(ratings, on='id', how='left')

print(movies_ratings.head())