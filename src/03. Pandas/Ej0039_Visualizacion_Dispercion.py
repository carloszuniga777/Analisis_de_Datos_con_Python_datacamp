# Oferta y demanda de aguacate
# 
# Los gráficos de dispersión son ideales para visualizar relaciones entre variables numéricas. 
# 
# En este ejercicio, compararás el número de aguacates vendidos con el precio medio y verás si están relacionados. 
# Si están relacionados, puedes utilizar un número para predecir el otro.

import pandas as pd
import matplotlib.pyplot as plt
import os


# Obtener ruta base del archivo
base_path = os.path.dirname(os.path.abspath(__file__))
ruta_archivo = os.path.join(base_path, "..", "..", "Archivos", "avocados.csv")

# Importa el excel sales.csv
avocados = pd.read_csv(ruta_archivo)

# ------------------------------------------------

# Dibujando diagrama de dispercion que relaciona el precio de los aguacates y las ventas 
avocados.plot(
               kind='scatter',                                       # Grafico de dispercion     
               x='nb_sold', 
               y='avg_price',                                          
               title='Number of avocados sold vs. average price',
               ylabel='Ventas',
               xlabel='Precio',
            )

plt.show()