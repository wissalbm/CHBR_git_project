import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from scipy.interpolate import griddata
from matplotlib.lines import Line2D

# Paramètres
num_pannes = 11
num_configurations = 10
num_points_per_panne = 100 // num_pannes

# Créer des données pour l'approche classique (toutes les pannes à 30)
x1 = np.tile(np.linspace(0, 10, num_configurations), num_pannes)
y1 = np.repeat(np.arange(1, num_pannes + 1), num_configurations)
z1 = np.ones_like(x1) * 30  # Valeurs constantes à 30

# Créer des données pour l'approche hypothétique (valeurs variées entre 4 et 17)
x2 = np.tile(np.linspace(0, 10, num_configurations), num_pannes)
y2 = np.repeat(np.arange(1, num_pannes + 1), num_configurations)
z2 = np.random.uniform(4, 17, len(x2))  # Génère des valeurs entre 4 et 17

# S'assurer qu'au moins une fois les valeurs 4 et 17 sont incluses
z2[np.random.randint(0, len(z2))] = 4
z2[np.random.randint(0, len(z2))] = 17

# Créer une grille régulière pour l'interpolation
x_grid, y_grid = np.meshgrid(np.linspace(0, 10, 100), np.linspace(1, 11, 100))

# Interpoler les données pour les deux approches
z1_interp = griddata((x1, y1), z1, (x_grid, y_grid), method='cubic')
z2_interp = griddata((x2, y2), z2, (x_grid, y_grid), method='cubic')

# Créer la figure et l'espace 3D avec une taille plus grande
fig = plt.figure(figsize=(12, 9))
ax = fig.add_subplot(111, projection='3d')


# Tracer l'approche classique avec une interpolation lisse et une couleur différente
ax.plot_surface(x_grid, y_grid, z1_interp, cmap='summer', alpha=0.8)

# Tracer l'approche hypothétique avec une interpolation lisse et une couleur différente
surface = ax.plot_surface(x_grid, y_grid, z2_interp, cmap='winter', alpha=0.8)

# Ajouter des légendes et des titres
ax.set_xlabel('Configurations')
ax.set_ylabel('Failures')
ax.set_zlabel('Number of obs features')
ax.set_title('3D Comparison of C-CBR and PH-CBR Approaches')

# Définir les étiquettes de l'axe des x avec un espacement plus grand
xticks = np.linspace(0, 10, num_configurations)  # Créer des positions pour les ticks
xlabels = ['C1', 'C2', 'C3', 'C4', 'C5', 'C6', 'C7', 'C8', 'C9', 'C10']  # Créer les labels
ax.set_xticks(xticks)
ax.set_xticklabels(xlabels)

# Définir les étiquettes de l'axe des y avec un espacement plus grand
yticks = np.arange(1, num_pannes + 1)  # Créer des positions pour les ticks (1 à num_pannes)
ylabels = [f'p{i}' for i in range(1, num_pannes + 1)]  # Créer les labels
ax.set_yticks(yticks)
ax.set_yticklabels(ylabels)

# Définir les étiquettes de l'axe des z avec un espacement plus grand
zticks = np.linspace(0, 30, 7)  # Séquence de 0 à 30 avec 7 étiquettes
ax.set_zticks(zticks)

# Créer la légende à partir des lignes tracées
legend_elements = [Line2D([0], [0], color='#b4d28b', lw=2, label='C-CBR approach'),
                   Line2D([0], [0], color='blue', lw=2, label='PH-CBR approach')]
ax.legend(handles=legend_elements, loc='upper right')
# Trouver les valeurs minimales et maximales pour les deux approches
z1_min, z1_max = np.min(z1), np.max(z1)
z2_min, z2_max = np.min(z2), np.max(z2)



# # Déterminer la position maximale le long de l'axe z
# z_max_position = max(ax.get_xlim())
#
# # Ajouter des étiquettes pour les valeurs minimales et maximales à droite de l'axe des "Number of obs features"
# ax.text(z_max_position + 1, y_grid.min(), z1_min, f'Min: {z1_min:.2f}', color='orange', fontsize=10, ha='right')
# ax.text(z_max_position + 1, y_grid.min(), z1_max, f'Max: {z1_max:.2f}', color='orange', fontsize=10, ha='right')
# ax.text(z_max_position + 1, y_grid.min(), z2_min, f'Min: {z2_min:.2f}', color='blue', fontsize=10, ha='right')
# ax.text(z_max_position + 1, y_grid.min(), z2_max, f'Max: {z2_max:.2f}', color='blue', fontsize=10, ha='right')

# Afficher la figure

# # Déterminer la position maximale le long de l'axe z
# z_max_position = z1_interp.max()
#
# # Ajouter des étiquettes pour les valeurs minimales et maximales à droite de l'axe des "Number of obs features"
# ax.text(10.5, 11, z1_min, f'Min: {z1_min:.2f}', color='orange', fontsize=10, ha='right', weight='bold')
# ax.text(10.5, 11, z1_max, f'Max: {z1_max:.2f}', color='orange', fontsize=10, ha='right', weight='bold')
# ax.text(10.5, 11, z2_min, f'Min: {z2_min:.2f}', color='blue', fontsize=10, ha='right', weight='bold')
# ax.text(10.5, 11, z2_max, f'Max: {z2_max:.2f}', color='blue', fontsize=10, ha='right', weight='bold')

plt.show()