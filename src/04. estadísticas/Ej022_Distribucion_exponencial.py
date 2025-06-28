# Distribución exponencial:
#
# - La distribucion exponencial representa la probabilidad de que 
# transcurra un cierto tiempo entre eventos de Poisson
# 
# - La distribución exponencial calcula cuánto tiempo esperarás entre eventos 
# aleatorios (como clientes o fallas) que ocurren con un ritmo promedio constante (λ). 
# 
# Es "sin memoria": si ya esperaste un rato, la probabilidad de que el evento suceda en los próximos minutos no cambia. 
# Además, es la contraparte del tiempo en los procesos de Poisson 
# (si los eventos siguen Poisson, el tiempo entre ellos es exponencial). 
#
# - Imagina que observas un fenómeno donde suceden eventos impredecibles 
# (ej: destellos de una estrella, llegada de meteoritos). 
# Solo conoces su ritmo promedio (ej: "2 eventos por hora"). La distribución exponencial responde:
#
# 🔹 "¿Cuál es la probabilidad de que el próximo evento tarde MÁS de un tiempo 't' en ocurrir?"


# Diferencia con la distribucion uniforme continua:
# Uniforme: Los periodos entre dos eventos suceden exactos y tu llegas al azar, 
#           ejemplo: Un bus pasa cada 15 minutos EXACTOS y tu llegas a la parada en un momento aleatorio,
#                    dentro de ese intervalo
#
#Exponencial: Los eventos ocurren al azar en el tiempo, con una tasa promedio constante
#             Ejemplo:  Si el autobús llega de forma totalmente impredecible, 
#                       pero sabes que en promedio pasa uno cada 15 minutos (λ = 1/15).
#                       Esto es más realista en ciudades con tráfico. 


# Ejercicio:
# Tiempo de modelado entre clientes potenciales
# Para evaluar mejor el rendimiento de Amir, quieres saber cuánto tarda en responder a un cliente potencial 
# después de abrirlo. 
# 
# De media, responde a 1 solicitud cada 2,5 horas. En este ejercicio, calcularás las probabilidades de que pasen 
# diferentes cantidades de tiempo entre que Amir recibe un cliente potencial y envía una respuesta.

from scipy.stats import expon

#--------------------------------------------------
# Ejemplo 1: ¿Cuál es la probabilidad de que Amir tarde menos de una hora en responder a un cliente potencial?


# Probabilidad que responsa menos de 1 hora (responder < 1 hora)
horas = 1
scale = 2.5     # Media: 1 solicitud cada 2.5 horas

response = expon.cdf(horas, scale=scale)

print(f'La probabilidad de que Ami responda menos de 1 hora es: {response:.1%}') 

#---------------------------------------------------
# Ejemplo 2: ¿Cuál es la probabilidad de que Amir tarde más de 4 horas en responder a un cliente potencial?

# Probabilidad que responsa mas de 4 hora (responder > 4 hora)
horas = 4
scale = 2.5 #La media es 1 solicutud cada 2.5 horas


response = 1 - expon.cdf(horas, scale=scale)                    # El 1 representa el 100% de probabilidad total

print(f'La probabilidad de que Ami responda mas de 4 hora es: {response:.1%}') 

#--------------------------------------------------------
# Ejemplo 3: ¿Cuál es la probabilidad de que Amir tarde 3-4 horas en responder a un cliente potencial?

# Probabilidad que responsa entre 3 y 4 hora ( responder > 3 & responder < 4 hora)
hora1 = 3
hora2 = 4 
scale = 2.5 #media en responder 1 solicitud cada 2.5 hroas

response = expon.cdf(hora2, scale=scale) - expon.cdf(hora1, scale=scale)

print(f'La probabilidad de que Ami responda entre 3 y 4 hora es: {response:.1%}') 

# Hay solo alrededor de un 20% de probabilidad de que Amir tarde más de 4 horas en responder,
# así que es bastante rápido en sus respuestas.