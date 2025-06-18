# Segmentar en ambas direcciones 
# 
# Ya has visto segmentar los DataFrames por filas y por columnas, 
# pero como los DataFrames son objetos bidimensionales, 
# a menudo es natural segmentar ambas dimensiones a la vez. 
# 
# Es decir, pasando dos argumentos a .loc[], puedes subconjuntar por filas 
# y columnas de una sola vez.

import pandas as pd
import os


# Obtener ruta base del archivo
base_path = os.path.dirname(os.path.abspath(__file__))
ruta_archivo = os.path.join(base_path, "..", "..", "Archivos", "temperatures.csv")

# Importa el excel sales.csv
temperatures = pd.read_csv(ruta_archivo)

# --------------------------------------------------

# Estableciendo el indice multinivel en Country y city
temperatures_ind = temperatures.set_index(['country', 'city'])

#-----------------------------------

# Ordenar el index (IMPORTANTE)
temperatures_srt = temperatures_ind.sort_index()

#-----------------------------------
#Ejemplo1: Filtrando solo por indice padre e hijo

# Obteniendo los datos de Argentina hasta Costa Rica

print( temperatures_srt.loc[('Argentina','Buenos Aires'): ('Costa Rica', 'San Jose')] )


print('\n\n')
#-------------------------------------
# Ejemplo 2: Seleccionando las columnas

#Seleccionando las columnas desde date hasta avg_temp_c
print( temperatures_srt.loc[:, 'date':'avg_temp_c'] )

print('\n\n')
#-------------------------------------
# Ejemplo 3: Convinando Ejemplo 1 y Ejemplo 2

# Filtrando desde Argentina hasta Costa Rica (Indice padre e hijo)
#  y seleccionando las columnas desde date hasta avg_temp_c 
print( temperatures_srt.loc[
                            ('Argentina','Buenos Aires'): ('Costa Rica', 'San Jose'), 
                            'date':'avg_temp_c'
                            ] 
     )
