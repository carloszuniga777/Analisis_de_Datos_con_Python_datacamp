# Visualizar las relaciones a lo largo del tiempo
# 
# Ahora que tus datos de fecha se guardan como datos DateTime, 
# ¡puedes explorar patrones a lo largo del tiempo! 
# ¿Tiene relación el año en que se casó una pareja con el número de hijos que tiene en el momento del divorcio? 
# ¡Tu tarea es averiguarlo!

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import os

# Obtener ruta base del archivo
base_path = os.path.dirname(os.path.abspath(__file__))
ruta_archivo = os.path.join(base_path, "..", "..", "Archivos", "divorce.csv")

# Importar divorce.csv 
divorce = pd.read_csv(ruta_archivo, parse_dates=['divorce_date', 'dob_man', 'dob_woman', 'marriage_date'])

#-----------------------------------------------------------

# Crear columna de Año de matrimonio
divorce["marriage_year"] = divorce["marriage_date"].dt.year


# Crea un gráfico de líneas que muestre el número medio de hijos que tuvo una pareja durante su matrimonio, 
# ordenado por el año en que la pareja se casó.
sns.lineplot(data=divorce, x='marriage_year', y='num_kids' )

plt.show()


# Conclusion:
# Has descubierto un patrón aquí: parece que las parejas que se casaron en años posteriores
#  también tuvieron menos hijos durante su matrimonio.