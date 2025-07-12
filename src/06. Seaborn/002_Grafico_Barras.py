import seaborn as sns
import matplotlib.pyplot as plt

gender = ["Female", "Female", "Female", "Female", "Male", "Male", "Male", "Male", "Male", "Male"]

sns.countplot(x=gender)

plt.show()