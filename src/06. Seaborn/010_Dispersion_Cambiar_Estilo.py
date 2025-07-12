# Cambiar el estilo de los puntos del gráfico de dispersión
# Sigamos explorando el conjunto de datos mpg de Seaborn observando la relación entre la velocidad 
# a la que puede acelerar un coche ("acceleration") y su eficiencia de combustible ("mpg"). 
# ¿Varían estas propiedades según el país de origen ("origin")?
#
# Observa que la variable "acceleration" es el tiempo de aceleración de 0 a 60 millas por hora, en segundos. 
# Los valores más altos indican una aceleración más lenta.


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

# Create a scatter plot of acceleration vs. mpg
g = sns.relplot(
            kind='scatter',    # Grafico dispesion
            data=mpg,          # dataframe 
            x='acceleration',  # eje x: Aceleracion 
            y='mpg',           # eje y: Eficiencia de combustible 
            hue='origin',       # Color 
            style='origin'     # Estilos 
            )

# 1. Título principal usando el objeto Figure
g.figure.suptitle('Relación entre la velocidad a la se puede acelerar (acceleration)\n y su eficiencia de Combustible (mpg)', 
                  fontsize=10, y=0.95) 

# 2. Etiquetas globales para ejes X e Y
g.set_axis_labels("Aceleracion (acceleration)", "Eficiencia de combustible (mpg)", fontsize=10)


# 3. Reserva espacio para el título superior 
plt.subplots_adjust(top=0.85)  

# Show plot
plt.show()

# # Conclusion:
#  Los coches de EE. UU. tienden a acelerar más rápido y obtener menos millas por galón 
# en comparación con los coches de Europa y Japón