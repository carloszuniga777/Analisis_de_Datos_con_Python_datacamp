# Varianza y desviación típica
# La varianza y la desviación típica son dos de las formas más habituales de medir la dispersión de una variable, 
# y en este ejercicio practicarás su cálculo. La dispersión es importante, ya que puede ayudar a definir las expectativas. 
# 
# Por ejemplo, si un vendedor vende una media de 20 productos al día, pero tiene una desviación típica de 10 productos, 
# probablemente habrá días en los que venda 40 productos, pero también días en los que solo venda uno o dos. 
# 
# Este tipo de información es importante, sobre todo a la hora de hacer predicciones.

# Import sales data
import pandas as pd
import matplotlib.pyplot as plt
import os

# Obtener ruta base del archivo
base_path = os.path.dirname(os.path.abspath(__file__))
ruta_archivo = os.path.join(base_path, "..", "..", "Archivos", "food_consumption.csv")

# Importa el excel sales.csv
food_consumption = pd.read_csv( ruta_archivo)  

#-------------------------------------------
# Print variance and sd of co2_emission for each food_category 
print(  food_consumption.groupby('food_category')['co2_emission'].agg(['var','std'])  )


food_consumption[food_consumption['food_category']=='beef']['co2_emission'].hist(bins=20)

plt.title('Beef')
plt.xlabel('CO2 Emission')
plt.ylabel('Frequency')


# # Create histogram of co2_emission for food_category 'eggs'
plt.figure(figsize=(10, 5))
food_consumption.query('food_category == "eggs"')['co2_emission'].hist(bins=20)

plt.title('Eggs')
plt.xlabel('CO2 Emission')
plt.ylabel('Frequency')
plt.show()

# La carne de res tiene la mayor cantidad de variación en sus emisiones de CO2, 
# mientras que los huevos tienen una cantidad relativamente pequeña de variación.