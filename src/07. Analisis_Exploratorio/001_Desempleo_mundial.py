# Desempleo mundial en 2021
# ¡Es hora de explorar algunos de los datos numéricos en unemployment! 
# ¿Cuál fue el desempleo típico en un año determinado? 
# ¿Cuál era la tasa de desempleo mínima y máxima, y cómo era la distribución de las tasas de desempleo en el mundo? 
# Un histograma es una buena forma de hacerse una idea de las respuestas a estas preguntas.
#
# Tu tarea en este ejercicio es crear un histograma que muestre la distribución de las tasas de paro mundiales en 2021.

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os

# Obtener ruta base del archivo
base_path = os.path.dirname(os.path.abspath(__file__))
ruta_archivo = os.path.join(base_path, "..", "..", "Archivos", "unemployment.csv")

# Read in the CSV as a DataFrame
unemployment = pd.read_csv(ruta_archivo)

#----------------------------------------------------------------

# Create a histogram of 2021 unemployment; show a full percent in each bin
g = sns.histplot(data=unemployment, x='2021', binwidth=1)


# 1. Título principal usando el objeto Figure
g.figure.suptitle('Desempleo en 2021', fontsize=10, y=0.99) 

# 2. Titulo de los ejes
g.set(xlabel='2021', ylabel='Cantidad')

plt.show()

# Conclusion
# parece que el desempleo en 2021 se mantuvo alrededor del 3% al 8% para la mayoría de los países en el conjunto de datos, 
# pero algunos países experimentaron un desempleo muy alto del 20% al 35%.