# Tabulación cruzada
# La tabulación cruzada puede ayudar a identificar cómo se combinan las observaciones.
#
# Utilizando el conjunto de datos salaries, que se ha importado como un DataFrame pandas, 
# realizarás una tabulación cruzada de múltiples variables, incluyendo el uso de la agregación, 
# para ver la relación entre "Company_Size" y otras variables.

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import os

# Obtener ruta base del archivo
base_path = os.path.dirname(os.path.abspath(__file__))
ruta_archivo = os.path.join(base_path, "..", "..", "Archivos", "salaries.csv")

# Importar csv 
salaries = pd.read_csv(ruta_archivo)

#-----------------------------------------------------------
# Ejercicio 1:
# Realiza una tabulación cruzada, estableciendo "Company_Size" como índice, y las columnas a las clases en "Experience".

# Crosstab: Realiza un conteo por variables de dos o mas variables categoricas, parecido a un pivot 

# Cross-tabulate Company_Size and Experience
print(f'\n {
       pd.crosstab(salaries["Company_Size"], salaries["Experience"]) 
}')


#--------------------------------------------------------------
# Ejercicio 2:
# Cruza "Job_Category" y las clases de "Company_Size" como nombres de columna.


# Cross-tabulate Job_Category and Company_Size
print(f'\n {
    pd.crosstab(salaries["Job_Category"], salaries["Company_Size"])
}')

#--------------------------------------------------------------------
# Ejercicio 3:
# Actualiza pd.crosstab() para que devuelva los valores medios de "Salary_USD".

# Calculando el salario medio por categoria y por empresa
print(f'\n {
    pd.crosstab(salaries["Job_Category"], salaries["Company_Size"],
                values=salaries["Salary_USD"], aggfunc="mean") 
}')

#-------------------------------------------------------------------


# ¿Qué hace pd.crosstab??
# 
# La función pd.crosstab() crea una tabla de contingencia que muestra la frecuencia (o recuento) 
# de las observaciones combinadas de dos (o más) variables categóricas.
#
# Por defecto, cuenta cuántas veces aparece cada par de valores entre el índice (primera variable) 
# y las columnas (segunda variable).
#
# Se puede extender para agregar valores (por ejemplo, promedios, sumas) 
# o normalizar (convertir a proporciones) usando parámetros como values=, aggfunc= o normalize=.
#
#
# Por ejemplo:
#
# Company_Size	EN	EX	MI	SE
#      L	    24	7	49	44
#      M	    25	9	58	136
#      S	    18	1	21	15
# 
# 
# - Las filas (L, M, S) representan el tamaño de la empresa (Large, Medium, Small).
#
# - Las columnas (EN, EX, MI, SE) representan niveles de experiencia (Entry, Executive, Mid, Senior).
#
# - Cada celda indica cuántos encuestados de un tamaño de empresa específico tienen ese nivel de experiencia.


# Conclusion:
# Esta es una función útil para examinar la combinación de frecuencias, 
# así como para encontrar estadísticas agregadas. 
# ¡Parece que el salario medio más alto es para roles de datos gerenciales en grandes empresas!