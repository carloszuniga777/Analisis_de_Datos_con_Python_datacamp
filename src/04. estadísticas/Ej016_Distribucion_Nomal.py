# Distribución normal:
# 
# La distribución normal (o "campana de Gauss") describe fenómenos naturales 
# y sociales donde la mayoría de resultados se concentran cerca de un valor central, 
# disminuyendo simétricamente hacia los extremos. Por ejemplo: estaturas de personas, 
# donde la mayoría mide cerca del promedio (ej. 1.70m) y pocos son muy bajos o altos. 
# 
# Se caracteriza por dos parámetros: la media (centro de la curva) 
# y la desviación estándar (grado de dispersión). 
# 
# El 68% de los datos está dentro de ±1 desviación estándar de la media, 
# el 95% dentro de ±2, y el 99.7% dentro de ±3, lo que permite predecir probabilidades de eventos.



# Ejercicio: Probabilidades de la distribución normal
# 
# Como cada acuerdo en el que trabajó Amir (tanto los conseguidos como los perdidos) era diferente, 
# cada uno valía una cantidad de dinero distinta. 
# 
# Estos valores se almacenan en la columna amount de amir_deals y siguen una distribución normal 
# con una media de 5000 dólares y una desviación típica de 2000 dólares. 
# 
# Como parte de sus parámetros de rendimiento, quieres calcular la probabilidad de que Amir cierre 
# un acuerdo por valor de diferentes cantidades.

import pandas as pd
from scipy.stats import norm
import matplotlib.pyplot as plt
import os


# Obtener ruta base del archivo
base_path = os.path.dirname(os.path.abspath(__file__))
ruta_archivo = os.path.join(base_path, "..", "..", "Archivos", "amir_deals.csv")


# Cargando los archivos CSV
amir_deals = pd.read_csv(ruta_archivo)

#-------------------------------------------------------------------
# Graficando en un histograma Amount y observar que es una distribucion normal

amir_deals['amount'].hist(bins=10)

plt.title('Histograma de Distribucion normal')
plt.ylabel('Frecuencia')
plt.xlabel('Amount')


#---------------------------------------------------------------------
# Ejemplo 1: ¿Cuál es la probabilidad de que Amir cierre un acuerdo por un valor inferior a 7500 $?

# La función norm.cdf calcula la probabilidad acumulada en una distribución normal. 
# Responde a preguntas como: "¿Qué probabilidad hay de que un valor sea menor o igual a X?"
# 
# Sintaxis:
# norm.cdf(x, loc=media, scale=desviacion_estandar)
# Donde:
#   - x: Valor límite que estás evaluando
#   - loc: Media (centro de la distribución)
#   - scale: Desviación estándar (dispersión de los datos)

evaluar = 7000
media = 5000
desviacion_standar = 2000

# Probabilidad de Acuerdos < 7500
prob_less_7500 = norm.cdf(evaluar, media, desviacion_standar)
print(f'La probabilidad que Ami cierre un acuerdo inferior de 7,500 dolares es: { prob_less_7500:.1%}')



#-----------------------
# Ejemplo 2: ¿Cuál es la probabilidad de que Amir cierre un acuerdo por un valor de más de 1000 $?

evaluar = 1000
media = 5000
desviacion_standar = 2000

# Probabilidad de acuerdos > 1000 
prob_over_1000 = 1 - norm.cdf(evaluar, media, desviacion_standar)   # El 1 representa el 100% de probabilidad total

print(f'La probabilidad que Ami cierre un acuerdo por un valor de mas de 1,000 dolares es: { prob_over_1000:.1%}')

#----------------------------------------
# Ejemplo 3: Probabilidad que Amir cierre un acuerdo por un valor de USD 3000 y 7000

evaluar1 = 7000   # mayor primero en la formula
evaluar2 = 3000   # menor segundo en la formula
media = 5000
desviacion_standar = 2000

# Probabilidad de acuerdos entre 3000 and 7000
prob_3000_to_7000 = norm.cdf(evaluar1, media, desviacion_standar)  - norm.cdf(evaluar2, media, desviacion_standar) 


print(f'La probabilidad que Ami cierre un acuerdo entre USD 3000 y 7000 dolares es: { prob_3000_to_7000:.1%}')


#----------------------------------------
# Ejemplo 4: ¿A qué cantidad será inferior el 25 % de las ventas de Amir?

# La función norm.ppf (Percent Point Function) es la inversa de la distribución acumulada (cdf). 
# Mientras norm.cdf te dice "¿qué probabilidad hay de que un valor sea ≤ X?", 
# norm.ppf responde: "¿qué valor X corresponde a una probabilidad acumulada dada?"
#
# Sintaxis 
# valor = norm.ppf(q, loc=media, scale=desviacion_estandar)
# 
# Donde:    
#   q: Probabilidad acumulada (entre 0 y 1)
#   loc: Media de la distribución
#   scale: Desviación estándar

porcentaje_ventas = 0.25
media = 5000
desviacion_standar = 2000

#  Calcula la cantidad por debajo de la cual estará el 25% de los acuerdos.
pct_25 = norm.ppf(porcentaje_ventas, media, desviacion_standar)

print(f'El 25% de los acuerdos de Amir son de una cantidad de al menos de: USD { pct_25 }')


# Sabes que puedes contar con Amir el 75% (1 - 0.25) del tiempo para hacer una venta de al menos $3651.02. 
# Esta información podría ser útil para hacer proyecciones de ventas a nivel de la empresa.

#-----------------------------------------
plt.show()