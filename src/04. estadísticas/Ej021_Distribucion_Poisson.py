# Distribucion de Poisson
# 
# - La distribución de Poisson es una distribución de probabilidad discreta. 
# Esto significa que se usa para calcular la probabilidad de que ocurra 
# un número específico de eventos (un número entero: 0, 1, 2, 3,...) dentro de:
#       
#       1. Un intervalo fijo de tiempo (ej: en 1 hora).
#       2. Una región fija de espacio (ej: en 1 metro cuadrado, en 1 kilómetro de carretera).
#
# - Un proceso de Poisson es un proceso en el que los eventos parecen ocurrir a un ritmo determinado,
# Pero de forma completamente aleatoria
#
# - La distribucion de Poisson describe la probabilidad de que ocurra una determinada cantidad
# de eventos durante un periodo fijo de tiempo
#
# - La distribucion de Poisson responde preguntas como:
# ¿Probabilidad de que lleguen exactamente 2 clientes (k=2) en esa hora donde el promedio es 3 (λ=3)?
# 
# La distribución de Poisson es como una máquina matemática que toma:
#   - El promedio que conoces (λ = 3)
#   - El número exacto que te interesa (k = 2)
# ...y te escupe la probabilidad de que eso pase.

from scipy.stats import poisson

#--------------------------------------------
# Ejemplo 1: Probabilidad de que Amir responda a 5 clientes potenciales en un dia,
# dado que responde a una media de 4



clientes = 5
media = 4

# Probabilidad de responder a 5 clientes potenciales (clientes == 5)
prob_5 = poisson.pmf(clientes, media)

print(f'La probabilidad que Amir responda a 5 clientes potenciales en un dia es de: {prob_5:.1%}')

#-----------------------------------------------------------------
# Ejemplo 2:
# El compañero de trabajo de Amir responde a una media de 5,5 clientes potenciales al día. 
# ¿Cuál es la probabilidad de que responda a 5 clientes potenciales en un día?



clientes = 5
media = 5.5

# Probabilidad de responder a 5 clientes potenciales (clientes == 5)
prob_coworker = poisson.pmf(clientes, media)

print(f'La probabilidad que el compañero de Amir responda a 5 clientes potenciales en un dia es de: {prob_coworker:.1%}')

#----------------------------------------------------
# Ejemplo 3: ¿Cuál es la probabilidad de que Amir responda a 2 o menos clientes potenciales en un día?


clientes = 2
media = 4 

# Probabilidad de responder a menos de 2 clientes potenciales (clientes < 2)
prob_2_or_less = poisson.cdf(clientes, media)

print(f'La probabilidad de Amir a responder a menos de 2 clientes potenciales en un dia es de: {prob_2_or_less:.1%}')

#-------------------------------------------------------------
# Ejemplo 4: ¿Cuál es la probabilidad de que Amir responda a más de 10 clientes potenciales en un día?

clientes = 10
media = 4

# Probabilidad de reponder a mas de 10 clientes (clientes > 10 )
prob_over_10 = 1 - poisson.cdf(clientes, media)                         # El 1 representa el 100% de probabilidad total

print(f'La probabilidad de Amir a responder a mas de 10 clientes potenciales en un dia es de: {prob_over_10:.1%}')
