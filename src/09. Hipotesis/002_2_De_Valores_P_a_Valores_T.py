# De t a p
# 
# Anteriormente, calculaste el estadístico de prueba para el problema de dos muestras de si el peso medio 
# de los envíos era menor en los envíos que no se retrasaron (late == "No") 
# que en los envíos que se retrasaron (late == "Yes"). 
# 
# Para tomar decisiones al respecto, debes transformar el estadístico de prueba con una función de distribución acumulativa 
# para obtener un valor p.
#
# Recuerda las hipótesis:
# H0: el peso medio de los envíos que no se retrasaron es igual que el peso medio de los envíos que se retrasaron.
# HA: el peso medio de los envíos que no se retrasaron es menor que el peso medio de los envíos que se retrasaron.
#
# El estadístico de prueba, t_stat, está disponible, igual que los tamaños de muestra de cada grupo, 
# n_no y n_yes. Utiliza un nivel de significación de alpha = 0.05.

import pandas as pd
import numpy as np
from scipy.stats import t
import os

# Obtener ruta base del archivo
base_path = os.path.dirname(os.path.abspath(__file__))
ruta_archivo = os.path.join(base_path, "..", "..", "Archivos", "late_shipments.csv")


# Importa el excel
late_shipments = pd.read_csv( ruta_archivo)  


#--------------------------------------------------------------------------
# Parte 1: Calculando la Medias, Desviacion estandar y tamano de la muestras
#---------------------------------------------------------------------------

# xbar_no → media muestral del grupo "No" (envíos que llegaron a tiempo).
#
# xbar_yes → media muestral del grupo "Yes" (envíos que llegaron tarde).
#
# s_no → desviación estándar muestral del grupo "No".
#
# s_yes → desviación estándar muestral del grupo "Yes".
#
# n_no → cantidad de observaciones en el grupo "No".
#
# n_yes → cantidad de observaciones en el grupo "Yes".


# Calculando la Medias

xbar_no = late_shipments[late_shipments['late']=='No']['weight_kilograms'].mean()
xbar_yes = late_shipments[late_shipments['late']=='Yes']['weight_kilograms'].mean()

# Calculando la Desviaciones estandar (muestrales)
s_no = late_shipments[late_shipments['late']=='No']['weight_kilograms'].std()
s_yes = late_shipments[late_shipments['late']=='Yes']['weight_kilograms'].std()

# Calculando el tamano de muestra
n_no = late_shipments[late_shipments['late']=='No']['weight_kilograms'].count()
n_yes = late_shipments[late_shipments['late']=='Yes']['weight_kilograms'].count()


# Resumen en tabla mental
# Variable	  |      Qué es	                        |  Cómo se obtiene
#-----------------------------------------------------------------------
# xbar_no     | Media del peso de envíos a tiempo	|   mean() sobre late == "No"
# xbar_yes	  | Media del peso de envíos tardíos	|   mean() sobre late == "Yes"
# s_no	      | Desv. estándar a tiempo	            |   std() sobre late == "No"
# s_yes	      | Desv. estándar tardíos	            |   std() sobre late == "Yes"
# n_no	      | Número de envíos a tiempo	        |   count() sobre late == "No"
# n_yes	      | Número de envíos tardíos	        |   count() sobre late == "Yes"

#------------------------------------------------------------
# Parte 2: Calculando t
#----------------------------------------------------------

# Calcula el numerador del estadístico de prueba t
# Primer grupo:   xbar_no  ->  Envios que llegaron a tiempo
# Segundo grupo:  xbar_yes ->  Envios que llegaron tarde
numerator = xbar_no - xbar_yes


# Calcula el denominador del estadístico de prueba t
# Raiz cuadrada de ( desviacion estandar de muestra 1 / tamano de muestra 1 ) + ( desviacion estandar de muestra 2 / tamano de muestra 2 )
denominator = np.sqrt(s_no ** 2 / n_no + s_yes ** 2 / n_yes)

# Utiliza esos dos números para calcular el estadístico de prueba
t_stat = numerator / denominator

#--------------------------------------------------------------------------
# Pregunta: ¿Qué tipo de prueba indica la hipótesis alternativa que necesitamos?
#---------------------------------------------------------------------------
#          - - -  
#        -      -
#       -        - 
#      -          -
# -----             - ----
# 
# Respuesta: De cola izquierda
#
# Por tanto la formula para calcular valor p es: t.cdf(t_stat, df=degrees_of_freedom)

# Es de cola izquierda debido a la hipotesis alternativa que sugiere que los envios que no se retrasaron es menor:
# # HA: el peso medio de los envíos que no se retrasaron es menor que el peso medio de los envíos que se retrasaron.

#---------------------------------------------------------
# Parte 3: Calculando Valor P
#---------------------------------------------------------


# Nivel de significacion
alpha = 0.05                    # Nivel de significancia 𝛼 = 0.05: aceptas un 5% de riesgo de falso positivo.

# Calcula los grados de libertad de la prueba.
degrees_of_freedom = n_no + n_yes - 2      # Formula: Número de envíos a tiempo	 + Número de envíos tardíos	 - 2

# Calcula el valor p utilizando el estadístico de prueba, t_stat.
p_value = t.cdf(t_stat, df=degrees_of_freedom)

print(p_value)  # 0.008432382146249523

# Resultado:
# la muestra sugiere que la proporcion real retrazos es 6%. Por tanto, no rechazo H0
print( p_value <= alpha) # True


# 🔍 Interpretación paso a paso:
#
# Hipótesis nula (H₀): El peso medio de ambos grupos es igual.
#
# Hipótesis alternativa (Hₐ): El peso medio de los envíos puntuales es menor que el de los retrasados.
#
# Nivel de significancia (α): 0.05 (5 %).
#
# Valor p obtenido: ≈ 0.00843.
#
# 📊 Qué significa:
#
# El valor p indica la probabilidad de obtener un estadístico de prueba tan extremo (o más) 
# que el observado si la H₀ fuera cierta.
#
# Como 0.00843 < 0.05, existe evidencia estadísticamente significativa para rechazar la H₀.
#
# En contexto: los datos apoyan la afirmación de que, en promedio, 
# los envíos puntuales pesan menos que los que se retrasaron.
#
# 💡 En términos prácticos: Bajo este análisis, la diferencia observada no parece deberse al azar. 
# Aunque recuerda que estadísticamente significativo no siempre implica una diferencia importante en magnitud
#  —ahí entra el tamaño del efecto y el contexto operacional.


# ¿Qué decisión debes tomar basándote en los resultados de la prueba de hipótesis?
# Rechazar la hipótesis nula (H0).

# Conclusion: 
# Cuando el error estándar se estima a partir de la desviación estándar de la muestra 
# y el tamaño de la muestra, la estadística de prueba se transforma en un valor p utilizando la distribución t.