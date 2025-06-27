# Concatenar con claves
# La dirección de la empresa de streaming de música ha acudido a ti 
# y te ha pedido ayuda para analizar las ventas de un trimestre comercial reciente. 
# Les gustaría saber en qué mes del trimestre se registró el total medio de facturas más 
# alto. 
# 
# Se te han proporcionado tres tablas con datos de facturas 
# y Concatena estas tablas en una sola para crear un gráfico del promedio mensual 
# del total de las facturas.
# 
# Equivalente a SQL UNION

import pandas as pd
import matplotlib.pyplot as plt
import os


# Obtener ruta base del archivo
base_path = os.path.dirname(os.path.abspath(__file__))
ruta_archivo_inv_jul = os.path.join(base_path, "..", "..", "Archivos", "inv_jul.csv")
ruta_archivo_inv_aug= os.path.join(base_path, "..", "..", "Archivos", "inv_aug.csv")
ruta_archivo_inv_sep = os.path.join(base_path, "..", "..", "Archivos", "inv_sep.csv")

# Cargando los archivos CSV
inv_jul = pd.read_csv(ruta_archivo_inv_jul)
inv_aug = pd.read_csv(ruta_archivo_inv_aug)
inv_sep       = pd.read_csv(ruta_archivo_inv_sep)
# ------------------------------------------------
# Concatena las tablas y agrega las claves de los meses como indices multiple
inv_jul_thr_sep = pd.concat([inv_jul,inv_aug, inv_sep], 
                            keys=['7Jul','8Aug','9Sep'])

print(inv_jul_thr_sep)

# Agrupa por el primer nivel del indice (mes) y calcula el primedio total de las facturas
# 
# El primer nivel del indice (level=0) es el mes [creado anteriormente por las claves [7Jul','8Aug','9Sep']]
# y el segundo nivel es el indice original de las facturas
avg_inv_by_month = inv_jul_thr_sep.groupby(level=0).agg({'total':'mean'})


# Bar plot of avg_inv_by_month
avg_inv_by_month.plot(kind='bar')
plt.show()