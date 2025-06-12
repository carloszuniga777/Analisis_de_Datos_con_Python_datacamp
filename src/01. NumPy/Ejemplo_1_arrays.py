import numpy as np

height = [1.73, 1.68, 1.71, 1.89, 1.79]
weight = [65.4, 59.2, 63.6, 88.4, 68.7]

np_height = np.array(height)
np_weight = np.array(weight)

#Divide cada elemento del arreglo automaticamente 
bmi = np_weight / np_height**2

print(f"Calculando bmi de cada elemento {bmi}")
print(f"Calculando el elemento mayor a 23: {bmi[bmi > 23]}")
