# Cambiar de estilo y de paleta
# Volvamos a nuestro conjunto de datos que contiene los resultados de una encuesta realizada a jóvenes 
# sobre sus hábitos y preferencias. Hemos proporcionado el código para crear un gráfico de recuento de sus 
# respuestas a la pregunta 
# "¿Con qué frecuencia escuchas los consejos de tus padres?". Ahora vamos a cambiar el estilo 
# y la paleta para que esta trama sea más fácil de interpretar.


# Import Matplotlib, pandas, and Seaborn
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import os


# Obtener ruta base del archivo
base_path = os.path.dirname(os.path.abspath(__file__))
ruta_archivo = os.path.join(base_path, "..", "..", "Archivos", "survey_data3.csv")

# Read in the student_data CSV as a DataFrame
survey_data = pd.read_csv(ruta_archivo)


#---------------------------------------------
# Ejercicio 1:  

# Algunas paletas de colores: https://r02b.github.io/seaborn_palettes/

# Estableciendo el estilo a 'whitegrid'
sns.set_style('whitegrid')

# Creando un gráfico de conteo de las respuestas de la encuesta
category_order = ["Never", "Rarely", "Sometimes", 
                  "Often", "Always"]

g = sns.catplot(
             kind="count", 
             data=survey_data, 
             x="Parents Advice", 
             order=category_order,
             palette="RdBu",            # Aplicando colores
             legend=False,              # 👈 Esto elimina la leyenda de los colores

             height=4,                  # Altura de la figura en pulgadas
             aspect=1.5,  
            )


# 1. Título principal usando el objeto Figure
g.figure.suptitle('¿Con qué frecuencia escuchas los consejos de tus padres?', fontsize=10, y=0.99) 


# 2. Etiquetas globales para ejes X e Y
g.set_axis_labels( "Consejo de los padres", "Cantidad", fontsize=10)


# 3. Ajustar márgenes (top = espacio superior) para que el titulo no superponga al grafico
plt.subplots_adjust(top=0.90)  # 85% del espacio para gráfico + título

# Show plot
plt.show()

# Este estilo y la paleta de colores divergente resaltan mejor la diferencia 
# entre el número de jóvenes que suelen escuchar los consejos de sus padres frente a los que no lo hacen.