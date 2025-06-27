# Unir las tablas por INNER JOIN

import pandas as pd
import matplotlib.pyplot as plt
import os


# Obtener ruta base del archivo
base_path = os.path.dirname(os.path.abspath(__file__))
ruta_archivo_licenses = os.path.join(base_path, "..", "..", "Archivos", "licenses.csv")
ruta_archivo_zip_demo = os.path.join(base_path, "..", "..", "Archivos", "zip_demo.csv")
ruta_archivo_wards = os.path.join(base_path, "..", "..", "Archivos", "wards.csv")

# Importa el excel sales.csv
licenses = pd.read_csv(ruta_archivo_licenses)
zip_demo = pd.read_csv(ruta_archivo_zip_demo)
wards = pd.read_csv(ruta_archivo_wards)
# ------------------------------------------------

# Uniendo las tablas licenses, ward y zip_demo
licenses_zip_ward = (
        licenses.merge(zip_demo, on='zip') 
            	.merge(wards, on='ward')
)


# Print the results by alderman and show median income
print(licenses_zip_ward.groupby('alderman').agg({'income':'median'}))


