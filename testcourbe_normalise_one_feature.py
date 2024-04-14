import numpy as np
import matplotlib.pyplot as plt

def moyenne(a, b):
    return (a + b) / 2

def ecart_type(a, b):
    moy = moyenne(a, b)
    ecart_a = (a - moy) ** 2
    ecart_b = (b - moy) ** 2
    variance = (ecart_a + ecart_b) / 2
    return np.sqrt(variance)

def generer_valeurs_normales(moyenne, ecart_type, nombre_valeurs):
    return np.random.normal(moyenne, ecart_type, nombre_valeurs)

def normaliser_valeurs(valeurs):
    return (valeurs - np.min(valeurs)) / (np.max(valeurs) - np.min(valeurs))

a = 0
b = 100

moyenne_calculée = moyenne(a, b)
ecartype_calculé = ecart_type(a, b)
print("Moyenne de", a, "et", b, ":", moyenne_calculée)
print("Écart type de", a, "et", b, ":", ecartype_calculé)

nombre_valeurs = 10

valeurs_normales = generer_valeurs_normales(moyenne_calculée, ecartype_calculé, nombre_valeurs)
print("Valeurs générées selon la loi normale avec une moyenne de", moyenne_calculée, "et un écart type de", ecartype_calculé, ":")
print(valeurs_normales)

# Définir les valeurs de Vx
Vx = ["cas1", "cas2", "cas3", "cas4", "cas5", "cas6", "cas7", "cas8", "cas9", "cas10"]

# Normalisation des valeurs
valeurs_normales_normalisees = normaliser_valeurs(valeurs_normales)

# Tracer la courbe avec un design amélioré
plt.plot(Vx, valeurs_normales_normalisees, marker='o', linestyle='-', color='green', markersize=8, linewidth=2, label='Valeurs normalisées')

# Ajouter des titres et des labels
plt.title('Courbe des valeurs normales normalisées en fonction des cas (FN22)', fontsize=14)
plt.xlabel('HDB', fontsize=14)
plt.ylabel('Valeurs normales normalisées', fontsize=12)

# Afficher la légende
plt.legend(fontsize=10)

# Afficher la courbe avec une grille
plt.grid(True)

# Afficher la courbe
plt.show()
