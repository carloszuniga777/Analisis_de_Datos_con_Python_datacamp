# Cambiar la escala
# 
# En este ejercicio, seguiremos examinando el conjunto de datos que contiene las respuestas de una encuesta a jóvenes. 
# ¿Varía el porcentaje de personas que declaran sentirse solas en función del número de hermanos que tienen? 
# Averigüémoslo utilizando un diagrama de barras, al tiempo que exploramos las cuatro escalas de diagrama 
# diferentes de Seaborn ("contextos").

# Import Matplotlib, pandas, and Seaborn
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import os


# Obtener ruta base del archivo
base_path = os.path.dirname(os.path.abspath(__file__))
ruta_archivo = os.path.join(base_path, "..", "..", "Archivos", "survey_data4.csv")

# Read in the student_data CSV as a DataFrame
survey_data = pd.read_csv(ruta_archivo)


#---------------------------------------------
# Ejercicio 1: Establece la escala ("contexto") en "paper", que es la más pequeña de las opciones de escala.
 
# El contexto cambia la escala de los elementos del grafico y labels

# Cambiando el contexto a paper (Me gusta)
sns.set_context("paper")


g = sns.catplot(  
            data=survey_data, 
            kind="bar",
            x="Number of Siblings", 
            y="Feels Lonely",
         )

# 1. Título principal usando el objeto Figure
g.figure.suptitle('Porcentaje de personas que declaran sentirse solas\n en función del número de hermanos que tienen\n Contexto = paper', fontsize=10, y=0.99) 


# 2. Etiquetas globales para ejes X e Y
g.set_axis_labels( "Numero de hermanos", "Nivel del soledad", fontsize=10)


# 3. Ajustar márgenes (top = espacio superior) para que el titulo no superponga al grafico
plt.subplots_adjust(top=0.90)  # 85% del espacio para gráfico + título

#---------------------------------------------
# Ejercicio 2: Cambia el contexto a "notebook" para aumentar la escala.

# Cambiando el contexto a notebook (EL MEJOR)
sns.set_context("notebook")

g = sns.catplot(  
            data=survey_data, 
            kind="bar",
            x="Number of Siblings", 
            y="Feels Lonely",
         )

# 1. Título principal usando el objeto Figure
g.figure.suptitle('Porcentaje de personas que declaran sentirse solas\n en función del número de hermanos que tienen\n Contexto = notebook', fontsize=10, y=0.99) 


# 2. Etiquetas globales para ejes X e Y
g.set_axis_labels( "Numero de hermanos", "Nivel del soledad", fontsize=10)


# 3. Ajustar márgenes (top = espacio superior) para que el titulo no superponga al grafico
plt.subplots_adjust(top=0.90)  # 85% del espacio para gráfico + título


#---------------------------------------------
# Ejercicio 3: Cambia el contexto a "talk" para aumentar la escala.

# Cambiando el contexto a talk
sns.set_context("talk")

g = sns.catplot(  
            data=survey_data, 
            kind="bar",
            x="Number of Siblings", 
            y="Feels Lonely",
         )

# 1. Título principal usando el objeto Figure
g.figure.suptitle('Porcentaje de personas que declaran sentirse solas\n en función del número de hermanos que tienen\n Contexto = talk', fontsize=10, y=0.99) 


# 2. Etiquetas globales para ejes X e Y
g.set_axis_labels( "Numero de hermanos", "Nivel del soledad", fontsize=10)


# 3. Ajustar márgenes (top = espacio superior) para que el titulo no superponga al grafico
plt.subplots_adjust(top=0.90)  # 85% del espacio para gráfico + título


#---------------------------------------------
# Ejercicio 4: Cambia el contexto a "poster", que es la mayor escala disponible.

# Cambiando el contexto a talk
sns.set_context("poster")

g = sns.catplot(  
            data=survey_data, 
            kind="bar",
            x="Number of Siblings", 
            y="Feels Lonely",
         )

# 1. Título principal usando el objeto Figure
g.figure.suptitle('Porcentaje de personas que declaran sentirse solas\n en función del número de hermanos que tienen\n Contexto = Poster', fontsize=10, y=0.99) 


# 2. Etiquetas globales para ejes X e Y
g.set_axis_labels( "Numero de hermanos", "Nivel del soledad", fontsize=10)


# 3. Ajustar márgenes (top = espacio superior) para que el titulo no superponga al grafico
plt.subplots_adjust(top=0.90)  # 85% del espacio para gráfico + título


#---------------------------------------------
# Show plot
plt.show()

#  Cada nombre de contexto da la sugerencia de Seaborn sobre cuándo usar una escala de gráfico dada 
# (en un artículo, en un cuaderno de iPython, en una charla/presentación o en una sesión de póster).