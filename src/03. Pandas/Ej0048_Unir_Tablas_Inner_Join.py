# Unir las tablas por INNER JOIN

import pandas as pd
import matplotlib.pyplot as plt
import os


# Obtener ruta base del archivo
base_path = os.path.dirname(os.path.abspath(__file__))
ruta_archivo_licenses = os.path.join(base_path, "..", "..", "Archivos", "licenses.csv")
ruta_archivo_biz_owners = os.path.join(base_path, "..", "..", "Archivos", "biz_owners.csv")

# Importa el excel sales.csv
licenses = pd.read_csv(ruta_archivo_licenses)
biz_owners = pd.read_csv(ruta_archivo_biz_owners)
# ------------------------------------------------

# Unir las tablas licenses y biz_owners 
licenses_owners = licenses.merge(biz_owners, on='account')

# Agrupe los resultados por título y luego cuente el número de cuentas
counted_df = licenses_owners.groupby('title').agg({'account':'count'})

# Ordenar el counted_df en orden descendente
sorted_df = counted_df.sort_values( 'account', ascending=False)


print(sorted_df.head())
