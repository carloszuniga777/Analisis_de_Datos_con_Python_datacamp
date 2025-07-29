# Muestreo sistemático
# Un método de muestreo que evita la aleatoriedad se llama muestreo sistemático. 
# Aquí, eliges filas de la población a intervalos regulares.
#
# Por ejemplo, si el conjunto de datos de población tuviera mil filas y quisieras un tamaño de muestra de cinco, 
# podrías elegir las filas 0, 200, 400, 600 y 800.

import pandas as pd
import os

# Obtener ruta base del archivo
base_path = os.path.dirname(os.path.abspath(__file__))
ruta_archivo = os.path.join(base_path, "..", "..", "Archivos", "attrition_pop.csv")


# Importa el excel
attrition_pop = pd.read_csv( ruta_archivo)  


#-------------------------------------------------

# Configurar el tamano de muestra en 70 registros
sample_size = 70

# Calcula el tamaño de la población a partir de attrition_pop.
pop_size = len(attrition_pop)

# Calcula el intervalo entre las filas a muestrear.
interval = pop_size // sample_size   # Division ( // ): Deja solo el entero de la division y quita la parte fraccionaria

# Muestrea sistemáticamente attrition_pop para obtener las filas de la población en cada interval, 
# empezando por 0; asigna las filas a attrition_sys_samp.
attrition_sys_samp = attrition_pop.iloc[::interval]

# Print the sample
print(attrition_sys_samp)


# Conclusion:
#  El muestreo sistemático evita la aleatoriedad al seleccionar filas a intervalos regulares.

#--------------------------------------------------------------------------
# Muestreo sistemático
# 
# En lugar de sacar al azar cada vez, primero ordenas todos los elementos 
# y luego eliges uno inicial al azar y, a partir de ahí, tomas cada k-ésimo elemento.
#
#
# Ejemplo con canicas:
#   1. Ordenas las canicas en fila (mezcladas).
#   2. Sacas una canica al azar como punto de partida.
#   3. A partir de esa posición, cuentas (por ejemplo) cada décima canica y la tomas para la muestra.
#
# Ventajas
# - Muy sencillo de aplicar con listas largas
# - Asegura una cobertura uniforme a lo largo de toda la población
#
# Limitaciones
# Si hay un patrón repetitivo en la fila (por ejemplo, cada décima canica es del mismo color), 
# puede sesgar el resultado