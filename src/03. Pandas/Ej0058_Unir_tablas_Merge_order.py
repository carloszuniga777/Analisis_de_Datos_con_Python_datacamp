# Une las tablas como merge pero ordena los datos para poder 
# rellanar los valores NaN con el valor anterior: fill_method='ffill'  

import pandas as pd
import matplotlib.pyplot as plt
import os


# Obtener ruta base del archivo
base_path = os.path.dirname(os.path.abspath(__file__))
ruta_archivo_gdp = os.path.join(base_path, "..", "..", "Archivos", "gdp.csv")
ruta_archivo_sp500= os.path.join(base_path, "..", "..", "Archivos", "sp500.csv")

# Cargando los archivos CSV
gdp = pd.read_csv(ruta_archivo_gdp)
sp500 = pd.read_csv(ruta_archivo_sp500)

# ------------------------------------------------

# El merge_ordered funciona igual que el merge, a diferencia que en este caso
# devuelve datos ordenados al momento de fusionar (util para datos ordenados o series temporales) 
# 
# Esto permite rellenar los valores faltante (NaN) de las columnas con el valor anterior
#
# A diferencia del merge normal que se cruza por defecto con inner join, 
# el merge_ordered se cruza por defecto como outer join, por lo que se debe 
# especificar el tipo de unionque se desea realizar

gdp_sp500 = pd.merge_ordered( gdp,                                      #Tabla izquierda
                             sp500,                                     #Tabla derecha      
                             left_on='year', right_on='date',           #Cruzar por las columnas 
                             how='left',                                #Tipo de union (left, right, inner, outer)  
                             fill_method='ffill'                        #Rellenar los valores NaN con el valor anterior
                             )

# Subset the gdp and returns columns
gdp_returns = gdp_sp500.loc[:,['gdp', 'returns']]


# Print gdp_returns correlation
print (gdp_returns.corr())