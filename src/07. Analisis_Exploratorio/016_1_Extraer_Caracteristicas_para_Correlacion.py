# Extraer características para la correlación
# 
# En este ejercicio, trabajarás con una versión del conjunto de datos salaries 
# que contiene una nueva columna llamada "date_of_response".
#
# El conjunto de datos se ha leído como un DataFrame de pandas, 
# con "date_of_response" como tipo de datos datetime.
#
# Tu tarea consiste en extraer los atributos fecha-hora de esta columna y, 
# a continuación, crear un mapa de calor para visualizar los coeficientes de correlación entre las variables.

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

# Extrae el mes de "date_of_response", almacenándolo como una columna llamada "month"
salaries["month"] = salaries["date_of_response"].dt.month

# Crea la columna "weekday", que contiene el día de la semana en que los participantes completaron la encuesta.
salaries["weekday"] = salaries['date_of_response'].dt.weekday

# Traza un mapa de calor, incluyendo las puntuaciones del coeficiente de correlación de Pearson.
fig, ax = plt.subplots(figsize=(10, 8))                             # Ajustar el tamano de la venta
sns.heatmap(salaries.corr(numeric_only=True), annot=True, ax=ax)    # Grafico de calor
plt.tight_layout()                                                  # Ajuste automático para evitar cortes
plt.show()


# Conclusion:
# Parece que no hay relaciones significativas entre nuestras variables numéricas, 
# así que veamos si convertir los datos numéricos en clases ofrece información adicional.