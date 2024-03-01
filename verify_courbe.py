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

a = 0
b = 100

moyenne_calculée = moyenne(a, b)
ecartype_calculé = ecart_type(a, b)
print("Moyenne de", a, "et", b, ":", moyenne_calculée)
print("Écart type de", a, "et", b, ":", ecartype_calculé)

nombre_valeurs = 10

valeurs_normales1 = generer_valeurs_normales(moyenne_calculée, ecartype_calculé, nombre_valeurs)
valeurs_normales2 = valeurs_normales1 + 3.5
print("Valeurs générées selon la loi normale avec une moyenne de", moyenne_calculée, "et un écart type de", ecartype_calculé, ":")
print("Valeurs normales 1:", valeurs_normales1)
print("Valeurs normales 2:", valeurs_normales2)

# Définir les valeurs de Vx
Vx = ["cas1", "cas2", "cas3", "cas4", "cas5", "cas6", "cas7", "cas8", "cas9", "cas10"]

# Tracer les courbes
plt.plot(Vx, valeurs_normales1, marker='o', linestyle='-', color='orange', markersize=8, linewidth=2, label='Valeurs normales 1')
plt.plot(Vx, valeurs_normales2, marker='o', linestyle='-', color='green', markersize=8, linewidth=2, label='Valeurs normales 2')

# Ajouter des titres et des labels
plt.title('Courbe des valeurs normales en fonction des cas (FN22)', fontsize=14)
plt.xlabel('HDB', fontsize=14)
plt.ylabel('Valeurs normales', fontsize=12)

# Afficher la légende
plt.legend(fontsize=10)

# Afficher la courbe avec une grille
plt.grid(True)

# Afficher la courbe
plt.show()
