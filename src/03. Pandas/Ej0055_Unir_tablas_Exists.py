# Realizar una antiunión
# En nuestro conjunto de datos de empresas de streaming de música, 
# a cada cliente se le asigna un empleado representante para que le asista. 
# 
# En este ejercicio, filtra la tabla de empleados por una tabla de clientes principales, 
# devolviendo sólo aquellos empleados que no estén asignados a ningún cliente. 
# 
# Los resultados deben parecerse a los de una antiunión. 
# La dirección de la empresa asignará a estos empleados formación adicional 
# para que puedan trabajar con clientes muy valorados.
#
# Equivalente a not exists en SQL

import pandas as pd
import matplotlib.pyplot as plt
import os


# Obtener ruta base del archivo
base_path = os.path.dirname(os.path.abspath(__file__))
ruta_archivo_non_mus_tcks = os.path.join(base_path, "..", "..", "Archivos", "non_mus_tcks.csv")
ruta_archivo_top_invoices= os.path.join(base_path, "..", "..", "Archivos", "top_invoices.csv")
ruta_archivo_genres = os.path.join(base_path, "..", "..", "Archivos", "genres.csv")

# Cargando los archivos CSV
non_mus_tcks = pd.read_csv(ruta_archivo_non_mus_tcks)
top_invoices = pd.read_csv(ruta_archivo_top_invoices)
genres       = pd.read_csv(ruta_archivo_genres)
# ------------------------------------------------
# Paso 1. Uniendo la tabla non_mus_tcks y top_invoices por inner join
tracks_invoices = non_mus_tcks.merge(top_invoices, on='tid')


# Paso 2. Buscandando en non_mus_tcks los registros coincidentes entre esa tabla 
# y tracks_invoices (resultado de la union anterior)
# Asegurando que solo se muestren los registros  non_mus_tcks y evitando la duplicidad 
# 
# Equivalente a SQL EXISTS (paso 1 y 2): Primero buscar coincidencias en el primer cruce
# y luego filtrar la tabla principal con el resultado del primer cruce
top_tracks = non_mus_tcks[non_mus_tcks['tid'].isin(tracks_invoices['tid'])]


# Group the top_tracks by gid and count the tid rows
cnt_by_gid = top_tracks.groupby(['gid'], as_index=False).agg({'tid':'count'})

# Merge the genres table to cnt_by_gid on gid and print
print(cnt_by_gid.merge(genres, on='gid'))
