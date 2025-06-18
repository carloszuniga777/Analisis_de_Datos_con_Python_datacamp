# Establecer y eliminar índices
#
# pandas te permite designar columnas como índice. 
# Esto permite un código más limpio al tomar subconjuntos 
# (además de proporcionar una búsqueda más eficaz en algunas circunstancias).
#
# En este capítulo, explorarás temperatures, un DataFrame de temperaturas medias 
# en ciudades de todo el mundo.


import pandas as pd
import os


# Obtener ruta base del archivo
base_path = os.path.dirname(os.path.abspath(__file__))
ruta_archivo = os.path.join(base_path, "..", "..", "Archivos", "temperatures.csv")

# Importa el excel sales.csv
temperatures = pd.read_csv(ruta_archivo)

# --------------------------------------------------
# Ejemplo 1

# Estableciendo el indice de temperatures en city
temperatures_ind = temperatures.set_index('city')

print(temperatures_ind)

#-----------------------------------------------
# Ejemplo 2

# Restableciendo el indice
result1 = temperatures_ind.reset_index()

print(result1.head())


#-------------------------------------------------------
#Ejemplo 3

# Restablece el indice y elimina el contenido del indice (city)
result2 = temperatures_ind.reset_index(drop=True)

print(result2.head())