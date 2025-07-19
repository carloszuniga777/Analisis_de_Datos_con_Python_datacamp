# Rango de validación
# Ahora es el momento de validar nuestros datos numéricos. 
# En la lección anterior vimos, utilizando .describe(), que la mayor tasa de desempleo durante 2021 fue de casi el 34 %, 
# mientras que la más baja estuvo justo por encima de cero.
#
# Tu tarea en este ejercicio es obtener información mucho más detallada sobre el rango de los datos 
# de unemployment utilizando el diagrama de caja de Seaborn, y también visualizarás el rango de las 
# tasas de desempleo en cada continente para comprender las diferencias de rango geográfico.

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

# Imprimir el valor maximo y minimo durante 2021
print(unemployment['2021'].min(), unemployment['2021'].max())


# Create a boxplot of 2021 unemployment rates, broken down by continent
g = sns.boxplot(data=unemployment, x='2021', y='continent')

# 1. Título principal usando el objeto Figure
g.figure.suptitle('Desempleo en 2021', fontsize=10, y=0.99) 

# 2. Titulo de los ejes
g.set(xlabel='2021', ylabel='Continentes')

plt.show()

# Conclusion
#  Observa cómo varían los rangos de desempleo entre continentes. Por ejemplo, el percentil 50 de África es más bajo 
# que el de América del Norte, pero el rango es mucho más amplio.