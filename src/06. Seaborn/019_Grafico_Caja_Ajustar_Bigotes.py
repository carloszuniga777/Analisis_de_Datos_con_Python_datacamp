# Ajustar los bigotes
# En la lección vimos que hay múltiples formas de definir los bigotes en un diagrama de caja. 
# En esta serie de ejercicios, seguiremos utilizando el conjunto de datos student_data para comparar 
# la distribución de las calificaciones finales ("G3") entre los estudiantes que mantienen una relación romántica y los que no. 
# 
# Utilizaremos la variable "romantic", que es un indicador sí/no de si el alumno tiene una relación romántica.

# Import Matplotlib, pandas, and Seaborn
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import os


# Obtener ruta base del archivo
base_path = os.path.dirname(os.path.abspath(__file__))
ruta_archivo = os.path.join(base_path, "..", "..", "Archivos", "student_data2.csv")

# Read in the student_data CSV as a DataFrame
student_data = pd.read_csv(ruta_archivo)

#---------------------------------------------
# Ejercicio 1:  
# Ajusta el código para que los bigotes del gráfico de caja se extiendan hasta 0,5 * IQR. 
# Recordemos que el IQR es el rango intercuartílico.


# Set the whiskers to 0.5 * IQR
g = sns.catplot(
             kind='box',                  # Tipo de grafico: caja
             data=student_data,           # Dataframe
             x='romantic',                # Variable categorica
             y='G3',                      # Notas finales
             whis=0.5,                    # Ajusta los bigotes en 0.5  

             palette=["#3498db", "#e74c3c"],   # Personaliza los Colores 
            )

# 1. Título principal usando el objeto Figure
g.figure.suptitle('Relación entre estudiantes con relaciones romanticas\n y calificaciones finales\n Bigotes en 0.5', fontsize=10, y=0.99) 


# 2. Etiquetas globales para ejes X e Y
g.set_axis_labels( "Relacion romantica", "Calificaciones", fontsize=10)


# 3. Ajustar márgenes (top = espacio superior) para que el titulo no superponga al grafico
plt.subplots_adjust(top=0.90)  # 85% del espacio para gráfico + título




#------------------------------------------------------------------
# Ejercicio 2:
# Cambia el código para que los bigotes se extiendan hasta los percentiles 5 y 95.


# Extend the whiskers to the 5th and 95th percentile
g = sns.catplot(
             kind='box',                  # Tipo de grafico: caja
             data=student_data,           # Dataframe
             x='romantic',                # Variable categorica
             y='G3',                      # Notas finales
             whis=[5, 95],                # Ajusta los bigotes en percentil 5 y 95

             palette=["#3498db", "#e74c3c"],   # Personaliza los Colores 
            )

# 1. Título principal usando el objeto Figure
g.figure.suptitle('Relación entre estudiantes con relaciones romanticas\n y calificaciones finales.\n Bigotes en Percentil 5 y 95', fontsize=10, y=0.99) 


# 2. Etiquetas globales para ejes X e Y
g.set_axis_labels( "Relacion romantica", "Calificaciones", fontsize=10)


# 3. Ajustar márgenes (top = espacio superior) para que el titulo no superponga al grafico
plt.subplots_adjust(top=0.90)  # 85% del espacio para gráfico + título

#------------------------------------------------------------------
# Ejercicio 3: Cambia el código para que los bigotes se extiendan hasta los valores mínimo y máximo.

# Set the whiskers at the min and max values
g = sns.catplot(
             kind='box',                  # Tipo de grafico: caja
             data=student_data,           # Dataframe
             x='romantic',                # Variable categorica
             y='G3',                      # Notas finales
             whis=[0, 100],               # Ajusta los bigotes en minimo y maximo 

             palette=["#3498db", "#e74c3c"],   # Personaliza los Colores 
            )

# 1. Título principal usando el objeto Figure
g.figure.suptitle('Relación entre estudiantes con relaciones romanticas\n y calificaciones finales.\n Bigotes en minimo y maximo', fontsize=10, y=0.99) 


# 2. Etiquetas globales para ejes X e Y
g.set_axis_labels( "Relacion romantica", "Calificaciones", fontsize=10)


# 3. Ajustar márgenes (top = espacio superior) para que el titulo no superponga al grafico
plt.subplots_adjust(top=0.90)  # 85% del espacio para gráfico + título


#------------------------------------------------------------------
# Show plot
plt.show()

#------------------------------------------------------------------

# ¿Por qué se ajustan los bigotes con whis?
#
# Los bigotes en un diagrama de caja definen el rango de valores "normales" o no atípicos. Por defecto:
# - Los bigotes se extienden hasta 1.5 × IQR desde los cuartiles
# - Cualquier valor fuera de este rango se considera valor atípico (outlier)

# Opciones de ajuste con whis:
# 
# 1. whis=2.0 (Extender bigotes a 2.0 × IQR)
#
#                   sns.catplot(kind='box', whis=2.0, ...)
#
#   - Efecto: Los bigotes se extienden más lejos
#   - Resultado: Menos valores serán considerados atípicos
#   - Uso típico: Cuando quieres ser más tolerante con la variabilidad de los datos
#
# 2. whis=[5, 95] (Mostrar percentiles 5 y 95)
#
#               sns.catplot(kind='box', whis=[5, 95], ...)
# 
#   - Efecto: Los bigotes mostrarán exactamente el percentil 5 (inferior) y 95 (superior)
#   - Resultado: El 90% central de tus datos estará dentro de los bigotes
#   - Uso típico: Cuando quieres enfocarte en el rango central ignorando extremos
#
# 3. whis=[0, 100] (Mostrar valores mínimo y máximo)
#
#               sns.catplot(kind='box', whis=[0, 100], ...)
#   - Efecto: Los bigotes llegarán al valor mínimo y máximo absolutos
#   - Resultado: No se mostrarán valores atípicos
#   - Uso típico: Cuando quieres ver el rango completo sin outliers


# ¿Cómo elegir el valor de whis?
#--------------------------------------------------------------------------------
#   Valor	        Cuando usarlo	                    Sensibilidad a outliers
#---------------------------------------------------------------------------------
# whis=1.5	    Detección estricta de anomalías	            Alta
# 
# whis=2.0	    Análisis general de distribuciones	        Media
# 
# whis=[5,95]	Enfocarse en el núcleo principal de datos	Baja
# 
# whis=[0,100]	Ver el rango completo sin outliers	        Nula


# Regla práctica:
#  - Comienza con el valor por defecto (whis=1.5)
#
# - Si hay demasiados outliers que dificultan la lectura, prueba con whis=2.0
#
# - Para análisis específicos de rangos percentílicos, usa valores personalizados

# Conclusion:
# La nota media es la misma entre estos dos grupos, 
# pero la nota máxima es más alta entre los estudiantes que no están en una relación romántica.