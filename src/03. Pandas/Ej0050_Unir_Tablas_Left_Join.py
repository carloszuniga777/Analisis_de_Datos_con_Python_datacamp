# Unir las tablas por LEFT JOIN

import pandas as pd
import matplotlib.pyplot as plt
import os


# Obtener ruta base del archivo
base_path = os.path.dirname(os.path.abspath(__file__))
ruta_archivo_movies = os.path.join(base_path, "..", "..", "Archivos", "movies.csv")
ruta_archivo_financials = os.path.join(base_path, "..", "..", "Archivos", "financials.csv")

# Importa el excel sales.csv
movies = pd.read_csv(ruta_archivo_movies)
financials = pd.read_csv(ruta_archivo_financials)

# ------------------------------------------------

# Merge the movies table with the financials table with a left join
movies_financials = movies.merge(financials, on='id', how='left')

# Count the number of rows in the budget column that are missing
number_of_missing_fin = movies_financials['budget'].isnull().sum()

# Print the number of movies missing financials
print(number_of_missing_fin)