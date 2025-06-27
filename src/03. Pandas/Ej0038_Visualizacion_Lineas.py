# Cambios en las ventas a lo largo del tiempo
# 
# Los gráficos de líneas están diseñados para visualizar la relación entre dos variables 
# numéricas, donde cada valor de los datos está conectado con el siguiente. 
# 
# Son especialmente útiles para visualizar el cambio de un número a lo largo del tiempo,
#  ya que cada punto temporal está conectado de forma natural con el punto temporal siguiente. 
# 
# En este ejercicio, visualizarás el cambio en las ventas de aguacate a lo largo de tres años.

import pandas as pd
import matplotlib.pyplot as plt
import os


# Obtener ruta base del archivo
base_path = os.path.dirname(os.path.abspath(__file__))
ruta_archivo = os.path.join(base_path, "..", "..", "Archivos", "avocados.csv")

# Importa el excel sales.csv
avocados = pd.read_csv(ruta_archivo)

# ------------------------------------------------

# Calculando el total de aguacates vendidos en cada fecha
nb_sold_by_date = avocados.groupby(['date'])['nb_sold'].sum()


# Dibujando diagrama de barras de numeros de aguacates vendidos por tamano
nb_sold_by_date.plot(
                     kind='line',                                           # Grafico de lineas
                     title='Aguacate vendidos a lo largo del tiempo', 
                     ylabel='Total Vendido',
                     xlabel='Tiempo',
                     rot=45                                                 # Rotar el lableX 45 grados
                     )

plt.show()