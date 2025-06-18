# Contar variables categóricas:
# 
# Contar es una forma estupenda de tener una visión general de tus datos 
# y de detectar curiosidades que de otro modo no notarías. 
# 
# En este ejercicio, contarás el número de cada tipo de tienda 
# y el número de cada número de departamento utilizando los DataFrames 
# que creaste en el ejercicio anterior:


import pandas as pd
import os

# Obtener ruta base del archivo
base_path = os.path.dirname(os.path.abspath(__file__))
ruta_archivo = os.path.join(base_path, "..", "..", "Archivos", "sales.csv")

# Importa el excel sales.csv
sales = pd.read_csv( ruta_archivo)  

#--------------------------------------------------

# Elimnar los duplicados combinacion store/type 
store_types = sales.drop_duplicates(subset=['store', 'type'])

# Elimnar los duplicados combinacion store/department 
store_depts = sales.drop_duplicates(subset=['store', 'department'])


#----------------------------------------------------------

# Ejemplo 1:
#Contar el numero de tiendas por cada tipo
store_counts = store_types['type'].value_counts()
#print(store_counts)


# Ejemplo 2:
# 
# Obtener la proporcion de tiendas en cada tipo
# Normalizar sirve para obtener la distribucion porcentual de categorias: 
# Ejemplo: (ej: "¿Qué % de tiendas son de tipo 'A'?").
store_props = store_types['type'].value_counts(normalize=True)
#print(store_props)

#Ejemplo 3
#
# Contar el numero de tiendas de cada departamento 
# y ordenarlo para que los mayores recuentos aparezcan arriba 
dept_counts_sorted = store_depts['department'].value_counts(sort=True)
print(dept_counts_sorted)


#Ejemplo 4
#
# Obtener la proporcion de cada departamento 
# y ordenarlo para que los mayores recuentos aparezcan arriba 
dept_props_sorted = store_depts['department'].value_counts(sort=True, normalize=True)
print(dept_props_sorted)