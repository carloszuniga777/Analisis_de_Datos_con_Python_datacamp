# Prueba para proporciones únicas
# 
# En el capítulo 1, calculaste un valor p para una prueba en la que se planteaba la hipótesis 
# de que la proporción de envíos retrasados era superior al 6 %. 
# 
# En ese capítulo, utilizaste una distribución bootstrap para estimar el error típico del estadístico. 
# 
# Una alternativa es utilizar una ecuación para el error típico basada en la proporción de muestra, 
# la proporción hipotética y el tamaño de muestra.
#
#   z =     P - P0
#       ----------------
#       \  /---------- 
#        \/  p0 * (1 -p0)
#            ------------
#                n      
# 
# Volverás al valor p utilizando este cálculo más sencillo.

import pandas as pd
import numpy as np
from scipy.stats import norm
import os

# Obtener ruta base del archivo
base_path = os.path.dirname(os.path.abspath(__file__))
ruta_archivo = os.path.join(base_path, "..", "..", "Archivos", "late_shipments.csv")


# Importa el excel
late_shipments = pd.read_csv( ruta_archivo)  


#----------------------------------------------
# Ejemplo 1
#----------------------------------------------

# Plantear la hipótesis de que la proporción de envíos retrasados es del 6%
p_0 = 0.06

# Calcular la proporción muestral de envíos retrasados
p_hat = (late_shipments['late'] == "Yes").mean()

# Calcular el tamaño de la muestra
n = len(late_shipments)

# Calcular el numerador y el denominador del estadístico de prueba
numerator = p_hat - p_0
denominator = np.sqrt(p_0 * (1 - p_0) / n)

# Calcular el estadístico de prueba (z)
z_score = numerator / denominator

# Hipótesis alternativa "mayor que" => 1 - norm.cdf(z)
# Calcular el valor p a partir del estadístico z
p_value = 1 - norm.cdf(z_score)

# Imprimir el valor p
print(p_value)

# Nivel de significacion 
alpha = 0.05

# - Hipótesis nula (H₀): La proporción de envíos retrasados es igual al 6 %.
# - Hipótesis alternativa (H₁): La proporción de envíos retrasados es mayor al 6 %.

if p_value <= alpha:
    print('Rechazar hipotesis nula H0')
else:
    print('No rechazar hipotesis nula H0')




#-----------------------------------------------------------
# Cálculo del valor p
#
# 1. Cola izquierda ("menor que"):
#   
#       p_value = norm.cdf(z_score)
#
# 2. Cola derecha ("mayor que"):
#
#      p_value = 1 - norm.cdf(z_score)
#
#
# 3. Dos colas ("distinto de"):
#       p_value = norm.cdf(-z_score) + 1 - norm.cdf(z_score)
# 
#           o equivalente:
#       
#       p_value = 2 * (1 - norm.cdf(z_score))
#
#
# Comparación con el nivel de significancia:
#       p_value <= alpha   # Devuelve True si el valor p es menor o igual que alfa



# Explicación en palabras simples
#   - Valor p: es la probabilidad de obtener un resultado tan extremo (o más) que el observado,
#              si la hipótesis nula fuera cierta.
#
#   - Cola izquierda: se usa cuando la hipótesis alternativa dice que el valor real es menor que el hipotético.
#
#   - Cola derecha: se usa cuando la hipótesis alternativa dice que el valor real es mayor que el hipotético.
#
#   - Dos colas: se usa cuando la hipótesis alternativa dice que el valor real es diferente (puede ser mayor o menor).
#
#   - norm.cdf(z_score): calcula la probabilidad acumulada hasta el valor z_score en la distribución normal.
#
#   - 1 - norm.cdf(z_score): calcula la probabilidad de estar por encima de ese z_score.


# Conclusion:
# Aunque el bootstrapping se puede usar para estimar el error estándar de cualquier estadística,
# es computacionalmente intensivo. Para proporciones, usar una ecuación simple de la proporción hipotetizada 
# y el tamaño de la muestra es más fácil de calcular.