# Ordenar filas:

# Encontrar datos interesantes en un DataFrame suele ser más fácil
# si cambias el orden de las filas. Puedes ordenar las filas pasando
# un nombre de columna a .sort_values().

# En los casos en que las filas tengan el mismo valor
# (esto es habitual si ordenas sobre una variable categórica),
# puedes romper los empates ordenando sobre otra columna.
# Puedes ordenar varias columnas de esta forma pasando una lista de nombres de columnas.

# Ordenar en …	   |    Sintaxis
# -----------------------------------------------------------
# una columna	   |    df.sort_values("breed")
# varias columnas  |   df.sort_values(["breed", "weight_kg"])
#
#
# Combinando .sort_values() con .head() puedes responder a preguntas del tipo:
# "¿Cuáles son los principales casos en los que…?".

# Import homelessness data
import pandas as pd
import os

# Obtener ruta base del archivo
base_path = os.path.dirname(os.path.abspath(__file__))
ruta_archivo = os.path.join(base_path, "..", "..", "Archivos", "homelessness.csv")

# Importa el excel homelessness.csv
homelessness = pd.read_csv( ruta_archivo)  

# --------------------------------------------------

# Ordenando homelessness por el numero de personas sin hogar, de menor a mayor
homelessness_ind = homelessness.sort_values("individuals")

print(homelessness.head())

# ---------------------------------------

# Ordenando homelessness por el número de family_members sin hogar en orden descendente
homelessness_fam = homelessness.sort_values('family_members', ascending=False)

print(homelessness_fam.head())

#------------------------------------

# Ordenando homelessness, primero por región (ascendente) 
# y luego por número de miembros de la familia (descendente) 
homelessness_reg_fam = homelessness.sort_values( ['region', 'family_members'], 
                                                 ascending=(True, False)
                                                )

print(homelessness_reg_fam.head())
