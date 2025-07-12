# Cambiar el tamaño de los puntos del diagrama de dispersión
# En este ejercicio, exploraremos el conjunto de datos mpg de Seaborn, que contiene una fila por modelo de coche 
# e incluye información como el año de fabricación del coche, el número de millas por galón ("M.P.G.") que alcanza, 
# la potencia de su motor (medida en "caballos") y su país de origen.
#
# ¿Cuál es la relación entre la potencia del motor de un coche ("horsepower") y su eficiencia de combustible ("mpg")? 
# ¿Y cómo varía esta relación según el número de cilindros ("cylinders") que tenga el coche? Averigüémoslo.

# Import Matplotlib, pandas, and Seaborn
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import os


# Obtener ruta base del archivo
base_path = os.path.dirname(os.path.abspath(__file__))
ruta_archivo = os.path.join(base_path, "..", "..", "Archivos", "mpg.csv")

# Read in the Netflix CSV as a DataFrame
mpg = pd.read_csv(ruta_archivo)

#---------------------------------------------

# Create scatter plot of horsepower vs. mpg
g = sns.relplot(
            kind='scatter',    # Grafico dispesion
            data=mpg,          # dataframe 
            x='horsepower',    # eje x: Potencia de un coche 
            y='mpg',           # eje y: Eficiencia de combustible 
            size='cylinders',  # Tamano puntos: Cylindros 
            hue='cylinders'    # Color 
            )

# 1. Título principal usando el objeto Figure
g.figure.suptitle('Relación entre Potencia del moto (horsepower)\n y su eficiencia de Combustible (mpg)', 
                  fontsize=10, y=0.95) 

# 2. Etiquetas globales para ejes X e Y
g.set_axis_labels("Potencia del coche (horsepower)", "Eficiencia de combustible (mpg)", fontsize=10)


# 3. Reserva espacio para el título superior 
plt.subplots_adjust(top=0.85)  

# Show plot
plt.show()

# Conclusion:
# Los coches con mayor potencia tienden a tener un menor número de millas por galón. 
# También tienden a tener un mayor número de cilindros.