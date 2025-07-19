# Estrategias para los datos que faltan
# La regla del cinco por ciento ha funcionado muy bien en tu conjunto de datos planes, 
# ¡eliminando los valores perdidos de nueve de las 11 columnas!

# Ahora tienes que decidir qué hacer con las columnas "Additional_Info" y "Price", 
# a las que les faltan los valores 300 y 368 respectivamente.

# Primero echarás un vistazo a lo que contiene "Additional_Info", 
# y después visualizarás el precio de los billetes de avión de distintas compañías aéreas.

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os

# Obtener ruta base del archivo
base_path = os.path.dirname(os.path.abspath(__file__))
ruta_archivo = os.path.join(base_path, "..", "..", "Archivos", "planes.csv")

# Read in the CSV as a DataFrame
planes = pd.read_csv(ruta_archivo)

#----------------------------------------------------------------
# 1. Limpieza de valores faltantes, (Ejercicio anterior)

# Definicion del umbral
threshold = len(planes) * 0.05

# Creacion del filtro
cols_to_drop = planes.columns[planes.isna().sum() <= threshold]

# Elimina filas que contiene valores perdidos en las columnas que contienen un umbral de <=5% de valores faltantes
planes.dropna(subset=cols_to_drop, inplace=True)

print(f'\n(Antes) Valores faltantes:\n {planes.isna().sum()}')

#-----------------------------------------------------------------------
# 2. Imprimiendo valores y frecuencia en Additional_Info

# Check the values of the Additional_Info column
print(f'\n\nConteo de valores "Additional_Info":\n  { planes['Additional_Info'].value_counts() }')

# Se observa que la informacion no es nada relevante, por tanto, se elimina la columna:
del planes['Additional_Info']

#-----------------------------------------------------
# 3. Creacion de grafico de caja entre 'Price' y 'Airline'

sns.boxplot(data=planes, x='Airline', y='Price')

plt.xticks(rotation=45)  # Rota 45 grados las etiquetas del eje x


plt.tight_layout()                       # Ajuste automático para evitar cortes



#--------------------------------------------------------
# 4. ¿Cómo debes tratar los valores que faltan en "Additional_Info" y "Price"? 

# Respuesta correcta:
# Elimina la columna "Additional_Info" e imputa la mediana por "Airline" para los valores que falten de "Price".

# ¿Por qué la media no es adecuada? 
#
# Las imputar la media por "Airline" para los valores faltantes, no es correcto, 
# porque las distribuciones "Price" por "Airline" vistas en el grafico de caja
# tienen valores extremos (Los circulos por encima y debajo de las cajas, 
# son precios que estan muy alejados del rango tipico de cada aerolinea ), 
# por lo que la media no es la mejor estadistica para imputar
# 
# Problema con la media:
# - La media es sensible a valores extremos
# - Si una aerolínea tiene algunos vuelos muy caros (outliers), la media se "sesga" hacia arriba
# - No representa el precio "típico" que paga la mayoría de pasajeros
#
# Ejemplo práctico:
# 
# Imagina que Jet Airways tiene estos precios:
#  - 90% de vuelos: entre $10,000 - $15,000
#  - 10% de vuelos: $50,000+ (outliers)
#
# Media: ~$18,500 (inflada por los outliers)
# Mediana: ~$12,500 (valor central, no afectada por outliers)
# 
# ¿Qué estadística usar para imputación?
# ✅ Mediana (recomendada):
#  - No se ve afectada por valores extremos
#  - Representa mejor el valor "típico"
#  - Más robusta para imputación
#
# ❌ Media (no recomendada):
# - Distorsionada por outliers
# - Podría imputar valores irrealmente altos/bajos
# - No representa la tendencia central real

#--------------------------------------------------------------------------------
# 5. Imputar/Rellenar los precios de los aviones que faltan
# 
# ¡Ahora solo queda una columna con valores perdidos!
# Has eliminado la columna "Additional_Info" de planes, 
# el último paso es imputar los datos que faltan en la columna "Price" del conjunto de datos.
#
# Como recordatorio, tú generaste este diagrama de caja, que sugería que imputar 
# el precio mediano basándose en el "Airline" ¡es un enfoque sólido!


# 5.1 Agrupa planes por aerolínea y calcula el precio mediano.
airline_prices = planes.groupby("Airline")["Price"].agg('median')

print(f'\nMediana de precios por Aerolineas:\n {airline_prices}')


# 5.2 Convertir los precios medianos agrupados a diccionario
prices_dict = airline_prices.to_dict()


# 5.3 Imputa condicionalmente los valores perdidos de "Price" asignando los valores 
#     de la columna "Airline" en función de prices_dict.

# Asignando el diccionario a los valores faltantes de precio por Aerolinea
planes["Price"] = planes["Price"].fillna( planes["Airline"].map(prices_dict) )

# Valores faltantes despues
print(f'\n(Despues) Valores faltantes:\n {planes.isna().sum()}')


# En resumen, los valores faltantes de la columna precio se relleno con la mediana precios 
# de vuelos por aerolinea

#-------------------------------------------
plt.show()