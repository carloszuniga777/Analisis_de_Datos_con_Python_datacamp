import numpy as np

baseball = [
    [191, 86],  #0
    [185, 92],  #1
    [182, 80],  #2
    [193, 88],  #3
    [188, 94],  #4
    [176, 79],  #5
    [190, 91],  #6
    [198, 100], #7
    [183, 85],  #8
    [177, 77],  #9
    [184, 90],  #10
    [189, 89]]  #11


np_baseball = np.array(baseball)

# Imprime la fila 5 de np_baseball 
# y todas las columnas (:) que contiene esa fila: [176  79]
print(np_baseball[5, :])

# Crea np_weight_lb con la segunda columna: [ 86  92  80  88  94  79  91 100  85  77  90  89]
np_weight_lb = np_baseball[:, 1]  # Selecciona toda la segunda columna

print(np_weight_lb)


# Imprime la altura (primera columna) del jugador 1: 185
print(np_baseball[1, 0])  