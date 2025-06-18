# Valores del índice de segmentación
# 
# Segmentar te permite seleccionar elementos consecutivos de un objeto utilizando 
# la sintaxis first:last. Los DataFrames se pueden segmentar por valores índice 
# o por número de fila/columna; empezaremos por el primer caso. 
# Esto implica cortar dentro del método .loc[].

# En comparación con las listas de segmentación, 
# hay algunas cosas que debes recordar.

#  - Solo puedes segmentar un índice si está ordenado (mediante .sort_index()).
#  - Para segmentar en el nivel exterior, first y last pueden ser cadenas.
#  - Para segmentar en niveles internos, first y last deben ser tuplas.
#  - Si pasas un único corte a .loc[], segmentará las filas.

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
#Ejemplo1: Filtrando solo por indice padre

# Obteniendo los datos de Argentina hasta Costa Rica
result1 = temperatures_srt.loc['Argentina':'Costa Rica']

print(result1)

print('\n\n')
#-------------------------------------
# Ejemplo 2: Filtrando por indice padre e hijo

#Obteniendo los datos desde brazil hasta honduras
print( temperatures_srt.loc[("Brazil", "Belo Horizonte"):("Honduras", "Tegucigalpa")] )