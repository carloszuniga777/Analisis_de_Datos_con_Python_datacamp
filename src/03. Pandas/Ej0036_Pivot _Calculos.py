# Calcular en una tabla dinámica
# 
# Las tablas dinámicas están llenas de estadísticas resumidas, pero solo son un primer paso para encontrar algo revelador. 
# A menudo necesitarás realizar más cálculos sobre ellos. Algo habitual es encontrar las filas 
# o columnas donde se produce el valor más alto o más bajo.

# Recuerda del Capítulo 1 que puedes subconjuntar fácilmente una Serie o un DataFrame para encontrar filas de interés 
# utilizando una condición lógica entre corchetes. Por ejemplo: series[series > value].

import pandas as pd
import os


# Obtener ruta base del archivo
base_path = os.path.dirname(os.path.abspath(__file__))
ruta_archivo = os.path.join(base_path, "..", "..", "Archivos", "temperatures.csv")

# Importa el excel sales.csv
temperatures = pd.read_csv(ruta_archivo)

# ------------------------------------------------

# Convierte la fecha string a formato datetime de python
temperatures['date'] = pd.to_datetime( 
    temperatures['date'],
    format='%Y-%m-%d',  # Formato yyyy-mm-dd
    errors='coerce'     # Maneja valores invalidos como Nat        
)

print(temperatures['date'].dtype)  # Debería mostrar: datetime64[ns]

#Agregando columna de year
temperatures['year'] = temperatures['date'].dt.year



# Pivot
temp_by_country_city_vs_year = temperatures.pivot_table(
                                values='avg_temp_c',                # Valor
                                index=['country', 'city'],          # Filas
                                columns='year',                      # Columnas    
                                fill_value=0
                                )

print(f'pivot: \n\n {temp_by_country_city_vs_year}\n\n')
#--------------------------------------------------------
# Ejemplo 1:

# Calculando la media de cada ano
mean_temp_by_year = temp_by_country_city_vs_year.mean()

print(f'Media en cada ano:\n {mean_temp_by_year}\n\n')

# Obteniendo la media mas alta

maxDate =  mean_temp_by_year.max()

mediaAlta = mean_temp_by_year[ mean_temp_by_year == maxDate]

print(f'La media mas alta es:\n {mediaAlta}\n\n')

#--------------------------------------------------------
# Ejemplo 2: Calculando la temperatura media en cada ciudad (a traves de las columnas)

# Obteniendo la temperatura media en cada ciudad
mean_temp_by_city = temp_by_country_city_vs_year.mean(axis='columns')

print(f'Media en cada ciudad:\n {mean_temp_by_city}\n\n')



# Filtrando para obtener la temperatura media mas baja

minTemp = mean_temp_by_city.min()

mediaBaja = mean_temp_by_city[ mean_temp_by_city == minTemp]

print(f'Ciudad con temperatura media mas baja:\n {mediaBaja}\n\n')