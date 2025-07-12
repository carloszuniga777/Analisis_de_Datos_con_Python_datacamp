# En este capítulo, crearás y personalizarás gráficos que visualizan la relación entre dos variables cuantitativas. 
# Para ello, utilizarás gráficos de dispersión y de líneas para explorar cómo cambia el nivel de contaminación atmosférica 
# en una ciudad a lo largo de un día y cómo se relacionan los caballos de potencia con la eficiencia del combustible en los coches. 
# También verás otra gran ventaja de utilizar Seaborn: ¡la posibilidad de crear fácilmente subtramas en una sola figura!

# Crear subtramas con columna y fila
# 
# Hemos visto en ejercicios anteriores que los alumnos con más faltas ("absences") tienden a tener notas finales más bajas ("G3"). 
# ¿Se mantiene esta relación independientemente de cuánto tiempo estudien los alumnos cada semana?
#
# Para responder a esto, observaremos la relación entre el número de faltas de asistencia a clase de un alumno 
# y su calificación final en el curso, creando subtramas separadas en función del tiempo de estudio semanal de cada alumno ("study_time").

# Import Matplotlib, pandas, and Seaborn
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import os


# Obtener ruta base del archivo
base_path = os.path.dirname(os.path.abspath(__file__))
ruta_archivo = os.path.join(base_path, "..", "..", "Archivos", "student_data.csv")

# Read in the Netflix CSV as a DataFrame
student_data = pd.read_csv(ruta_archivo)

#---------------------------------------------
# Ejemplo 1: Modifica el código para crear un gráfico de dispersión para cada nivel de la variable "study_time", ordenado en columnas.


# relplot genera multiples graficos de dispecion (kind="scatter") organizados en columnas (col='study_time')

# Grafico 1:

g = sns.relplot(
            kind="scatter",            # Tipo de grafico: Dispercion
            data=student_data,         # Dataframe     
            x="absences",              # Eje x: Numero de ausencias
            y="G3",                    # Eje y: Califacion final 
            col='study_time',           # Divide el gráfico en columnas según los valores únicos de study_time (tiempo de estudio).
           
           # col_wrap=2,  # Organiza en máximo 2 columnas
            height=3.5,   # Altura de cada subplot
            aspect=1.2    # Relación ancho/alto
           )

# 1. Título principal usando el objeto Figure
g.figure.suptitle('Relación ausencias-calificación por tiempo de estudio', 
                  fontsize=14, y=1)  # y controla posición vertical

# 2. Etiquetas globales para ejes X e Y
g.set_axis_labels("Número de ausencias", "Calificación final (G3)", fontsize=10)


# 3. Personalizar títulos de cada columna
g.set_titles("Tiempo estudio: {col_name}", fontsize=11, pad=10)  # Pad aumenta espacio


# 5. Ajuste final para evitar cortes
g.tight_layout(pad=2.0)        # Aumenta espacio entre elementos
plt.subplots_adjust(top=0.85)  # Reserva espacio para el título superior 


#--------------------------------------------------------------------------------
#Ejemplo 2: Adapta tu código para crear un gráfico de dispersión para 
# cada nivel del tiempo de estudio semanal de un alumno, esta vez ordenado en filas.

# Grafico 2:
         
# relplot genera multiples graficos de dispecion (kind="scatter") organizados en filas (row='study_time')

g = sns.relplot(
            kind="scatter",            # Tipo de grafico: Dispercion
            data=student_data,         # Dataframe     
            x="absences",              # Eje x: Numero de ausencias
            y="G3",                    # Eje y: Califacion final 
            row='study_time',           # Divide el gráfico en columnas según los valores únicos de study_time (tiempo de estudio).

            height=3,          # Altura de cada subgráfico
            aspect=1.8,        # Relación ancho/alto de cada subgráfico  
           )

# 1. Título principal usando el objeto Figure
g.figure.suptitle('Relación ausencias-calificación\n por tiempo de estudio', 
                  fontsize=12, y=0.98)  # y controla posición vertical

# 2. Etiquetas globales para ejes X e Y
g.set_axis_labels("Número de ausencias", "Calificación final (G3)", fontsize=10)


# 3. Personalizar títulos de cada fila
g.set_titles("Tiempo estudio: {row_name}\n", fontsize=11, pad=5)  # Pad aumenta espacio


# 5. Ajustar espacios críticos
g.tight_layout(pad=1.0)        # Aumenta espacio entre elementos
plt.subplots_adjust(
    top=0.88,                   # Más espacio superior para título
    hspace=0.4                  # Espacio vertical entre filas
    )  


#-----------------------------------------------------------------

# Display plot
plt.show()
