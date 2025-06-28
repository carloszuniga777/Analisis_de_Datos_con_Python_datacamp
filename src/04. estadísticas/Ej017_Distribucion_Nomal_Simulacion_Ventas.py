# Simulación de ventas en nuevas condiciones de mercado
# 
# El analista financiero de la empresa prevé que el próximo trimestre el valor de cada venta aumentará un 20 % 
# y la volatilidad, o desviación típica, del valor de cada venta aumentará un 30 %. 
# 
# Para ver cómo podrían ser las ventas de Amir el próximo trimestre en estas nuevas condiciones de mercado, 
# simularás nuevas cantidades de ventas utilizando la distribución normal y las almacenarás en el DataFrame new_sales, 
# que ya se ha creado.

import pandas as pd
from scipy.stats import norm
import matplotlib.pyplot as plt

#-------------------------------------------
# Parte 1:
# Actualmente, la cantidad media de las ventas de Amir es de 5000 $. 
# Calcula cuál será su nueva cantidad media si aumenta un 20 % y guárdala en new_mean.

# Calculando la nueva media de ventas (aumento del 20%)
new_mean = 5000 * 1.20   # 6000$

#-----------------------------------------
# Parte 2:
# La desviación típica actual de Amir es de 2000 $. Calcula cuál será su nueva desviación típica 
# si aumenta un 30 % y guárdala en new_sd.

# Calculando la nueva desviacion estandar (aumento del 30%)
new_sd = 2000 * 1.30  # 2600$

#------------------------------------------
# Crea una variable llamada new_sales, que contiene 36 cantidades simuladas de una distribución 
# normal con una media de new_mean 
# y una desviación típica de new_sd.


# norm.rvs es una función de la biblioteca scipy.stats en Python,
# utilizada para generar números aleatorios que siguen una distribución normal
# Sintaxis: norm.rvs(media, desviacion estandar, cantidad numeros aleatorios a generar)

new_sales = norm.rvs(new_mean, new_sd, size=36)

#Crear un histograma 
plt.hist(new_sales,             # Data
         bins=8,                # Número de barras
         edgecolor='black',     # Bordes visibles
         alpha=0.7              # Transparencia
        )

plt.title('Distribución de nuevas ventas de Amir\n(Media = ${:.2f}, Desv = ${:.2f})'.format(new_mean, new_sd))
plt.xlabel("Monto de ventas ($)")
plt.ylabel("Cantidad de ventas")
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()

# Aunque la cantidad promedio de ventas aumentó, la variación también aumentó, por lo que no es sencillo decidir si estas ventas son mejores que las actuales. 
# En el próximo ejercicio, explorarás los efectos de una mayor variación.