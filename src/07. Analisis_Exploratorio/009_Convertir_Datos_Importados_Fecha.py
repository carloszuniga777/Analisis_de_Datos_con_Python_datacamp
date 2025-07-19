# Importar datos DateTime
# ¡Ahora trabajarás con todo el conjunto de datos del divorcio! 
# Los datos describen los matrimonios mexicanos disueltos entre 2000 y 2015.
# Contiene las fechas de matrimonio y divorcio, el nivel educativo, la fecha de nacimiento, 
# los ingresos de cada miembro de la pareja y la duración del matrimonio, 
# así como el número de hijos que tenía la pareja en el momento del divorcio.
#
# Los nombres de las columnas y los tipos de datos son los siguientes:
#
# divorce_date          object
# dob_man               object
# education_man         object
# income_man           float64
# dob_woman             object
# education_woman       object
# income_woman         float64
# marriage_date         object
# marriage_duration    float64
# num_kids             float64
# 
# ¡Parece que hay mucha información de fecha en estos datos que todavía no son de tipo DateTime! 
# Tu tarea es arreglarlo para que puedas explorar patrones a lo largo del tiempo.

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import os

# Obtener ruta base del archivo
base_path = os.path.dirname(os.path.abspath(__file__))
ruta_archivo = os.path.join(base_path, "..", "..", "Archivos", "divorce.csv")

# Importar divorce.csv y parsear las columnas apropiadas a fechas en el import
divorce = pd.read_csv(ruta_archivo, parse_dates=['divorce_date', 'dob_man', 'dob_woman', 'marriage_date'])

print(divorce.dtypes)
