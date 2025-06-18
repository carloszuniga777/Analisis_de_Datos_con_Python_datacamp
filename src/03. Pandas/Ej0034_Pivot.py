# Temperatura dinámica por ciudad y año
# 
# Es interesante ver cómo cambian las temperaturas de cada ciudad a lo largo del tiempo: 
# si se mira cada mes, se obtiene una gran tabla, que puede ser difícil de interpretar. 
# En su lugar, veamos cómo cambian las temperaturas por año.

# Puedes acceder a los componentes de una fecha (año, mes y día) 
# utilizando código de la forma dataframe["column"].dt.component. 
# Por ejemplo, 
# el componente del mes es dataframe["column"].dt.month, 
# y el componente del año es dataframe["column"].dt.year.

# Una vez que tengas la columna del año, puedes crear una tabla dinámica 
# con los datos agregados por ciudad y año, que explorarás en los próximos ejercicios.

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

print(temp_by_country_city_vs_year)