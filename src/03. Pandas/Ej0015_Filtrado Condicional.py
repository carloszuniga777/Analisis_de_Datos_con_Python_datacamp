# Filtrado concidiconal:

# Import homelessness data
import pandas as pd
import os

# Obtener ruta base del archivo
base_path = os.path.dirname(os.path.abspath(__file__))
ruta_archivo = os.path.join(base_path, "..", "..", "Archivos", "homelessness.csv")

# Importa el excel homelessness.csv
homelessness = pd.read_csv( ruta_archivo)  

# --------------------------------------------------

#  Filtra homelessness para los casos en los que el número 
#  de family_members sea inferior a 1000 
#  y el region sea "Pacific", asignándolo a fam. Muestra el resultado.

condicion1 = (homelessness['family_members'] < 1000) 
condicion2 = (homelessness['region'] =='Pacific')
fam = homelessness[condicion1 & condicion2]

print(fam)

