# Hacer un gráfico de recuento con un DataFrame
# En este ejercicio, examinaremos las respuestas a una encuesta enviada a los jóvenes. Nuestra pregunta principal aquí es: ¿cuántos jóvenes encuestados afirman tener miedo a las arañas? Se pidió a los participantes en la encuesta que estuvieran de acuerdo o en desacuerdo con la afirmación "Tengo miedo a las arañas". Las respuestas varían de 1 a 5, 
# donde 1 es "Totalmente en desacuerdo" y 5 es "Totalmente de acuerdo".

# Import Matplotlib, pandas, and Seaborn
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import os


# Obtener ruta base del archivo
base_path = os.path.dirname(os.path.abspath(__file__))
ruta_archivo = os.path.join(base_path, "..", "..", "Archivos", "csv_filepath.csv")

# Read in the Netflix CSV as a DataFrame
df = pd.read_csv(ruta_archivo)

#---------------------------------------------

# Create a count plot with "Spiders" on the x-axis
sns.countplot(data=df, x='Spiders')


# Display the plot
plt.show()