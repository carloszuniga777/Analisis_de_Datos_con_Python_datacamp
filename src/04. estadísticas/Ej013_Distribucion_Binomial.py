# Concepto teórico de distribución binomial: 
# 
# La distribución binomial es un modelo estadístico que calcula la probabilidad 
# de obtener exactamente "k" éxitos en "n" intentos repetidos e independientes
# de un experimento que solo tiene dos resultados posibles (éxito o fracaso), 
# donde la probabilidad de éxito (p) se mantiene constante en cada intento. 
# 
# Piensa en lanzar una moneda al aire varias veces 
# y contar cuántas veces sale "cara": cada lanzamiento es independiente, 
# solo hay cara o cruz, y la probabilidad de cara no cambia.


# Ejercicio: Simular acuerdos de venta
#
# Supongamos que Amir suele trabajar en 3 acuerdos por semana y que, 
# en general, consigue el 30 % de los acuerdos en los que trabaja. 
# Cada acuerdo tiene un resultado binario: o se pierde o se consigue. 
# Así que puedes modelar sus acuerdos de venta con una distribución binomial. 
# 
# En este ejercicio, ayudarás a Amir a simular el valor de un año de sus acuerdos para que pueda comprender mejor su rendimiento.

# binom.rvs de en SciPy:
# 
# es una función que genera muestras aleatorias de una distribución binomial. 
# Simula experimentos donde cuentas cuántos "éxitos" ocurren en una cantidad fija de intentos independientes, 
# cada uno con una probabilidad fija de éxito.
# 
# Donde:
# n: Número de intentos (pruebas) en un experimento. Ejemplo: n=3 (Amir trabaja 3 acuerdos por semana).
# p: Probabilidad de éxito en cada intento (Valor entre 0 y 1). Ejemplo: p = 0.30 (30% de probabilidad de cerrar un acuerdo).
# size: Cantidad de experimentos a simular.Ejemplo: size=52 (simula 52 semanas).
# 
# ¿Para qué sirve? Casos de uso:
#   Simular escenarios reales:
#       - Predecir ventas semanales de un vendedor.
#       - Calcular probabilidades de fallos en componentes electrónicos.
#       - Modelar lanzamientos de monedas/dados.


import numpy as np
from scipy.stats import binom

# Set random seed to 10
np.random.seed(10)

# -------------------------------------
# Ejemplo 1: Simula 1 acuerdo en el que ha trabajado Amir, que consigue el 30 % de los acuerdos en los que trabaja.


# En este ejemplo, vamos a simular que amir, trabaja 1 acuerdo en 1 una semana, con probabilidad de exito de 30%

coins = 1,         # Numero de acuerdos     
probability = 0.30 # 30% posibilidad de exito
quantity = 1       # Cantidad de muestras (Semanas)

# binom.rvs(Numero de monedas/Numero Intentos, probabilidad, cantidad de experimentos)
print( binom.rvs(coins, probability, size = quantity ) )

# Interpretación del resultado:
#
# 1: Indica "éxito" (Amir consiguió el acuerdo).
# 0: Indicaría "fracaso" (no lo consiguió).
#
# En tu caso, el resultado [1] es válido pero aleatorio. 
# Si repites la simulación varias veces, obtendrás 
# 0 en aproximadamente el 70% de los casos 
# y 1 en el 30% restante.

#-------------------------------------------------
# Ejemplo 2: Simula una semana típica de acuerdos de Amir o una semana de 3 acuerdos.

# En este ejemplo, vamos a simular que amir hace 3 acuerdo en 1 semana
# Con una probabilidad de exito de 30%

coins = 3           # 3 Acuerdos
probability = 0.30  # 30% posibilidad de exito
quantity = 1        # Cantidad de muestras (Semanas)

print( binom.rvs(coins, probability, size = quantity ) )

#----------------------------------------------------
# Ejemplo 3: Simula el valor de un año de acuerdos de Amir o 52 semanas de 3 acuerdos cada una y guárdalo en deals.
# Imprime el número medio de acuerdos que consiguió por semana.

# En este ejemplo, vamos a simular que amir, hace 3 acuerdos en 52 semanas (1 año), con una 
# probabidad de exito de 30% 

coins = 3           # 3 Acuerdos
probability = 0.30  # 30% posibilidad de exito
quantity = 52       # Semanas


acuerdos = binom.rvs(coins, probability, size = quantity )

print( f'Acuerdos con exito en 52 semanas\n\n {acuerdos}')

# Interpretacion del resutado
# 
# 1.Cada número representa el total de acuerdos exitosos en una semana:
#   0: Ningún acuerdo conseguido (todos perdidos).
#   1: Consiguió 1 de 3 acuerdos.
#   2: Consiguió 2 de 3 acuerdos.
#   3: Consiguió los 3 acuerdos.
#
#
# 2. Análisis de los resultados:
#   - Semanas con 0 éxitos: Hay varias (ej: semanas 4, 5, 7, 8...).
#   - Semanas con 1 éxito: Son las más frecuentes (ej: semanas 1, 2, 3, 6...).
#   - Semanas con 2 éxitos: Menos frecuentes pero ocurren (ej: semanas 10, 13, 17...).
#   - Semanas con 3 éxitos: No hubo ninguna en esta simulación 
#                           (lo esperado, ya que la probabilidad es baja:  0.3^3 = 0.027


# Calculando el promedio de acuerdos con exito en 52 semanas
promedio = np.mean(acuerdos)

print(f'En este año simulado, Amir ganó una media de 0.83 acuerdos por semana de: { promedio }')

# En este año simulado, Amir ganó una media de 0.83 acuerdos por semana.
# Eso significa que Amir gano al menos 1 acuerdo por semana
