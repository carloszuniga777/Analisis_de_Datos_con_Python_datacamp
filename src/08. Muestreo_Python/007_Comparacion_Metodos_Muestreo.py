# 3 tipos de muestreo
# Vas a comparar el rendimiento de las estimaciones puntuales mediante muestreo simple, estratificado y por clústeres. 
# Antes de hacerlo, tendrás que configurar las muestras.
#
# Utilizarás la columna RelationshipSatisfaction del conjunto de datos attrition_pop, 
# que clasifica la relación del empleado con la empresa. Tiene cuatro niveles: Low, Medium, High y Very_High.

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import random
import os

# Obtener ruta base del archivo
base_path = os.path.dirname(os.path.abspath(__file__))
ruta_archivo = os.path.join(base_path, "..", "..", "Archivos", "attrition_pop.csv")


# Importa el excel
attrition_pop = pd.read_csv( ruta_archivo,  dtype={'RelationshipSatisfaction': 'category'})  

#-------------------------------------------------
#           Parte 1
#-------------------------------------------------

# 1. Muestreo Aleatorio Simple
#
# Realiza un muestreo aleatorio simple en attrition_pop para obtener un cuarto de la población, 
# fijando el valor de inicialización en 2022.

attrition_srs = attrition_pop.sample(frac=1/4, random_state=2022)



#-------------------------------------------------
# 2. Muestreo Estratificado

# Realiza un muestreo estratificado en attrition_pop para muestrear una cuarta parte de cada grupo de RelationshipSatisfaction, 
# estableciendo el valor de inicialización en 2022

attrition_strat = (
                    attrition_pop.groupby('RelationshipSatisfaction', observed=False)
                    .sample(frac=1/4, random_state=2022)
                   )

# observed=False:
# Para quitar un Warinig de un cambio futuro en groupby
#   - Actualmente (observed=False): Muestra todas las categorías posibles, incluso si no tienen datos
#   - En futuras versiones (observed=True): Mostrará solo las categorías con datos presentes

#--------------------------------------------------
# 3. Muestreo por Clusteres
# Crea una lista de valores únicos a partir de la columna RelationshipSatisfaction de attrition_pop.
# 
# Toma una muestra aleatoria de satisfaction_unique para obtener dos valores.
# 
# Subconjunta la población para las filas en las que RelationshipSatisfaction está en satisfaction_samp 
# y borra las categorías no utilizadas de RelationshipSatisfaction; asígnalas a attrition_clust_prep.
# 
# Realiza un muestreo por clústeres en los grupos de satisfacción seleccionados, 
# muestreando una cuarta parte de la población y fijando el valor de inicialización en 2022


# Crea una lista de valores unicos de RelationshipSatisfaction: ['Very_High', 'High', 'Low', 'Medium'] 
satisfaction_unique = list(attrition_pop['RelationshipSatisfaction'].unique())

# Seleccionamos aleatoriamente dos valores de la lista satisfaction_unique
satisfaction_samp = random.sample(satisfaction_unique, k=2)

# Se crea un nuevo Dataframe con las categorias filtradas
satis_condition = attrition_pop['RelationshipSatisfaction'].isin(satisfaction_samp)
attrition_clust_prep = attrition_pop[satis_condition].copy()


#print(attrition_clust_prep['RelationshipSatisfaction'].value_counts())

# Imprime esto:
# High         459
# Very_High    432
# Low            0
# Medium         0 
# Por lo que se procede a eliminar las categorias en 0 con remove_unused_categories

# Se eliminan las categorias que estan en cero
attrition_clust_prep['RelationshipSatisfaction'] = attrition_clust_prep['RelationshipSatisfaction'].cat.remove_unused_categories()


# Perform cluster sampling on the selected group, getting 0.25 of attrition_pop

attrition_clust = (
     attrition_clust_prep.groupby("RelationshipSatisfaction", observed=False )
     .sample(frac=0.25, random_state=2022)
    )

# observed=False:
# Para quitar un Warinig de un cambio futuro en groupby
#   - Actualmente (observed=False): Muestra todas las categorías posibles, incluso si no tienen datos
#   - En futuras versiones (observed=True): Mostrará solo las categorías con datos presentes

#----------------------------------------------------------
# Calculando la media
#----------------------------------------------------------
# Comparar estimaciones puntuales
# Ahora que tienes tres tipos de muestra (simple, estratificada y de clústeres), 
# puedes comparar las estimaciones puntuales de cada muestra con el parámetro poblacional. 
# Es decir, puedes calcular la misma estadística de resumen en cada muestra 
# y ver cómo se compara con la estadística de resumen de la población.
#
# Aquí veremos cómo influye la satisfacción con la empresa en que el trabajador la abandone o no. 
# Es decir, calcularás la proporción de empleados que abandonaron la empresa (tienen un valor de Attrition 1 ) 
# para cada valor de RelationshipSatisfaction.


# Media de la poblacion total 
mean_attrition_pop = attrition_pop.groupby('RelationshipSatisfaction', observed=False)['Attrition'].mean()

# Media de la muestra aleatoria simple
mean_attrition_srs = attrition_srs.groupby('RelationshipSatisfaction', observed=False)['Attrition'].mean()

# Media de la muestra estratificada
mean_attrition_strat = attrition_strat.groupby('RelationshipSatisfaction', observed=False)['Attrition'].mean()

# Media de la muestra de clusteres
mean_attrition_clust = attrition_clust.groupby('RelationshipSatisfaction', observed=False)['Attrition'].mean()



# Print the result
print('\n\n')
print(f'Media poblacional:\n\n {mean_attrition_pop}')
print('\n\n')
print(f'Media muestra aleatoria simple:\n\n {mean_attrition_srs}')
print('\n\n')
print(f'Media muestra estratificada:\n\n {mean_attrition_strat}')
print('\n\n')
print(f'Media muestra de clusteres:\n\n {mean_attrition_clust}')
print('\n\n')

#---------------------------------------------------------------
# Grafico

# Graficar comparación
categories = ['High', 'Low', 'Medium', 'Very_High']
plt.figure(figsize=(12, 8))



# Población
plt.plot(categories, mean_attrition_pop, 
         'o-', label='Población', lw=2, markersize=10)

# Muestras
plt.plot(categories, mean_attrition_srs, 
         's--', label='Aleatorio Simple', alpha=0.7)

plt.plot(categories, mean_attrition_strat, 
         'd--', label='Estratificado', alpha=0.7)

plt.plot(['High', 'Medium'], mean_attrition_clust, 
         'x-', label='Conglomerados', lw=3, markersize=12)


plt.title('Comparación de Métodos de Muestreo por Categoría')
plt.ylabel('Tasa de Rotación')
plt.xlabel('Categorías de Satisfacción')
plt.legend()
plt.grid(alpha=0.3)
plt.show()

#--------------------------------------------------------------


# Conclusion
# Los números son todos bastante similares, con la notable excepción de que el muestreo por conglomerados 
# solo da resultados para los conglomerados incluidos en la muestra.


# Conclusión General
# 1. Muestreo estratificado es el más preciso para estimar parámetros por subgrupos
#
# 2. Muestreo por conglomerados:
#       - Proporciona solo información parcial
#       - Introduce mayor sesgo en las estimaciones
#       - Su principal ventaja es la practicidad operativa, no la precisión
#
# 3. DataCamp tiene razón:
#       - Los valores están en rangos similares (12-23% vs 14-20% poblacional)
#       - La limitación clave de conglomerados es la cobertura incompleta