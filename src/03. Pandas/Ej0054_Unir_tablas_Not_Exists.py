# Realizar una antiunión
# En nuestro conjunto de datos de empresas de streaming de música, 
# a cada cliente se le asigna un empleado representante para que le asista. 
# 
# En este ejercicio, filtra la tabla de empleados por una tabla de clientes principales, 
# devolviendo sólo aquellos empleados que no estén asignados a ningún cliente. 
# 
# Los resultados deben parecerse a los de una antiunión. 
# La dirección de la empresa asignará a estos empleados formación adicional 
# para que puedan trabajar con clientes muy valorados.
#
# Equivalente a not exists en SQL

import pandas as pd
import matplotlib.pyplot as plt
import os


# Obtener ruta base del archivo
base_path = os.path.dirname(os.path.abspath(__file__))
ruta_archivo_employees = os.path.join(base_path, "..", "..", "Archivos", "employees.csv")
ruta_archivo_top_cust = os.path.join(base_path, "..", "..", "Archivos", "top_cust.csv")

# Cargando los archivos CSV
employees = pd.read_csv(ruta_archivo_employees)
top_cust = pd.read_csv(ruta_archivo_top_cust)

# ------------------------------------------------
# Uniendo las tablas employees y top_cust por left join 
# y colocando el indicador a true para identificar las registros coincidentes y no coincidentes 
empl_cust = employees.merge(top_cust, 
                             on='srid', 
                             how='left', 
                             indicator=True)

# Seleccionar los registros que estan en employees pero no en top_cust (left_only)
srid_list = empl_cust.loc[empl_cust['_merge'] == 'left_only', 'srid']

# Obteniendo los empleados que no estan asignado a ningun cliente
print(employees[employees['srid'].isin(srid_list)])