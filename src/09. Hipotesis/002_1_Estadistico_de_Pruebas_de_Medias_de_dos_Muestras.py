# Estadístico de prueba de media de dos muestras
# 
# La prueba de hipótesis para determinar si existe una diferencia entre las medias de dos poblaciones utiliza 
# un tipo de estadístico de prueba distinto de los z-scores que viste en el capítulo 1. 
# 
# Se llama "t", y puede calcularse a partir de tres valores de cada muestra utilizando esta ecuación:
#
#  t = (Xchild - X adult)
#     -------------------
#     \  /--------------
#      \/  S^2child + S^2adult
#         --------    --------    
#         Nchild      Nadult
#
# Mientras intentas determinar por qué algunos envíos llegan tarde, puedes preguntarte si el peso de los envíos que llegaron 
# a tiempo es menor que el peso de los envíos que llegaron tarde. 
# 
# El conjunto de datos late_shipments se ha dividido en un grupo "yes", 
# donde late == "Yes", y un grupo "no", donde late == "No". 
# 
# El peso del envío se indica en la variable weight_kilograms.
#
# Las medias muestrales de los dos grupos están disponibles como xbar_no y xbar_yes. 
# Las desviaciones típicas de la muestra son s_no y s_yes. Los tamaños de las muestras son n_no y n_yes.

import pandas as pd
import numpy as np
from scipy.stats import norm
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

print(t_stat) # -2.3936661778766433


# Interpretacion
#
# En el análisis se comparó el peso promedio de dos grupos de envíos:
#   1. “No” → envíos que llegaron a tiempo.
#   2. “Yes” → envíos que llegaron tarde.
#
# El cálculo se hizo restando: 
#       Promedio de “No”  −  Promedio de “Yes”
# El resultado fue un número negativo.
# 
# Interpretación sencilla: 
# Cuando el resultado de esta resta es negativo, significa que el segundo grupo (“Yes”, los envíos tardíos) 
# tiene un promedio mayor que el primero (“No”, los envíos puntuales). 
# 
# En otras palabras:
# Los envíos que llegaron tarde, en promedio, pesaron más que los que llegaron a tiempo.


# Conclusion:
# Al probar diferencias entre medias, el estadístico de prueba se llama 't' en lugar de 'z', 
# y se puede calcular usando seis números de las muestras. 
# Aquí, el valor es aproximadamente -2.39 o 2.39, dependiendo del orden en que calculaste el numerador.

#----------------------------------------------------
# La idea principal
#
# Queremos saber si dos o más grupos son realmente diferentes o si las diferencias que vemos son solo casualidad.

# 🌭 Ejemplo con perros y comida
# 
# Imagínate que tienes dos tipos de croquetas: Marca A y Marca B.
#   
#   1. Le das Marca A a un grupo de perros y anotas cuánto comen.
#   2. Le das Marca B a otro grupo de perros y también anotas.
#   3. Calculas el promedio de cada grupo.
#   4. Si la diferencia de promedios es grande y no parece fruto del azar, decimos “sí, hay diferencia”.
#   5. Si es pequeña o podría ser pura casualidad, decimos “no tenemos pruebas suficientes”.
#
# 🛠 Cómo lo hace la estadística
#   - Prueba t → Sirve para comparar dos grupos.
#   - ANOVA → Sirve para comparar tres o más grupos.
#
# 
# El proceso, paso a paso, sin saltos:
#   1. Pregunta: ¿Los grupos comen diferente?
#   2.Medimos: cuánto come cada perro.
#   3. Promedio y variación: ver cuál es la media y cómo varían los datos.
#   4. Cálculo del “número t”: compara la diferencia con el “ruido” de los datos.
#   5. Valor p: un número que dice si lo que vemos es raro o no bajo la idea de “no hay diferencia”.
#   6. Decisión: si el valor p es pequeño (como menor a 0.05), la diferencia es probablemente real; si no, no podemos asegurarlo.
#
# 💡 En pocas palabras: es como una lupa matemática que mira las diferencias entre grupos 
#   y te dice si creerlas o pensar que fue azar.

#--------------------------------

# Imagina que tienes dos cajas de manzanas 🍎🍏
#
#   - Caja A → manzanas del grupo 1
#   - Caja B → manzanas del grupo 2
#
# Si quieres saber cuál caja tiene en promedio manzanas más pesadas, restas:
#
#           promedio_A - promedio_B
#
# - Si el resultado es positivo → la Caja A gana.
# - Si es negativo → la Caja B gana.
#
# En tu ejercicio de late_shipments:
#
#           xbar_no - xbar_yes
# 
#  - Primer grupo → xbar_no (llegaron a tiempo)
#  - Segundo grupo → xbar_yes (llegaron tarde)
#
# Como el número salió negativo, significa:
#
# El promedio de peso de los envíos “No” es menor que el de los “Yes”.