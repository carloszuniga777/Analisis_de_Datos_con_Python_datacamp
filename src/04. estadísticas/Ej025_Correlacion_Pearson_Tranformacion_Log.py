# Transformación de variables
# Cuando las variables tienen distribuciones sesgadas, a menudo requieren una transformación para formar una relación lineal 
# con otra variable, de modo que pueda calcularse la correlación. En este ejercicio realizarás una transformación.

import pandas as pd
from scipy.stats import norm
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import os


# Obtener ruta base del archivo
base_path = os.path.dirname(os.path.abspath(__file__))
ruta_archivo = os.path.join(base_path, "..", "..", "Archivos", "world_happiness.csv")


# Cargando los archivos CSV
world_happiness = pd.read_csv(ruta_archivo)

#-------------------------------------------------------------------
# Ejemplo 1: Grafico de dispercion sin transformacion logaritmica
# 
# Crea un diagrama de dispersión de happiness_score frente a gdp_per_cap y calcula la correlación entre ambos.


plt.figure(1)

# Dibujando la dispercion de happiness_score vs. gdp_per_cap
sns.scatterplot(data=world_happiness, x='gdp_per_cap', y='happiness_score')

# Calculando la correlacion
cor = world_happiness['gdp_per_cap'].corr(world_happiness['happiness_score'])
print(cor)


plt.title('Grafico 1:Relación entre Esperanza de Vida y PBI per capita\n(Sin Tranformacion Logoritmica)', fontsize=12, loc='center', pad=10)
plt.xlabel('PIB per capita', fontsize=12)
plt.ylabel('Esperanza de vida', fontsize=12)
plt.grid(True, linestyle='--', alpha=0.3)
plt.tight_layout()                       # Ajuste automático para evitar cortes

#----------------------------------------------------
# Ejemplo 2:Creando columna de algoritmo de PIB para poder 
# distribuir la relacion de manera lineal


plt.figure(2)


# Creando columna de algoritmo pib, para que los valores sesgado de pbi tengan una distribucion simetrica,
# Y poder convertir el grafico en un distribucion lineal 
world_happiness['log_gdp_per_cap'] = np.log(world_happiness['gdp_per_cap'])

# Dibujando el diagrama de dispercion
sns.scatterplot(data=world_happiness, x='log_gdp_per_cap', y='happiness_score' )


#Calculando la correlacion
cor = world_happiness['log_gdp_per_cap'].corr(world_happiness['happiness_score'])
print(cor)



plt.title('Grafico 2:Relación entre Esperanza de Vida y PBI per capita\n(Con Tranformacion Logoritmica)', fontsize=12, loc='center', pad=10)
plt.xlabel('PIB per capita', fontsize=12)
plt.ylabel('Esperanza de vida', fontsize=12)
plt.grid(True, linestyle='--', alpha=0.3)
plt.tight_layout()                       # Ajuste automático para evitar cortes
#--------------------------------------------------
plt.show()