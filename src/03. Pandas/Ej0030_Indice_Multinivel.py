# Establecer índices multinivel
#
# Los índices también pueden estar formados por varias columnas, 
# formando un índice multinivel (a veces llamado índice jerárquico). 
# Utilizarlos tiene su contrapartida.
#
# La ventaja es que los índices multinivel facilitan la interpretación a partir 
# de variables categóricas anidadas. 
# 
# Por ejemplo, en un ensayo clínico, puedes tener grupos de control y de tratamiento. 
# Entonces, cada sujeto de prueba pertenece a uno u otro grupo, 
# y podemos decir que un sujeto de prueba está anidado dentro del grupo de tratamiento. 
# 
# Del mismo modo, en el conjunto de datos de temperatura, 
# la ciudad está situada en el país, por lo que podemos decir 
# que una ciudad está anidada dentro del país.
#
# El principal inconveniente es que el código para manipular 
# índices es distinto del código para manipular columnas, 
# por lo que tienes que aprender dos sintaxis 
# y estar al tanto de cómo se representan tus datos.

import pandas as pd
import os


# Obtener ruta base del archivo
base_path = os.path.dirname(os.path.abspath(__file__))
ruta_archivo = os.path.join(base_path, "..", "..", "Archivos", "temperatures.csv")

# Importa el excel sales.csv
temperatures = pd.read_csv(ruta_archivo)

# --------------------------------------------------

# Estableciendo el indice multinivel en Country y city
temperatures_ind = temperatures.set_index(['country', 'city'])

filter = [
            ('Honduras', 'Tegucigalpa'),
            ('Brazil', 'Belo Horizonte')
         ]

# Filtrando por indice: Country y City
result = temperatures_ind.loc[filter]

print(result)