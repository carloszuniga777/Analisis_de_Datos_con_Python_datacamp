# Altura de los jugadores de béisbol:
# Eres un gran aficionado al béisbol. Decides llamar a MLB (las Grandes Ligas de Béisbol) 
# y preguntar por más estadísticas sobre la estatura de los principales jugadores. 
# 
# Te facilitan datos sobre más de mil jugadores, almacenados como una lista normal 
# de Python: height_in. La altura se expresa en pulgadas. 
# 
# ¿Puedes hacer una matriz de numpy y convertir las unidades a metros?

# Import numpy
import numpy as np

#Altura de los jugadores
height_in = [74, 74, 72, 75, 75, 73]

# Creacion de un arreglo numpy de from height_in
np_height_in = np.array(height_in) 

# Print out np_height_in
print(np_height_in)

# Convertir la altura de los jugadores de pies a metros
np_height_m = np_height_in * 0.0254

# Print np_height_m
print(np_height_m)