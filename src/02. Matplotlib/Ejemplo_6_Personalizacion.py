import matplotlib.pyplot as plt

year = [1950, 1970, 1990, 2010]
poblacion = [2.519, 3.692, 5.263, 6.972]


# Agregar mas data
year = [1800, 1850, 1900] + year
poblacion = [1.0, 1.262, 1.650] + poblacion

# Dibujar 
plt.plot(year, poblacion) #<eje horizontal><eje vertical>


#Etiquetas
plt.xlabel('Año')          #Eje X
plt.ylabel('Poblacion')    #Eje Y 
plt.title('Proyeccion de la poblacion mundial')  #Titulo

# Personalizar los valores del eje y para que inicien en 0 y vaya de 2 en 2
plt.yticks([0, 2, 4, 6, 8, 10],                    # Valores del eje Y 
           ['0', '2B', '4B', '6B', '8B', '10B'])   # Renombrar los valores del eje Y


#Visualizar
plt.show()