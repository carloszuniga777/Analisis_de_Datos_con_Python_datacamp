
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import os

# Obtener ruta base del archivo
base_path = os.path.dirname(os.path.abspath(__file__))
ruta_archivo = os.path.join(base_path, "..", "..", "Archivos", "planes2.csv")

# Read in the CSV as a DataFrame
planes = pd.read_csv(ruta_archivo)

#----------------------------------------------------------------
# 1. Encontrar el número de valores únicos
#    Te gustaría practicar algunas de las habilidades de manipulación y análisis de datos categóricos que acabas de ver.
#    Para ayudarte a identificar qué datos podrían reformatearse para extraer valor, 
#    vas a averiguar qué columnas no numéricas del conjunto de datos planes tienen un gran número de valores únicos.

# Filtro del Dataframe para buscar las columnas de tipo objeto 
non_numeric = planes.select_dtypes("object")

# Itera en cada columna para imprimir los valores unicos de cada columna
for i in non_numeric.columns:
  # Print the number of unique values
  print(f"Numero de valores unicos en la columna {i}: ", non_numeric[i].nunique())

#-------------------------------------------
# 2. Categorías de duración de los vuelos
# Como has visto, hay 362 valores únicos en la columna "Duration" de planes. 
# Llamando a planes["Duration"].head(), vemos los siguientes valores:

# 0        19h
# 1     5h 25m
# 2     4h 45m
# 3     2h 25m
# 4    15h 30m
# Name: Duration, dtype: object

# Parece que no será sencillo convertirlo en números. Sin embargo, ¡podrías clasificar los vuelos por duración 
# y examinar la frecuencia de las distintas longitudes de vuelo!
#
# Crearás una columna "Duration_Category" en el DataFrame planes. 
# Antes tendrás que crear una lista de los valores que deseas insertar en el DataFrame, 
# seguida de los valores existentes a partir de los cuales deben crearse.



# 2.1 Creando una lista de categorias, que nos permita clasificar los datos de la columna "Duration"
flight_categories = ["Corto-Vuelo", "Medio-Vuelo", "Largo-Vuelo"]


# 2.2 Creando variables que nos permita filtrar por categoria.

# Creando una cadena Corto-Vuelo para capturar los valores "0h", "1h", "2h", "3h", o "4h"
short_flights = "^0h|^1h|^2h|^3h|^4h"

# Creando una cadena Medio-Vuelo para capturar los valores de "5h" y "9h"
medium_flights = "^5h|^6h|^7h|^8h|^9h"

# Creando una cadena Largo-Vuelo para capturar los valores de "10h" hasta "16h"
long_flights = "^10h|^11h|^12h|^13h|^14h|^15h|^16h"

#-------------------------------------------
# 3. Añadir categorías de duración
# Ahora que has configurado las categorías y los valores que quieres capturar,
# ¡es hora de construir una nueva columna para analizar la frecuencia de los vuelos según su duración!

# 3.1 Crear las condiciones para la creacion de valores en flight_categories
conditions = [
    (planes["Duration"].str.contains(short_flights)),
    (planes["Duration"].str.contains(medium_flights)),
    (planes["Duration"].str.contains(long_flights))
]


# # Apply the conditions list to the flight_categories
# Crea una nueva columna llamada 'Duration_Category' y categoriza los vuelos segun su duracion en:
# "Corto-Vuelo", "Medio-Vuelo", "Largo-Vuelo" y los valores no encontrados los clasifica en "Extreme duration" 
planes["Duration_Category"] = np.select(conditions, 
                                        flight_categories,
                                        default="Extreme duration"
                                        )


# Plot the counts of each category
g = sns.countplot(data=planes, x="Duration_Category")

g.figure.suptitle('Duracion de vuelos por categoria', fontsize=10, y=0.95)

g.set(ylabel='Cantidad', xlabel='Categoria de duracion')


#-------------------------------------------
plt.show()