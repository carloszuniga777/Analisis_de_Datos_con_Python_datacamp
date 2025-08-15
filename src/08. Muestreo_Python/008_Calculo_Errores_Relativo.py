# Cálculo de errores relativos
# El tamaño de la muestra que tomes afecta a la precisión con la que las estimaciones puntuales reflejan 
# el parámetro poblacional correspondiente. 
# 
# Por ejemplo, cuando calculas una media muestral, quieres que se aproxime a la media poblacional. 
# Sin embargo, si tu muestra es demasiado pequeña, puede que no sea así.
#
# La métrica más habitual para evaluar la precisión es el error relativo. 
# Es la diferencia absoluta entre el parámetro poblacional y la estimación puntual, todo 
# ello dividido por el parámetro poblacional. A veces se expresa en porcentaje.


import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import random
import os

# Obtener ruta base del archivo
base_path = os.path.dirname(os.path.abspath(__file__))
ruta_archivo = os.path.join(base_path, "..", "..", "Archivos", "attrition_pop.csv")


# Importa el excel
attrition_pop = pd.read_csv( ruta_archivo,  dtype={'RelationshipSatisfaction': 'category'})  


#-----------------------------------------------
# Referencia: Media poblacional de Attrition
 
mean_attrition_pop = attrition_pop['Attrition'].mean()

#-------------------------------------------------
#  Ejemplo 1: Calculo de error relativo con 50 muestras
# 

# Generar una muestra aleatoria simple de 50 filas, con semilla 2022
attrition_srs50 = attrition_pop.sample(n=50, random_state=2022)

# Calcular la media de rotación de empleados en la muestra
mean_attrition_srs50 = attrition_srs50['Attrition'].mean()

# Calcular el porcentaje de error relativo
rel_error_pct50 = 100 * abs(mean_attrition_srs50 - mean_attrition_pop) / mean_attrition_pop

# Imprimir el porcentaje de error relativo
print(rel_error_pct50)

# Con 50 muestras se puede ver que el error relativo es de 62.78481012658227
# Lo cual es demasiado alto, para reducir el error relativo es necesario aumentar el numero de muestras

#----------------------------------------------------
#  Ejemplo 2: Calculo de error relativo con 100 muestras
# 

# Generar una muestra aleatoria simple de 100 filas, con semilla 2022
attrition_srs100 = attrition_pop.sample(n=100, random_state=2022)

# Calcular la media de rotación de empleados en la muestra
mean_attrition_srs100 = attrition_srs100['Attrition'].mean()

# Calcular el porcentaje de error relativo
rel_error_pct100 = 100 * abs(mean_attrition_srs100 - mean_attrition_pop) / mean_attrition_pop

# Imprimir el porcentaje de error relativo
print(rel_error_pct100)

# El error relativo es de 6.962025316455695 es mucho mas bajo que el primero

#---------------------------------------------------------------------
# Conclusion
# A medida que aumentas el tamaño de la muestra, la media de la muestra generalmente se acerca más 
# a la media de la población, y el error relativo disminuye.