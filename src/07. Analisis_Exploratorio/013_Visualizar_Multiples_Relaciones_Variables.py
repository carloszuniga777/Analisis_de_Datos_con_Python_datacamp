# Visualizar las relaciones entre múltiples variables
# Seaborn's .pairplot() es excelente para comprender las relaciones entre varias
# o todas las variables de un conjunto de datos, agregando gráficos de dispersión por pares en un solo visual.

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import os

# Obtener ruta base del archivo
base_path = os.path.dirname(os.path.abspath(__file__))
ruta_archivo = os.path.join(base_path, "..", "..", "Archivos", "divorce.csv")

# Importar divorce.csv 
divorce = pd.read_csv(ruta_archivo, parse_dates=['divorce_date', 'dob_man', 'dob_woman', 'marriage_date'])

#-----------------------------------------------------------
# Visualizando múltiples variables:
#   - Con pairplot de seaborn puedes ver gráficos de dispersión entre cada par de variables.
#   - Facilita detectar patrones no lineales, agrupamientos o posibles relaciones espurias.

# Visualizar todas las relaciones del conjunto de datos
g = sns.pairplot(data=divorce)

 
# Visualizando solo las variables de interes
g = sns.pairplot(data=divorce, vars=["income_man", "income_woman", "marriage_duration"])

# Visualizando solo las variables de interes
g = sns.pairplot(data=divorce, vars=["income_woman", "marriage_duration"])

#---------------------------------------------------------------
plt.show()
