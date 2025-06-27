# Lista de diccionarios
#
#  Recientemente has obtenido nuevos datos de aguacates de 2019 que te gustaría 
#  introducir en un DataFrame utilizando el método de lista de diccionarios. 
#  Recuerda que con este método, recorres los datos fila a fila.

#    date	       small_sold	    large_sold
# "2019-11-03"	    10376832	    7835071
# "2019-11-10"	    10717154	    8561348


import pandas as pd
import matplotlib.pyplot as plt
import os

# Creando una lista de diccionarios con nueva data
avocados_list = [
    {"date": "2019-11-03", "small_sold": 10376832, "large_sold": 7835071},
    {"date": "2019-11-10", "small_sold": 10717154, "large_sold": 8561348},
]

# Convirtiendo la lista a DataFrame
avocados_2019 = pd.DataFrame(avocados_list)

# Print the new DataFrame
print(avocados_2019)