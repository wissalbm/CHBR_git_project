import random
import matplotlib.pyplot as plt

def generer_vecteur(n):
    # Générer n valeurs aléatoires dans l'intervalle [0, 1]
    valeurs = [random.uniform(0, 1) for _ in range(n)]
    return valeurs

# Générer un vecteur de 10 valeurs aléatoires dans l'intervalle [0, 1]
valeurs = generer_vecteur(10)

# Plot de la courbe
plt.plot(valeurs)
plt.xlabel('Index')
plt.ylabel('Valeurs')
plt.title('Courbe avec des valeurs entre 0 et 1')
plt.grid(True)
plt.show()
