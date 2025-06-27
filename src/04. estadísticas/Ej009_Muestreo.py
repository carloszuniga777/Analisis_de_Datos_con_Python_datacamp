# Muestreo:
#
# Muestreo Sin Remplazo: 
# Procedimiento donde cada elemento seleccionado no se devuelve a la población, 
# por lo que no puede ser elegido nuevamente.
# Caracteristicas:
#    - Las probabilidades se actualizan tras cada selección
#    - Las muestras son unicas, no hay elementos repetidos en las muestas
#    - La extracciones son eventos dependientes (La seleccion previa afecta la siguiente)     
#
# Muestreo Con reemplazo:
# Procedimiento donde cada elemento seleccionado se devuelve a la población, 
# por lo que puede ser elegido múltiples veces.
# Caracteristicas:
#        - Poblacion constante, el tamano de la poblacion permanece constante en todas la extracciones
#        - Probabilidades fijas
#        - Muestra con posibles repeticiones
#        - Las extracciones son eventos independientes (Una seleccion no afecta a la siguiente)
# 
# Ejercicio:        
# Ahora es el momento de elegir aleatoriamente cinco acuerdos 
# para poder ponerte en contacto con cada cliente y preguntarle 
# si quedó satisfecho con el servicio que recibió. 
# Intentarás hacerlo tanto con reemplazo como sin él.
# 
# Además, quieres asegurarte de que esto se haga aleatoriamente 
# y de que pueda reproducirse en caso de que te pregunten 
# cómo elegiste las acuerdos, por lo que tendrás que establecer 
# la semilla aleatoria antes de realizar el muestreo de los acuerdos.


import pandas as pd
import numpy as np
import os

# Obtener ruta base del archivo
base_path = os.path.dirname(os.path.abspath(__file__))
ruta_archivo = os.path.join(base_path, "..", "..", "Archivos", "amir_deals.csv")

# Importa el excel sales.csv
amir_deals = pd.read_csv( ruta_archivo)  

#-------------------------------------------
# Set random seed
np.random.seed(24)

# Toma una muestra de 5 acuerdos sin reemplazo 
sample_without_replacement = amir_deals.sample(5)
print(sample_without_replacement)
print('\n\n')

# Toma una muestra de 5 acuerdos con reemplazo
sample_with_replacement = amir_deals.sample(n=5, replace=True)
print(sample_with_replacement)