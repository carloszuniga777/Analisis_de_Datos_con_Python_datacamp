# Visualizar la desviación típica con gráficos de líneas
# 
# En el último ejercicio, vimos cómo ha cambiado a lo largo del tiempo la media de millas por galón que alcanzan los coches.
# Ahora utilicemos un gráfico lineal para visualizar cómo ha cambiado la distribución de millas por galón a lo largo del tiempo.

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


# Make the shaded area show the standard deviation
g = sns.relplot(
            kind='line',       # Grafico Lineas
            data=mpg,          # dataframe 
            x='model_year',    # eje x: Tiempo
            y='mpg',           # eje y: Eficiencia de combustible 
            ci='sd'            # Desviación estándar  
            )

# 1. Título principal usando el objeto Figure
g.figure.suptitle('Distribución Millas por galon alcanzadas de los coches\n a lo largo del tiempo', 
                  fontsize=10, y=0.95) 

# 2. Etiquetas globales para ejes X e Y
g.set_axis_labels("Tiempo (model_year)", "Eficiencia de combustible (mpg)", fontsize=10)


# 3. Reserva espacio para el título superior 
plt.subplots_adjust(top=0.85)  

# Show plot
plt.show()

#------------------------------------------------------
# Explicación del gráfico
# La línea azul central representa la media (promedio) de millas por galón (mpg) para cada año modelo. 
# Muestra la tendencia central del consumo de combustible a lo largo del tiempo.
# 
# La sombra azul ahora representa la desviación estándar (sd) de los datos en cada año. 
# Esto es diferente al intervalo de confianza que vimos antes. Veamos qué significa:



# Interpretación de la desviación estándar (sd) en este contexto:
# 
# 1. Medida de dispersión:
# La desviación estándar indica cuánto se dispersan los valores individuales de mpg alrededor de la media en cada año.
#   - Sombra estrecha = Baja dispersión (los coches tienen consumos similares)
#   - Sombra ancha = Alta dispersión (grandes diferencias de consumo entre coches)
#
# 2. Cálculo visual:
# Para cada año, el rango sombreado abarca:
# 
# Límite inferior = Media - 1 Desviación Estándar
# Límite superior = Media + 1 Desviación Estándar
# 
# Contiene aproximadamente el 68% de los vehículos de ese año (en una distribución normal).



# Análisis del gráfico paso a paso:
# 
# 1. Tendencia general (línea azul):
# Confirma que los coches mejoraron su eficiencia con los años:
#   - 1970: ~18 mpg
#   - 1982: ~30 mpg
# 
# 2. Cambios en la dispersión (sombra azul):
#  - 1970-1975: Sombra estrecha
#        → Coches con consumos similares (baja diversidad tecnológica)
#  
#  - 1976-1982: Sombra se ensancha progresivamente
# → Mayor variabilidad en la eficiencia entre modelos



# Conclusión del ejercicio:
# 
# El gráfico revela dos fenómenos simultáneos:
#   1. Mejora general en eficiencia (línea ascendente)
#   2. Aumento en la desigualdad tecnológica (sombra más ancha)
#
# Esto refleja:
#  - Respuestas heterogéneas de fabricantes a regulaciones
#  - Segmentación del mercado (ej. coches económicos vs. deportivos)
#  - Innovación rápida pero desigual en motores
#
# 💡 Insight clave: Mientras el consumo promedio mejoró, la brecha entre los coches más 
#  y menos eficientes se amplió con el tiempo.
#
#
# A diferencia del gráfico en el último ejercicio, este gráfico nos muestra la distribución de millas 
# por galón para todos los coches en cada año.
