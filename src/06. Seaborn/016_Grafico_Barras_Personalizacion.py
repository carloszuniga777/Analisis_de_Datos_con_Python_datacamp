# Personalizar gráficos de barras
# 
# En este ejercicio, exploraremos datos de alumnos de secundaria. La variable "study_time" registra el tiempo de estudio semanal 
# declarado por cada estudiante como una de las siguientes categorías: "<2 hours", "2 to 5 hours", "5 to 10 hours", o ">10 hours". 
# ¿Los alumnos que declaran estudiar más tienden a obtener mejores notas finales? 
# Comparemos la nota media final entre los alumnos de cada categoría mediante un diagrama de barras.

# Import Matplotlib, pandas, and Seaborn
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import os


# Obtener ruta base del archivo
base_path = os.path.dirname(os.path.abspath(__file__))
ruta_archivo = os.path.join(base_path, "..", "..", "Archivos", "student_data2.csv")

# Read in the student_data CSV as a DataFrame
student_data = pd.read_csv(ruta_archivo)

#---------------------------------------------
# Ejercicio 1:  

# List of categories from lowest to highest
category_order = ["<2 hours", 
                  "2 to 5 hours", 
                  "5 to 10 hours", 
                  ">10 hours"]


# El grafico de barras calcula por defecto la media de cada categoria, 
# es decir, saca un promedio de los datos de esa categoria
# Ejemplo:
# 
# Categoría "<2 hours": (10 + 12) / 2 = 11
# Categoría "2-5 hours": (14 + 16) / 2 = 15
# Categoría ">10 hours": 18 / 1 = 18


# Creando un grafico de barras 
g = sns.catplot(
            kind='bar',                  # Tipo de grafico: barra
            data=student_data,           # Dataframe
            x='study_time',              # Variable categorica
            y='G3',                      # Notas finales
            order=category_order,        # Ordena los datos de las categorias (study_time)
            ci=None,                     # Desactiva los intervalos de confianza   
            #estimator=sum,

             palette=["#3498db", "#e74c3c", "#2ecc71", "#f1c40f"],   # Colores 
             legend=False,                                                    # 👈 Esto elimina la leyenda de los colores
             height=4,                                                        # Altura de la figura en pulgadas
             aspect=1.5,                                                      # Relación ancho/alto (ancho = 6 * 1.5 = 9 pulgadas
            )

# 1. Título principal usando el objeto Figure
g.figure.suptitle('Relación entre horas de estudio y calificaciones finales', fontsize=10, y=0.99) 


# 2. Etiquetas globales para ejes X e Y
g.set_axis_labels( "Tiempo de estudio (Promedio)", "Calificaciones", fontsize=10)


# 3. Ajustar márgenes (top = espacio superior) para que el titulo no superponga al grafico
plt.subplots_adjust(top=0.90)  # 85% del espacio para gráfico + título

# 4. Calcula el máximo valor del eje Y automáticamente
max_valor = student_data.groupby('study_time')['G3'].mean().max()
g.set(ylim=(0, max_valor * 1.15))  # 15% más alto que el valor máximo


# 5. Añadir valores a las barras
for ax in g.axes.flat:
    for bar in ax.patches:
        altura = bar.get_height()
        ax.text(
            bar.get_x() + bar.get_width() / 2,
            altura + 0.1,
            f'{altura:.1f}',
            ha='center',
            va='bottom',
            fontsize=10
        )

#------------------------------------------------------------------
# Show plot
plt.show()

# Conclusion:
# Los estudiantes en nuestra muestra que estudiaron más tienen un promedio de calificaciones ligeramente más alto, 
# pero no es una relación fuerte.