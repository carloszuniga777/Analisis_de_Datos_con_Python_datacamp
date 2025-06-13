import numpy as np
import matplotlib.pyplot as plt

# ---------Generacion de data aleatoria -------------------

np.random.seed(123)                                # Para reproducibilidad (opcional)

# Generar datos para PIB per cápita (gdp_cap)
log_gdp = np.random.normal(8.5, 1.2, 1000)         # Distribución log-normal (media log=8.5, desviación log=1.2)
pib = np.round(np.exp(log_gdp), 2)

# Generar datos para esperanza de vida (life_exp)
life = np.random.normal(72, 8, 1000)           # Distribución normal (media=72, desviación=8)  
life = np.round(np.clip(life, 45, 90), 2)      # Ajusta valores extremos

# ---------Dibuja el grafico de dispesion-------------

plt.scatter(pib, life)      #Eje (x,y)
plt.xscale('log')           # Correlacion logatimica para mejor distribucion 
    

#--------------Etiquetas -------------------
xlab = 'PBI per Capita [en USD]'
ylab = 'Esperanza de vida [en Años]'
title = 'Desarrollo mundial 2007'

plt.xlabel(xlab)    #Configuracion etiqueta del eje x
plt.ylabel(ylab)    #Configuracion etiqueta del eje y
plt.title(title)    #Configuracion del Titulo


#---------Renombra los valores del eje x ---------------
#Se renombran para que no se vea as: 10^2, 10^3, 10^4 ...

#Definicion de los ticks
tick_val = [100, 1000, 10000, 100000]  
tick_lab = ['100', '1k', '10k', '100k']

# Adapta los ticks on el eje-x
plt.xticks(tick_val, tick_lab)
#---------------------------------------------

#Visualizar
plt.show()