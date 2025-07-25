import numpy as np

baseball = [[180, 78.4],
            [215, 102.7],
            [210, 98.5],
            [188, 75.2]]

# Create a 2D numpy array from baseball: np_baseball

np_baseball = np.array(baseball)

# Print out the type of np_baseball: <numpy.ndarray>
print(type(np_baseball))

# Print out the shape of np_baseball: 4 filas y 2 columas
print(np_baseball.shape)