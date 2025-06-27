# Cálculo de probabilidades binomiales
# Igual que en el ejercicio anterior, supongamos que Amir consigue el 30 % de los acuerdos.
#  Quiere hacerse una idea de las probabilidades que tiene de cerrar un determinado número de acuerdos cada semana. 
# 
# En este ejercicio, calcularás qué probabilidades hay de que cierre distintos números de acuerdos 
# utilizando la distribución binomial.


from scipy.stats import binom

# ---------------------------------------------------------------
# Ejemplo 1: Probabilidad de un resultado exacto  
# ¿Cuál es la probabilidad de que Amir cierre los 3 acuerdos en una semana?
# P(head == 3)

# La función pmf (Probability Mass Function, o Función de Masa de Probabilidad) es la herramienta fundamental 
# para calcular probabilidades exactas en distribuciones discretas como la binomial. 
# Te explica qué tan probable es un resultado específico.

# El ejercicio dice cual es la probabilidad de que amy cierre 3/3 acuerdos exactos en una semana

coin = 3                # Numero de Intentos
exitoCara = 3           # Numero de exito    
probability = 0.30      # Probabilidad

# Probabilidad de cerrar 3 de 3 acuerdos
prob_3 = binom.pmf(exitoCara, coin, probability)

print(f'La probabilidad de tener 3 acuerdos de 3 es de: {prob_3 * 100}%')


#  Conclusión: pmf es tu calculadora de probabilidades exactas 
#  para escenarios específicos en procesos binomiales. 
#  Es esencial para tomar decisiones cuantitativas cuando necesitas precisión matemática, 
#  no solo simulaciones aleatorias.

#-------------------------------------------------------------------
# Ejemplo 2:
# ¿Cuál es la probabilidad de que Amir cierre 1 acuerdo o menos en una semana?
# P(head <= 1)

# La función binom.cdf (Cumulative Distribution Function - Función de Distribución Acumulada) 
# calcula la probabilidad acumulada de que ocurran hasta cierto número de éxitos en una distribución binomial. 
# Es la herramienta esencial para responder preguntas del tipo: 
# "¿Cuál es la probabilidad de obtener X éxitos o menos?"


coin = 1                # Numero de Intentos
exitoCara = 3           # Numero de exito    
probability = 0.30      # Probabilidad

# Probabilidad de cerrar 1 o 0 (acuerdos <= 1) acuerdos de 3
prob_less_than_or_equal_1 = binom.cdf(coin, exitoCara, probability)

print(f'La  probabilidad de cerrar 1 o 0 acuerdos es de: { prob_less_than_or_equal_1 }%')

# Conclusion: binom.cdf es esencial para tomar decisiones basadas en umbrales mínimos, 
# evaluar riesgos de no alcanzar objetivos, y calcular probabilidades acumuladas en cualquier escenario binomial. 
# Su valor está en la capacidad de cuantificar "peores escenarios" de manera precisa.

#------------------------------------------------------------------
# Ejemplo 3: 
# ¿Cuál es la probabilidad de que Amir cierre más de 1 acuerdo?

coin = 1                # Numero de Intentos
exitoCara = 3           # Numero de exito    
probability = 0.30      # Probabilidad

# Probabilidad de cerrar mas de un acuerdos  (acuerdos > 1) de 3 acuerdos
prob_greater_than_1 = 1 -  binom.cdf(coin, exitoCara, probability)                         # El 1 representa el 100% de probabilidad total

print(f'La  probabilidad de cerrar mas de 1 acuerdo es: { prob_greater_than_1 }%')