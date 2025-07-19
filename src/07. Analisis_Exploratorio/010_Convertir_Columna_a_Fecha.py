# Actualizar tipo de datos a DateTime
# 
# Ahora se te ha cargado el DataFrame divorce, pero una columna se almacena como una cadena 
# que debería ser un dato DateTime. ¿Cuál es? Una vez que hayas identificado la columna, 
# la actualizarás para que puedas explorarla más de cerca en el siguiente ejercicio.

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import os

# Obtener ruta base del archivo
base_path = os.path.dirname(os.path.abspath(__file__))
ruta_archivo = os.path.join(base_path, "..", "..", "Archivos", "divorce.csv")

# Importar divorce.csv y parsear las columnas apropiadas a fechas en el import
divorce = pd.read_csv(ruta_archivo)

#-----------------------------------------------------------
# Convierte la columna marriage_date del DataFrame divorce en valores de DateTime.

divorce["marriage_date"] = pd.to_datetime(divorce['marriage_date'], errors='coerce')

print(divorce.dtypes)
