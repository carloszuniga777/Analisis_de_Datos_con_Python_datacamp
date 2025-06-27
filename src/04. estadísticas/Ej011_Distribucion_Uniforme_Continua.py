# Distribución Uniforme Continua:
#
# Es un modelo donde todos los valores dentro de un rango fijo tienen exactamente la misma probabilidad de ocurrir. 
# Imagínalo como una línea recta donde cada punto tiene igual oportunidad de ser elegido: 
# desde números decimales entre 0 y 1 hasta cualquier minuto dentro de una hora. 
# 
# Su característica principal es que forma un rectángulo perfecto al graficarse,
#  reflejando que no hay zonas "más probables" que otras. 
# 
# Es ideal para fenómenos donde la aleatoriedad es perfectamente equilibrada, 
# como seleccionar coordenadas en un mapa o tiempos aleatorios en experimentos

# Ejercicio: Copias de seguridad de datos:
#
# El software de ventas utilizado en tu empresa está configurado para hacer copias de seguridad automáticas, 
# pero nadie sabe exactamente a qué hora se hacen. 
# 
# Sin embargo, se sabe que las copias de seguridad se realizan exactamente cada 30 minutos. 
# Amir vuelve de las reuniones de ventas a horas aleatorias para actualizar los datos del cliente 
# con el que se acaba de reunir. 
# 
# Quiere saber cuánto tiempo tendrá que esperar para que se haga una copia de seguridad de sus datos recién introducidos. 
# Utiliza tus nuevos conocimientos sobre las distribuciones uniformes continuas 
# para modelar esta situación y responder a las preguntas de Amir.

#    <-------------------------Tiempo de Espera ------------------------------->      
#    | 
#    |  
#    | 
#  1 _========================================================================= 
#    |                                                                         ||   
#    |                                                                         || 
#    |                                                                         || 
#    |_________|___________|____________|____________|____________|_____________|___________> 
#    0         5          10            15          20           25            30  
#                      

#--------------------------------------------------------------
from scipy.stats import uniform 

# Para modelar cuánto tiempo esperará Amir para una copia de seguridad utilizando una distribución uniforme continua, 
# guarda su menor tiempo de espera posible como min_time y su mayor tiempo de espera posible como max_time. 
# Recuerda que las copias de seguridad se realizan cada 30 minutos.

min_time = 0
max_time = 30

#------------------------------------------------------------
# Ejercicio 1:


#    <-------------------------Tiempo de Espera ------------------------------->      
#    | 
#    |  
#    | 
#  1 _========================================================================= 
#    |                                                                         ||   
#    |         |-------------------------------------------------------------- ||  
#    |         |                                                               || 
#    |_________|___________|____________|____________|____________|_____________|___________> 
#    0         5          10            15          20           25            30  
#                      Probabilidad esperar mas de 5 minutos


# Calcula la probabilidad de que Amir tenga que esperar más de 5 minutos
# El 1 representa el 100% de probabilidad total
prob_greater_than_5 = 1 - uniform.cdf(5, min_time, max_time)

print(f'Probabilidad de que Amir tenga que esperar más de 5 minutos es de: {prob_greater_than_5 * 100} %')


#-------------------------------------------------------------
# Ejercicio 2: Calcula la probabilidad de que Amir tenga que esperar entre 10 y 20 minutos


#    <-------------------------Tiempo de Espera ------------------------------->      
#    | 
#    |  
#    | 
#  1 _========================================================================= 
#    |                                                                         ||   
#    |                      -------------------------                          ||  
#    |                     |                         |                         || 
#    |_________|___________|____________|____________|____________|_____________|___________> 
#    0         5          10            15          20           25            30  
#                      Probabilidad esperar entre 10 y 20 minutos


prob_between_10_and_20 = uniform.cdf(20, min_time, max_time) - uniform.cdf(10, min_time, max_time)

print(f'Probabilidad de que Amir tenga que esperar entre 10 y 20 minutos es de: {prob_between_10_and_20 * 100} %')


#------------------------------------------------------------------
# Ejercicio: Probabilidad de que Amir tenga que esperar menos de 10 minutos

prob_menos_10 = uniform.cdf(10, min_time, max_time)

print(f'Probabilidad de que Amir tenga que esperar menos de 10 minutos: {prob_menos_10 * 100} %')