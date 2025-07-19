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
# # Correlación
# La correlación mide la dirección (positiva o negativa) 
# y la fuerza de la relación lineal entre dos variables numéricas. 
# 
# Un coeficiente: 
# cercano a +1 indica una relación directa fuerte; 
# cercano a –1, una relación inversa fuerte; 
# y cerca de 0, ausencia de relación lineal.

# 1. Se utiliza el método .corr() de pandas para obtener la matriz de correlación.
print( divorce.corr(numeric_only=True) )


# 2. Para visualizarla, se recurre a seaborn.heatmap(), 
# que muestra valores y colores según la intensidad de la relación.

sns.heatmap(divorce.corr(numeric_only=True), annot=True)
plt.tight_layout() # Ajuste automático para evitar cortes


# Interpretación de mapas de calor
#  - Colores más intensos (oscuros o muy claros) señalan correlaciones fuertes.
#  - Valores exactos ayudan a distinguir qué pares de variables merecen mayor atención.



#---------------------------------------------------------------
plt.show()
