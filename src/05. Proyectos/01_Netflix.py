# Importing pandas and matplotlib
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os


# Obtener ruta base del archivo
base_path = os.path.dirname(os.path.abspath(__file__))
ruta_archivo = os.path.join(base_path, "..", "..", "Archivos", "netflix_data.csv")

# Read in the Netflix CSV as a DataFrame
netflix_df = pd.read_csv(ruta_archivo, index_col=0)

# Start coding here! Use as many cells as you like|

#----------Creando columna de año de estreno-----------------------------------

#Creando la columna Year y extrayendo los ultimos 4 caracteres
netflix_df['Year'] = ( netflix_df['release_year'].astype(str).str[-4:])

#Convirtiendo los valores a numerico
netflix_df['Year'] = pd.to_numeric(netflix_df['Year'], errors= 'coerce')

#-----------Obteniendo peliculas que se estrenaron en los 90s------------------

#obtener la columna fecha de estreno
fecha = netflix_df['Year'] 

#Obteniendo todas las peliculas de los años 90s
peliculas90s = netflix_df[ 
    (fecha >= 1990) & 
    (fecha <= 1999)
]

#---------------Dibujando el histograma de duracion de peliculas-----------------
 
#Dibujando el histograma
plt.hist(peliculas90s['duration'], bins=10, color='skyblue', edgecolor='black')


# Validacion visual del grafico: Duración mas frecuente:
duration= 100
print(f'La duracion mas frecuente fue: {duration}')

#titulos
plt.title('Frecuencia de duracion de peliculas (Años 90s)')
plt.xlabel('Duracion (minutos)')
plt.ylabel('Frecuencia')
plt.grid(axis='y', alpha=0.75)

plt.show()

#-----------------------------------------------------------------------------

# Filtra las peliculas con duracion de menos de 90 min, y genera una serie de valores
# boleanos (true/false) y con sum cuenta cuantos true hay 
short_movie_count = (    
                        ( peliculas90s['duration'] < 90 ) &   
                        ( peliculas90s['type'] == 'Movie' ) &
                        ( peliculas90s['genre'] == 'Action' )
                    ).sum()

print(f'La cantidad de peliculas con duracion de menos de 90 min es: {short_movie_count}')
