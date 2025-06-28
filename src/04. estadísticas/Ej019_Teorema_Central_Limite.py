# El CLT en acción
# 
# El teorema central del límite afirma que la distribución muestral de un estadístico muestral se aproxima 
# a la distribución normal a medida que tomas más muestras, independientemente de la distribución original 
# de la que se tome la muestra.

# En este ejercicio, te centrarás en la media muestral y verás el teorema central del límite en acción mientras 
# examinas más de cerca la columna num_users de amir_deals, que contiene el número de personas que tienen intención 
# de utilizar el producto que Amir está vendiendo.


import pandas as pd
import numpy as np
from scipy.stats import norm
import matplotlib.pyplot as plt
import os


# Obtener ruta base del archivo
base_path = os.path.dirname(os.path.abspath(__file__))
ruta_archivo = os.path.join(base_path, "..", "..", "Archivos", "amir_deals.csv")


# Cargando los archivos CSV
amir_deals = pd.read_csv(ruta_archivo)

#-------------------------------------------------------------------
# Parte 1: Crea un histograma de la columna num_users de amir_deals y muestra el gráfico.


# Crea un histograma de num_users y visualizar
amir_deals['num_users'].hist(bins=10)

plt.figure(1)                       # Crea una nueva figura
plt.xlabel('Numero de usuarios')
plt.ylabel('Cantidad')
plt.title('Histograma de numeros de usuarios con intencion\n de comprar los productos de Amir')
plt.grid(axis='y', linestyle='--', alpha=0.7)


#------------------------------------------------------------
# Parte 2: Tomando una muestra de tamano de 20 num_users con reemplazo (true) y calcula su media

# Set seed to 104
np.random.seed(104)


# Para realizar las muestras con sample:
# 
# .sample(20, replace=True):
#      - 20: Toma una muestra aleatoria de 20 elementos de la columna.
#      -  replace=True: Indica que el muestreo es con reemplazo, 
#                       lo que significa que un mismo valor puede aparecer 
#                       múltiples veces en la muestra.
#
# Ejemplo visual:
#  Si amir_deals['num_users'] tiene valores como: [10, 15, 20, 25, 30] (5 registros originales)...
#  
#   Una muestra de 20 elementos con reemplazo podría ser: [10, 15, 10, 20, 25, 30, 15, 10, 20, 15, ...] 
#  (20 valores, permitiendo repeticiones).


# Tomando 20 muestras de num_users
samp_20 = amir_deals['num_users'].sample(20, replace=True)

# Calcular la media
print(f'La media de 20 muestras es { np.mean(samp_20) }')

#----------------------------------------------------------------------------------
# Parte 3:  Repítelo 100 veces utilizando un bucle for y guárdalo como sample_means. 
# Esto tomará 100 muestras diferentes y calculará la media de cada una.



sample_means = []

# Loop 100 times
for i in range(100):
  
  samp_20 = amir_deals['num_users'].sample(20, replace=True)    # Toma 20 muestras de num_users
  samp_20_mean = np.mean(samp_20)                               # Calculando la media de samp_20
  sample_means.append(float(samp_20_mean))                      # Almacena la media en el arreglo sample_means
  
print(sample_means)

#-----------------------------------------------------------------
# Parte 4:
# Convirtiendo sample_means a Series y luego dibujar un histograma

sample_means_series = pd.Series(sample_means)

plt.figure(2)    # Segunda figura

sample_means_series.hist(bins=15)

plt.xlabel('Promedio de usuarios')  
plt.ylabel('Frecuencia')
plt.title('Histograma TLC de promedio de usuarios en 100 muestras')
plt.grid(axis='y', linestyle='--', alpha=0.7)

plt.show()

# cabas de ver el teorema del límite central en acción. Aunque la distribución de num_users no es normal, 
# la distribución de sus medias muestrales se asemeja a la distribución normal.