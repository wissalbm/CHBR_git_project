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

a = -101,300003

b = -81,300003

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

# Tracer la courbe
plt.plot(Vx, valeurs_normales, marker='o', linestyle='-', color='green', markersize=8, linewidth=2, label='Valeurs normales')

# Ajouter des titres et des labels
plt.title('Courbe des valeurs normales en fonction des cas (FN1)', fontsize=14)
plt.xlabel('HDB', fontsize=14)
plt.ylabel('Valeurs normales', fontsize=12)

# Afficher la légende
plt.legend(fontsize=10)

# Afficher la courbe avec une grille
plt.grid(True)

# Afficher la courbe
plt.show()












# import os
# import numpy as np
# import matplotlib.pyplot as plt
# import pandas as pd
#
# def moyenne(a, b):
#     return (a + b) / 2
#
# def ecart_type(a, b):
#     moy = moyenne(a, b)
#     ecart_a = (a - moy) ** 2
#     ecart_b = (b - moy) ** 2
#     variance = (ecart_a + ecart_b) / 2
#     return np.sqrt(variance)
#
# def generer_valeurs_normales(moyenne, ecart_type, nombre_valeurs):
#     return np.random.normal(moyenne, ecart_type, nombre_valeurs)
#
# # Create a directory named "courbe" if it doesn't exist
# output_dir = "courbe"
# os.makedirs(output_dir, exist_ok=True)
#
# # Load data from CSV
# data = pd.read_csv('sourceFiles/primitives.csv')
#
# # Process rows 1 to 23
# for index, row in data.iloc[0:23].iterrows():
#     symbol = row['Symbols FN1-23/ FB1-7']
#     a = float(row['Lower_Limit'])  # Convert to float
#     b = float(row['Upper_Limit'])  # Convert to float
#
#     moyenne_calculée = moyenne(a, b)
#     ecartype_calculé = ecart_type(a, b)
#
#     nombre_valeurs = 10
#
#     valeurs_normales = generer_valeurs_normales(moyenne_calculée, ecartype_calculé, nombre_valeurs)
#
#     # Define values for Vx
#     Vx = ["cas1", "cas2", "cas3", "cas4", "cas5", "cas6", "cas7", "cas8", "cas9", "cas10"]
#
#     # Define different styles for each curve
#     line_styles = ['-', '--', '-.', ':']
#     marker_styles = ['o', 's', 'v', '^']
#
#     # Plot the curve with different styles
#     plt.plot(Vx, valeurs_normales, marker=marker_styles[index % len(marker_styles)],
#              linestyle=line_styles[index % len(line_styles)], markersize=8, linewidth=2,
#              label=f'{symbol}')
#
#     # Save the plot in the "courbe" folder
#     plt.savefig(os.path.join(output_dir, f'{symbol}.png'))
#
#     # Clear the current figure to avoid overlapping plots
#     plt.clf()
#
# # Add titles and labels
# plt.title('Courbe des valeurs normales en fonction des cas (FN22)', fontsize=14)
# plt.xlabel('Valeurs de X', fontsize=14)
# plt.ylabel('Valeurs normales', fontsize=12)
#
# # Display legend
# plt.legend(fontsize=10)
#
# # Display grid
# plt.grid(True)
#
# # Display the plot
# plt.show()
#
