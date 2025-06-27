
# Crear una distribución de probabilidad
# 
# Hace unos meses se inauguró un nuevo restaurante, y su dirección quiere optimizar el espacio para sentarse en función 
# del tamaño de los grupos que acuden con más frecuencia. 
# 
# Una noche, hay 10 grupos de personas esperando para sentarse en el restaurante, pero en lugar de ser llamadas en el orden 
# en que llegaron, serán llamadas aleatoriamente. 
# 
# En este ejercicio, investigarás la probabilidad de que grupos de diferentes tamaños sean elegidos en primer lugar. Los datos de cada uno de los diez grupos están contenidos en el DataFrame restaurant_groups.
# 
# Recuerda que el valor esperado puede calcularse multiplicando cada resultado posible por su probabilidad correspondiente y tomando la suma.
# 
# #

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os

# Obtener ruta base del archivo
base_path = os.path.dirname(os.path.abspath(__file__))
ruta_archivo = os.path.join(base_path, "..", "..", "Archivos", "restaurant_groups.csv")

# Importa el excel sales.csv
restaurant_groups = pd.read_csv( ruta_archivo)  

#-------------------------------------------
# Parte 1: Crea un histograma de la columna group_size de restaurant_groups, ajustando bins a [2, 3, 4, 5, 6]. 

restaurant_groups['group_size'].hist(bins=[2, 3, 4, 5, 6])

plt.ylabel('Frecuencia')
plt.xlabel('Group size')
plt.title('Grupos de restaurante')


#-------------------------------------------------
# Parte 2: Calcular la probabilidad de seleccionar aleatoriamente un grupo de cada tamaño.

# Creando la distribucion de probabilidad
size_dist = restaurant_groups['group_size'].value_counts(normalize=True)

# Otra forma de calcularlo es:
# size_dist = restaurant_groups['group_size'].value_counts() / restaurant_groups.shape[0]

# Explicacion:
# Cuenta la frecuencia de cada tamaño de grupo
# Divide cada conteo entre el total de grupos (10)
#
# Resultado:
# Para grupos de 2 personas, la probabilidad es: 0.6
# Para grupos de 4 personas, la probabilidad es: 0.2
# Para grupos de 6 personas, la probabilidad es: 0.1
# Para grupos de 3 personas, la probabilidad es: 0.1



# Concepto estadistico: Distribucion de Probabilidad:
#  
# - Definición: Lista de todos los resultados posibles con sus probabilidades asociadas
# - Fórmula: P(X=x) = Número de resultados favorables / Número total de resultados
# 
# ¿Por qué es importante en el mundo real?
#   En un restaurante, esto te dice que:
#      - 60% de los grupos son de 2 personas
#      - Solo 10% son grupos grandes (6 personas)
#
# Aplicación: Decidir cuántas mesas para 2, 4, 6 personas necesitas



# Reset index and rename columns
size_dist = size_dist.reset_index()
size_dist.columns = ['group_size', 'probability']

print(f'\nProbabilidad de seleccionar aleatoriamente un grupo de cada tamaño:\n\n {size_dist}')

#--------------------------------------------------------
# Parte 3: Calculando el valor esperado: Promedio ponderado de todos los resultados posibles

expected_value = np.sum(size_dist['group_size'] * size_dist['probability'])
print(f'\nValor esperado promedio: {expected_value}')

# Calculo detallado:
#  
# group_size * probability:
#  (2 * 0.6) = 1.2
#  (3 * 0.1) = 0.3
#  (4 * 0.2) = 0.8
#  (6 * 0.1) = 0.6
#
# Suma = 1.2 + 0.3 + 0.8 + 0.6 = 2.9

# Concepto estadístico:
# 
# - Definición: Promedio ponderado de todos los resultados posibles
# - Fórmula: E[X] = Σ [x_i * P(X=x_i)]
# - Es el valor medio "esperado" a largo plazo
# 
# Aplicación en restaurante:
# - El tamaño de grupo promedio es 2.9 personas
# - Decisiones de negocio:
#       - Si tienes 100 grupos por noche: esperas 290 personas
#       - Calcular necesidades de personal: 1 mesero por cada 30 personas → 10 meseros
#       - Estimar consumo de comida: 290 personas × $15 por persona = $4350 ingresos esperados


#-------------------------------------------------------------------------
# Calculando la probabilidad de elegir aleatoriamente un grupo de 4 o más personas

# Subset groups of size 4 or more
groups_4_or_more = size_dist[size_dist['group_size'] >= 4]

# Sum the probabilities of groups_4_or_more
prob_4_or_more = groups_4_or_more['probability'].sum()
print(f'\nProbabilidad de elegir aleatoriamente un grupo de 4 o mas personas: {prob_4_or_more}')

#-------------------

plt.show()