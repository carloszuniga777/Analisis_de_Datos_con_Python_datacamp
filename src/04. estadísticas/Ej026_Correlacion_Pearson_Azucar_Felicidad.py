# ¿El azúcar aumenta la felicidad?
# Se ha añadido una nueva columna a world_happiness llamada grams_sugar_per_day, 
# que contiene la cantidad media de azúcar ingerida por persona y día en cada país. 
# 
# En este ejercicio, examinarás el efecto del consumo medio de azúcar de un país en su puntuación de felicidad.
import pandas as pd
from scipy.stats import norm
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import os


# Obtener ruta base del archivo
base_path = os.path.dirname(os.path.abspath(__file__))
ruta_archivo = os.path.join(base_path, "..", "..", "Archivos", "world_happiness2.csv")


# Cargando los archivos CSV
world_happiness = pd.read_csv(ruta_archivo)

#-------------------------------------------------------------------
# Ejemplo 1: Crea un diagrama de dispersión seaborn que muestre la relación entre
# grams_sugar_per_day (en el eje X) y happiness_score (en el eje Y).


plt.figure(1)

# Dibujando la dispercion de happiness_score vs. gdp_per_cap
sns.scatterplot(data=world_happiness, x='grams_sugar_per_day', y='happiness_score')


# Calculando la correlacion
cor = world_happiness['happiness_score'].corr(world_happiness['grams_sugar_per_day'])
print(cor)


plt.title('Grafico: Corelación entre el Azucar y la Felicidad', fontsize=12, loc='center', pad=10)
plt.xlabel('Gramos de Azucar por dia', fontsize=12)
plt.ylabel('Felicidad', fontsize=12)
plt.grid(True, linestyle='--', alpha=0.3)
plt.tight_layout()                       # Ajuste automático para evitar cortes


plt.show()

#  ¿qué afirmación sobre el consumo de azúcar y las puntuaciones de felicidad es cierta?
#   Un mayor consumo de azúcar se asocia a una mayor puntuación de felicidad.

# Si la correlación siempre implicara que una cosa causa otra, la gente podría hacer cosas sin sentido, 
# como comer más azúcar para ser más feliz.