# merge_asof() es un Left join (inteligente) a diferencia del merge normal, 
# este permite unir dos tablas por sus llaves (generalmente fechas o valores numericos)
# que no requieren una coincidencia exacta, busca el valor mas cercano para cada fila de la tabla izquierda,
# encuentra el valor en la tabla derecha que es menor o igual al valor de la tabla izquierda.
#
#
#
# # Por ejemplo, si unimos dos tablas cuya llave es una fecha y hora

# Tabla A                                           Tabla B                 Valor                                           
# 2025-01-01 00:00:01                                 2025-01-01 00:00:01      A                                            
# 2025-01-01 00:00:10                                 2025-01-01 00:00:18      B    👈 *Coincidencia más cercana*       
# 2025-01-01 00:00:20   👈 Busca coincidencia         2025-01-01 00:00:30      C 

# Tabla Resultado           Valor
# 2025-01-01 00:00:01         A
# 2025-01-01 00:00:20         B

# Toma el valor B porque es el mas cercano a 2025-01-01 00:00:20  

# Reglas clave:
#
# Orden obligatorio: Las tablas deben estar ordenadas por la clave de unión.
# Dirección por defecto: Busca valores anteriores (direction='backward'). Puedes cambiarlo a:
#   'forward': El siguiente valor mayor.
#   'nearest': El valor más cercano (anterior o posterior).


# ¿Por qué es útil?
# Datos de sensores: Unir mediciones tomadas en tiempos ligeramente distintos.
# Transacciones financieras: Relacionar operaciones con cotizaciones más recientes.
# Eventos en tiempo real: Vincular registros de sistemas con desfases temporales.

# ----------------------------------------------------------------------------
# Ejercicio: 
# Utilizar merge_asof() para estudiar las cotizaciones
# Tienes un feed de cotizaciones bursátiles que estás registrando, 
# Intenta seguir el precio cada cinco minutos. 
# Sin embargo, debido a la latencia de la red, los precios que obtienes 
# son solo aproximadamente cada cinco minutos. 
# 
# Sacas los registros de precios de tres bancos: 
# JP Morgan (JPM), Wells Fargo (WFC) y Bank Of America (BAC). 
# 
# Quieres saber cómo se compara el cambio de precio de los otros 
# dos bancos con JP Morgan. Por lo tanto, tendrás que fusionar 
# estos tres registros en una sola tabla. 
# 
# Después, utilizarás el método pandas .diff() para calcular 
# la variación del precio a lo largo del tiempo. 
# 
# Por último, traza los cambios de precio para poder revisar tu análisis.


import pandas as pd
import matplotlib.pyplot as plt
import os


# Obtener ruta base del archivo
base_path = os.path.dirname(os.path.abspath(__file__))
ruta_archivo_jpm = os.path.join(base_path, "..", "..", "Archivos", "jpm.csv")
ruta_archivo_wells= os.path.join(base_path, "..", "..", "Archivos", "wells.csv")
ruta_archivo_bac= os.path.join(base_path, "..", "..", "Archivos", "bac.csv")

# Cargando los archivos CSV
jpm = pd.read_csv(ruta_archivo_jpm)
wells = pd.read_csv(ruta_archivo_wells)
bac = pd.read_csv(ruta_archivo_bac)

# # ------------------------------------------------
# Formtenado la columna de fecha y hora
jpm['date_time'] = pd.to_datetime(jpm['date_time'], format='%d/%m/%Y %H:%M', errors='coerce')
wells['date_time'] = pd.to_datetime(wells['date_time'], format='%d/%m/%Y %H:%M', errors='coerce')
bac['date_time'] = pd.to_datetime(bac['date_time'], format='%d/%m/%Y %H:%M', errors='coerce')

#-------------------------------------------------------------------

# Uniendo las tablas jpm y wells utilizando merge_asof(), y lo une por el valor mas cercano de la columna 'date_time'
jpm_wells = pd.merge_asof(jpm, wells, on='date_time', suffixes=('', '_wells'), direction='nearest')


# Uniendo la tabla resultante jpm_wells con bac utilizando merge_asof(), y lo une por el valor mas cercano de la columna 'date_time'
jpm_wells_bac = pd.merge_asof(jpm_wells, bac, on='date_time', suffixes=('_jpm', '_bac'), direction='nearest')


# Diff calcula la diferencia entre el precio actual y el anterior, en una serie de datos
# Esto permite ver como ha cambiado el precio a lo largo del tiempo
#
# formula: valor_actual - valor_anterior
price_diffs = jpm_wells_bac.diff()


# Dibuja un grafico de lineas para visualizar los cambios de precio, 
# en panda el grafico de lineas esta por defecto, por lo que no es necesario especificarlo
price_diffs.plot(
                 y=['close_jpm', 'close_wells', 'close_bac'],   # Columnas a graficar
                 title='Cambios Diarios en Precios de Bancos', 
                 ylabel='Cambio de Precio ($)',
                 xlabel='Fecha y hora',
                 #grid=True,                          # Lineas de la cuadricula   
                 figsize=(12, 6)                     # Tamano del grafico       
                 ).axhline(0, color='gray', ls='--') # Línea de referencia en cero


plt.show()



# ¿Qué muestra el gráfico?
#  El gráfico visualizará los cambios diarios en los precios de las acciones de los tres bancos:
#   -Picos positivos: Días con fuertes alzas
#   -Valles negativos: Días con fuertes caídas
#   -Cerca de cero: Días con poca variación

#  Interpretación práctica
# - Análisis de volatilidad: Muestra qué banco tuvo mayores movimientos diarios
# - Correlación: Permite ver si los bancos se mueven en la misma dirección
# - Eventos específicos: Picos pronunciados pueden indicar noticias o eventos del mercado

# Puedes ver que durante este período, el cambio de precio de estas acciones bancarias fue aproximadamente el mismo, 
# aunque el cambio de precio de _JP Morgan_ fue más variable. 
# 
# El punto crítico aquí es que la función merge_asof() es muy útil para realizar la coincidencia difusa 
# entre las marcas de tiempo de todas las tablas