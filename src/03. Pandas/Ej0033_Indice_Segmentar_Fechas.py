# Cortar series temporales
# La segmentación es especialmente útil para las series temporales, 
# ya que es habitual querer filtrar los datos dentro de un intervalo de fechas. 
# 
# Añade la columna date al índice y utiliza .loc[] para realizar el subconjunto. 
# Lo importante es recordar que debes mantener tus fechas en formato ISO 8601, 
# es decir, "yyyy-mm-dd" para año-mes-día, "yyyy-mm" para año-mes y "yyyy" para año.

# Recuerda del Capítulo 1 que puedes combinar varias condiciones booleanas utilizando operadores lógicos,
#  como &. Para hacerlo en una línea de código, tendrás que añadir paréntesis () alrededor de cada condición.

import pandas as pd
import os


# Obtener ruta base del archivo
base_path = os.path.dirname(os.path.abspath(__file__))
ruta_archivo = os.path.join(base_path, "..", "..", "Archivos", "temperatures.csv")

# Importa el excel sales.csv
temperatures = pd.read_csv(ruta_archivo)

# --------------------------------------------------

#Ejemplo 1

# Filtrando fechas utilizando condicones boleanas
temperatures_bool = temperatures[(temperatures['date'] >= '2010-01-01') & (temperatures['date'] <= '2011-12-31')]

print(temperatures_bool)

#-----------------------------------------------------

# Configurando temperatures_ind para que el indice sea Date y ordernarlo
temperatures_ind = temperatures.set_index('date').sort_index()

#------------------------------------------------------
#Ejemplo 2

# Obtener fechas desde el 2010 hasta 2011
print( temperatures_ind.loc['2010':'2011'] )

#------------------------------------------------------
# Ejemplo 3

# Obtener fechas desde agosto 2010 hasta febrero 2011
print( temperatures_ind.loc['2010-08':'2011-02'] )