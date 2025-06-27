# Precio de los aguacates convencionales frente a los ecológicos
#
# Crear varios gráficos para distintos subconjuntos de datos te permite comparar grupos. 
# En este ejercicio, crearás varios histogramas para comparar los precios de los aguacates convencionales y ecológicos.
import pandas as pd
import matplotlib.pyplot as plt
import os


# Obtener ruta base del archivo
base_path = os.path.dirname(os.path.abspath(__file__))
ruta_archivo = os.path.join(base_path, "..", "..", "Archivos", "avocados.csv")

# Importa el excel sales.csv
avocados = pd.read_csv(ruta_archivo)

# ------------------------------------------------
# Histograma de precios de aguacates convencionales
avocados[avocados['type']=='conventional']['avg_price'].hist(alpha=0.8, bins=20)     # Alpha: opacidad | Bins: Cantidad de barras

# Histograma de precios de aguacates organico
avocados[avocados['type']=='organic']['avg_price'].hist(alpha=0.8, bins=20)

# Leyenda
#El orden debe coincidir con el orden de graficos
plt.legend(['conventional', 'organic']) 

#Labels
plt.title('Histograma de precios de aguacates convencionales vs organico')
plt.ylabel("Cantidad")
plt.xlabel("Precio")


plt.show()


