import numpy as np

np_baseball = np.array([
    [74.0, 180.0, 22.99],
    [74.0, 215.0, 34.69],
    [72.0, 210.0, 30.78],
    [75.0, 205.0, 25.19],
    [75.0, 190.0, 31.01],
    [73.0, 195.0, 27.92],
    [75.0, 205.0, 25.19],
    [75.0, 190.0, 31.01],
    [73.0, 195.0, 27.92]
])

#promedio
avg = np.mean(np_baseball[:,0])
print("Average: " + str(avg))

# media
med = np.median(np_baseball[:, 0])
print("Median: " + str(med))

# desviacion estandar
stddev = np.std(np_baseball[:, 0])
print("Standard Deviation: " + str(stddev))

# Print out correlation between first and second column
corr = np.corrcoef(np_baseball[:,0], np_baseball[:,1])
print("Correlation: " + str(corr))