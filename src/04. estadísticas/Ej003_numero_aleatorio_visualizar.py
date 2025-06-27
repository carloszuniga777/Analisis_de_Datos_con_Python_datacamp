# numpy and matplotlib imported, seed set.
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(123)

# initialize and populate all_walks
all_walks = []

for i in range(5) :
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
    all_walks.append(random_walk)


# 1. Convierte todos los pasos (all_walks) en un array numpy 
np_aw = np.array(all_walks)

# Dibujar np_aw

print(f'arreglo np_aw:\n {np_aw}')     # arreglo de 5 filas y 100 columnas

plt.plot(np_aw)
plt.show()

# Clear the figure
plt.clf()

# Tranponer el arreglo np_aw
np_aw_t = np.transpose(np_aw)

print(f'\narreglo np_aw_t:\n {np_aw_t}') 

# Plot np_aw_t and show
plt.plot(np_aw_t)
plt.show()


# La función np.transpose() en NumPy realiza la transposición de un array,
# intercambiando sus dimensiones. 
#
# En tu caso, el array original np_aw tiene una forma (shape) de (5, 100) (5 filas, 100 elementos por fila).
# Al aplicar np.transpose(np_aw), ocurre lo siguiente:
#
# 1. Cambio de dimensiones:
#      Original: (5, 100)        → 5 filas y 100 columnas.
#      Tras transponer: (100, 5) → 100 filas y 5 columnas.
#
# 2. Reorganización de los datos:
#       
#       Paso 0 (primera fila del resultado transpuesto):
#           [0, 0, 0, 0, 0] → Todos los valores iniciales de las 5 caminatas.

#       Paso 1 (segunda fila):
#           [3, 4, 2, 6, 6] → Segundo paso de cada caminata.

