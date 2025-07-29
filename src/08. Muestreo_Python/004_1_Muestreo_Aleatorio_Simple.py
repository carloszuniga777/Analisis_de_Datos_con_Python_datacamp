# Muestreo aleatorio simple
# 
# El método más sencillo de muestreo de una población es el que ya has visto. Se conoce como muestreo aleatorio simple 
# (a veces abreviado como "SRS") y consiste en elegir filas al azar, de una en una, donde cada fila tiene la misma probabilidad 
# de ser elegida que cualquier otra.
#
# En este capítulo, aplicarás métodos de muestreo a un conjunto de datos sintético (ficticio) de bajas de empleados de IBM, 
# donde "bajas" en este contexto significa abandonar la empresa.

import pandas as pd
import os

# Obtener ruta base del archivo
base_path = os.path.dirname(os.path.abspath(__file__))
ruta_archivo = os.path.join(base_path, "..", "..", "Archivos", "attrition_pop.csv")


# Importa el excel
attrition_pop = pd.read_csv( ruta_archivo)  


#-------------------------------------------------
# Sample 70 rows using simple random sampling and set the seed
attrition_samp = attrition_pop.sample(
                                      n=70, 
                                      random_state=18900217  # Seed: Para que se pueda replicar la muestra en otros ambientes
                                      )

# Print the sample
print(attrition_samp)


# Conclusion:
# Observa cómo los índices en la muestra no siempre están en orden ascendente. Son simplemente aleatorios.


#---------------------------------------------------------------------
# Muestreo aleatorio simple
# 
# Consiste en elegir objetos completamente al azar, de manera que cada uno tenga la misma oportunidad de ser seleccionado.
#
# Ejemplo con canicas:
#
#   - Mezclas bien la caja.
#   - Cierras los ojos y sacas 30 canicas.
#   - Con esas 30 estimas la proporción de colores en toda la caja.
#
# Ventajas
#   - Fácil de entender
#   - No introduce sesgos si realmente cada elemento se elige al azar
#
# Limitaciones
#   - Difícil si la caja es muy grande y no puedes mezclar bien
#   - Puede que, por azar, no salgan bien representados algunos colores