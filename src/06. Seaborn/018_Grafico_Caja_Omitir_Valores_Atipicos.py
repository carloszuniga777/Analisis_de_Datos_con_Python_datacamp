# Omitir valores atípicos
# Ahora vamos a utilizar el conjunto de datos student_data para comparar la distribución de las calificaciones finales ("G3")
# entre los estudiantes que tienen acceso a Internet en casa y los que no. 
# 
# Para ello, utilizaremos la variable "internet", que es un indicador binario (sí/no) 
# de si el alumno tiene acceso a Internet en casa.
#
# Dado que Internet puede ser menos accesible en las zonas rurales, 
# añadiremos subgrupos en función de dónde viva el alumno. Para ello, podemos utilizar la variable "location",
# que es un indicador de si un estudiante vive en una localidad urbana ("Urban") o rural ("Rural").

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
# - Utiliza sns.catplot() para crear un gráfico de caja con el DataFrame student_data, 
#   poniendo "internet" en el eje x y "G3" en el eje y.
# - Añade subgrupos para que cada diagrama de caja se coloree en función de "location".
# - No muestres los valores atípicos.


# Create a box plot with subgroups and omit the outliers
g = sns.catplot(
             kind='box',                  # Tipo de grafico: caja
             data=student_data,           # Dataframe
             x='internet',                # Variable categorica
             y='G3',                      # Notas finales
             hue='location',              # Clasifica por localizacion  
             showfliers=False ,           # Desactiva los valores atipicos (Los puntitos que aparecen al inicio/final de la caja)   

             palette=["#3498db", "#e74c3c"],   # Personaliza los Colores 
            )

# 1. Título principal usando el objeto Figure
g.figure.suptitle('Relación entre horas de estudio y calificaciones finales', fontsize=10, y=0.99) 


# 2. Etiquetas globales para ejes X e Y
g.set_axis_labels( "Internet", "Calificaciones", fontsize=10)


# 3. Ajustar márgenes (top = espacio superior) para que el titulo no superponga al grafico
plt.subplots_adjust(top=0.90)  # 85% del espacio para gráfico + título


#------------------------------------------------------------------
# Show plot
plt.show()

#------------------------------------------------------------------

# Conclusion:
# Las calificaciones medianas son bastante similares entre cada grupo, 
# pero la dispersión de la distribución parece mayor entre los estudiantes que tienen acceso a internet.