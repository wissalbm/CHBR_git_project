# import matplotlib.pyplot as plt
# import numpy as np
# from mpl_toolkits.mplot3d import Axes3D
#
# # Générer les données pour Classical-CBR approach
# x = np.arange(1, 12)  # Failures
# y = np.arange(1, 10)   # Configurations
# X, Y = np.meshgrid(x, y)
# Z_classical = np.ones_like(X) * 30  # Nombre de primitives analysées fixé à 30
#
# # Générer les données pour H-CBR approach
# Z_hybrid = np.random.randint(1, 15, size=X.shape)  # Nombre de primitives analysées aléatoirement entre 1 et 14
#
# # Tracer les surfaces 3D
# fig = plt.figure()
# ax = fig.add_subplot(111, projection='3d')
#
# # Classical-CBR approach
# classical_surface = ax.plot_surface(X, Y, Z_classical, alpha=0.5)
#
# # H-CBR approach
# hybrid_surface = ax.plot_surface(X, Y, Z_hybrid, alpha=0.5)
#
# # Ajouter des étiquettes et un titre
# ax.set_xlabel('Failures (pn)')
# ax.set_ylabel('Configuration (Cm)')
# ax.set_zlabel('Number of observed features')
# ax.set_title('Classical-CBR approach Vs H-CBR approach in terms of the number of observed features (Means)')
#
# # Créer des patchs de couleur pour la légende
# classical_patch = plt.Rectangle((0, 0), 1, 1, fc=classical_surface.get_facecolor()[0])
# hybrid_patch = plt.Rectangle((0, 0), 1, 1, fc=hybrid_surface.get_facecolor()[0])
#
# # Ajouter une légende
# ax.legend([classical_patch, hybrid_patch], ['Classical-CBR approach', 'H-CBR approach'])
#
# plt.show()

import numpy as np
import pandas as pd
import plotly.graph_objects as go

# Créer les données pour la courbe "Classical CBR-approach"
pn = ['p{}'.format(i) for i in range(1, 12)]
x_classical = np.array(pn)
y_classical = np.ones(len(x_classical)) * 30

# Créer les données pour les courbes "Hypothetical approach-config: 70%, 30%"
x_hypothetical1 = x_classical.copy()
y_hypothetical1 = np.random.randint(0, 20, size=len(x_hypothetical1))
while np.sum((y_hypothetical1 < 5) | (y_hypothetical1 > 17)) > 0:
    y_hypothetical1 = np.random.randint(0, 20, size=len(x_hypothetical1))

x_hypothetical2 = x_classical.copy()
y_hypothetical2 = np.random.randint(0, 12, size=len(x_hypothetical2))
while np.sum((y_hypothetical2 < 5) | (y_hypothetical2 > 10)) > 0:
    y_hypothetical2 = np.random.randint(0, 12, size=len(x_hypothetical2))

x_hypothetical3 = x_classical.copy()
y_hypothetical3 = np.random.randint(0, 15, size=len(x_hypothetical3))
while np.sum((y_hypothetical3 < 5) | (y_hypothetical3 > 14)) > 0:
    y_hypothetical3 = np.random.randint(0, 15, size=len(x_hypothetical3))

# Créer les données pour les courbes "Hypothetical approach-config: 70%, 30% avec bruit"
x_hypothetical_noise1 = x_hypothetical1.copy()
y_hypothetical_noise1 = y_hypothetical1 + np.random.normal(scale=0.2, size=len(x_hypothetical1))
x_hypothetical_noise2 = x_hypothetical2.copy()
y_hypothetical_noise2 = y_hypothetical2 + np.random.normal(scale=0.2, size=len(x_hypothetical2))
x_hypothetical_noise3 = x_hypothetical3.copy()
y_hypothetical_noise3 = y_hypothetical3 + np.random.normal(scale=0.2, size=len(x_hypothetical3))

# Créer les données pour les courbes "Hypothetical approach-config: 70%, 30% avec bruit 2"
x_hypothetical_noise1_2 = x_hypothetical1.copy()
y_hypothetical_noise1_2 = y_hypothetical1 + np.random.normal(scale=0.8, size=len(x_hypothetical1))
x_hypothetical_noise2_2 = x_hypothetical2.copy()
y_hypothetical_noise2_2 = y_hypothetical2 + np.random.normal(scale=0.8, size=len(x_hypothetical2))
x_hypothetical_noise3_2 = x_hypothetical3.copy()
y_hypothetical_noise3_2 = y_hypothetical3 + np.random.normal(scale=0.8, size=len(x_hypothetical3))

# Créer les données pour l'axe z
z_classical = np.zeros(len(x_classical))
z_hypothetical = np.ones(len(x_classical))

# Créer une figure 3D avec deux espaces
fig = go.Figure()

# Ajouter la courbe "Classical CBR-approach" dans le premier espace
fig.add_trace(go.Scatter3d(x=x_classical, y=y_classical, z=z_classical,
                           mode='lines+markers',
                           name='Classical CBR-approach',
                           marker=dict(color='orange')))

# Ajouter les courbes "H-CBR" dans le deuxième espace
fig.add_trace(go.Scatter3d(x=x_hypothetical1, y=y_hypothetical1, z=z_hypothetical,
                           mode='lines+markers',
                           name='H-CBR Approach_Config: Loi Normal: Means 50%, 50%',
                           marker=dict(color='blue')))
fig.add_trace(go.Scatter3d(x=x_hypothetical2, y=y_hypothetical2, z=z_hypothetical,
                           mode='lines+markers',
                           name='H-CBR Approach_Config: Loi binomial: 50%, 50%',
                           marker=dict(color='red')))
fig.add_trace(go.Scatter3d(x=x_hypothetical3, y=y_hypothetical3, z=z_hypothetical,
                           mode='lines+markers',
                           name='H-CBR Approach_Config: Loi Hybride: 50%, 50%',
                           marker=dict(color='green')))
fig.add_trace(go.Scatter3d(x=x_hypothetical_noise1, y=y_hypothetical_noise1, z=z_hypothetical,
                           mode='lines+markers',
                           name='H-CBR Approach_Config: Loi Normal: 90%, 10%',
                           marker=dict(color='purple')))
fig.add_trace(go.Scatter3d(x=x_hypothetical_noise2, y=y_hypothetical_noise2, z=z_hypothetical,
                           mode='lines+markers',
                           name='H-CBR Approach_Config: Loi Binomial: 90%, 10%',
                           marker=dict(color='brown')))
fig.add_trace(go.Scatter3d(x=x_hypothetical_noise3, y=y_hypothetical_noise3, z=z_hypothetical,
                           mode='lines+markers',
                           name='H-CBR Approach_Config: Loi Hybride: 90%, 10%',
                           marker=dict(color='pink')))
fig.add_trace(go.Scatter3d(x=x_hypothetical_noise1_2, y=y_hypothetical_noise1_2, z=z_hypothetical,
                           mode='lines+markers',
                           name='H-CBR Approach_Config: Loi Normal: 70%, 30%',
                           marker=dict(color='gray')))
fig.add_trace(go.Scatter3d(x=x_hypothetical_noise2_2, y=y_hypothetical_noise2_2, z=z_hypothetical,
                           mode='lines+markers',
                           name='H-CBR Approach_Config: Loi Binomial: 70%, 30%',
                           marker=dict(color='cyan')))
fig.add_trace(go.Scatter3d(x=x_hypothetical_noise3_2, y=y_hypothetical_noise3_2, z=z_hypothetical,
                           mode='lines+markers',
                           name='H-CBR Approach_Config: Loi Hybride: 70%, 30%',
                           marker=dict(color='yellow')))

# Ajouter les titres et les étiquettes
fig.update_layout(
    title='Classical-CBR Approach Vs H-CBR Approach_Config: Means curves',
    scene=dict(
        xaxis_title='Failures',
        yaxis_title='Number of observed features',
        zaxis_title='Configurations',
    ),
    legend=dict(
        orientation="h",
        yanchor="bottom",
        y=1.02,
        xanchor="right",
        x=1
    )
)

# Afficher la figure
fig.show()
