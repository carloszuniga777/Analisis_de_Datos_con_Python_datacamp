# Distribución muestral exacta
# 
# Para cuantificar cómo varía la estimación puntual (estadística muestral) que te interesa, 
# ecesitas conocer todos los valores posibles que puede tomar y con qué frecuencia. 
# Es decir, necesitas conocer su distribución.
# 
# La distribución de una estadística muestral se llama distribución muestral. Cuando podemos calcularla exactamente, 
# en lugar de utilizar una aproximación, se conoce como distribución muestral exacta.
#
# Echemos otro vistazo a la distribución muestral de las tiradas de dados. 
# Esta vez, veremos cinco dados de ocho caras. (Estos tienen los números del uno al ocho).


import pandas as pd
import matplotlib.pyplot as plt
import itertools


#----------------------------------------------
# Definicion de la funcion expand_grid, proporcionada por pandas: 
# https://pandas.pydata.org/pandas-docs/version/0.17.1/cookbook.html#creating-example-data

def expand_grid(data_dict):
	rows = itertools.product(*data_dict.values())
	return pd.DataFrame.from_records(rows, columns=data_dict.keys())

#-----------------------------------------------

# 1. Generar todas las combinaciones posibles de cinco dados de 8 caras
#    Esto crea un DataFrame de 8⁵ = 32 768 filas, cubriendo cada tira posible.
dice = expand_grid({
    "die1": [1, 2, 3, 4, 5, 6, 7, 8],  # Valores posibles para el dado 1
    "die2": [1, 2, 3, 4, 5, 6, 7, 8],  # Valores posibles para el dado 2
    "die3": [1, 2, 3, 4, 5, 6, 7, 8],  # Valores posibles para el dado 3
    "die4": [1, 2, 3, 4, 5, 6, 7, 8],  # Valores posibles para el dado 4
    "die5": [1, 2, 3, 4, 5, 6, 7, 8],  # Valores posibles para el dado 5
})

# 2. Calcular la media de cada fila (cada tira de cinco dados)
#    Suma los valores de die1 a die5 y divide entre 5
dice['mean_roll'] = (
    dice['die1']
  + dice['die2']
  + dice['die3']
  + dice['die4']
  + dice['die5']
) / 5

# 3. Convertir la columna mean_roll en tipo 'category'
#    Esto fija el rango de categorías (1.0, 1.2, 1.4, …, 8.0) y preserva su orden natural
dice['mean_roll'] = dice['mean_roll'].astype('category')

# 4. Generar un diagrama de barras con la frecuencia de cada valor de mean_roll
#    value_counts(sort=False) mantiene el orden de las categorías
dice['mean_roll'] \
    .value_counts(sort=False) \
    .plot(kind='bar')

# 5. Mostrar el gráfico en pantalla
plt.xlabel('Media de los 5 dados')          # Etiqueta del eje X
plt.ylabel('Número de combinaciones')       # Etiqueta del eje Y
plt.title('Distribución muestral de la media de cinco dados de 8 caras')  # Título del gráfico
plt.xticks(rotation=90)                     # Rota las etiquetas del eje X para mayor legibilidad
plt.tight_layout()                          # Ajusta márgenes para evitar recortes
plt.show()

# Conclusion
# La distribución de muestreo exacta muestra todas las variaciones posibles de la estimación puntual que te interesa.

# La distribución muestral exacta solo puede calcularse si sabes cuál es la población 
# y si los problemas son pequeños y suficientemente sencillos de calcular.
# Si no, hay que utilizar la distribución muestral aproximada.

#---------------------------------------------------------------------
# Distribución muestral exacta
# 
# 1. Definición
# La distribución muestral exacta es el conjunto de todos los valores que puede tomar una estadística 
# (por ejemplo, la media o la proporción) al considerar todas las posibles muestras de un tamaño dado. 
# Cada valor va acompañado de su frecuencia real, sin aproximaciones.

# 2. Explicación paso a paso
# 	- Seleccionas la estadística de interés (media, proporción, varianza, etc.).
# 	- Generas todas las muestras posibles de tu población o rango de valores.
# 	- Calculas la estadística en cada muestra.
# 	- Cuentan cuántas veces aparece cada valor de la estadística: eso forma la distribución muestral exacta.
#
# Ejemplo rápido: cinco dados de ocho caras
#  - Hay 8⁵ = 32 768 tiradas distintas.
#  - Para cada tirada calculas la media de los cinco dados.
#  - Reúnes todas esas medias y mides la frecuencia de cada valor.
#  - El gráfico de barras resultante es la distribución muestral exacta de la media.
#
# ¿Para qué sirve?
# 	- Permite ver exactamente cuánto varía tu estadística en todas las posibles muestras.
# 	- Sirve de referencia para medir precisión y crear intervalos de confianza reales.
# 	- Evita depender de aproximaciones (normal, bootstrap) cuando la población es pequeña o manejable.
#
# Cuándo utilizarla
# 	- Cuando el número de muestras posibles es relativamente bajo y factible de calcular.
# 	- En contextos controlados, con poblaciones pequeñas o exhaustivas.
# 	- Para validar métodos aproximados: comparas la aproximación con la distribución exacta.
# 	- En enseñanza para ilustrar de forma clara cómo funciona el muestreo y la variabilidad de estimadores.