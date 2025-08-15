# Realizar un muestreo por clústeres
# Ahora que sabes cuándo utilizar el muestreo por clústeres, es hora de ponerlo en práctica. 
# 
# En este ejercicio, explorarás la columna JobRole del conjunto de datos de bajas. 
# Puedes pensar en cada función laboral como un subgrupo de toda la población de empleados.

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import random
import os

# Obtener ruta base del archivo
base_path = os.path.dirname(os.path.abspath(__file__))
ruta_archivo = os.path.join(base_path, "..", "..", "Archivos", "attrition_pop.csv")


# Importa el excel
attrition_pop = pd.read_csv( ruta_archivo,  dtype={'JobRole': 'category'})  

#print(attrition_pop['JobRole'].dtype) 
#-------------------------------------------------

# Paso 1: Crear una lista con los roles de trabajo únicos
job_roles_pop = list(attrition_pop['JobRole'].unique())

# Paso 2: Seleccionar aleatoriamente cuatro roles de trabajo
job_roles_samp = random.sample(job_roles_pop, k=4)


# Paso 3: Filtrar el DataFrame para quedarnos solo con las filas cuyo JobRole esté en nuestra muestra
jobrole_condition = attrition_pop['JobRole'].isin(job_roles_samp)
attrition_filtered = attrition_pop[jobrole_condition].copy()             # Debido a un Warning que genera al eliminar las categorias vacias remove_unused_categories() se realiza una copia


#print(attrition_filtered['JobRole'].value_counts())

# Se puede observar, aunque este filtrado, panda sigue manteniendo las categorias originales definidas:
# 
# JobRole
# Manager                      102
# Sales_Representative          83
# Research_Director             80
# Human_Resources               52
# Healthcare_Representative      0
# Manufacturing_Director         0
# Laboratory_Technician          0
# Research_Scientist             0

# Por tanto se eliminan las categorias que aparecen en 0 con el paso 4



# Paso 4: Eliminar categorías de JobRole que ya no aparecen en el DataFrame filtrado
attrition_filtered['JobRole'] = attrition_filtered['JobRole'].cat.remove_unused_categories()


# Paso 5: Agrupar por JobRole y tomar 10 empleados al azar de cada grupo
# (muestreo por clúster, fijando random_state para reproducibilidad)
attrition_clust = (
    attrition_filtered
    .groupby('JobRole', observed=False) 
    .sample(n=10, random_state=2022)
)
# observed=False:
# Para quitar un Warinig de un cambio futuro en groupby
#   - Actualmente (observed=False): Muestra todas las categorías posibles, incluso si no tienen datos
#   - En futuras versiones (observed=True): Mostrará solo las categorías con datos presentes


# Paso 6: Mostrar por pantalla la muestra obtenida
print(attrition_clust['JobRole'].value_counts())


# Conclusion:
# La técnica de muestreo en dos etapas te da control sobre el muestreo
# tanto entre subgrupos como dentro de subgrupos.

#------------------------------------------------------------------------

# Muestreo de Cluster (Notas mias):
# Es parecido al muestreo estratificado, donde se selecciona una proporcion de registros en cada grupo 
# de manera aleatoria.
# Lo que lo diferencia del muestreo estratificado, es que en vez de seleccionar todos los grupos,
# selecciona una cantidad especifica de grupos al azar y luego realiza la muestras en esos grupos


#IA
# Muestreo por Clústeres vs. Muestreo Estratificado
# 
# Definiciones
#   - Muestreo estratificado Consiste en dividir la población en subgrupos (estratos) mutuamente excluyentes 
#     y relativamente homogéneos, y luego extraer muestras aleatorias de cada estrato.
#
#   - Muestreo por clústeres En la primera etapa se seleccionan aleatoriamente algunos grupos (clústeres) 
#     de la población y en la segunda se muestrean elementos dentro de esos grupos.
#
#
#
#  ¿Cuándo elegir muestreo estratificado?
#   - Cuando conocemos características clave de la población y queremos garantizar la representación de cada 
#     subgrupo importante (por ejemplo, edades, niveles socioeconómicos, regiones).
#
#   - Si el objetivo principal es comparar o analizar diferencias entre esos subgrupos.
#
#   - Cuando los estratos son internamente homogéneos, lo que reduce la varianza de las estimaciones.
#
#   - Si el coste y la logística permiten acceder por separado a cada estrato sin implicar desplazamientos excesivos.
#
#
#
# ¿Cuándo elegir muestreo por clústeres?
#   - Cuando la población está naturalmente agrupada (por ejemplo, escuelas, manzanas de un barrio, sucursales).
#
#   - Si los desplazamientos para recopilar datos en cada unidad son costosos o complicados, 
#     reducir el número de viajes agrupando muestreos dentro de clústeres mejora la eficiencia.
#
#   - Cuando el coste y la logística dominan la decisión, aún a costa de un ligero aumento en la varianza de la muestra.
#
#   - Si no requiere comparar subgrupos específicos dentro de cada clúster, sino estimar parámetros globales de la población.
