# Muestreo estratificado proporcional
# 
# Si te interesan los subgrupos dentro de la población, puede que tengas que controlar cuidadosamente los recuentos 
# de cada subgrupo dentro de la población. 
# 
# El muestreo estratificado proporcional da lugar a tamaños de subgrupo dentro de la muestra que son representativos
#  de los tamaños de subgrupo dentro de la población. 
# 
# Equivale a realizar una muestra aleatoria simple en cada subgrupo.

import pandas as pd
import matplotlib.pyplot as plt
import os

# Obtener ruta base del archivo
base_path = os.path.dirname(os.path.abspath(__file__))
ruta_archivo = os.path.join(base_path, "..", "..", "Archivos", "attrition_pop.csv")


# Importa el excel
attrition_pop = pd.read_csv( ruta_archivo)  


#-------------------------------------------------
# Ejercicio 1: 


# 1. Obtén la proporción de empleados por nivel Education de attrition_pop.

# Proportion of employees by Education level
education_counts_pop = attrition_pop['Education'].value_counts(normalize=True)

# Print education_counts_pop
print(education_counts_pop)

# Se puede visualizar la proporcion, sin aplicar ningun muestreo: 
# Education
# Bachelor         0.389116
# Master           0.270748
# College          0.191837
# Below_College    0.115646
# Doctor           0.032653


# 2. Utiliza el muestreo estratificado proporcional en attrition_pop 
#    para muestrear el 40 % de cada grupo de Education, 
#    fijando el valor de inicialización en 2022.

# Muestreo estratificado proporcional para el 40% de cada grupo educativo
attrition_strat = attrition_pop.groupby("Education").sample(frac=0.4, random_state=2022)

# Calcular las proporciones del nivel de educación a partir de attrition_strat
education_counts_strat = attrition_strat['Education'].value_counts(normalize=True)

# Print education_counts_strat
print(f'\n\n { education_counts_strat }')

# Se puede visualizar la proporcion aplicando el muestreo estratificado proporcional del 40% de cada grupo educativo:
#  Education
# Bachelor         0.389456
# Master           0.270408
# College          0.192177
# Below_College    0.115646
# Doctor           0.032313

# Conclusion:
# Al agrupar y luego muestrear, el tamaño de cada grupo en la muestra es representativo 
# del tamaño de la muestra en la población.

#---------------------------------------------------

# ¿Qué es el muestreo estratificado?
# 
#   1. Dividir la población en grupos más pequeños (estratos) que compartan alguna característica relevante.
#       - Ejemplo: en un colegio, podríamos usar como estratos los grados (1.º, 2.º, 3.º…).
#
#   2. Extraer aleatoriamente muestras dentro de cada estrato, en proporción al tamaño de ese estrato o con tamaños iguales por estrato, según convenga.
#
# Ventajas
#      - Cada subgrupo clave está garantizado en la muestra.
#      - Reduce la variabilidad de las estimaciones si los estratos son internamente homogéneos.
#
#
#
# 2. Ejemplo sencillo paso a paso:
# 
# Imagina 1800 estudiantes repartidos así:
#
# Grado	  |  Número de estudiantes
#-------------------------------
# A	          1000
# B	          600
# C	          200
#-----------------------------
#
# Queremos una muestra del 20% de alumnos:
#
# 1.    Proporcional:
#   - A(1000) = 200 alumnos
#   - B(600)  = 120 alumnos
#   - C(200)  = 40 alumnos
#
#
#
# 2. O con Tamano fijo por estracto (Digamos 50 alumnos por grupo)
# 
# A(1000) = 50 alumnos
# B(600)  = 50 alumnos
# C(200)  = 50 alumnos