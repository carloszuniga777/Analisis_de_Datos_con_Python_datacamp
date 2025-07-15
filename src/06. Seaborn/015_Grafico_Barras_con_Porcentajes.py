# Diagramas de barras con porcentajes
# Sigamos explorando las respuestas a una encuesta enviada a los jóvenes. 
# La variable "Interested in Math" es True si la persona declaró estar interesada o muy interesada en las matemáticas, 
# y False en caso contrario. 
# 
# ¿Qué porcentaje de jóvenes afirma estar interesado en las matemáticas, y varía esto en función del género? 
# Utilicemos un diagrama de barras para averiguarlo.
#
# Como recordatorio, crearemos un gráfico de barras utilizando la función catplot(), 
# proporcionando el nombre de la variable categórica a poner en el eje x (x=____), 
# el nombre de la variable cuantitativa a resumir en el eje y (y=____), 
# el DataFrame de pandas a utilizar (data=____), y el tipo de gráfico categórico (kind="bar").

# Import Matplotlib, pandas, and Seaborn
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import os


# Obtener ruta base del archivo
base_path = os.path.dirname(os.path.abspath(__file__))
ruta_archivo = os.path.join(base_path, "..", "..", "Archivos", "survey_data2.csv")

# Read in the survey_data CSV as a DataFrame
survey_data = pd.read_csv(ruta_archivo)

#---------------------------------------------
# Ejercicio 1:  
# Utiliza sns.catplot() para crear un gráfico de recuento utilizando el DataFrame survey_data con "Internet usage" en el eje x.

# Creando un grafico de barras 
g = sns.catplot(
            kind='bar',                  # Tipo de grafico: barra
            data=survey_data,            # Dataframe
            x='Gender',                  # Variable categorica
            y='Interested in Math',      # El eje Y muestra la PROPORCIÓN (promedio) de respuestas "True" por categoría.
            
             palette=["#1f77b4", "#ff7f0e"],   # Colores para Male y Female (azul y naranja)
             legend=False,                         # 👈 Esto elimina la leyenda de los colores
             height=4,                             # Altura de la figura en pulgadas
             aspect=1.5,                           # Relación ancho/alto (ancho = 6 * 1.5 = 9 pulgadas
            )

#  Agregar título y etiquetas
g.set(
    title='Interés en Matemáticas por Género',
    ylabel='Proporción de Interesados (Porcentaje)',
    xlabel= 'Genero' 
)

# Ajustar espacio inferior para evitar cortes
plt.subplots_adjust(top=0.85)  # Aumenta este valor si aún hay corte


#------------------------------------------------------------------
# Show plot
plt.show()

# Conclusion:
