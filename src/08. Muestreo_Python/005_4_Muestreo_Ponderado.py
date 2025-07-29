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

# 1) Crear una condición booleana: True si Education es 'Master', False en caso contrario 
condition = attrition_pop['Education'] == 'Master'

# 2) Asignar la columna 'peso' usando np.where:
#    - Si condition es True (Master), peso = 2
#    - Si condition es False (otros niveles), peso = 1

attrition_pop['peso'] = np.where(condition, 2, 1)


# 3) Tomar una muestra aleatoria del 10% de todo el DataFrame,
#    usando la columna 'peso' para ponderar la probabilidad de selección
attrition_sample = attrition_pop.sample(frac=0.1, weights='peso')


# 4) Calcular la frecuencia relativa de cada valor de 'Education'
#    dentro de la muestra obtenida
attrition_sample_count = attrition_sample['Education'].value_counts(normalize=True)

# 5) Mostrar en pantalla las proporciones de cada nivel educativo
print(attrition_sample_count)

# Interpretación de la muestra ponderada
# Los resultados muestran la proporción de cada nivel educativo en la muestra tras asignar peso 2 a “Master” 
# y peso 1 al resto. Esto significa que “Master” tiene el doble de probabilidad de aparecer respecto a los otros grupos
#
# Education
# Master           0.455782
# Bachelor         0.285714
# College          0.142857
# Below_College    0.095238
# Doctor           0.020408



#------------------------------------------

# - El muestreo ponderado asignando un peso a la categoria que se quiere dar prioridad, 
# para que el momento de la muestra, tenga mas posibilidades de ser seleccionada
# 
# - Puede conducir a sesgo