import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Créer les données pour la courbe "Classical CBR-approach"
pn = ['p{}'.format(i) for i in range(1, 12)]
x_classical = np.array([int(p.replace('p', '')) for p in pn])
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

# Création de la figure et de l'axe
fig, ax = plt.subplots()

# Définir la largeur des barres et les positions sur l'axe x
bar_width = 0.08
x_indices = np.arange(len(x_classical))

# Tracer les barres pour chaque série de données
ax.bar(x_indices - 4 * bar_width, y_classical, width=bar_width, label='C-CBR', color='orange')
ax.bar(x_indices - 3 * bar_width, y_hypothetical1, width=bar_width, label='PH-CBR_Normal Dis_(µ,σ)', color='blue')
ax.bar(x_indices - 2 * bar_width, y_hypothetical2, width=bar_width, label='PH-CBR_Binomial Dis_(ON=70%,OFF=30%)', color='#3b75af')
ax.bar(x_indices - 1 * bar_width, y_hypothetical3, width=bar_width, label='PH-CBR_Hybrid Dis_(µ,σ),(ON=70%,OFF=30%)', color='green')
ax.bar(x_indices + 0 * bar_width, y_hypothetical_noise1, width=bar_width, label='PH-CBR_Normal Dis_(µ,2σ)', color='purple')
ax.bar(x_indices + 1 * bar_width, y_hypothetical_noise2, width=bar_width, label='PH-CBR_Binomial Dis_(ON=90%,OFF=10%)', color='brown')
ax.bar(x_indices + 2 * bar_width, y_hypothetical_noise3, width=bar_width, label='PH-CBR_Hybrid Dis_(µ,2σ),(ON=90%,OFF=10%)', color='#add151')
ax.bar(x_indices + 3 * bar_width, y_hypothetical_noise1_2, width=bar_width, label='PH-CBR_Normal Dis_(µ,3σ)', color='gray')
ax.bar(x_indices + 4 * bar_width, y_hypothetical_noise2_2, width=bar_width, label='PH-CBR_Binomial Dis_(ON=99%,OFF=1%)', color='cyan')
ax.bar(x_indices + 5 * bar_width, y_hypothetical_noise3_2, width=bar_width, label='PH-CBR_Hybrid Dis_(µ,3σ),(ON=99%,OFF=1%)', color='#12223e')

# Configurer les étiquettes et le titre
ax.set_xlabel('Failures')
ax.set_ylabel('Number of observed features')
ax.set_title('Comparison of Observed Features: Classic Approach vs. PH-CBR Approach')
ax.set_xticks(x_indices)
ax.set_xticklabels(pn)
ax.legend()

# Afficher la figure
plt.show()
