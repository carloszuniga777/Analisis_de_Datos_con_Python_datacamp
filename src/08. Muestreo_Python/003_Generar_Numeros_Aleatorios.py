# Generar números aleatorios
# Has utilizado .sample() para generar números pseudoaleatorios a partir de un 
# conjunto de valores de un DataFrame. Una tarea relacionada es generar números 
# aleatorios que sigan una distribución estadística, como la distribución uniforme o la distribución normal.
#
# Cada función de generación de números aleatorios tiene argumentos específicos de la distribución 
# y un argumento para especificar el número de números aleatorios a generar.

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

#------------------------------------------------------------------
# Ejercicio 1:

# 1. Genera 5000 números a partir de una distribución uniforme, 
# ajustando los parámetros low a -3 y high a 3.
uniforms = np.random.uniform(low=-3, high=3, size=5000)

# 2. Genera 5000 números a partir de una distribución normal, 
# ajustando los parámetros loc a 5 y scale a 2.
normals = np.random.normal(loc=5, scale=2, size=5000)   #Loc: Media | scale: desviacion standard, size: cantidad de muestras





# 3. Traza un histograma de uniforms con contenedores con anchura de 0.25 de -3 a 3

plt.figure(1)

# Configurar estilo
sns.set_style("whitegrid")

# Definiendo el cotendor (EXPLICACION ABAJO DEL SCRIPT)
# Anchura: 02.5 de -3 a 3
bins = np.arange(-3, 3.25,0.25)

g = sns.histplot(
    data=uniforms,
    bins=bins,           # Número de barras
    kde=True,          # Añadir curva de densidad
    color='royalblue',  # Color de las barras
    edgecolor='black',  # Borde de las barras
    alpha=0.7          # Transparencia
)

g.figure.suptitle('Distribución Uniforme Continua', fontsize=14)
g.set_xlabel('Valores')
g.set_ylabel('Frecuencia')





# 4. Traza un histograma de normals con contenedores con anchura de 0.5 de -2 a 13

plt.figure(2)

# Configurar estilo
sns.set_style("whitegrid")

#Contenedores                        (EXPLICACION ABAJO DEL SCRIPT)
bins = np.arange(-2, 13.5,0.5) 

g = sns.histplot(
    data=normals,
    bins=bins,           # Número de barras
    kde=True,          # Añadir curva de densidad
    color='#2ecc71',  # Color de las barras
    edgecolor='black',  # Borde de las barras
    alpha=0.7,          # Transparencia,
)

g.figure.suptitle('Distribución Normal', fontsize=14)
g.set_xlabel('Valores')
g.set_ylabel('Frecuencia')

#---------------------------------------------------------------------
# Mostrar
plt.show()

#-------------------------------------------------------------------

# Explicacion np.arange:
# 
# Esta línea de código crea los límites de los intervalos (bins) para un histograma usando NumPy. 
#
# 1. Qué es np.arange()?
# - Es una función de NumPy que genera un array de valores espaciados uniformemente.
#
#  Sintaxis: np.arange(start, stop, step)
#       - start: Valor inicial (incluido)
#       - stop: Valor final (no incluido)
#       - step: Tamaño del paso entre valores
#
#
#
# 2. Ejemplo:
#
# start = -2   # Primer valor del array
# stop  = 13.5 # El array NO incluye este valor (es el límite superior)
# step  = 0.5  # Distancia entre valores consecutivos
#
#
# 3. Valores generados:
#
# El array comenzará en -2 y aumentará de 0.5 en 0.5 hasta el mayor valor menor que 13.5:
# 
#               [-2.0, -1.5, -1.0, -0.5, 0.0, 0.5, 1.0, ..., 12.0, 12.5, 13.0]
# 
# Último valor: 13.0 (porque 13.0 + 0.5 = 13.5, y stop no se incluye).
#
#
#
# 4. Características clave:
#
#    Parámetro	            Valor	            Explicación
#-------------------------------------------------------------
# Número de bins	        31	                Se crean 31 bordes (desde -2.0 hasta 13.0)
# Ancho de bin	            0.5	                Todos los intervalos tienen igual amplitud (0.5 unidades)
# Rango cubierto	    -2.0 ≤ x < 13.0	        ¡El último bin termina en 13.0, no en 13.5!
#
#
# 5. ¿Para qué sirve en un histograma?
#   
# Estos bins definen cómo se agrupan los datos:
# 
#
#           import matplotlib.pyplot as plt
#           plt.hist(datos, bins=np.arange(-2, 13.5, 0.5))
# 
# Un dato con valor -1.7 caerá en el bin [-2.0, -1.5).
#
# Un dato con valor 12.9 caerá en el bin [12.5, 13.0].
