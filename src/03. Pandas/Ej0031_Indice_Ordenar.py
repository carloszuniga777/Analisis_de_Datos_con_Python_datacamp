# Ordenar por valores índice
# Antes, cambiabas el orden de las filas de un DataFrame llamando a .sort_values(). 
# También es útil poder ordenar por elementos del índice. 
# Para ello, tienes que utilizar .sort_index().
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

#---------------------------------------------
# Ejemplo 1

# Ordena el indice ascendente
result1 = temperatures_ind.sort_index()

print(result1)

print('\n\n')

#---------------------------------------
#  Ejemplo 2

# Ordena el indice city ascedente
result2 = temperatures_ind.sort_index( level = 'city')

print(result2)


print('\n\n')

#----------------------------------------------

#Ordena el indice country ascendente y el city como descendente
result3 = temperatures_ind.sort_index(level= ['country', 'city'], ascending=(True, False))

print(result3)