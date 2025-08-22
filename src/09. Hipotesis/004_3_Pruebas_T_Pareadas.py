# Pruebas t pareadas
# 
# La prueba ANOVA no te decía qué categorías de modo de envío tenían diferencias significativas 
# en los precios de los paquetes. Para determinar con precisión qué categorías tenían diferencias, 
# podrías utilizar pruebas t pareadas.

import pandas as pd
import pingouin
import os

# Obtener ruta base del archivo
base_path = os.path.dirname(os.path.abspath(__file__))
ruta_archivo = os.path.join(base_path, "..", "..", "Archivos", "late_shipments.csv")


# Importa el excel
late_shipments = pd.read_csv( ruta_archivo)  


#----------------------------------------------
# Ejemplo 1
#----------------------------------------------
# Ejecuta pruebas t pareadas sobre la variable pack_price de late_shipments, 
# agrupando por shipment_mode, sin hacer ningún ajuste del valor p.


# pingouin.pairwise_tests(...)
#   - Es una función que compara dos grupos a la vez (por eso “pairwise” = por pares).
#   - Aquí compara los precios entre cada par de modos de envío:
#            - Air ✈ vs Air Charter ✈✈
#            - Air ✈ vs Ocean 🚢
#            - Air Charter ✈✈ vs Ocean 🚢


# Perform a pairwise t-test on pack price, grouped by shipment mode
pairwise_results = pingouin.pairwise_tests(data=late_shipments,
                                           dv='pack_price',            # dv (variable dependiente): el precio del paquete. | Es la columna que quieres comparar: el precio del paquete
                                           between='shipment_mode',    # Indica que los grupos se forman según el modo de envío (por ejemplo: Air, Air Charter, Ocean).
                                           padjust='none'              # No se ajustan los valores p por comparaciones múltiples (se dejan “crudos”) 
                                          ) 




# Print pairwise_results
print(pairwise_results)

# 🛫 Contexto del ejercicio
# Tienes una tabla (late_shipments) con información de envíos. Cada envío tiene:
#   - pack_price → el precio del paquete.
#   - shipment_mode → el modo de envío (por ejemplo: Air, Air Charter, Ocean).
# 
# Lo que quieres saber es:
# “¿El precio promedio de los paquetes es diferente según el modo de envío?”


# Cómo leer el resultado
# La tabla que ves es el resumen de las comparaciones:
#
# Comparación	                p-unc (valor p)	                Qué significa
#-----------------------------------------------------------------------------------------------------------
# Air vs Air Charter	    8.748e-75 (muy pequeño)	        Hay una diferencia enorme en el precio promedio.
# Air vs Ocean	            6.935e-71 (muy pequeño)	        También hay una diferencia enorme.
# Air Charter vs Ocean	    3.123e-03 (0.003)	            Hay diferencia, pero menos marcada.


# 🧠 Explicado sin estadística
# Imagina que tienes tres tipos de transporte y quieres saber si cobran lo mismo.
#   - Tomas muchos envíos de cada tipo.
#   - Calculas el precio promedio de cada grupo.
#   - Luego, para cada par de grupos, haces una “prueba” que te dice si la diferencia que ves podría ser solo 
#     por casualidad o si es tan grande que probablemente sea real.
#
# El valor p es como una alarma:
#    - Si es muy pequeño (por ejemplo, menor a 0.05), significa que es muy poco probable que la diferencia 
#      sea por azar → hay diferencia real.
#    - Si es grande, no hay evidencia suficiente para decir que los precios son distintos.
# 
# En tu caso, todos los valores p son pequeños, así que los precios promedio sí cambian según el modo de envío.

  
#-------------------------------------------------------------
# Ejemplo 2
#-------------------------------------------------------------
# Modifica las pruebas t pareadas para utilizar el ajuste del valor p de Bonferroni.

# Modify the pairwise t-tests to use Bonferroni p-value adjustment
pairwise_results = pingouin.pairwise_tests(data=late_shipments, 
                                           dv='pack_price',            # dv (variable dependiente): el precio del paquete. | Es la columna que quieres comparar: el precio del paquete
                                           between='shipment_mode',    # Indica que los grupos se forman según el modo de envío (por ejemplo: Air, Air Charter, Ocean).
                                           padjust="bonf")

print('\n\n')

# Print pairwise_results
print(pairwise_results)

# 📦 El escenario
# Tienes datos de envíos (late_shipments) con:
#   - pack_price → el precio del paquete.
#   - shipment_mode → el tipo de transporte (Air ✈, Air Charter ✈✈, Ocean 🚢).
# Quieres saber si el precio promedio cambia según el tipo de transporte.


# Qué hace este código
# 1. Compara los precios entre cada par de modos de envío
#   - Air vs Air Charter
#   - Air vs Ocean
#   - Air Charter vs Ocean
#
# 2. Usa una “prueba t”
#   - Es como una lupa matemática que revisa si las diferencias de precio son reales o podrían ser pura casualidad.
#
# 3. padjust="bonf"
#   - Aquí está la novedad: antes comparabas sin ajustar nada, pero ahora aplicas el ajuste Bonferroni.
#   - Esto es como ser más estricto para decidir si algo es “diferente” cuando haces muchas comparaciones a la vez.
#   - ¿Por qué? Porque si comparas muchas veces, aumenta la probabilidad de encontrar diferencias “falsas” solo por azar. 
#     Bonferroni reduce ese riesgo.


# Cómo leer la tabla
#
#  Comparación	            p-unc (sin ajustar)	        p-corr (ajustado Bonferroni)	        ¿Diferencia real?
#---------------------------------------------------------------------------------------------------------------------
# Air vs Air Charter	    8.74e-75	                2.62e-74	                        Sí, diferencia enorme
# Air vs Ocean	            6.93e-71	                2.08e-70	                        Sí, diferencia enorme
# Air Charter vs Ocean	    0.0031	                    0.00937	                            Sí, diferencia moderada
#
#
#   - p-unc → valor p original (sin ajuste).
#   - p-corr → valor p corregido con Bonferroni.
# 
# Si el valor p corregido es menor que 0.05, decimos que la diferencia es estadísticamente significativa.



# 🧠 Explicado sin estadística
# Imagina que pruebas tres tipos de transporte y quieres saber si cobran distinto.
#   - Haces tres comparaciones.
#   - Sin ajuste, podrías equivocarte más fácilmente y pensar que hay diferencias cuando no las hay.
#   - Bonferroni es como un “filtro extra” que te obliga a estar más seguro antes de decir “sí, son distintos”.
#
# En este caso, incluso con el filtro extra, las diferencias siguen siendo claras.

#---------------------------------------------------------
# Pregunta:

# Utilizando los resultados de la corrección de Bonferroni y suponiendo un nivel de significación de 0,1,
# ¿para qué pares de modos de envío deberías rechazar la hipótesis nula de que los precios de los paquetes son iguales?

# Si tomamos un nivel de significación α = 0,1 (es decir, 10 % de tolerancia al error tipo I), 
# la interpretación de las comparaciones por pares sería así, 
# usando los valores p sin ajuste que aparecen en los resultados:

# Comparación	                p‑valor	        ¿p < 0,1?	    Significativa al 10 %
# ----------------------------------------------------------------------------
# Air vs Air Charter	       8,748 × 10⁻⁷⁵	    ✅	            Sí
# Air vs Ocean	               6,935 × 10⁻⁷¹   	    ✅	            Sí
# Air Charter vs Ocean	       3,123 × 10⁻³	        ✅	            Sí
# 
# 📌 Conclusión: Con α = 0,1, todas las comparaciones son estadísticamente significativas. 
# Por lo tanto, la opción correcta sería:
#
# "Ocean" y "Air Charter"; "Ocean" y "Air"; "Air Charter" y "Air".
#
# Significa que, con un nivel de significación del 10 %, los datos muestran evidencia suficiente para concluir 
# que los precios promedio de los paquetes son distintos entre cada par de modos de envío que comparaste.
#
# En otras palabras:
#   - Ocean vs Air Charter → el precio medio de enviar por barco no es igual al de enviar por avión chárter.
#   - Ocean vs Air → el precio medio de enviar por barco no es igual al de enviar por avión regular.
#   - Air Charter vs Air → el precio medio de enviar por avión chárter no es igual al de enviar por avión regular.
#
#💡 Interpretación práctica: el tipo de transporte influye de forma clara en el precio, 
# y esa diferencia no se debe al azar según la prueba estadística. Si fueras a tomar decisiones 
# comerciales (por ejemplo, elegir un modo de envío para optimizar costos o márgenes), podrías justificar 
# que cada modalidad tiene un rango de precios propio y diferenciado.