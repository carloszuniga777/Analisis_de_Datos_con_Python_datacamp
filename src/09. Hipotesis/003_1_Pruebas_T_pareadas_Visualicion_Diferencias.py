# Visualización de la diferencia
# 
# Antes de empezar a ejecutar pruebas de hipótesis, es una excelente idea realizar un análisis exploratorio de datos, 
# es decir, calcular la síntesis estadística y visualizar las distribuciones.
#
# Aquí verás la proporción de votos a nivel de condado para el candidato demócrata en 2012 y 2016, sample_dem_data. 
# Como los condados son los mismos en ambos años, estas muestras son pareadas. 
# 
# Las columnas que contienen las muestras son dem_percent_12 y dem_percent_16.
import pandas as pd
import matplotlib.pyplot as plt
import os

# Obtener ruta base del archivo
base_path = os.path.dirname(os.path.abspath(__file__))
ruta_archivo = os.path.join(base_path, "..", "..", "Archivos", "sample_dem_data.csv")


# Importa el excel
sample_dem_data = pd.read_csv( ruta_archivo)  


#--------------------------------------------------------------------------
# 
#---------------------------------------------------------------------------
# Crea una nueva columna diff que contenga el porcentaje de votos por el candidato demócrata en 2012
#  menos el porcentaje de votos por el candidato demócrata en 2016.

# Calculate the differences from 2012 to 2016
sample_dem_data['diff'] = sample_dem_data['dem_percent_12'] - sample_dem_data['dem_percent_16']


# Calcula la media de la columna diff como xbar_diff.
xbar_diff = sample_dem_data['diff'].mean()

# Calcula la desviación típica de la columna diff como s_diff.
s_diff = sample_dem_data['diff'].std() 

# Crea un histograma de la columna diff con 20 bins.
sample_dem_data['diff'].hist(bins=20)

plt.show()


# Conclusion:
# Observa que la mayoría del histograma se encuentra a la derecha de cero.