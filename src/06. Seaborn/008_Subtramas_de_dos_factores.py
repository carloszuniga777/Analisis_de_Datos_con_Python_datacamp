# Crear subtramas de dos factores
# Sigamos examinando el conjunto de datos student_data de alumnos de secundaria. 
# Aquí queremos responder a la siguiente pregunta: ¿la nota del primer semestre de un alumno ("G1") 
# tiende a correlacionarse con su nota final ("G3")?
# 
# Hay muchos aspectos de la vida de un alumno que pueden dar lugar a una nota final más alta o más baja en la clase.
# Por ejemplo, algunos alumnos reciben apoyo educativo adicional de su centro escolar ("schoolsup") 
# o de su familia ("famsup"), lo que podría traducirse en mejores notas. 
# 
# Intentemos controlar estos dos factores creando subtramas en función de si el alumno recibió apoyo educativo adicional 
# de su escuela o de su familia.


# Import Matplotlib, pandas, and Seaborn
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import os


# Obtener ruta base del archivo
base_path = os.path.dirname(os.path.abspath(__file__))
ruta_archivo = os.path.join(base_path, "..", "..", "Archivos", "student_data2.csv")

# Read in the Netflix CSV as a DataFrame
student_data = pd.read_csv(ruta_archivo)

#---------------------------------------------
# Ejemplo 1: Modifica el código para crear un gráfico de dispersión para cada nivel de la variable "study_time", ordenado en columnas.


# relplot genera multiples graficos de dispecion (kind="scatter") organizados en columnas (col='study_time')

# Grafico 1:

g = sns.relplot(
            kind="scatter",            # Tipo de grafico: Dispercion
            data=student_data,         # Dataframe     
            x="G1",                    # Eje x: Nota del primer semestre
            y="G3",                    # Eje y: Nota final
            col="schoolsup",           # Divide en columnas: Apoyo escolar extra (sí/no)
            col_order=["yes", "no"],   # Orden columnas: Primero 'sí apoyo', luego 'no apoyo' 
            row='famsup',              # Divide en filas: Apoyo familiar educativo (sí/no) 
            row_order=["yes", "no"]    # Orden filas: Primero 'sí apoyo', luego 'no apoyo'
            )
        

# 1. Título principal usando el objeto Figure
g.figure.suptitle('Relación entre notas del primer semestre (G1) y notas finales (G3)', 
                  fontsize=14, y=0.95)  # y controla posición vertical

# 2. Etiquetas globales para ejes X e Y
g.set_axis_labels("Notas primer semestre (G1)", "Calificación final (G3)", fontsize=10)


# 3. Etiquetas para cada subgráfico
g.set_titles(
    col_template="Apoyo escolar: {col_name}",
    row_template="Apoyo familiar: {row_name}",
    fontsize=9
)

# 4. Ajuste final para evitar cortes
g.tight_layout(pad=2.0)        # Aumenta espacio entre elementos
plt.subplots_adjust(top=0.85)  # Reserva espacio para el título superior 


#-----------------------------------------------------------------

# Display plot
plt.show()

# Conclusion:
# Parece que la nota del primer semestre sí correlaciona con la nota final, 
# independientemente del tipo de apoyo que recibió el estudiante.