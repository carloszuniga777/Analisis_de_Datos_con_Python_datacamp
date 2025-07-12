# Interpretación de gráficos lineales
# En este ejercicio, seguiremos explorando el conjunto de datos mpg de Seaborn, 
# que contiene una fila por modelo de coche e incluye información como el año de fabricación del coche, 
# su eficiencia de combustible (medida en "millas por galón" o "M.P.G") y su país de origen (, Europa o Japón).
#
# ¿Cómo ha cambiado con el tiempo la media de millas por galón que alcanzan estos coches? 
# ¡Utilicemos gráficos lineales para averiguarlo!


# Import Matplotlib, pandas, and Seaborn
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import os


# Obtener ruta base del archivo
base_path = os.path.dirname(os.path.abspath(__file__))
ruta_archivo = os.path.join(base_path, "..", "..", "Archivos", "mpg.csv")

# Read in the Netflix CSV as a DataFrame
mpg = pd.read_csv(ruta_archivo)

#---------------------------------------------


# Create line plot
g = sns.relplot(
            kind='line',       # Grafico Lineas
            data=mpg,          # dataframe 
            x='model_year',    # eje x: Tiempo
            y='mpg',           # eje y: Eficiencia de combustible 
            )

# 1. Título principal usando el objeto Figure
g.figure.suptitle('Millas por galon alcanzadas por los coches a lo largo del tiempo', 
                  fontsize=10, y=0.95) 

# 2. Etiquetas globales para ejes X e Y
g.set_axis_labels("Tiempo (model_year)", "Eficiencia de combustible (mpg)", fontsize=10)


# 3. Reserva espacio para el título superior 
plt.subplots_adjust(top=0.85)  

# Show plot
plt.show()

#------------------------------------------------------

# Sombra Azul:
# La sombra azul alrededor de la línea representa el intervalo de confianza (IC), 
# típicamente del 95%, para la estimación de la media de millas por galón (mpg) en cada año. 
# Es una característica fundamental de los gráficos de línea en Seaborn cuando se usa kind='line'.

# Explicación detallada:
# 
# 1. ¿Qué calcula?
# Para cada año (model_year), Seaborn:
#   - Calcula la media de mpg (y)
#   - Calcula un rango de incertidumbre alrededor de esa media usando técnicas estadísticas (por defecto, bootstrapping).
#
# 2. Interpretación práctica:
# - Línea central: Valor promedio de mpg para ese año.
# - Sombra azul: Rango donde se espera que esté la verdadera media poblacional con un 95% de confianza.
#
# Ejemplo: Si en 1980 la media es 20 mpg con IC [18, 22], significa que tenemos un 95% de confianza 
# en que la verdadera media de todos los coches de 1980 está entre 18 y 22 mpg.  
# 
# 3. ¿Por qué es importante?
# - Si la sombra es estrecha → Alta precisión en la estimación (poca variabilidad entre coches del mismo año).
# - Si la sombra es ancha → Baja precisión (mucha variabilidad entre coches o muestra pequeña).
# - Si las sombras de años consecutivos no se superponen → Es probable que el cambio en la media sea estadísticamente significativo.




# # Conclusion:
# - El promedio de millas por galón ha aumentado generalmente con el tiempo.
# 
# - El intervalo de confianza del 95 % para la media de millas por galón 
#   en 1970 es de aproximadamente 16 - 19,5 millas por galón.
#
# - Este gráfico asume que nuestros datos son una muestra aleatoria 
#   de todos los automóviles en EE. UU., Europa y Japón.
#
# - El gráfico muestra que la eficiencia de combustible (mpg) ha aumentado significativamente con los años, evidenciado por:
#   1. Tendencia ascendente clara de la línea.
#   2.Intervalos de confianza (sombras) que no se superponen entre años extremos 
#     (ej. años 70 vs años 80), confirmando que el aumento es estadísticamente significativo.
#   3.La pendiente se acelera después de ~1975, sugiriendo avances tecnológicos o cambios normativos.