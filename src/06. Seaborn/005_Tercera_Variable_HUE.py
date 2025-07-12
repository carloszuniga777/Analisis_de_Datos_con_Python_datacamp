# Gráficos de tono y dispersión
# En el vídeo anterior, aprendimos cómo hue nos permite hacer fácilmente subgrupos dentro de los gráficos Seaborn. 
# Vamos a probarlo explorando los datos de los alumnos de secundaria. Tenemos mucha información sobre cada alumno, 
# como su edad, dónde vive, sus hábitos de estudio y sus actividades extraescolares.
#
# Por ahora, nos fijaremos en la relación entre el número de faltas que tienen en la escuela y su calificación final en el curso, 
# segmentada por el lugar donde vive el alumno (zona rural frente a zona urbana).

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
# Ejemplo 1: Crear un grafico de dispercion de ausencias vs nota final

plt.figure(1)

sns.scatterplot(data=student_data,
                x='absences',       # Eje X: Número de ausencias (absences).
                y='G3',             # Eje Y: Nota final (G3, probablemente una calificación académica).
                hue='location'      # Color: Ubicación del estudiante | hue: se utiliza para diferenciar grupos de datos mediante colores según una variable categórica.
                )



plt.title('Relacion entre el numero de faltas vs calificacion final', fontsize=12, loc='center', pad=10)
plt.xlabel('Ausencias', fontsize=12)
plt.ylabel('Notas', fontsize=12)
plt.tight_layout()                       # Ajuste automático para evitar cortes


#---------------------------------------------------------------------
# Ejemplo 2: Haz que "Rural" aparezca antes que "Urban" en la leyenda del gráfico.

plt.figure(2)

palette_colors = {"Rural": "green", "Urban": "red"}

# Change the legend order in the scatter plot
sns.scatterplot(data=student_data,
                x="absences",                 # Eje X: Número de ausencias (absences).
                y="G3",                       # Eje Y: Nota final (G3, probablemente una calificación académica). 
                hue="location",               # Color: Ubicación del estudiante                   
                hue_order=['Rural', 'Urban'],  # Orden de la leyenda
                palette=palette_colors         # Paleta de colores 
                )

#----------------------------------------------------------------

plt.title('Relacion entre el numero de faltas vs calificacion final', fontsize=12, loc='center', pad=10)
plt.xlabel('Ausencias', fontsize=12)
plt.ylabel('Notas', fontsize=12)
plt.tight_layout()                       # Ajuste automático para evitar cortes


# Show plot
plt.show()

#-----------------------------------------------------------
# Calculando la correlacion

correlacion = student_data['absences'].corr(student_data['G3'])
print(correlacion)

# Conclusion:
# - Los estudiantes urbanos muestran, en promedio, un mejor desempeño (menos faltas, mejores notas) que los rurales.
# - Parece que los estudiantes con más ausencias tienden a tener calificaciones más bajas tanto en áreas rurales como urbanas.