# Generar una distribución muestral aproximada
# 
# Calcular la distribución muestral exacta solo es posible en situaciones muy sencillas. Con solo cinco dados de ocho caras, 
# el número de tiradas posibles es 8**5, es decir, más de treinta mil. 
# 
# Cuando el conjunto de datos es más complicado, por ejemplo, cuando una variable tiene cientos o miles de categorías, 
# el número de resultados posibles se vuelve demasiado difícil de calcular con exactitud.
#
# En esta situación, puedes calcular una distribución muestral aproximada simulando la distribución muestral exacta. 
# Es decir, puedes repetir un procedimiento una y otra vez para simular tanto el proceso de muestreo 
# como el proceso de cálculo de la estadística muestral.

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


#----------------------------------------------
 #1. Preparar una lista vacía para almacenar medias de muestra
sample_means_1000 = []

# 2. Repetir el muestreo 1000 veces
for i in range(1000):
    # 2.1 np.random.choice(...)
    #     - Primer argumento: lista de valores posibles [1,2,…,8]
    #     - size=5: extrae 5 valores para cada experimento
    #     - replace=True: con reemplazo (puede repetirse el mismo número)
    #
    #     Esto simula lanzar cinco dados de 8 caras en cada iteración.
    draws = np.random.choice(list(range(1, 9)), size=5, replace=True)
    
    # Size: Viene siendo 5 dados y la lista son los valores que tiene esos dados (1 al 8)
    

    # 2.2 .mean()
    #     Calcula la media aritmética de esos cinco resultados de dado
    mean_of_draws = draws.mean()
    

    # 2.3 Guardar la media en la lista
    sample_means_1000.append(mean_of_draws)

# 3. Dibujar un histograma de las 1000 medias obtenidas
#    - bins=20: divide el rango de medias en 20 contenedores (barras)
plt.hist(sample_means_1000, bins=20)
plt.xlabel('Media de 5 dados')
plt.ylabel('Frecuencia')
plt.title('Distribución muestral aproximada (1000 réplicas)')
plt.show()

# Conclusion:
# Una vez que tu conjunto de datos se hace lo suficientemente grande, no se pueden calcular distribuciones de muestreo exactas, 
# por lo que se debe usar una distribución de muestreo aproximada. 
# 
# Observa que el histograma es similar pero no exactamente igual a la forma del gráfico de barras del ejercicio anterior.

#-------------------------------------------------------------------------
#  np.random.choice

# np.random.choice: es una función de NumPy para extraer muestras aleatorias de un conjunto de valores.
#
# Parámetros principales:
#   - a (array_like): secuencia de elementos a muestrear (aquí, [1, 2, …, 8]).
#   - size (int o tuple): número de elementos a extraer. Si es un entero, devuelve un arreglo unidimensional de esa longitud.
#   - replace (bool):
#               - True: cada extracción vuelve al “bolso”, por lo que un mismo valor puede salir varias veces.
#               - False: sin reemplazo; cada valor solo puede salir una vez por llamada.

# #--------------------------------------------------------------------------
# Distribución muestral aproximada
#
# Definición
# La distribución muestral aproximada es una representación de cómo varía una estadística 
# (por ejemplo, la media o la proporción) cuando extraemos repetidamente muestras aleatorias de una población. 
# 
# En lugar de calcular la distribución exacta, que a menudo resulta compleja o imposible, 
# simulamos el muestreo muchas veces y registramos el valor de la estadística en cada réplica. 
# 
# Al graficar esas réplicas (por ejemplo, en un histograma), obtenemos una visión clara de la variabilidad 
# y la forma que adopta nuestro estimador.
#
#
# Explicación detallada
# Para generar una distribución muestral aproximada, seguimos estos pasos:
#   - Extraer con reemplazo una muestra aleatoria de la población (o del conjunto de datos original).
#   - Calcular la estadística de interés (media, mediana, proporción, etc.) sobre esa muestra.
#   - Repetir el proceso un gran número de veces (por ejemplo, 1 000 o 10 000 réplicas).
#   - Agrupar todos los valores obtenidos en un histograma o densidad para visualizar su dispersión y forma.
#   - Esta simulación refleja la incertidumbre inherente al muestreo y permite ver si el estimador tiende a concentrarse 
#     alrededor de cierto valor o si presenta sesgos o colas largas.
#
# Cuándo utilizarla
# Utiliza una distribución muestral aproximada cuando:
#   - La distribución exacta de la estadística es difícil o imposible de derivar con fórmulas.
#   - La población tiene muchas categorías o es continua y no existen tablas de referencia.
#   - Deseas estimar intervalos de confianza sin depender completamente de supuestos teóricos (como normalidad estricta).
#   - Quieres explorar el comportamiento de estadísticas complejas (razones, quantiles) para las cuales no hay soluciones cerradas.
#   - En todos estos casos, la simulación proporciona una forma práctica y accesible de entender la precisión 
#     y la variabilidad de tus estimaciones.


# Exacta vs Aproximada
# 
# 1. Cobertura del espacio muestral
#   
#   Exacta: Enumeras todas las muestras posibles de un tamaño dado. 
#   • Para cinco dados de 8 caras son 8⁵ = 32 768 tiradas. 
#   • Obtienes la frecuencia real de cada media.
#
#   Aproximada (aleatoria): Sacas al azar un subconjunto de réplicas (por ejemplo, 500 lanzamientos). 
#   • No cubres todo el espacio; solo una muestra de él. 
#   • Las frecuencias son estimaciones de las probabilidades reales.
# 
# 
# 2. Precisión vs variabilidad
#   - Con la distribución exacta la curva de frecuencias es “la verdad absoluta” 
#     para ese experimento: no varía si la recalculas.

#   - Con la distribución aproximada cada vez que simulas (p. ej. 500 réplicas), 
#     tu histograma cambiará ligeramente. 
#          • Cuantas más réplicas uses, más cerca llegarás de la forma exacta, pero siempre habrá un error de simulación.
#
# 3. ¿Cuándo usar cada una?
# 
#   Distribución exacta
#       - Poblaciones muy pequeñas o rango de valores limitado (dados, cartas, poblaciones breves).
#       - Necesitas la probabilidad real sin aproximaciones.
# 
#   Distribución aproximada
#       - Poblaciones grandes o continuas (personas, datos médicos, encuestas).
#       - Cuando la enumeración completa es inviable y basta una buena aproximación.
#       - Para aplicar teoremas asintóticos (CLT) o técnicas de remuestreo (bootstrap).