# Personalizar los gráficos de puntos
# Sigamos examinando datos de alumnos de secundaria, esta vez utilizando un gráfico de puntos para responder a la pregunta: 
# ¿influye la calidad de la relación familiar del alumno en el número de faltas que tiene en la escuela? 
# Aquí utilizaremos la variable "famrel", que describe la calidad de la relación familiar de un alumno de 1 (muy mala) a 5 (muy buena).
#
# Como recordatorio, para crear un gráfico de puntos, utiliza la función catplot() 
# y especifica el nombre de la variable categórica a poner en el eje x (x=____),
#  el nombre de la variable cuantitativa a resumir en el eje y (y=____), 
# el DataFrame de pandas a utilizar (data=____), y el tipo de gráfico categórico (kind="point").

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

# Graficos de puntos
# - Los graficos de puntos muestarn la media de una variable cuantitativa
# - Las líneas verticales representan intervalos de confianza del 95%

# Create a point plot of family relationship vs. absences
g = sns.catplot(
             kind='point',                # Tipo de grafico: puntos
             data=student_data,           # Dataframe
             x='famrel',                  # Variable categorica
             y='absences',                # Variable Cuantitativa
             capsize=0.2,                 # Controla el tamano de las 'tapas' que aparecen en los extremos de las barras de error  en los graficos de puntos, Estas líneas ayudan a visualizar mejor dónde terminan exactamente los intervalos de confianza 
             join=False                   # Elimina las uniones de los puntos
            )

# 1. Título principal usando el objeto Figure
g.figure.suptitle('Relación entre calidad de la relacion familiar del alumno y el numero de faltas en la escuela', fontsize=10, y=0.99) 


# 2. Etiquetas globales para ejes X e Y
g.set_axis_labels( "Relacion familiar", "Numero de ausencias", fontsize=10)


# 3. Ajustar márgenes (top = espacio superior) para que el titulo no superponga al grafico
plt.subplots_adjust(top=0.90)  # 85% del espacio para gráfico + título

# Show plot
plt.show()

#-----------------------------------------------------------------

# Intervalos de confianza (IC) (Lineas verticales)
# Los intervalos de confianza en un gráfico de puntos 
# se refieren específicamente a intervalos de confianza para la media de cada grupo.
# 
# ¿Qué significa esto?
# 
# Para cada categoría (en tu caso, cada valor de "famrel")
# Se calcula la media de la variable dependiente ("absences")
# Se estima el intervalo de confianza alrededor de esa media



# Interpretación práctica:
#
# El punto representa la media estimada de ausencias para cada nivel de relación familiar
# Las líneas verticales (barras de error) muestran el rango donde probablemente se encuentra la verdadera media poblacional
# 95% de confianza significa que si repitieras el estudio 100 veces,
# en 95 de esas veces la verdadera media estaría dentro de ese intervalo
#
# Ejemplo:
# 
# Si para "famrel = 3" tienes:
# - Media: 5.2 ausencias
# - IC 95%: [4.1, 6.3]
#
# Esto significa que puedes estar 95% seguro de que la verdadera media de ausencias para estudiantes 
# con relación familiar nivel 3 está entre 4.1 y 6.3.



# Por defecto, seaborn usa:
#
# Intervalos de confianza bootstrap
# Nivel de confianza del 95%
# Puedes cambiarlo con el parámetro ci (ej: ci=90 para 90% de confianza)

#---------------------------------------------------------

# Interpretación del Gráfico
#
# Descripción de los datos observados
# Patrón aparente: Se observa una tendencia descendente en el número promedio de ausencias a medida 
# que mejora la calidad de la relación familiar.


# Análisis por categorías:
#
# 1. Famrel = 1 (muy mala relación):
#   - Media: ~7.5 ausencias
#   - IC muy amplio (aproximadamente 3-10.5)
#   - Mayor variabilidad en los datos
#
# 2. Famrel = 2 (mala relación):
#   - Media: ~6 ausencias
#   - IC moderadamente amplio
#
# 3. Famrel = 3 (relación regular):
#   - Media: ~5.5 ausencias
#   - IC más estrecho, mayor precisión
#
# 4. Famrel = 4 (buena relación):
#   - Media: ~5 ausencias
#   - IC relativamente estrecho
#
# 5. Famrel = 5 (muy buena relación):
#   - Media: ~4 ausencias (la más baja)
#   - IC moderado

# Limitaciones estadísticas
# Problema principal: Los intervalos de confianza de las diferentes categorías se superponen considerablemente, 
# especialmente entre los niveles 1, 2, 3, 4 y 5.
# 
# Implicaciones:
#   - La alta variabilidad en los datos impide establecer diferencias estadísticamente significativas
#   - No se puede descartar que las diferencias observadas sean producto del azar
#   - Los intervalos amplios sugieren incertidumbre en las estimaciones

# Conclusión IA
# Respuesta a la pregunta: Aunque se observa una tendencia hacia menor ausentismo en estudiantes 
# con mejores relaciones familiares, no es posible establecer una asociación estadísticamente significativa 
# entre la calidad de la relación familiar y las ausencias escolares debido a la alta variabilidad en los datos, 
# evidenciada por los amplios intervalos de confianza que se superponen entre categorías.
# La evidencia es insuficiente para concluir que existe una influencia real de la calidad de la relación familiar 
# en el número de ausencias escolares.

# Conclusion Curso:
# Aunque el número promedio de ausencias es ligeramente menor entre los estudiantes con relaciones 
# familiares de mayor calidad, los grandes intervalos de confianza nos dicen que no podemos estar 
# seguros de que haya una asociación real aquí.