# Visualizar el paseo:
# ¡Visualicemos este paseo aleatorio! 
# ¿Recuerdas cómo podías utilizar matplotlib para construir un gráfico lineal?
#
# import matplotlib.pyplot as plt
# plt.plot(x, y)
# plt.show()
#
# La primera lista que pases se mapea en el eje x 
# y la segunda lista se mapea en el eje y.

# Si solo pasas un argumento, Python sabrá qué hacer 
# y utilizará el índice de la lista para mapearla en el eje x, 
# y los valores de la lista en el eje y.


import numpy as np
import matplotlib.pyplot as plt

np.random.seed(123)

# Initialization
random_walk = [0]

for x in range(100) :
    step = random_walk[-1]
    dice = np.random.randint(1,7)

    if dice <= 2:
        step = max(0, step - 1)
    elif dice <= 5:
        step = step + 1
    else:
        step = step + np.random.randint(1,7)

    random_walk.append(step)

# Dibujar random_walk
plt.plot(random_walk)    # Python mapea automaticamente la lista, 
                         # el indice como eje x, y valores en eje y 


plt.ylabel('Valores Random Walk')
plt.xlabel('Pasos')
plt.title('Ejercicio paseo')

# Visualizar
plt.show()
