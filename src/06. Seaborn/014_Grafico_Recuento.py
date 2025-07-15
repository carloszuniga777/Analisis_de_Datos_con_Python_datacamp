# Gráficos de recuento
# En este ejercicio, volveremos a explorar nuestro conjunto de datos que contiene las respuestas a una encuesta enviada a los jóvenes.
# Podríamos sospechar que los jóvenes pasan mucho tiempo en Internet, pero ¿cuánto declaran utilizar Internet al día? 
# Utilicemos un gráfico de recuento para desglosar el número de respuestas de la encuesta en cada categoría 
# y luego exploremos si cambia en función de la edad.
#
# Como recordatorio, para crear un gráfico de recuento, utilizaremos la función catplot() 
# y especificaremos el nombre de la variable categórica a contar (x=____), 
# el DataFrame de pandas a utilizar (data=____), y el tipo de gráfico (kind="count").

# Import Matplotlib, pandas, and Seaborn
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import os


# Obtener ruta base del archivo
base_path = os.path.dirname(os.path.abspath(__file__))
ruta_archivo = os.path.join(base_path, "..", "..", "Archivos", "survey_data.csv")

# Read in the survey_data CSV as a DataFrame
survey_data = pd.read_csv(ruta_archivo)

#---------------------------------------------
# Ejercicio 1:  
# Utiliza sns.catplot() para crear un gráfico de recuento utilizando el DataFrame survey_data con "Internet usage" en el eje x.


# Create count plot of internet usage
g = sns.catplot(
            kind='count',                # Tipo de grafico: Recuento
            data=survey_data,            # Dataframe
            x='Internet usage',          # Variable categorica

            height=4,                    # Altura de la figura en pulgadas
            aspect=1.5                   # Relación ancho/alto (ancho = 6 * 1.5 = 9 pulgadas
            )


# 1. Título principal usando el objeto Figure
g.figure.suptitle('Grafico de recuento', fontsize=10, y=0.95) 


# 2. Etiquetas globales para ejes X e Y
g.set_axis_labels("Uso de Internet", "Cantidad", fontsize=10)

# 3. Rotar etiquetas 45° y ajustar alineación
g.set_xticklabels(rotation=45, ha='right', fontsize=8)  # ha='right' para mejor alineación


# Ajustar espacio inferior para evitar cortes
plt.subplots_adjust(bottom=0.32)  # Aumenta este valor si aún hay corte

#------------------------------------------------------------------
# Ejercicio 2: 
# Haz que las barras sean horizontales en lugar de verticales.


# Create count plot of internet usage
g = sns.catplot(
            kind='count',                # Tipo de grafico: Recuento
            data=survey_data,            # Dataframe
            y='Internet usage',          # Variable categorica

            height=4,                    # Altura de la figura en pulgadas
            aspect=1.5                   # Relación ancho/alto (ancho = 6 * 1.5 = 9 pulgadas
            )


# 1. Título principal usando el objeto Figure
g.figure.suptitle('Grafico de recuento vertical', fontsize=10, y=0.99) 


# 2. Etiquetas globales para ejes X e Y
g.set_axis_labels( "Cantidad", "Uso de Internet", fontsize=10)


# 3. Ajustar márgenes (top = espacio superior) para que el titulo no superponga al grafico
plt.subplots_adjust(top=0.85)  # 85% del espacio para gráfico + título

# 4. Ajustar el tamano de las categorias del eje y
g.set_yticklabels(fontsize=8)  

#------------------------------------------------------------------
# Ejercicio 3:
# Separa este gráfico en dos subtramas de columnas contiguas en función de "Age Category",
# que separa a los encuestados en menores de 21 años y mayores de 21 años. A partir de 21 años.


# Create count plot of internet usage
g = sns.catplot(
            kind='count',                # Tipo de grafico: Recuento
            data=survey_data,            # Dataframe
            y='Internet usage',          # Variable categorica
            col='Age Category',          # Separa los graficos en dos categorias (Los menores de 18 anos y mayores de 18 anos)   

            height=4,                    # Altura de la figura en pulgadas
            aspect=1.5                   # Relación ancho/alto (ancho = 6 * 1.5 = 9 pulgadas
            )


# 1. Título principal usando el objeto Figure
g.figure.suptitle('Grafico de recuento por categoria', fontsize=10, y=0.99) 


# 2. Etiquetas globales para ejes X e Y
g.set_axis_labels( "Cantidad", "Uso de Internet", fontsize=10)


# 3. Ajustar márgenes (top = espacio superior) para que el titulo no superponga al grafico
plt.subplots_adjust(top=0.85)  # 85% del espacio para gráfico + título

# 4. Ajustar el tamano de las categorias del eje y
g.set_yticklabels(fontsize=8)  



#------------------------------------------------------------------
# Show plot
plt.show()

# Conclusion:
# Parece que la mayoría de los jóvenes usan internet durante unas pocas horas todos los días, 
# independientemente de su edad.