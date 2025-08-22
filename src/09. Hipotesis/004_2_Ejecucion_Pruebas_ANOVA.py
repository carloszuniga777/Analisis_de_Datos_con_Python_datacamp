# Ejecución de una prueba ANOVA
# 
# Los diagramas de caja hacían que pareciera que la distribución del precio del paquete 
# era diferente para cada uno de los tres modos de envío. Sin embargo, esto no nos decía 
# si el precio medio del paquete era diferente en cada categoría. 
# 
# Para determinarlo, podemos utilizar una prueba ANOVA. Las hipótesis nula 
# y alternativa pueden escribirse como se indica a continuación.
#
# H0: los precios de los paquetes para cada categoría de modo de envío son los mismos.
#
# HA: los precios de los paquetes para algunas categorías de modo de envío son diferentes.

# Utiliza un nivel de significación de 0,1.

import pandas as pd
import pingouin
import os

# Obtener ruta base del archivo
base_path = os.path.dirname(os.path.abspath(__file__))
ruta_archivo = os.path.join(base_path, "..", "..", "Archivos", "late_shipments.csv")


# Importa el excel
late_shipments = pd.read_csv( ruta_archivo)  


#----------------------------------------------
# Parte 1
#----------------------------------------------
# Ejecuta ANOVA en late_shipments investigando 'pack_price' (la variable dependiente) entre los grupos de 'shipment_mode'.

# Run an ANOVA for pack_price across shipment_mode
anova_results = pingouin.anova(data=late_shipments, 
                                dv='pack_price',
                                between='shipment_mode')



# Print anova_results
print(anova_results)  # p-unc=>  5.089479e-10  ==> 0.0000000005089

alpha = 0.1

if (anova_results['p-unc'][0] < alpha):
    print('Rechazar H0')
else:
    print('No rechazar H0')

# Pregunta
# Suponiendo un nivel de significación de 0,1, ¿deberías rechazar la hipótesis nula 
# de que no hay diferencia en los precios de los paquetes entre los modos de envío?
#
# Sí. El valor p es menor o igual que el nivel de significación, por lo que debe rechazarse la hipótesis nula.


# Conclusion:
# Hay una diferencia significativa en los precios de los paquetes entre los modos de envío. 
# Sin embargo, no sabemos a qué modos de envío se aplica esto.