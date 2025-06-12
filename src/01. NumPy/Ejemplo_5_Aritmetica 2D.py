import numpy as np

baseball = [
 [ 74, 180, 22.99],
 [ 74, 215, 34.69],
 [ 72, 210, 30.78],
 [ 75, 205, 25.19],
 [ 75, 190, 31.01],
 [ 73, 195, 27.92]]

updated =[
 [1.2303559, -11.16224898, 1],
 [1.02614252, 16.09732309, 1],
 [1.1544228,   5.08167641, 1],
 [1.09349925,  4.23890778, 1],
 [0.82285669,-17.78200035, 1],
 [0.99484223,  8.14402711, 1]]

#Se crea el objeto numpy baseball
np_baseball = np.array(baseball)

# Print out addition of np_baseball and updated
 
suma =  np_baseball + updated

print(f'\n Suma de np_baseball + updated: {suma}')

#-------------------------------------------

# Create numpy array: conversion
conversion = [0.0254, 0.453592, 1]


# Print out product of np_baseball and conversion
transformacion = np_baseball * conversion

print(f'\n Convesion: {transformacion}')