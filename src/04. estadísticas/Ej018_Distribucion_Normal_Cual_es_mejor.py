# ¿Qué mercado es mejor?
# 
# El parámetro clave que la empresa utiliza para evaluar a los vendedores es el porcentaje de ventas que realizan por encima de $1000, 
# ya que el tiempo invertido en cada venta suele valer algo más que eso, por lo que, cuanto mayor sea este parámetro,
# mejor será el rendimiento del vendedor.

# Recuerda que las cantidades de las ventas actuales de Amir tienen una media de 5000 y una desviacion tipica de 2000,
#  y las cantidades previstas de Amir en el mercado del próximo trimestre tienen una media de 6000 y una desviacion tipica de 2600
#
# Basándote solo en el parámetro del porcentaje de ventas sobre $1000, 
# ¿tiene Amir mejores resultados en el mercado actual o en el mercado previsto?

#-------------------------------------
from scipy.stats import norm

#------------------------------------
# Porcentaje de ventas actuales de Amir


evaluar = 1000
media = 5000
desviacion_estandar = 2000

# Porcentaje ventas superiores a 1000 USD (ventas > 1000)
ventasActuales = 1 - norm.cdf(evaluar, media, desviacion_estandar)

print(f'El porcentaje de ventas actuales de Amir es de: {ventasActuales :.1%}')

#-----------------------------------------
# Porcentaje de ventas prevista

evaluar = 1000
media = 6000
desviacion_estandar = 2600

# Porcentaje ventas superiores a 1000 USD (ventas > 1000)
ventasPrevista = 1 - norm.cdf(evaluar, media, desviacion_estandar)

print(f'El porcentaje de ventas previstas de Amir es de: {ventasPrevista :.1%}')

#------------------------------------

# Amir realiza ventas por encima de $1000 aproximadamente el 97.7% del tiempo, 
# y aproximadamente el 97.3% del tiempo en el mercado predicho, por lo que no hay mucha diferencia. 
# 
# Sin embargo, su monto promedio de venta es mayor en el mercado predicho, 
# por lo que tu empresa puede querer considerar otras métricas también.