import numpy as np
import matplotlib.pyplot as plt

# Define the two vectors
V1 = np.array([14, 5, 15, 4, 11, 19, 1, 13])
V2 = np.array([14, 15, 4, 11, 19, 13, 5])

# Calculate the distance between the two vectors using the NN method
def calc_distance_nn(V1, V2):
    dist = np.inf
    for i in range(len(V1)):
        for j in range(len(V2)):
            d = np.linalg.norm(V1[i] - V2[j])
            if d < dist:
                dist = d
    return dist

distance = calc_distance_nn(V1, V2)

# Generate a range of distances for the x-axis of the plot
distances = np.linspace(0, np.max([np.linalg.norm(V1), np.linalg.norm(V2)])*2, 100)

# Calculate the possibility distribution using the formula for the NN method
possibilities = np.zeros(len(distances))
for i in range(len(distances)):
    possibilities[i] = np.exp(-(distances[i] - distance)**2 / (2 * 0.5**2))

# Normalize the possibilities so that they sum to 1
possibilities = possibilities / np.sum(possibilities)

# Plot the possibility distribution
plt.plot(distances, possibilities)
plt.xlabel('Distance')
plt.ylabel('Possibility')
plt.title('Possibility distribution of the distance between V1 and V2')
plt.show()
