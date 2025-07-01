# ¿Qué no puede medir la correlación?
# Aunque el coeficiente de correlación es una forma cómoda de cuantificar la fuerza 
# de una relación entre dos variables, dista mucho de ser perfecto. 
# 
# En este ejercicio, explorarás una de las advertencias del coeficiente de correlación 
# al examinar la relación entre el PIB per cápita de un país (gdp_per_cap) 
# y la puntuación de felicidad.

import pandas as pd
from scipy.stats import norm
import matplotlib.pyplot as plt
import seaborn as sns
import os


# Obtener ruta base del archivo
base_path = os.path.dirname(os.path.abspath(__file__))
ruta_archivo = os.path.join(base_path, "..", "..", "Archivos", "world_happiness.csv")


# Cargando los archivos CSV
world_happiness = pd.read_csv(ruta_archivo)

#-------------------------------------------------------------------
# Ejemplo 1: 
# Crea un diagrama de dispersión seaborn (sin línea de tendencia) 
# que muestre la relación entre gdp_per_cap (en el eje X) y life_exp (en el eje Y).



sns.scatterplot( data=world_happiness,
                x='gdp_per_cap',
                y='life_exp'
                )

plt.title('Grafico 1:\nRelación entre Esperanza de Vida y PBI per capita', fontsize=14)
plt.xlabel('PIB per capita', fontsize=12)
plt.ylabel('Esperanza de vida', fontsize=12)
plt.grid(True, linestyle='--', alpha=0.3)



# Calcula la correlación entre gdp_per_cap y life_exp
cor = world_happiness['gdp_per_cap'].corr(world_happiness['life_exp'])

print(f'La correlacion entre esperanza de vida y PIB per capita es: {cor}')

plt.show()

# ¿Por qué la correlación no es la mejor forma de medir la relación entre estas dos variables?
# Respuesta: La correlación solo mide las relaciones lineales.

# El coeficiente de correlación no puede dar cuenta de ninguna relación que no sea lineal, 
# independientemente de su fuerza.