# Antes, los operadores operativos como < y >= funcionaban con matrices NumPy 
# de forma inmediata. 
# Desgraciadamente, no es el caso con los operadores booleanos and, or y not.
#
# Para utilizar estos operadores con NumPy, 
# necesitarás np.logical_and(), np.logical_or() y np.logical_not(). 


import numpy as np

height = [1.73, 1.68, 1.71, 1.89, 1.79]
weight = [65.4, 59.2, 63.6, 88.4, 68.7]

np_height = np.array(height)
np_weight = np.array(weight)

#Divide cada elemento del arreglo automaticamente 
bmi = np_weight / np_height**2

print('bmi', bmi)

#AND
result = bmi[ np.logical_and(bmi > 21, bmi < 22) ]
print(f'\nObteniendo los elementos mayores a 21 y menores a 22:\n {result}\n\n')

#OR
result = bmi[ np.logical_or(bmi >= 24, bmi < 21) ]
print(f'\nObteniendo los elementos menores a 21 o mayores a 24:\n {result}\n\n')


#NOT
result = bmi[ np.logical_not(bmi >= 24) ]
print(f'\nObteniendo los elementos que no sean mayores a 24:\n {result}\n\n')