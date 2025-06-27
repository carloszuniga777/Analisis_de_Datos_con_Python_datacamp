# El azar tiene muchos usos en la ciencia, el arte, la estadística,
# la criptografía, el juego, las apuestas y otros campos.
# Vas a utilizar el azar para simular un juego.
#
# seed(): establece el valor de inicialización aleatorio,
#         para que tus resultados sean reproducibles entre simulaciones.
#         Como argumento, toma un número entero de tu elección.
#         Si llamas a la función, no se generará ninguna salida.
#
# rand(): si no especificas ningún argumento,
#         genera un float aleatorio entre cero y uno.

# Import numpy as np
import numpy as np

# Set the seed
np.random.seed(123)

# Genera numeros aleatorios flotante entre 0 y 1
random = np.random.rand()
print(random)

# Genera numeros aleatorios entre 1 y 6 (7 no esta incluido)
random = np.random.randint(1,7)
print(random)