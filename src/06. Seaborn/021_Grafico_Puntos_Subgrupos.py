# Gráficos de puntos con subgrupos
# Sigamos explorando el conjunto de datos de los alumnos de secundaria. 
# Esta vez, formularemos la pregunta: ¿estar en una relación romántica está asociado a una mayor o menor asistencia a la escuela? 
# ¿Y difiere esta asociación en función de la escuela a la que asisten los alumnos? Averigüémoslo mediante un gráfico de puntos.



# Import Matplotlib, pandas, and Seaborn
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from numpy import median
import os


# Obtener ruta base del archivo
base_path = os.path.dirname(os.path.abspath(__file__))
ruta_archivo = os.path.join(base_path, "..", "..", "Archivos", "student_data2.csv")

# Read in the student_data CSV as a DataFrame
student_data = pd.read_csv(ruta_archivo)

#---------------------------------------------
# Ejercicio 1:  

# Graficos de puntos
# - Los graficos de puntos muestarn la media de una variable cuantitativa
# - Las líneas verticales representan intervalos de confianza del 95%


# Mediana:
# Como puede haber valores atípicos de alumnos con muchas ausencias, 
# utiliza la función median que hemos importado de numpy para mostrar la mediana del número de ausencias en lugar de la media.


# Crea un grafico de puntos que relaciona los estidiantes que estan en relacion romantica vs las ausencias por escuela
g = sns.catplot(
             kind='point',                # Tipo de grafico: puntos
             data=student_data,           # Dataframe
             x='romantic',                # Variable categorica
             y='absences',                # Variable Cuantitativa
             hue="school",                # Clasifica por escuela  
             ci=None,                      # Desactiva por intervalos de confianza  
             estimator=median             # Se calcula la mediana para mayor precision. Debido a los valores atipicos de la media  
            )

# 1. Título principal usando el objeto Figure
g.figure.suptitle('Relación entre relacion romantica de los alumnos\n y el numero de faltas por escuela', fontsize=10, y=0.99) 


# 2. Etiquetas globales para ejes X e Y
g.set_axis_labels( "Relacion romantica", "Numero de ausencias", fontsize=10)


# 3. Ajustar márgenes (top = espacio superior) para que el titulo no superponga al grafico
plt.subplots_adjust(top=0.90)  # 85% del espacio para gráfico + título

# Show plot
plt.show()

#-----------------------------------------------------------------
# Conclusion Curso:
# ¡Buen trabajo! Parece que los estudiantes en relaciones románticas tienen un promedio 
# y una mediana más altos de ausencias en la escuela GP, pero esta asociación no se mantiene para la escuela MS.
 
