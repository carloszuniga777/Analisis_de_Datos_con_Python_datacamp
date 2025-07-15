# Crea e interpreta un diagrama de cajas
# Sigamos utilizando el conjunto de datos student_data. En un ejercicio anterior, exploramos la relación entre el estudio 
# y la nota final utilizando un diagrama de barras para comparar la nota final media ("G3") entre los estudiantes de diferentes 
# categorías de "study_time".

# En este ejercicio, intentaremos utilizar un diagrama de cajas para ver esta relación. Como recordatorio, 
# para crear un gráfico de caja tendrás que utilizar la función catplot() y especificar el nombre de la variable 
# categórica a poner en el eje x (x=____), el nombre de la variable cuantitativa a resumir en el eje y (y=____), 
# el DataFrame de pandas a utilizar (data=____), y el tipo de gráfico (kind="box").

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
# Utiliza sns.catplot() y el DataFrame student_data para crear un gráfico de caja con "study_time" en el eje x y "G3" en el eje y. 
# Establece el orden de las categorías en study_time_order

# Specify the category ordering
study_time_order = ["<2 hours", 
                    "2 to 5 hours", 
                    "5 to 10 hours", 
                    ">10 hours"]



# Creando un grafico de caja 
g = sns.catplot(
            kind='box',                  # Tipo de grafico: caja
            data=student_data,           # Dataframe
            x='study_time',              # Variable categorica
            y='G3',                      # Notas finales
            order=study_time_order,      # Ordena los datos de las categorias (study_time)
            ci=None,                     # Desactiva los intervalos de confianza   

             palette=["#3498db", "#e74c3c", "#2ecc71", "#f1c40f"],   # Colores 
             legend=False,                                                    # 👈 Esto elimina la leyenda de los colores
             height=6,                                                        # Altura de la figura en pulgadas
             aspect=1.2,                                                      # Relación ancho/alto (ancho = 6 * 1.5 = 9 pulgadas
            )

# 1. Título principal usando el objeto Figure
g.figure.suptitle('Relación entre horas de estudio y calificaciones finales', fontsize=10, y=0.99) 


# 2. Etiquetas globales para ejes X e Y
g.set_axis_labels( "Tiempo de estudio", "Calificaciones", fontsize=10)


# 3. Ajustar márgenes (top = espacio superior) para que el titulo no superponga al grafico
plt.subplots_adjust(top=0.90)  # 85% del espacio para gráfico + título





#------------------------------------------------------------------
# Show plot
plt.show()

#------------------------------------------------------------------
# Explicacion IA:

# Explicacion visual:
#
# 1. La caja central (el corazón del gráfico)
#
#   - Es el rectángulo que ves para cada categoría de horas de estudio.
#
#   - Contiene el 50% de los estudiantes normales: Los que no son ni los mejores ni los peores.
#   
#   - Línea horizontal dentro de la caja:
#           - Es la MEDIANA (el estudiante promedio).
#           - Ejemplo: Si está en 10, significa que la mitad del grupo tiene menos de 10 y la mitad más de 10.

# 2. Los bigotes (las "antenas" que salen de la caja)
#
#   - Muestran el rango donde están la MAYORÍA de estudiantes.
#
#   - El extremo del bigote inferior: El estudiante con notas más bajas (pero normal).
#
#   - El extremo del bigote superior: El estudiante con notas más altas (pero normal).
#
# 3. Puntos sueltos (si aparecen)
#
#   - Son estudiantes ATÍPICOS: O genios que sacaron notas increíbles, o alumnos con problemas graves.
#
#   - Ejemplo: Si ves un punto arriba de todo, es alguien que sacó 20 cuando el promedio es 10.



# Cómo Leer tu Gráfico Paso a Paso:
# 
#  1. Para "<2 horas":
#
#  - La caja empieza en ≈7.5 (Q1) y termina en ≈12.5 (Q3): El 50% central de estudiantes tiene entre 7.5 y 12.5.
#
#  - La línea en la caja (mediana) está en ≈10: La mitad del grupo sacó menos de 10, la mitad más de 10.
#
#  - Bigote inferior llega a ≈5: El peor alumno "normal" sacó 5.
# 
# - Bigote superior llega a ≈15: El mejor alumno "normal" sacó 15.

# - Punto en 1.75: Un alumno atípico que sacó muy malas notas (posible problema personal).
#
#
# 2. Para ">10 horas":
#
#   - La caja está más alta (digamos entre 9 y 14.5): Sus estudiantes normales son mejores.
#
#   - Mediana en 12: La mitad sacó más de 12.
#
#   - Sin puntos atípicos: Todos rindieron como se esperaba.



# Qué te Dice esto sobre el Estudio vs. Notas
# 
# Responde tu pregunta con hechos visuales:
#
# 1. ¿Estudiar más mejora notas?
#
#   - Mira la POSICIÓN de las cajas: Si la caja de ">10 horas" está MÁS ARRIBA que la de "<2 horas" → SÍ.
#
#   -  En tu gráfico: Las cajas suben al aumentar horas → Confirmas que estudiar más se relaciona con mejores notas.
#
# 2. ¿Es consistente la mejora?
#
#   - Mira el TAMAÑO de las cajas:
#           - Caja pequeña (ej: "5-10 horas"): Notas muy parejas (estudiantes homogéneos).
#           - Caja grande (ej: "<2 horas"): Notas muy dispersas (desde genios hasta alumnos con problemas).

# 3. ¿Hay excepciones?
#
#   - Puntos atípicos abajo (ej: 1.75 en "<2 horas"): Algunos estudiantes rinden MUCHO MENOS de lo esperado.
#
#   - Puntos atípicos arriba: Algunos son brillantes incluso sin estudiar.


# ¿Por qué usar esto y no gráficos de barras?
# 
# - Barras: Solo te muestran el PROMEDIO (una línea).
#       Ej: "<2 horas" promedio=10 → Oculta que hay desde 1.75 hasta 15.
#
# - Cajas: Te revela TODA la historia:
#       - Cuánto varían las notas.
#       - Si el promedio es engañoso.
#       - Quiénes son los casos excepcionales


# Interpretación Profesional en 1 Minuto
# 
# "Los diagramas de caja muestran que existe una correlación positiva entre horas de estudio y rendimiento académico: 
# grupos con más horas de estudio presentan distribuciones de notas más altas y consistentes.
# Sin embargo, en todos los grupos hay excepciones notables (ej: un alumno con <2 horas de estudio obtuvo 1.75), 
# sugiriendo que factores adicionales (motivación, habilidades innatas) también influyen significativamente."


# Señales de Alerta en tu Gráfico
# 1. Cajas que no suben: Si ">10 horas" tuviera la caja al mismo nivel que "<2 horas", tu hipótesis sería falsa.
#
# 2. Muchos puntos abajo: Si ">10 horas" tuviera puntos bajos, indicaría que estudiar mucho no garantiza buenas notas.
#
# En tu caso: El patrón es claro: más estudio → notas más altas.


# Conclusion:
# - La nota media entre los alumnos que estudian menos de 2 horas es de 10,0.
# - La línea en el medio de cada caja representa la mediana.