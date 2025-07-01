# Correlación Producto-Momento de Pearson:
#
#  Concepto Fundamental
# El coeficiente de correlación de Pearson (r) mide la relación lineal entre dos variables
# cuantitativas. Es un valor entre -1 y 1 que indica:
#
#   - Dirección: Oscila entre -1 (correlación negativa perfecta) y 
#               1 (positiva perfecta), donde 0 indica ausencia de relación lineal. 
#   - Fuerza: Grado de asociación lineal
#   - Limitaciones: Solo detecta patrones lineales y es sensible a valores atípicos.
#
# Mide cómo se mueven juntas dos variables numéricas (como altura y peso). 
# Si una sube y la otra también, es correlación positiva (+1 es máximo). 
# Si una sube y la otra baja, es negativa (-1 es máximo). 
# Si no hay patrón claro, es cero.

#---------------------------------------------------
#          Grafico de dispersión
#---------------------------------------------------
# Para determinar qué variable va en el eje X y cuál en el eje Y 
# en un diagrama de dispersión, sigue estos principios fundamentales:
#
# 1. Relación causa-efecto (si aplica):
#   - Eje X (variable independiente/explicativa):
#          La variable que potencialmente influye o explica cambios en otra.
#          Ejemplo: Edad, tiempo, dosis de medicamento.
#
#   - Eje Y (variable dependiente/respuesta):
#        La variable que podría ser afectada por la variable del eje X.
#         Ejemplo: Presión arterial, ventas, satisfacción.
#
# 2. Convenciones en tu campo de estudio:
#   - En economía: PIB (X) vs. Desempleo (Y)
#   - En medicina: Dosis (X) vs. Efecto (Y)
#   - En ciencias sociales: Educación (X) vs. Ingresos (Y)

# 3. Pregunta de investigación:
#   - Si tu pregunta es:
#       "¿Cómo afecta la esperanza de vida al nivel de felicidad?"
#        → life_exp (X) y happiness_score (Y)

#   - Si fuera:
#       "¿Cómo afecta la felicidad a la longevidad?"
#       → happiness_score (X) y life_exp (Y)
#-----------------------------------------------------------------


# Ejercicio:
# Relaciones entre variables
# En este capítulo, trabajarás con un conjunto de datos world_happiness que contiene 
# los resultados de 2019 World Happiness Report. El informe puntúa a diferentes países
# en función de lo felices que son sus habitantes. También clasifica a cada país 
# en función de diversos aspectos sociales, como el apoyo social, 
# la libertad, la corrupción y otros. 
# 
# El conjunto de datos también incluye el PIB per cápita y la esperanza de vida de cada país.
# En este ejercicio, examinarás la relación entre la esperanza de vida de un país (life_exp)
# y la puntuación de felicidad (happiness_score) tanto visual como cuantitativamente. 

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
# Crea un diagrama de dispersión de happiness_score frente a life_exp 
# (sin línea de tendencia) utilizando seaborn.



sns.scatterplot(
                data=world_happiness,     # Dataframe
                y='happiness_score',      # Columna Y      
                x='life_exp',             # Columna x  
                alpha=0.7                 # Opcional: Transparencia               
              )

plt.title('Grafico 1:\nRelación entre Esperanza de Vida y Felicidad', fontsize=14)
plt.xlabel('Esperanza de Vida (años)', fontsize=12)
plt.ylabel('Puntuación de Felicidad', fontsize=12)
plt.grid(True, linestyle='--', alpha=0.3)


#--------------------------------------------------------------
# Ejemplo 2: Crea un diagrama de dispersión de happiness_score frente a life_exp 
# con una línea de tendencia lineal. Para ello, utiliza seaborn y establece ci en None.



# Create scatterplot of happiness_score vs life_exp with trendline
sns.lmplot( x='life_exp',           # Columna x  
            y='happiness_score',    # Columna y
            data=world_happiness,   # Dataframe
            ci=None,
            height=6,               # Altura de la figura en pulgadas
            aspect=6/6              # Relación ancho/altura: 10/6 ≈ 1.67 
         )


# Show plot
plt.title('Grafico 2:\nRelación entre Esperanza de Vida y Felicidad', fontsize=14)
plt.xlabel('Esperanza de Vida (años)', fontsize=12)
plt.ylabel('Puntuación de Felicidad', fontsize=12)
plt.grid(True, linestyle='--', alpha=0.3)

# Optimizar espacio y bordes
plt.tight_layout() # Ajuste automático para evitar cortes



#----------------------------------------------------------------
# Calcula la correlación entre life_exp y happiness_score

cor = world_happiness['life_exp'].corr(world_happiness['happiness_score'])

print(cor)

# Este valor indica una fuerte correlación positiva entre las variables.
# Significa que cuando aumenta la esperanza de vida, la puntuación de felicidad tiende a aumentar proporcionalmente 
# en un 78% de los casos, mostrando una relación lineal consistente y significativa.

#-------------------------------------------------------------
plt.show()

# Los diagramas de dispersión con líneas de tendencia son una excelente manera de verificar 
# que una relación entre dos variables es realmente lineal.