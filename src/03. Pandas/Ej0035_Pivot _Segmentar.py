# Subconjunto de tablas dinámicas
# Una tabla dinámica no es más que un DataFrame con índices ordenados, 
# por lo que las técnicas que ya has aprendido pueden utilizarse para subdividirlos.
#  En particular, la combinación .loc[] + segmentar suele ser útil.
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


#--------------------------------------------------------

# Segmentar de Argentina a Costa Rica por indice padre
print( temp_by_country_city_vs_year.loc['Argentina' : 'Costa Rica'] )

print('\n\n')

# Segmentar de Argentina a Guatemala por indice padre e hijo
print( temp_by_country_city_vs_year.loc[ ('Argentina', 'Buenos Aires') : ('Guatemala', 'Ciudad de Guatemala')] )


print('\n\n')

# Segmentar de Argentina a Guatemala por indice padre e hijo y columnas 
print( temp_by_country_city_vs_year.loc[ ('Argentina', 'Buenos Aires') : ('Guatemala', 'Ciudad de Guatemala'),   # Segmentando por fila
                                          2009:2011                                                              # Segmentando por columna       
                                       ] 
     )

