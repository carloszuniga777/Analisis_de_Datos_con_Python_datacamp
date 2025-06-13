# Cargando los datos a pandas desde un archivo cars.csv

import pandas as pd
import os

# Obtener ruta base del archivo
base_path = os.path.dirname(os.path.abspath(__file__))
ruta_archivo = os.path.join(base_path, '..', '..', 'Archivos', 'cars.csv')

#Importa el excel cars.csv 
cars = pd.read_csv(ruta_archivo, index_col = 0)  # index_col: Indica que la primer columna se debe utilizar como etiqueta de fila


#----------Filtracion de datos LOC--------------------

#La siguiente llamada selecciona las cinco primeras filas del DataFrame cars

#Filtrando toda la tabla desde la fila 0 hasta la 4 
rows = cars[0:5]
print(f'\nFiltrando toda la tabla desde la fila 0 hasta la 4:\n\n{rows}\n\n')

# El resultado es otro DataFrame que solo contiene las filas que has especificado.
# Presta atención: solo puedes seleccionar filas mediante corchetes si especificas 
# un segmento, como :4. Además, aquí estás utilizando los índices enteros de las filas,
# ¡no las etiquetas de las filas!

# Acceso a las filas con LOC
row = cars.loc["RU"]  #Filtrando por etiqueta de fila: RUSIA
print(f'\nAcceso a las filas con LOC:\n\n {row}\n\n')

# Acceso a las filas con LOC, en formato lineal usando doble [[]]
row = cars.loc[["RU"]]  #Filtrando por etiqueta de fila: RUSIA
print(f'\nAcceso a las filas con LOC, en formato lineal usando doble [[]]:\n\n {row}\n\n')


# Acceso a multiples filas con LOC
row = cars.loc[["RU", "IN", "US"]]  #Filtrando por etiqueta de fila: RUSIA
print(f'\nAcceso a multiples filas con LOC:\n\n{row}\n\n')


#Filtrando por filas y columas
row = cars.loc[["RU", "IN", "US"], ["country", "drives_right"]]
print(f'\nFiltrando por filas y columas:\n\n {row}\n\n')



#Filtrando por columnas
row = cars.loc[:, ["country", "drives_right"]]        #Selecciona todas las filas de las dos columnas
print(f'\nFiltrando por columnas:\n\n {row}\n\n')

#-------------Indice ILOC-----------------------------

#Obteniendo un registro apartir de un indice
row = cars.iloc[[1]]
print(f'\nObteniendo un registro apartir de un indice:\n\n {row}\n\n')

#Obteniendo varios registro apartir de un indice
row = cars.iloc[[1,2,3]]
print(f'\nObteniendo varios registro apartir de un indice:\n\n {row}\n\n')

#Obteniendo varios registro apartir de un indice y seleccionando las columnas a visualizar
row = cars.iloc[[1,2,3], [0, 1]]
print(f'\nObteniendo varios registro apartir de un indice y seleccionando las columnas a visualizar:\n\n {row}\n\n')

#Filtrando por columnas
row = cars.iloc[:, [0, 1]]
print(f'\nFiltrando por columnas:\n\n {row}\n\n')   #Selecciona todas las filas de las dos columnas