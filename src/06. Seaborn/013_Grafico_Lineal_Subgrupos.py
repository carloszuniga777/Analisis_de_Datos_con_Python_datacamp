# Trazar subgrupos en gráficos de líneas
# 
# Sigamos examinando el conjunto de datos mpg. Hemos visto que la media de millas por galón de los coches 
# ha aumentado con el tiempo, pero ¿cómo ha cambiado la media de caballos de los coches con el tiempo? 
# ¿Y difiere esta tendencia según el país de origen?

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


# Add markers and make each line have the same style
g = sns.relplot(
            kind="line",        # Tipo de gráfico: línea (muestra tendencias a lo largo del tiempo)
            data=mpg,           # Tipo de gráfico: línea (muestra tendencias a lo largo del tiempo)
            x="model_year",     # Eje X: año del modelo del vehículo (temporal)
            y="horsepower",     # Eje Y: caballos de fuerza (potencia del motor)
            ci=None,            # Desactiva intervalos de confianza/sombreado (no muestra variabilidad)
            style="origin",     # Estilo de línea diferente para cada categoría de 'origin' (procedencia)
            hue="origin",       # Color diferente para cada categoría de 'origin' (distinción por color)
            markers=True,       # Muestra marcadores en los puntos de datos (mejor identificación)
            dashes=False        # Todas las líneas son continuas (sin patrones de guiones)
            )

# 1. Título principal usando el objeto Figure
g.figure.suptitle('Distribución Millas por galon alcanzadas de los coches\n a lo largo del tiempo', 
                  fontsize=10, y=0.95) 

# 2. Etiquetas globales para ejes X e Y
g.set_axis_labels("Tiempo (model_year)", "Eficiencia de combustible (mpg)", fontsize=10)


# 3. Reserva espacio para el título superior 
plt.subplots_adjust(top=0.85)  

# Show plot
plt.show()

#------------------------------------------------------
# # Conclusion:
# Ahora que hemos añadido subgrupos, podemos ver que esta tendencia a la baja en la potencia 
# fue más pronunciada entre los coches de EE.UU.