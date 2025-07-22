import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import os

# Obtener ruta base del archivo
base_path = os.path.dirname(os.path.abspath(__file__))
ruta_archivo = os.path.join(base_path, "..", "..", "Archivos", "salaries.csv")

# Importar csv 
salaries = pd.read_csv(ruta_archivo, parse_dates=['date_of_response'])

#-----------------------------------------------------------
# Parte 1.
# Cálculo de los percentiles salariales
# 
# En el vídeo, has visto que la conversión de datos numéricos en categorías 
# a veces facilita la identificación de patrones.
#
# Tu tarea consiste en convertir la columna "Salary_USD" en categorías basadas en sus percentiles. 
# Primero, tienes que encontrar los percentiles y almacenarlos como variables.


# Encuentra el percentile 25th 
twenty_fifth = salaries["Salary_USD"].quantile(0.25)

# Encuentra la media
salaries_median = salaries["Salary_USD"].median()

# Encuentra el percentile 75th 
seventy_fifth = salaries['Salary_USD'].quantile(0.75)

#-----------------------------------------------------------
# Parte 2
# Categorizar los salarios:
# 
# Ahora es el momento de crear una nueva categoría! Utilizarás las variables 
# twenty_fifth, salaries_median, y seventy_fifth, que creaste en el ejercicio anterior, 
# para dividir los salarios en diferentes etiquetas.
#
# El resultado será una nueva columna llamada "salary_level", que incorporarás a una visualización 
# para analizar el salario de los encuestados y en empresas de distintos tamaños.

# Etiquetas:
# Crea salary_labels, una lista que contenga "entry", "mid", "senior", y "exec".
salary_labels = ['entry', 'mid', 'senior', 'exec']


# Lista de rango de salarios:
# Termina salary_ranges, añadiendo el percentil 25, la mediana, el percentil 75 y el valor más grande de "Salary_USD".
salary_ranges = [0, twenty_fifth, salaries_median, seventy_fifth, salaries["Salary_USD"].max()]


# Creando columna salary_level
salaries["salary_level"] = pd.cut(
                                  salaries["Salary_USD"],       # Columna a categorizar
                                  bins=salary_ranges,           # Rangos
                                  labels=salary_labels          # Etiqueta
                                  )

# Visualizar el recuento de Company_Size, factorizando las etiquetas de nivel salarial
sns.countplot(data=salaries, x="Company_Size", hue="salary_level")
plt.show()


# Conclusion:
# Al usar pd.cut() para dividir los datos numéricos en categorías, 
# puedes ver que una gran proporción de trabajadores en empresas pequeñas reciben salarios de nivel "entrada", 
# mientras que más personal en empresas medianas son recompensados con salarios de nivel "senior". 
# ¡Ahora vamos a ver cómo generar hipótesis a medida que llegas al final de la fase de EDA!