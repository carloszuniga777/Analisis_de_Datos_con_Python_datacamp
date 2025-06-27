# Subconjunto de filas con .query()
# En este ejercicio, volverás a consultar los datos de PIB y población de Australia y Suecia del Banco Mundial 
# y los ampliarás utilizando el método .query(). Fusionarás las dos tablas y calcularás el PIB per cápita. 
# 
# Después, utilizarás el método .query() para subseleccionar las filas y crear un gráfico. 
# Recuerda que tendrás que fusionar varias columnas en el orden adecuado.

import pandas as pd
import matplotlib.pyplot as plt
import os


# Obtener ruta base del archivo
base_path = os.path.dirname(os.path.abspath(__file__))
ruta_archivo_gdp = os.path.join(base_path, "..", "..", "Archivos", "gdp2.csv")
ruta_archivo_pop = os.path.join(base_path, "..", "..", "Archivos", "pop.csv")


# Cargando los archivos CSV
gdp = pd.read_csv(ruta_archivo_gdp)
pop = pd.read_csv(ruta_archivo_pop)


#-------------------------------------------------------------------

# Unir las tablas gpd y pop por merge_ordered y rellenar los valores nulos
gdp_pop = pd.merge_ordered(gdp, pop, on=['country','date'], fill_method='ffill')


# Agregar columna gdp_per_capita
gdp_pop['gdp_per_capita'] = gdp_pop['gdp'] / gdp_pop['pop']

# Realizando Pivot donde el campo valor es gdp_per_capita, el index es date y la columna es country
gdp_pivot = gdp_pop.pivot_table('gdp_per_capita', 'date', 'country')

# Seleccionando las fechas iguales o mayores a 1991-01-01
recent_gdp_pop = gdp_pivot.query('date >= "1991-01-01"')

# Plot recent_gdp_pop
recent_gdp_pop.plot(rot=90)

plt.show()

# Puedes ver en el gráfico que el PIB per cápita de Australia superó al de Suecia en 1992. Al usar el método .query(),
# pudiste seleccionar las filas apropiadas fácilmente. El método .query() es fácil de leer y directo.