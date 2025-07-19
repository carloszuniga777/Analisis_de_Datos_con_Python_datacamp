# Duración del vuelo
# Te gustaría analizar la duración de los vuelos, pero por desgracia, 
# la columna "Duration" del DataFrame planes contiene actualmente valores de cadena.
#
# Tendrás que limpiar la columna y convertirla al tipo de datos correcto para el análisis. 


import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import os

# Obtener ruta base del archivo
base_path = os.path.dirname(os.path.abspath(__file__))
ruta_archivo = os.path.join(base_path, "..", "..", "Archivos", "planes2.csv")

# Read in the CSV as a DataFrame
planes = pd.read_csv(ruta_archivo)

#----------------------------------------------------------------

# 1. Previsualizar la columna: Es de tipo objeto y necesitamos convertirlo a numerico
print(planes["Duration"].head(20))

# 2.Extrayendo las horas (26h 35m) y convertilo enformato ENTERO (26): 
# 
# debido a que extract() devuelve NaN cuando no encuentra alguna coincidencias no puede convertirlo a entero
# por lo que se rellena los valores nan en 0 y luego aplica conversion a la columna a entero 
planes['Duration'] = pd.to_numeric( 
    planes['Duration'].str.extract(r'(\d+)h')[0],
    errors='coerce'
).fillna(0).astype(int)

# 2.1 Otra manera es convirtiendo directamente a Float
# Usando float si funciona correctamete, ya que soporta valores NaN para probarlo 
# Comentar la conversion a entero
# Asi:
# planes['Duration'] =  planes['Duration'].str.extract(r'(\d+)h').astype(float)


# 2.2  El ejercicio orginal usaba replace h porque los datos venian asi ( 26h ) y no asi (26h 35m) 
# Asi:
# planes["Duration"] = planes["Duration"].str.replace("h", "").astype(float)



# 3. Plot a histogram
sns.catplot( kind='count', 
             data=planes, 
             x='Duration',  
             height=6,      # Altura en pulgadas
             aspect=2.5     # Relación ancho/alto (2.5 = 2.5 veces más ancho))
            ) 

# Otra forma de graficar   
#sns.countplot(data=planes, x='Duration')

plt.tight_layout()

plt.show()