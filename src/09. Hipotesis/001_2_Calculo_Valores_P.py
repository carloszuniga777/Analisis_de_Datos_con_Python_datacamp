
# Cálculo de valores p
# 
# Para determinar si debes elegir la hipótesis nula o la hipótesis alternativa, 
# debes calcular un valor p a partir de z-score.
#
# Ahora volverás al conjunto de datos de envíos retrasados y a la proporción de envíos retrasados.
#
# La hipótesis nula, Ho, es que la proporción de envíos retrasados es del 6 %.
#
# La hipótesis alternativa, Ha, es que la proporción de envíos retrasados es superior al 6 %.

import pandas as pd
import numpy as np
from scipy.stats import norm
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

# Hipotetiza que la proporción de envíos retrasados es del 6 %. (H0 - Hipotesis nula)
late_prop_hyp = 0.06

# Calcula el error típico a partir de la desviación típica de la distribución bootstrap.
std_error = np.std(late_shipments_boot_distn, ddof=1)


# Calcula z-score.
z_score = (late_prop_samp - late_prop_hyp) / std_error


#-----------------------------
# Parte 3: Calculando p_value
#-----------------------------

# Como la prueba es de cola derecha, el p‑value se obtiene como:
# p_value = 1 - norm.cdf(z)
# porque norm.cdf(z) da el área a la izquierda y tú quieres el área en la cola superior.

p_value = 1 - norm.cdf(z_score, loc=0, scale=1)

print(p_value) # ~ 0.4637224809357491

#-----------------------------------------------
# Planteamiento del problema
#
# - H₀ (hipótesis nula): la proporción de envíos retrasados es 6 %.
# - Hₐ (hipótesis alternativa): la proporción es mayor al 6 %. 
#   Esto significa que es una prueba de cola derecha (buscas valores altos de la proporción).

# Interpretar el p‑value:
#   - Si p_value ≤ nivel de significancia (por ejemplo, α = 0.05), hay suficiente evidencia para rechazar H₀ 
#     y concluir que la proporción es mayor al 6 %.
#   
# - Si p_value > α, no rechazas H₀; no hay evidencia estadística fuerte 
#     para decir que la proporción supera el 6 %.

# Resultado
#  p‑value ~ 0.4637224809357491 --> con α = 0.05
#
#  0.4637224809357491 > 0.05; la muestra sugiere que la proporcion real retrazos es 6%;
#  Por tanto, no rechazo H0


#-------------------------------------
# α
#
# Ese valor de α = 0.05 no viene explícitamente del ejercicio que tienes en pantalla; 
# lo usé como ejemplo típico para ilustrar cómo se interpreta un valor p en la práctica.
#
# En la mayoría de cursos y manuales de estadística:
#   - Se suele adoptar 0.05 (5 %) como nivel de significancia por defecto.
#   - Esto significa que estás dispuesto a aceptar un 5 % de probabilidad de cometer un error tipo I (rechazar H₀ cuando en realidad es verdadera).
#   - No es una “ley”: en entornos médicos, por ejemplo, a veces se usa 0.01; en exploratorios, incluso 0.10.
#
# En tu ejercicio, si el curso no te da un α específico, deberías:
#   - Usar el que indiquen en la clase o instrucciones.
#   - Si no lo indican, podrías trabajar con 0.05 como referencia estándar para interpretar el resultado.

# #---------------------------------------

# El flujo paso a paso
# 
# 1. Formular la pregunta:
#       ¿Hay una diferencia, cambio o efecto que valga la pena detectar?
#
# 2. Plantear hipótesis:
#      𝐻0: no hay efecto (p. ej., proporcion = 0.5) vs 𝐻1: sı hay efecto
# 
# 3.Elegir el tipo de prueba:
#   - Cola izquierda: buscas disminuciones.                      Ej: “¿La tasa cayó por debajo de 5%?”
#   - Cola derecha: buscas aumentos.                             Ej: “¿La conversión superó 10%?”    
#   - Dos colas: cualquier cambio (arriba o abajo) te importa.   Ej: “¿Cambió la media, sea al alza o baja?”
#
# 4. Recoger datos y calcular un estadístico:
#   - Media o proporción muestral: tu resultado observado.
#   - z-score: cuántas “desviaciones estándar” está tu resultado de lo que H0 espera.
#
#           𝑧 = resultado observado − resultado esperado bajo 𝐻0
#               -----------------------------------------------
#                  variacion esperada si 𝐻0 fuera cierta
# 
# 5. Calcular el valor p:
#   - Definición informal: la probabilidad de obtener un resultado tan extremo como el tuyo (o más), si H0 fuera verdadera.
# 
# 6. Comparar valor p con el nivel de significancia 𝛼:
#   - Si p ≤ α: la evidencia es lo bastante fuerte; rechazas H0.
#   - Si p > α: no hay evidencia suficiente; no rechazas H0.
#
# 7. Errores que puedes cometer
#   - Error tipo I (falso positivo): Rechazas H0 siendo verdadera. La probabilidad de cometerlo es 𝛼
#     (por ejemplo, 5% si usas 0.05).
#
#   - Error tipo II (falso negativo): No rechazas H0 siendo falsa. Su probabilidad se llama 𝛽, y 
#     1 − 𝛽 es la “potencia” (qué tan bueno eres para detectar un efecto real).
#
#
# 8 ¿Qué significa “significativo al 5%”?
# 
#   - Nivel de significancia 𝛼 = 0.05: aceptas un 5% de riesgo de falso positivo.
#
#   - Interpretación práctica: si no hubiera efecto, resultados tan extremos como el tuyo ocurrirían 
#     5 de cada 100 veces. Si tu valor p es menor o igual a 0.05, decides que la evidencia contra H0 es suficiente.