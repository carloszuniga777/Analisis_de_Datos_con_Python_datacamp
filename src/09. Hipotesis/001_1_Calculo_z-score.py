

import pandas as pd
import numpy as np
import os

# Obtener ruta base del archivo
base_path = os.path.dirname(os.path.abspath(__file__))
ruta_archivo = os.path.join(base_path, "..", "..", "Archivos", "late_shipments.csv")


# Importa el excel
late_shipments = pd.read_csv( ruta_archivo)  

#----------------------------------------------
# Parte 1: Cálculo de la media muestral
#---------------------------------------------
# El conjunto de datos late_shipments contiene datos de cadena de suministro sobre la entrega de suministros médicos.
# Cada fila representa una entrega de una pieza. Las columnas late indican si la pieza se entregó con retraso o no. 
# Un valor "Yes" significa que la pieza se entregó con retraso, y un valor "No" significa que la pieza se entregó a tiempo.
#
# Empezarás tu análisis calculando una estimación puntual (o estadístico), es decir, la proporción de envíos retrasados.


late_prop_samp = (late_shipments['late']=='Yes').mean()

#----------------------------------------
# Parte 2: Cálculo de z-score
#----------------------------------------
# Como las variables tienen intervalos y unidades arbitrarios, debemos estandarizarlos. 
# Por ejemplo, una prueba de hipótesis que diera respuestas diferentes si las variables estuvieran en euros 
# en lugar de en dólares US tendría poco valor. La estandarización lo evita.
#
# Un valor estandarizado de interés en una prueba de hipótesis se denomina z-score. 
# Para calcularlo, necesitas tres números: el estadístico (estimación puntual), el estadístico hipotético 
# y el error típico del estadístico (estimado a partir de la distribución bootstrap).

#----------------------------------------
# 2.1. Generando la distribucion de bootstrap
# En bootstrap tomas una sola muestra inicial de la población (sin reemplazo) 
# y luego generas muchas réplicas re-muestreando con reemplazo sobre esa misma muestra.

late_shipments_sample = late_shipments.sample(n=500, replace=False)

late_shipments_boot_distn = []

for i in range(5000):
    late_shipments_boot_distn.append(
        late_shipments_sample.sample(frac=1, replace=True)['late']
        .map({'Yes': 1, 'No': 0})
        .mean()
    )

#---------------------------
# 2.2 Calculando el z-score

# Hipotetiza que la proporción de envíos retrasados es del 6 %.
late_prop_hyp = 0.06

# Calcula el error típico a partir de la desviación típica de la distribución bootstrap.
std_error = np.std(late_shipments_boot_distn, ddof=1)


# Calcula z-score.
z_score = (late_prop_samp - late_prop_hyp) / std_error


print(z_score)


#----------------------------------------------------
# Conclusion:
# El z-score es una medida estandarizada de la diferencia entre la estadística de la muestra y la estadística hipotetizada.


# ¿Por qué estandarizar?
# Cuando trabajas con datos, las unidades pueden variar: centímetros, dólares, euros, segundos, etc. 
# Si una prueba de hipótesis arrojara conclusiones distintas solo por cambiar de unidad, sería poco fiable. 
# Estandarizar elimina ese problema al transformar todo a una escala común, sin unidades.
#
# En vez de decir "mi estimación está a 0.05 dólares de la hipótesis", decimos: 
# "mi estimación está a 2 errores típicos de distancia" Esto permite comparar resultados de manera justa, 
# independientemente de unidades o escalas.
#
# Qué es un z‑score
# En estadística, el z‑score mide cuántos errores estándar separan tu estimación puntual del valor 
# hipotético bajo la hipótesis nula.
#
# Su fórmula general es:
#
# 𝑧 =   Estimacion puntual − Valor hipotetico
#       -----------------------------------------
#       Error tipico
#
# Estimación puntual → el estadístico calculado con tus datos reales (ej. media muestral, proporción observada).
#
# Valor hipotético → el valor que asumes bajo la hipótesis nula (ej. "la proporción es 0.06").
#
# Error típico (o estándar) → variabilidad esperada del estadístico, estimada aquí con el desvío estándar de la distribución bootstrap.
#
#
#
# Interpretación:
#
# Si z_score ≈ 0 → tu muestra está cerca de la hipótesis nula.
#
# Si |z_score| es grande → hay mayor evidencia de que la hipótesis podría no ser cierta, dependiendo del umbral de significación.