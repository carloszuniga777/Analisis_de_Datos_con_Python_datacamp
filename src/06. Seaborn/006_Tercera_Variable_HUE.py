# Gráficos de tono y recuento
# Sigamos explorando nuestro conjunto de datos de alumnos de secundaria examinando una nueva variable. 
# La columna "school" indica las iniciales de la escuela a la que asistió el alumno: "GP" o "MS".

# En el último ejercicio, creamos un gráfico de dispersión en el que los puntos del gráfico se coloreaban
# en función de si el alumno vivía en una zona urbana o rural. ¿Cuántos alumnos viven en zonas urbanas frente a zonas rurales, 
# y varía esto en función de la escuela a la que asiste el alumno? Hagamos un gráfico de recuento con subgrupos para averiguarlo.

# Import Matplotlib, pandas, and Seaborn
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import os


# Obtener ruta base del archivo
base_path = os.path.dirname(os.path.abspath(__file__))
ruta_archivo = os.path.join(base_path, "..", "..", "Archivos", "student_data.csv")

# Read in the Netflix CSV as a DataFrame
student_data = pd.read_csv(ruta_archivo)

#---------------------------------------------

# Rellena el diccionario palette_colors para asignar el valor de ubicación "Rural" al color "green" 
# y el valor de ubicación "Urban" al color "blue".
palette_colors = {"Rural": "green", "Urban": "blue"}


# Crea un gráfico de recuento con "school" en el eje x utilizando el DataFrame student_data.
# 
# Añade subgrupos al gráfico utilizando la variable "location" 
# y utiliza el diccionario palette_colors para que los subgrupos de ubicación sean verdes y azules.

sns.countplot(data=student_data,
              x='school',
              hue='location',
              palette=palette_colors)



plt.title('Recuento entre numeros de alumnos en zonas urbanas vs zonas rurales', fontsize=10, loc='center', pad=10)
plt.xlabel('Escuelas', fontsize=12)
plt.ylabel('Cantidad', fontsize=12)
plt.tight_layout()     


# Display plot
plt.show()

# Conclusion:
# Los estudiantes en GP tienden a venir de una ubicación urbana, pero los estudiantes en MS están más equitativamente divididos. 