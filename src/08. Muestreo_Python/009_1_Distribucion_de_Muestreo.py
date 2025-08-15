# Replicar muestras
# Cuando calculas una estimación puntual, como la media muestral, el valor que calculas depende de las filas 
# que se incluyeron en la muestra. 
# 
# Eso significa que hay cierta aleatoriedad en la respuesta. Para cuantificar la variación causada por esta aleatoriedad, 
# puedes crear muchas muestras y calcular la media muestral (u otro estadístico) de cada muestra.

import pandas as pd
import matplotlib.pyplot as plt
import os

# Obtener ruta base del archivo
base_path = os.path.dirname(os.path.abspath(__file__))
ruta_archivo = os.path.join(base_path, "..", "..", "Archivos", "attrition_pop.csv")


# Importa el excel
attrition_pop = pd.read_csv( ruta_archivo,  dtype={'RelationshipSatisfaction': 'category'})  


#-----------------------------------------------

# Crea una lista vacia
mean_attritions = []

# Itera 500 veces y asigna la medias muestrales a la lista en cada iteracion
for i in range(500):
	mean_attritions.append(
    	attrition_pop.sample(n=60)['Attrition'].mean()
	)
  

# Crea un histograma de las 500 muestras
plt.hist(mean_attritions, bins=16)

plt.show()

# Conclusion:
# Al generar la estadística de la muestra muchas veces con diferentes muestras,
#  puedes cuantificar la cantidad de variación en esas estadísticas.

# Conclusion: https://campus.datacamp.com/es/courses/sampling-in-python/sampling-distributions?ex=6
# A medida que aumenta el tamaño de la muestra, en promedio cada media muestral tiene un error relativo menor 
# en comparación con la media de la población, reduciendo así el rango de la distribución.