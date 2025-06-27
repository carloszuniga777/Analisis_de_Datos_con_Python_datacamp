# Distribucion Uniforme Continua
# 
# Simulación de tiempos de espera
# 
# Para dar a Amir una mejor idea de cuánto tiempo tendrá que esperar, 
# simularás que Amir espera 1000 veces y crearás un histograma para mostrarle 
# lo que debe esperar. 
# 
# Recuerda del último ejercicio que su tiempo mínimo de espera es de 0 minutos 
# y su tiempo máximo de espera es de 30 minutos.
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import uniform


# Establece la semilla aleatoria en 334.
np.random.seed(334)

# Genera 1000 tiempos de espera a partir de la distribución uniforme continua 
# que modela el tiempo de espera de Amir. 

min_value = 0
max_value = 30
quantity = 1000

wait_times = uniform.rvs(min_value, max_value, size=quantity)

print(wait_times)


# Promedio

print(f'Promedio de tiempo de espera es de: { wait_times.mean() }')

# Crea un histograma de los tiempos de espera simulados y muestra el gráfico.

plt.hist(wait_times)
plt.title("Tiempos de espera de Amir")
plt.ylabel('Frecuencia')
plt.xlabel('Tiempo en minutos')
plt.show()

# A menos que Amir descubra exactamente a qué hora se realiza cada copia de seguridad, 
# no podrá cronometrar su entrada de datos para que se respalde antes,
# pero parece que esperará unos 15 minutos en promedio.