# Visualización de muchas categorías
# 
# Hasta ahora, en este capítulo, solo hemos tenido en cuenta el caso de diferencias en una variable numérica entre dos categorías. 
# Por supuesto, muchos conjuntos de datos contienen más categorías. 
# 
# Antes de realizar pruebas en muchas categorías, suele ser útil ejecutar un análisis exploratorio de datos (EDA) 
# calculando la síntesis estadística de cada grupo y visualizando las distribuciones de la variable numérica para 
# cada categoría mediante diagramas de caja.
#
# Aquí, volveremos a los datos de los envíos retrasados y a cómo varía el precio de cada paquete (pack_price) 
# entre los tres modos de envío (shipment_mode): "Air", "Air Charter" y "Ocean".

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Obtener ruta base del archivo
base_path = os.path.dirname(os.path.abspath(__file__))
ruta_archivo = os.path.join(base_path, "..", "..", "Archivos", "late_shipments.csv")


# Importa el excel
late_shipments = pd.read_csv( ruta_archivo)  


#----------------------------------------------
# Parte 1
#----------------------------------------------
# Agrupa late_shipments por shipment_mode, calcula la media de pack_price de cada grupo 
# y almacena el resultado en xbar_pack_by_mode.

# Calculate the mean pack_price for each shipment_mode
xbar_pack_by_mode = late_shipments.groupby('shipment_mode')['pack_price'].mean()

# Print the grouped means
print(xbar_pack_by_mode)

#-----------------------------------
# Parte 2
#-----------------------------------
# Agrupa late_shipments por shipment_mode, calcula la desviación típica de pack_price de cada grupo 
# y almacena el resultado en s_pack_by_mode.

# Calculate the standard deviation of the pack_price for each shipment_mode
s_pack_by_mode = late_shipments.groupby("shipment_mode")['pack_price'].std()


print('\n\n')

# Print the grouped standard deviations
print(s_pack_by_mode)

#-----------------------------------
# Parte 3
#-----------------------------------
# Crea un diagrama de caja a partir de late_shipments con "pack_price" como x y "shipment_mode" como y

# Boxplot of shipment_mode vs. pack_price
sns.boxplot(x='pack_price', y='shipment_mode', data=late_shipments )
plt.show()

# Conclusion:
# Ciertamente parece haber una diferencia en el precio del paquete entre cada uno de los tres modos de envío. 
# ¿Crees que las diferencias son estadísticamente significativas?