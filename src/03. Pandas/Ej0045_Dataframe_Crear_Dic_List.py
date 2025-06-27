# Diccionario de listas
#
# ¡Acaban de llegar más datos! Esta vez, utilizarás el método del diccionario de listas,
#  analizando los datos columna por columna.

#    date	       small_sold	large_sold
#  "2019-11-17"	    10859987	7674135
#  "2019-12-01"	    9291631	    6238096


import pandas as pd
import matplotlib.pyplot as plt
import os

# Creando un diccionario de listas con nueva data
avocados_dict = {
  "date": ["2019-11-17", "2019-12-01"],
  "small_sold": [10859987, 9291631],
  "large_sold": [7674135, 6238096]
}

# Convirtiendo la lista a DataFrame
avocados_2019 = pd.DataFrame(avocados_dict)

# Print the new DataFrame
print(avocados_2019)