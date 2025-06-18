# Import numpy as np
import numpy as np

np_height = np.array([74, 74, 72, 75, 75, 73])
np_baseball = np.array(
                        [  
                            [ 74, 180],
                            [ 74, 215],
                            [ 72, 210],
                            [ 75, 205],
                            [ 75, 190],
                            [ 73, 195]
                        ]
                    )

# Bucle FOR para numpy 1D
for i in np_height:
    print(f'{i} inches')


# Bucle FOR para numpy 2D
for i in np.nditer(np_baseball):
    print(i)