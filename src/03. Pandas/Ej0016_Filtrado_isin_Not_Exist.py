# Validar continentes
# Tu colega te ha informado de que los datos sobre el desempleo de los países de Oceanía no son fiables, 
# y te gustaría identificar y excluir a estos países de tus datos de unemployment. 
# ¡La función .isin() puede ayudarte con eso!
#
# Tu tarea consiste en utilizar .isin() para identificar los países que no están en Oceanía. 
# Estos países deberían devolver True mientras que los países de Oceanía deberían devolver False. 
# Esto te permitirá utilizar los resultados de .isin() para filtrar rápidamente los países de Oceanía 
# utilizando la indexación booleana.

import pandas as pd
import os

# Obtener ruta base del archivo
base_path = os.path.dirname(os.path.abspath(__file__))
ruta_archivo = os.path.join(base_path, "..", "..", "Archivos", "unemployment.csv")

# Read in the CSV as a DataFrame
unemployment = pd.read_csv(ruta_archivo)

#----------------------------------------------------------------

# Definiendo una serie con todos los paises que no son Oceania, 
# se utiliza el ~ para revertir de true a false, funcionando como un como un 'not in' en SQL
not_oceania = ~unemployment["continent"].isin(["Oceania"])

#imprimir
print(unemployment[not_oceania])