# ¿Qué tamaño de aguacate es el más popular?
#
# Los aguacates son cada vez más populares y están deliciosos 
# ya sea en forma de guacamole o sobre una tostada. 
# Hass Avocado Board hace un seguimiento de la oferta 
# y la demanda de aguacate en todo EE. UU., incluidas las ventas 
# de tres tamaños diferentes de aguacate. 
# 
# En este ejercicio, utilizarás un diagrama de barras para averiguar 
# qué tamaño es el más popular.
#
# Los gráficos de barras son estupendos para revelar las relaciones
# entre variables categóricas (tamaño) y numéricas (número vendido), 
# pero a menudo tendrás que manipular primero los datos para obtener 
# los números que necesitas para el gráfico.
import pandas as pd
import matplotlib.pyplot as plt
import os


# Obtener ruta base del archivo
base_path = os.path.dirname(os.path.abspath(__file__))
ruta_archivo = os.path.join(base_path, "..", "..", "Archivos", "avocados.csv")

# Importa el excel sales.csv
avocados = pd.read_csv(ruta_archivo)

# ------------------------------------------------

# Calculando el total de aguacates vendidos por cada tamano 
nb_sold_by_size = avocados.groupby('size')['nb_sold'].sum()

# Dibujando diagrama de barras de numeros de aguacates vendidos por tamano
nb_sold_by_size.plot(
                     kind='bar',                                    # Grafico de barras
                     title='Aguacate vendidos por tamano', 
                     ylabel='Ventas',
                     xlabel='Tipo'
                     )

plt.show()