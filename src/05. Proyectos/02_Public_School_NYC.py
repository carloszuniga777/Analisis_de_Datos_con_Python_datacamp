# Importing pandas and matplotlib
import pandas as pd
import os


# Obtener ruta base del archivo
base_path = os.path.dirname(os.path.abspath(__file__))
ruta_archivo = os.path.join(base_path, "..", "..", "Archivos", "schools.csv")

# Read in the Schools CSV as a DataFrame
schools = pd.read_csv(ruta_archivo)

# Preview the data
schools.head()

# Start coding here...
# Add as many cells as you like...

# --------1. Obteniendo las escuelas de NYC con mejores resultados en Matematicas ----------

# 1. Filtrar y seleccionar columnas relevantes
best_math_schools = (
        schools.loc[
                    schools['average_math'] >= 640, 
                    ['school_name', 'average_math']
        ]
)

# 2. Ordenar por promedio de matemáticas en orden descendente
best_math_schools = best_math_schools.sort_values('average_math', ascending = False)

print(best_math_schools)
print('\n\n')
#----------------2. Obteniendo las 10 mejores escuelas segun el SAT combinado-------------------


# 1. Se crea una columna y se calcula el SAT (Sumatoria de promedio de matematicas, lectura y escritura)
schools['total_SAT'] = schools['average_math'] + schools['average_reading'] + schools['average_writing']

# 2. Se ordena dataframe en descendente y se trae los primeros 10 registros
top_10_schools = (
    schools.sort_values('total_SAT', ascending=False)  # 1. Ordena por total_SAT descendente
    .loc[:, ['school_name', 'total_SAT']]              # 2. Selecciona solo las columnas requeridas
    .head(10)                                          # 3. Toma las 10 primeras filas
)

print(top_10_schools)
print('\n\n')
#--------3. Obteniendo el distrito con mayor desviacion estandar en puntaje SAT combinado---------


distros_std = (
    schools.groupby('borough', as_index=False)
    .agg(
        num_schools =('school_name', 'count'),   # Cuenta escuelas por distrito
        average_SAT =('total_SAT', 'mean'),      # Promedio de SAT por distrito
        std_SAT =('total_SAT', 'std')            # Desviación estándar por distrito
    )
    .round(2)  # Redondeo a 2 decimales
)

std_mayor = distros_std['std_SAT'].max()

largest_std_dev = distros_std[distros_std['std_SAT'] == std_mayor]

print(largest_std_dev)