# La media de las medias
# 
# Quieres saber cuál es el número medio de usuarios (num_users) por acuerdo, 
# pero quieres conocer este número para toda la empresa, de modo que puedas ver 
# si los acuerdos de Amir tienen más o menos usuarios que el acuerdo medio de la empresa. 
# 
# El problema es que, en el último año, la empresa ha trabajado en más de 10 000 acuerdos, 
# por lo que no es realista recopilar todos los datos. En vez de eso, estimarás la media tomando varias muestras 
# aleatorias de acuerdos, ya que esto es mucho más fácil que recopilar datos de todas las personas de la empresa.

import pandas as pd
import numpy as np
from scipy.stats import norm
import matplotlib.pyplot as plt
import os


# Obtener ruta base del archivo
base_path = os.path.dirname(os.path.abspath(__file__))
ruta_archivo_amir_deals = os.path.join(base_path, "..", "..", "Archivos", "amir_deals.csv")
ruta_archivo_all_deals = os.path.join(base_path, "..", "..", "Archivos", "all_deals.csv")


# Cargando los archivos CSV
amir_deals = pd.read_csv(ruta_archivo_amir_deals)
all_deals = pd.read_csv(ruta_archivo_all_deals)

#-------------------------------------------------------------------

# Para este ejercicio se necesita comparar la media de Amir 
# con la media de la empresa, por la cantidad enorme de acuerdos de la empresa 
# se decide solo obtener muestras 30 muestras y obtener una media total para comparar con la media de Amir

# Set seed to 321
np.random.seed(321)

sample_means = []

# Iterar 30 veces para tomar 30 medias
for i in range(30):
  
  # Toma 20 muestras de todos los num_users de la tabla all_deals con remplazamiento
  cur_sample = all_deals['num_users'].sample(20, replace=True) 
 
  cur_mean = np.mean(cur_sample)  # Calcula la media de las 20 muestas

  sample_means.append(cur_mean)  # Las guarda la lista to sample_means



# Print mean of sample_means
print(f'La media de usuarios por acuerdo de la empresa es: { np.mean(sample_means) }')

# Print mean of num_users in amir_deals
print(f'La media de usuarios por acuerdo de Amir es: { amir_deals['num_users'].mean() }'  )
