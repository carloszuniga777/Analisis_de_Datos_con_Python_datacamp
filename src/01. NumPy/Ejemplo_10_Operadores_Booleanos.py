# ¿Qué zonas son más pequeñas que 11 tanto en my_house como en your_house? 
#
import numpy as np

my_house = np.array([18.0, 20.0, 10.75, 9.50])
your_house = np.array([14.0, 24.0, 14.25, 9.0])

# Both my_house and your_house smaller than 11
print( np.logical_and(my_house < 11, your_house < 11) )
print(f'my house: {my_house[np.logical_and(my_house < 11, your_house < 11)]}')
print(f'your house: {your_house[np.logical_and(my_house < 11, your_house < 11)]}')
