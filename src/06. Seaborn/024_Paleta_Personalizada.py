# Utilizar una paleta personalizada
# Hasta ahora, hemos analizado varias cosas en el conjunto de datos de las respuestas a las encuestas de los jóvenes, 
# como el uso que hacen de Internet, la frecuencia con que escuchan a sus padres y cuántos de ellos dicen sentirse solos. 
# 
# Sin embargo, algo que no hemos hecho es un resumen básico del tipo de personas que responden a esta encuesta, 
# incluyendo su edad y género. Proporcionar estos resúmenes básicos es siempre una buena práctica cuando se trata 
# de un conjunto de datos desconocido.
#
# El código proporcionado creará un diagrama de cajas que mostrará la distribución de edades de los encuestados 
# masculinos frente a los femeninos. 
# 
# Vamos a ajustar el código para personalizar la apariencia, esta vez utilizando una paleta de colores personalizada.

# Import Matplotlib, pandas, and Seaborn
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import os


# Obtener ruta base del archivo
base_path = os.path.dirname(os.path.abspath(__file__))
ruta_archivo = os.path.join(base_path, "..", "..", "Archivos", "survey_data6.csv")

# Read in the student_data CSV as a DataFrame
survey_data = pd.read_csv(ruta_archivo)


#---------------------------------------------
# Ejercicio 1:  

# Configurando el estilo a "darkgrid"
sns.set_style('darkgrid')

# Configurando la paleta personalzida de colores
custom_palette = ["#39A7D0","#36ADA4"]


# Create the box plot of age distribution by gender
g = sns.catplot(
            kind="box",
            data=survey_data,
            x="Gender", 
            y="Age",  
            palette=custom_palette,            # Aplicando colores
            legend=False,      
           )



# 1. Título principal usando el objeto Figure
g.figure.suptitle('Resumen personas que realizan esta encuesta', fontsize=10, y=0.99) 


# 2. Etiquetas globales para ejes X e Y
g.set_axis_labels( "Genero", "Edad", fontsize=10)


# 3. Ajustar márgenes (top = espacio superior) para que el titulo no superponga al grafico
plt.subplots_adjust(top=0.90)  # 85% del espacio para gráfico + título

# Show plot
plt.show()

# Conclusion:
# Parece que la edad media es la misma para hombres y mujeres, 
# pero la distribución de las mujeres se inclina hacia edades más jóvenes que la de los hombres.