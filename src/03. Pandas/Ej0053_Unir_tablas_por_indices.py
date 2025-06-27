# Ejercicios de unir dos tablas por sus indices
import pandas as pd
import matplotlib.pyplot as plt
import os


# Obtener ruta base del archivo
base_path = os.path.dirname(os.path.abspath(__file__))
ruta_archivo_sequels = os.path.join(base_path, "..", "..", "Archivos", "sequels.csv")
ruta_archivo_financials = os.path.join(base_path, "..", "..", "Archivos", "financials.csv")

# Importa el excel sales.csv y se establece como indice la columna 'id'
sequels = pd.read_csv(ruta_archivo_sequels, index_col=['id'])
financials = pd.read_csv(ruta_archivo_financials, index_col=['id'])

# ------------------------------------------------

# Uniendo la tabla sequels y financials por sus indices por medio de left join
sequels_fin = sequels.merge(financials, on='id', how='left')

# Cruzando la tabla sequels_fin con sigo misma, por medio de inner join 
# y su indice 'id'

# Cuando las columnas llave son diferentes nombres se usa left_on y right_on 
# para establecer la union, y siempre que se use left_on y right_on, 
# se tiene que especificar right_index o left_index como True en la columna indice 

# En este ejemplo el unico que utiliza indice es la tabla de la derecha 

orig_seq = sequels_fin.merge(sequels_fin,                        # Tabla a cruzar
                             how='inner',                        # Tipo de union: inner join, left join, right join
                             left_on='sequel',                   # Columna que se va a usar para unir de la tabla izquierda 
                             right_on='id', right_index=True,    # Se establece el indice de la tabla derecha para unir
                             suffixes=('_org','_seq')            # Sufijo de las columnas coincidentes en ambas tablas
                             )

orig_seq['diff'] = orig_seq['revenue_seq'] - orig_seq['revenue_org']

# Seleccionando las columnas de interes
titles_diff = orig_seq[['title_org','title_seq','diff']]


print(titles_diff.sort_values('diff', ascending=False).head())