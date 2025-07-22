# Explorando con gráficos KDE
# 
# Los gráficos de Estimación de la Densidad del Núcleo (KDE) son una gran alternativa 
# a los histogramas cuando quieres mostrar varias distribuciones en el mismo gráfico.
#
# Supongamos que te interesa la relación entre la duración del matrimonio 
# y el número de hijos que tiene una pareja. Como los valores de la columna 
# num_kids sólo van de uno a cinco, puedes gráficar el KDE de cada valor en el mismo gráfico.
# 
# Recuerda que la columna num_kids de divorce solo muestra los valores N/A de las parejas sin hijos, 
# por lo que solo verás las distribuciones de las parejas divorciadas con al menos un hijo.

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
# 1. Crea un gráfico KDE que muestre marriage_duration en el eje x 
# y una línea de color diferente para cada posible número de hijos que pueda tener una pareja, 
# representada por num_kids

plt.figure(1)

# Grafico KDE
g = sns.kdeplot(
            data=divorce, 
            x='marriage_duration', 
            hue='num_kids', 
            cut=0                  # Evita que el grafico se suavice en los extremos, evitando valores negativos
            )
g.figure.suptitle('Grafico KDE', y=0.95)

#---------------------------------------------------------------
# 2. Actualiza el código del gráfico KDE del paso anterior para que muestre 
# una función de distribución acumulativa para cada número de hijos que tiene una pareja.

plt.figure(2)

g = sns.kdeplot(
            data=divorce, 
            x='marriage_duration', 
            hue='num_kids', 
            cut=0,
            cumulative=True  # Funcion de distribucion acomulativa                 
            )

g.figure.suptitle('Grafico KDE acomulativa', y=0.95)

#---------------------------------------------------------------
plt.show()
