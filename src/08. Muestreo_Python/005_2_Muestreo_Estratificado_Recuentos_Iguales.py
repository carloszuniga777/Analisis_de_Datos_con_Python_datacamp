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
import os

# Obtener ruta base del archivo
base_path = os.path.dirname(os.path.abspath(__file__))
ruta_archivo = os.path.join(base_path, "..", "..", "Archivos", "attrition_pop.csv")


# Importa el excel
attrition_pop = pd.read_csv( ruta_archivo)  


#-------------------------------------------------
# Ejercicio 1: 


# Utiliza un muestreo estratificado de recuentos iguales en attrition_pop para obtener 30 empleados de cada grupo de Education, 
# estableciendo el valor de inicialización en 2022.
attrition_eq = attrition_pop.groupby('Education').sample(n=30, random_state=2022)      

# Obtén la proporción de empleados por nivel Education de attrition_eq.
education_counts_eq = attrition_eq['Education'].value_counts(normalize=True)

# Print the results
print(education_counts_eq)

# Resultado:
# Education
# Bachelor         0.2
# Below_College    0.2
# College          0.2
# Doctor           0.2
# Master           0.2

# Conclusion:
#  Si deseas que cada subgrupo tenga el mismo peso en tu análisis, 
# entonces el muestreo estratificado de conteos iguales es la técnica adecuada.