# Conceptos básicos de concatenación
# Se te han proporcionado unas tablas de datos con información de pistas musicales 
# de distintos álbumes de la banda estadounidense de heavy metal​ Metallica. 
# 
# La información de los programas procede de sus álbumes Ride The Lightning, 
# Master Of Puppets y St. Prueba varias funciones del método concatenando 
# las tablas verticalmente de distintas formas..concat()
#
# Equivalente a SQL UNION

import pandas as pd
import matplotlib.pyplot as plt
import os


# Obtener ruta base del archivo
base_path = os.path.dirname(os.path.abspath(__file__))
ruta_archivo_tracks_master = os.path.join(base_path, "..", "..", "Archivos", "tracks_master.csv")
ruta_archivo_tracks_ride= os.path.join(base_path, "..", "..", "Archivos", "tracks_ride.csv")
ruta_archivo_tracks_st = os.path.join(base_path, "..", "..", "Archivos", "tracks_st.csv")

# Cargando los archivos CSV
tracks_master = pd.read_csv(ruta_archivo_tracks_master)
tracks_ride = pd.read_csv(ruta_archivo_tracks_ride)
tracks_st       = pd.read_csv(ruta_archivo_tracks_st)
# ------------------------------------------------

# Ejemplo 1 de UNION
# En este ejemplo, concatenamos las tablas por columnas coincidentes y no coincidentes,
# Si una columna no coincide con alguna de las otra tabla se rellenara con NaN

# En este caso, la tabla trackjs_master tiene una columna adicional llamada 'composer
# Para el resto de tablas esa columna se rellenara con NaN
tracks_from_albums = pd.concat([tracks_master,tracks_ride, tracks_st], sort=True)
print(tracks_from_albums)

print("\n\n")
#--------------------------------------------------
#Ejemplo 2 de UNION


# En este ejemplo, ignoramos los indices de las tablas originales 
# y establecemos uno propio para la tabla resultante, por medio de ignore_index=True 
tracks_from_albums = pd.concat([tracks_master, tracks_ride, tracks_st], 
                               ignore_index=True,
                               sort=True
                             )
print(tracks_from_albums)

print("\n\n")
#--------------------------------------------------
#Ejemplo 3 de UNION

# En este ejemplo, concatenamos las tablas y mostramos solo las columnas que coinciden en 
# todas las tablas, es decir, las columnas que tienen el mismo nombre en todas las tablas
# por medio de join="inner"
# En este caso, la colummna 'composer' de la tabla tracks_master no se mostrara 
tracks_from_albums = pd.concat([tracks_master,tracks_ride, tracks_st],
                               sort=True, 
                               join="inner"
                               )
print(tracks_from_albums)
