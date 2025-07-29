# Muestreo estratificado de recuentos iguales
# 
# Si un subgrupo es mayor que otro en la población, pero no quieres reflejar esa diferencia en tu análisis, 
# puedes utilizar el muestreo estratificado de recuentos iguales para generar muestras en las que cada subgrupo 
# tenga la misma cantidad de datos. 
# 
# Por ejemplo, si estás analizando tipos sanguíneos, el O es el más común en todo el mundo, pero puede que desees 
# tener cantidades iguales de O, A, B y AB en tu muestra.

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os

# Obtener ruta base del archivo
base_path = os.path.dirname(os.path.abspath(__file__))
ruta_archivo = os.path.join(base_path, "..", "..", "Archivos", "attrition_pop.csv")


# Importa el excel
attrition_pop = pd.read_csv( ruta_archivo)  


#-------------------------------------------------
# Ejercicio 1: 

# 1. Sin muestreo: 
# Traza YearsAtCompany desde attrition_pop como un histograma con contenedores con anchura 1 de 0 a 40.
attrition_pop['YearsAtCompany'].hist(bins=np.arange(0, 41, 1), color='blue')

# 2. Con muestreo Ponderado:

# Muestra de 400 empleados de attrition_pop ponderada por YearsAtCompany.
attrition_weight = attrition_pop.sample(n=400, weights="YearsAtCompany")

# Traza YearsAtCompany desde attrition_weight como un histograma con contenedores con anchura 1 de 0 a 40.
attrition_weight['YearsAtCompany'].hist(bins=np.arange(0, 41, 1), color='orange')


# El parámetro weights="YearsAtCompany" en el método sample() 
# hace que el muestreo no sea aleatorio uniforme, sino que cada fila tenga una probabilidad 
# de ser seleccionada proporcional al valor de la columna "YearsAtCompany".
# 
# ¿Cómo funciona?
# 1. Sin weights (muestreo uniforme):
#      - Cada fila tiene la misma probabilidad de ser seleccionada (1/n)
#      - Es completamente aleatorio
#
# 2. Con weights="YearsAtCompany":
#   - Las filas con más años en la empresa tienen mayor probabilidad de ser seleccionadas
#   - Las filas con menos años tienen menor probabilidad de ser seleccionadas
#
# Ejemplo práctico:
#    Si tienes estos datos:
#       Empleado A: 1 año  → Probabilidad baja de ser seleccionado
#       Empleado B: 5 años → Probabilidad media
#       Empleado C: 20 años → Probabilidad alta de ser seleccionado
# 
# Resultado:
# El DataFrame attrition_weight estará sesgado hacia empleados con más años de experiencia. Esto significa que:
#   - Habrá más representación de empleados con muchos años
#   - Habrá menos representación de empleados nuevos
#   - La distribución final será diferente a la población original


#-------------------------------------
# ¿Cuál es más alto? ¿ La media YearsAtCompany de attrition_pop o la media YearsAtCompany de attrition_weight?
# Media de la muestra.

print(f'media de la poblacion total: { attrition_pop['YearsAtCompany'].mean() }' )        # 7.0081632653061225
print(f'media de la muestra:  { attrition_weight['YearsAtCompany']. mean() }')            # 11.165  

# Conclusion:
# La media ponderada de la muestra es alrededor de 11, que es mayor que la media de la 
# población de alrededor de 7. 
# El hecho de que los dos números sean diferentes significa que la muestra aleatoria simple ponderada está sesgada.

#------------------------------------
plt.show()


#----------------------------------------
# Teoria:

# ¿Qué es el muestreo ponderado?
# En el muestreo ponderado, cada elemento de la población tiene una probabilidad distinta de ser elegido, según un “peso” asignado.
#   - Si un alumno tiene historial de no responder encuestas, podríamos darle un peso mayor para forzar su inclusión.
#   - Útil cuando ciertas observaciones son más “valiosas” o más difíciles de conseguir.
# 
# 
# Aclaración del muestreo ponderado
# En muestreo ponderado: 
#   - No defines cuotas estrictas por estrato.
#   - Asignas a cada individuo un “peso” (o probabilidad) de ser seleccionado.
#   - El muestreo ocurre sobre toda la población combinada, con probabilidades proporcionales a esos pesos.
#
# Si le das a todos en A un peso más alto, en promedio saldrán más de A, pero sin garantizar un mínimo por estrato. 
# Ejemplo de resultados posibles al extraer 130 muestras con pesos:
#
# A: 100
# B: 20
# C: 10