# Uso de ttest()
# Calcular manualmente los estadísticos de prueba y transformarlos con CDF para obtener un valor p supone 
# mucho esfuerzo para comparar dos medias muestrales. 
# 
# La comparación de dos medias muestrales se denomina prueba t, 
# y el paquete pingouin de Python tiene el método .ttest() para realizarla. Este método proporciona cierta flexibilidad 
# en la forma de realizar la prueba.
#
# Como en el ejercicio anterior, explorarás la diferencia entre la proporción de votos a nivel de condado 
# por el candidato demócrata en 2012 y 2016 para identificar si la diferencia es significativa. Las hipótesis son las siguientes:
#
# $H{0}$: la proporción de votos por los demócratas en 2012 y 2016 fue la misma. 
# $H{A}$: la proporción de votos por los demócratas en 2012 y 2016 fue diferente.

import pandas as pd
import matplotlib.pyplot as plt
import pingouin
import os

# Obtener ruta base del archivo
base_path = os.path.dirname(os.path.abspath(__file__))
ruta_archivo = os.path.join(base_path, "..", "..", "Archivos", "sample_dem_data.csv")


# Importa el excel
sample_dem_data = pd.read_csv( ruta_archivo)  


#--------------------------------------------------------------------------
# 
#---------------------------------------------------------------------------
# Crea una nueva columna diff que contenga el porcentaje de votos por el candidato demócrata en 2012
#  menos el porcentaje de votos por el candidato demócrata en 2016.

# Calculate the differences from 2012 to 2016
sample_dem_data['diff'] = sample_dem_data['dem_percent_12'] - sample_dem_data['dem_percent_16']


#--------------------------------------------------
# Ejemplo 1
#--------------------------------------------------
# Realiza una prueba t sobre las diferencias muestrales (la columna diff de sample_dem_data) 
# utilizando una hipótesis alternativa adecuada elegida entre "two-sided", "less" y "greater".

# Conduct a t-test on diff
test_results = pingouin.ttest(x=sample_dem_data['diff'], y=0, alternative='two-sided')


                              
# Print the test results
print(test_results) # p-val: 3.595436e-115  ====> # 0.00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000003595436


# Pregunta:
# ¿Cuál es la decisión correcta a partir de la prueba t, suponiendo alpha= 0.01?
# 
# 0.00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000003595436 <= 0.01
# Rechazar la hipótesis nula H0


#----------------------------------------------
# Ejemplo 2
#---------------------------------------------
# Realiza una prueba pareada sobre los votos por los demócratas en 2012 y 2016 
# (las columnas dem_percent_12 y dem_percent_16 de sample_dem_data) 
# utilizando una hipótesis alternativa adecuada

# Conduct a paired t-test on dem_percent_12 and dem_percent_16
paired_test_results = pingouin.ttest(x=sample_dem_data['dem_percent_12'],
                                     y=sample_dem_data['dem_percent_16'],
                                     paired=True,
                                     alternative="two-sided")

print('\n\n')

# Print the paired test results
print(paired_test_results)   #p-val: 3.595436e-115

#--------------------------------------------
# Ejemplo 3
#-------------------------------------------
# Compara la prueba t pareada con una prueba no pareada (inadecuada) sobre los mismos datos. ¿Cómo cambia el valor p?

no_paired_test_results = pingouin.ttest(x=sample_dem_data['dem_percent_12'],
                                     y=sample_dem_data['dem_percent_16'],
                                     paired=False,
                                     alternative="two-sided")


print('\n\n')

# Print the paired test results
print(no_paired_test_results)  # p-val: 1.345682e-12


if paired_test_results['p-val'][0] < no_paired_test_results['p-val'][0]:
    print('paired_test_results es menor que no_paired_test_results')
else:    
    print('paired_test_results es mayor que no_paired_test_results')


# Pregunta
# Compara la prueba t pareada con una prueba no pareada (inadecuada) sobre los mismos datos. ¿Cómo cambia el valor p?
 # El valor p de la prueba no pareada es mayor que el valor p de la prueba pareada.   

# Conclusion:
# Usar .ttest() te permite evitar el cálculo manual para realizar tu prueba. 
# Cuando tienes datos pareados, una prueba t pareada es preferible a la versión no pareada porque reduce 
# la posibilidad de un error falso negativo.