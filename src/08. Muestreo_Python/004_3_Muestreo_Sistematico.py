# ¿El muestreo sistemático es OK?
#
#  El muestreo sistemático tiene un problema: si los datos se han ordenado, 
# o hay algún tipo de patrón o significado detrás del orden de las filas, 
# la muestra resultante puede no ser representativa de toda la población. 
# 
# El problema puede resolverse barajando las filas, pero entonces el muestreo sistemático es equivalente 
# al muestreo aleatorio simple.
#
# Aquí verás cómo determinar si hay o no un problema.

import pandas as pd
import matplotlib.pyplot as plt
import os

# Obtener ruta base del archivo
base_path = os.path.dirname(os.path.abspath(__file__))
ruta_archivo = os.path.join(base_path, "..", "..", "Archivos", "attrition_pop.csv")


# Importa el excel
attrition_pop = pd.read_csv( ruta_archivo)  


#-------------------------------------------------
# Ejercicio 1: 

# Añade una columna índice a attrition_pop, asignando el resultado a attrition_pop_id.
attrition_pop_id = attrition_pop.reset_index()

# Crea un gráfico de dispersión de YearsAtCompany frente a index para attrition_pop_id utilizando pandas .plot().
attrition_pop_id.plot(x='index', y='YearsAtCompany', kind='scatter', title='Sin aplicar muestreo')



# Interpretación del primer gráfico (instrucción 1/3)
# 
# El gráfico de dispersión muestra cómo varía la antigüedad de los empleados (YearsAtCompany)
# en función del índice original de cada fila. En lugar de aparecer distribuidos al azar, 
# los puntos trazan una tendencia clara: a medida que el índice aumenta, también lo hacen los años en la compañía. 
# Esto indica que el DataFrame estaba ordenado —o al menos parcialmente estructurado— según la antigüedad del empleado.
#
#
# Observaciones clave
#   - Se aprecia una pendiente ascendente: los empleados con más años en la empresa ocupan índices más altos.
#
#   - Existen tramos uniformes donde la antigüedad se mantiene similar antes de cambiar bruscamente, 
#     sugiriendo agrupaciones por rangos de experiencia.
#
#   - La dispersión no es aleatoria; el orden original codifica información sobre la variable de interés.
#
#
# Implicaciones para el muestreo sistemático
# 
# Si aplicas muestreo sistemático directamente sobre este conjunto ordenado (p. ej., cada k-ésima fila), 
# tu muestra reflejará ese patrón de antigüedad y no será representativa de toda la población. 
# En el siguiente paso (instrucción 2/3) rompes este sesgo barajando los datos para eliminar cualquier orden preexistente. 
# Esto demuestra por qué, sin aleatorizar, el muestreo sistemático puede generar estimaciones sesgadas.

#----------------------------------------------------------------------------------------
# Ejercicio 2


# Baraja aleatoriamente las filas de attrition_pop.
attrition_shuffled = attrition_pop.sample(frac=1)

# Restablece los índices de las filas y añade una columna de índice a attrition_pop.
attrition_shuffled = attrition_shuffled.reset_index(drop=True).reset_index()

# Repite el diagrama de dispersión de YearsAtCompany frente a index, esta vez utilizando attrition_shuffled.
attrition_shuffled.plot(x='index', y='YearsAtCompany', kind='scatter', title='Aplicando Muestreo Simple')


# Interpretación del segundo gráfico (Instrucción 2/3)
# 
# Este scatter plot traza YearsAtCompany frente al índice tras haber barajado aleatoriamente las filas. 
# A diferencia del primer gráfico, aquí los puntos quedan distribuidos sin ninguna tendencia evidente, 
# formando una “nube” horizontal. Esto demuestra que el sample(frac=1) rompió cualquier orden preexistente
# basado en la antigüedad.
#
#
# Observaciones clave 
#
#    - Los puntos ocupan todo el rango de años de manera dispersa, sin pendiente ni agrupaciones claras.
#
#   - No se aprecia correlación entre el índice (posición en el DataFrame) y YearsAtCompany.
#
#   - La distribución parece uniforme en torno a cada valor de antigüedad, lo que refleja un muestreo verdaderamente aleatorio.
#
#
# Implicaciones para el muestreo sistemático
# 
# Al eliminar el orden original, cualquier selección de cada k-ésima fila (muestreo sistemático) 
# sobre este DataFrame barajado evitará sesgos vinculados a la antigüedad. 
# En otras palabras, ahora puedes aplicar .iloc[::k] con la confianza de que tu muestra
# representará bien la variabilidad de YearsAtCompany.



# (Continuacion ejercicio) Muestreo Sistematico

# Configurar el tamano de muestra en 70 registros
sample_size = 70

# Calcula el tamaño de la población a partir de attrition_pop.
pop_size = len(attrition_pop)

# Calcula el intervalo entre las filas a muestrear.
interval = pop_size // sample_size   # Division ( // ): Deja solo el entero de la division y quita la parte fraccionaria

# Muestrea sistemáticamente attrition_shuffled para obtener las filas de la población en cada interval, 
# empezando por 0; asigna las filas a attrition_sys_samp.
attrition_sys_samp = attrition_shuffled.iloc[::interval]


attrition_sys_samp.plot(x='index', y='YearsAtCompany', kind='scatter', title="Muestreo Sistematico")

# Print the sample
print(attrition_sys_samp)


# Interpretación del gráfico de muestreo sistemático
# 
# 1. ¿Qué muestra el gráfico?
# 
# El diagrama de dispersión traza la columna YearsAtCompany frente al índice de cada registro tras aplicar muestreo sistemático. 
# Cada punto representa un empleado seleccionado de manera periódica (por ejemplo, cada 70 filas si ese fuera el intervalo).
# Observamos la distribución de antigüedad de los empleados a lo largo del rango total de datos.
#
#
# 2. Representatividad de la muestra
# 
#   - La nube de puntos cubre todo el rango de índices desde el inicio hasta casi el final de la población, 
#     lo que sugiere que no hemos “saltado” grandes secciones.
#
#   - La concentración de valores entre 0 y 10 años indica que la muestra refleja la mayoría de la población, 
#      donde la mayor parte de empleados tiene poca antigüedad.
#
#   - Algunos puntos aislados en valores altos (20–30 años) actúan como outliers, confirmando que nuestro muestreo 
#     también captura los casos extremos.
#
# 
# 3. Posibles patrones y sesgos
# 
#   - Si existiera un patrón en el orden original (por ejemplo, ordenados por departamento o antigüedad), 
#     el muestreo sistemático podría sobre- o subrepresentar ciertos grupos.
#
#   - Al no ver franjas vacías ni concentraciones periódicas de puntos, no hay un indicio claro de sesgo por ordenamiento. 
#      Esto implica que, tras barajar (shuffle), aplicar un salto constante es, en la práctica, equivalente a un muestreo aleatorio simple.
#
# 4. ¿El muestreo sistemático es adecuado?
# 
#   - La uniformidad del diagrama sugiere que la muestra es representativa de la población en términos de YearsAtCompany.
#
#   - No se aprecian huecos ni agrupamientos regulares que delaten un patrón residual.
#
#   - Por lo tanto, podemos concluir que el muestreo sistemático aplicado (tras barajar el DataFrame) 
#     es válido y ofrece una buena aproximación de la distribución original.


#-------------------------------------------------------------------
plt.show()


# Pregunta:
# ¿Una muestra sistemática produce siempre una muestra similar a una muestra aleatoria simple?
# No. Esto no es cierto si los datos están ordenados de alguna manera.

# Conclusion:
# El muestreo sistemático tiene problemas cuando los datos están ordenados o contienen un patrón. 
# Barajar las filas lo hace equivalente a un muestreo aleatorio simple.