# Grafico de Histograma
# Crea un grafico apartir de los puntos dados, 
# los distribuye en el eje x (Valor minimo a Maximo)
# 
# Crea una barra segun las distribucion de los puntos  


import matplotlib.pyplot as plt

values = [0, 0.6, 1.4, 1.6, 2.2, 2.5, 2.6, 3.2, 3.5, 3.9, 4.2, 6]

plt.hist(values, bins=3)  # Bins: Numero de Barras: 3 

plt.show()