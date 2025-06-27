# El melt funciona de manera similar al unpivot de SQL, 
# conviriendo columnas en filas
# 
# Ejercicio:
# 
# Utilizar .melt() para remodelar datos gubernamentales
# 
# La Oficina de Estadísticas Laborales de EEUU (BLS) 
# suele proporcionar series de datos en un formato fácil de leer:
# tiene una columna distinta para cada mes, y cada año es una fila diferente. 
# 
# Desgraciadamente, este amplio formato dificulta el trazado de esta información a lo largo del tiempo. En este ejercicio, reestructurarás una tabla de datos de la tasa de desempleo de EE.UU. de la BLS de forma que puedas graficarla utilizando .melt(). Tendrás que añadir una columna de fecha a la tabla 
# y ordenar por ella para trazar los datos correctamente.


import pandas as pd
import matplotlib.pyplot as plt
import os


# Obtener ruta base del archivo
base_path = os.path.dirname(os.path.abspath(__file__))
ruta_archivo_ur_wide = os.path.join(base_path, "..", "..", "Archivos", "ur_wide.csv")


# Cargando los archivos CSV
ur_wide = pd.read_csv(ruta_archivo_ur_wide)


#-------------------------------------------------------------------

# unpivot everything besides the year column
ur_tall = ur_wide.melt(
                id_vars=['year'],                       # Columnas que no se van a transformar
                #value_vars = ['jan', 'feb', 'mar'],    # (Opcional) Columnas que se van a transformar a filas, si no se especifica, se transforman todas las columnas excepto las id_vars
                var_name='month',                       # Nombre de la nueva columna que contendrá los nombres de las columnas originales
                value_name='unempl_rate'                # Nombre de la nueva columna que contendrá los valores de las columnas originales
    )



# Creando la columna de fecha
ur_tall['date'] = pd.to_datetime(ur_tall['month'] + '-' + ur_tall['year'].astype(str))


# Ordernar de manera ascendente por fecha
ur_sorted = ur_tall.sort_values('date', ascending=True)

# Plot the unempl_rate by date
ur_sorted.plot( x='date', y='unempl_rate')
plt.show()


# El gráfico muestra una disminución constante en la tasa de desempleo con un aumento hacia el final. 
# Este aumento es probablemente el efecto de la pandemia de COVID-19 y su impacto en el cierre de la mayor parte de la economía de EE. UU. 
# En general, los datos a menudo se proporcionan (_especialmente por los gobiernos_) en un formato que es fácilmente leído por las personas pero no por las máquinas. 
# 
# El método .melt() es una herramienta útil para reorganizar los datos en una forma útil.