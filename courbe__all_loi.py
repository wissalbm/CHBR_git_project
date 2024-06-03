import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import numpy as np
import pandas as pd
from scipy.interpolate import make_interp_spline

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

# Concaténer toutes les valeurs de y des courbes H-CBR dans un seul tableau
hypothetical_y = np.concatenate([y_hypothetical1, y_hypothetical2, y_hypothetical3,
                                     y_hypothetical_noise1, y_hypothetical_noise2, y_hypothetical_noise3,
                                     y_hypothetical_noise1_2, y_hypothetical_noise2_2, y_hypothetical_noise3_2])

# Trouver les valeurs minimale et maximale des courbes H-CBR
y_min = np.min(hypothetical_y)
y_max = np.max(hypothetical_y)

# Fonction pour tracer les courbes avec interpolation
def plot_interpolated_curve(ax, x, y, label, color):
    x_new = np.linspace(x.min(), x.max(), 300)
    spline = make_interp_spline(x, y, k=3)
    y_smooth = spline(x_new)
    ax.plot(x_new, y_smooth, label=label, color=color)
    # Ajouter des points sur les courbes
    ax.scatter(x, y, color=color, marker='o', s=30, zorder=3)
    return x_new, y_smooth

# Créer une figure pour la fusion des 10 courbes
fig, ax = plt.subplots()
plot_interpolated_curve(ax, x_classical, y_classical, label='C-CBR', color='orange')
plot_interpolated_curve(ax, x_hypothetical1, y_hypothetical1, label='PH-CBR_Normal Dis_(µ,σ)', color='blue')
plot_interpolated_curve(ax, x_hypothetical2, y_hypothetical2, label='PH-CBR_Binomial  Dis_(ON=70%,OFF=30%)', color='#3b75af')
plot_interpolated_curve(ax, x_hypothetical3, y_hypothetical3, label='PH-CBR_Hybrid Dis_(µ,σ),(ON=70%,OFF=30%)', color='green')
plot_interpolated_curve(ax, x_hypothetical_noise1, y_hypothetical_noise1, label='PH-CBR_Normal Dis_(µ,2σ)', color='purple')
plot_interpolated_curve(ax, x_hypothetical_noise2, y_hypothetical_noise2, label='PH-CBR_Binomial Dis_(ON=90%,OFF=10%)', color='brown')
plot_interpolated_curve(ax, x_hypothetical_noise3, y_hypothetical_noise3, label='PH-CBR_Hybrid Dis_(µ,2σ),(ON=90%,OFF=10%)', color='#add151')
plot_interpolated_curve(ax, x_hypothetical_noise1_2, y_hypothetical_noise1_2, label='PH-CBR_Normal Dis_(µ,3σ)', color='gray')
plot_interpolated_curve(ax, x_hypothetical_noise2_2, y_hypothetical_noise2_2, label='PH-CBR_Binomial Dis_(ON=99%,OFF=1%)', color='cyan')
plot_interpolated_curve(ax, x_hypothetical_noise3_2, y_hypothetical_noise3_2, label='PH-CBR_Hybrid Dis_(µ,3σ),(ON=99%,OFF=1%)', color='#12223e')
ax.set_xlabel('Failures')
ax.set_ylabel('Number of observed features')
ax.set_title('Comparison of Observed Features: Classic Approach vs. PH-CBR Approach')
ax.legend()

# Ajouter des lignes horizontales et des étiquettes pour les valeurs minimale et maximale des courbes H-CBR
# ax.axhline(y=y_min, color='black', linestyle='--')
# ax.text(x_classical[0], y_min - 1, f'Min: ({int(y_min)})', color='black')
# ax.axhline(y=y_max, color='black', linestyle='--')
# ax.text(x_classical[0], y_max + 1, f'Max: ({int(y_max)})', color='black')

# Formater les étiquettes de l'axe des Y pour afficher uniquement des entiers entre 0 et 30
ax.yaxis.set_major_locator(ticker.MaxNLocator(integer=True, nbins=10, prune='upper'))
ax.yaxis.set_major_formatter(ticker.FormatStrFormatter('%d'))

# Ajouter les étiquettes 'P1', 'P2', ..., 'P11' sur l'axe des x
ax.set_xticks(x_classical)
ax.set_xticklabels(pn)

# Afficher la figure
plt.show()

# Créer 9 figures pour comparer chaque courbe H-CBR avec la courbe Classical-CBR
figures = [
    (x_hypothetical1, y_hypothetical1, 'blue', 'PH-CBR_Normal Dis_(µ,σ)'),
    (x_hypothetical2, y_hypothetical2, '#3b75af', 'PH-CBR_Binomial Dis_(ON=70%,OFF=30%)'),
    (x_hypothetical3, y_hypothetical3, 'green', 'PH-CBR_Hybrid Dis_(µ,σ),(ON=70%,OFF=30%)'),
    (x_hypothetical_noise1, y_hypothetical_noise1, 'purple', 'PH-CBR_Normal Dis_(µ,2σ)'),
    (x_hypothetical_noise2, y_hypothetical_noise2, 'brown', 'PH-CBR_Binomial Dis_(ON=90%,OFF=10%)'),
    (x_hypothetical_noise3, y_hypothetical_noise3, '#add151', 'PH-CBR_Hybrid Dis_(µ,2σ),(ON=90%,OFF=10%)'),
    (x_hypothetical_noise1_2, y_hypothetical_noise1_2, 'gray', 'PH-CBR_Normal Dis_(µ,3σ)'),
    (x_hypothetical_noise2_2, y_hypothetical_noise2_2, 'cyan', 'PH-CBR_Binomial Dis_(ON=99%,OFF=1%)'),
    (x_hypothetical_noise3_2, y_hypothetical_noise3_2, '#12223e', 'PH-CBR_Hybrid Dis_(µ,3σ),(ON=99%,OFF=1%)'),
]

for x, y, color, label in figures:
    plt.figure()
    ax = plt.gca()  # Créer une nouvelle instance de ax pour chaque figure
    plot_interpolated_curve(ax, x_classical, y_classical, label='C-CBR', color='orange')
    plot_interpolated_curve(ax, x, y, label=label, color=color)
    ax.set_xlabel('Failures')
    ax.set_ylabel('Number of observed features')
    ax.set_title(f'C-CBR Approach Vs {label}')
    ax.legend()

    # Ajouter les étiquettes 'P1', 'P2', ..., 'P11' sur l'axe des x
    ax.set_xticks(x_classical)
    ax.set_xticklabels(pn)

plt.show()

# Créer un tableau pour les données de la courbe "Classical CBR-approach"
table_classical = pd.DataFrame({
    'Failures': x_classical,
    'Number of observed features': y_classical
})
table_classical.to_csv('Classical_CBR_approach.csv', index=False)

# Créer un tableau pour les données de la courbe "Hypothetical approach-config: 70%, 30%"
table_hypothetical1 = pd.DataFrame({
    'Failures': x_hypothetical1,
    'Number of observed features': y_hypothetical1
})
table_hypothetical1.to_csv('Hypothetical_approach_Loi_Normal_Means_50_50.csv', index=False)

table_hypothetical2 = pd.DataFrame({
    'Failures': x_hypothetical2,
    'Number of observed features': y_hypothetical2
})
table_hypothetical2.to_csv('Hypothetical_approach_Loi_binomial_50_50.csv', index=False)

table_hypothetical3 = pd.DataFrame({
    'Failures': x_hypothetical3,
    'Number of observed features': y_hypothetical3
})
table_hypothetical3.to_csv('Hypothetical_approach_Loi_HYbride_50_50.csv', index=False)

# Créer un tableau pour les données de la courbe "Hypothetical approach-config: 70%, 30% avec bruit"
table_hypothetical_noise1 = pd.DataFrame({
    'Failures': x_hypothetical_noise1,
    'Number of observed features': y_hypothetical_noise1
})
table_hypothetical_noise1.to_csv('Hypothetical_approach_Loi_Normal_90_10.csv', index=False)

table_hypothetical_noise2 = pd.DataFrame({
    'Failures': x_hypothetical_noise2,
    'Number of observed features': y_hypothetical_noise2
})
table_hypothetical_noise2.to_csv('Hypothetical_approach_Loi_Binomial_90_10.csv', index=False)

table_hypothetical_noise3 = pd.DataFrame({
    'Failures': x_hypothetical_noise3,
    'Number of observed features': y_hypothetical_noise3
})
table_hypothetical_noise3.to_csv('Hypothetical_approach_Loi_Hybride_90_10.csv', index=False)

# Créer un tableau pour les données de la courbe "Hypothetical approach-config: 70%, 30% avec bruit 2"
table_hypothetical_noise1_2 = pd.DataFrame({
    'Failures': x_hypothetical_noise1_2,
    'Number of observed features': y_hypothetical_noise1_2
})
table_hypothetical_noise1_2.to_csv('Hypothetical_approach_Loi_Normal_70_30.csv', index=False)

table_hypothetical_noise2_2 = pd.DataFrame({
    'Failures': x_hypothetical_noise2_2,
    'Number of observed features': y_hypothetical_noise2_2
})
table_hypothetical_noise2_2.to_csv('Hypothetical_approach_Loi_Binomial_70_30.csv', index=False)

table_hypothetical_noise3_2 = pd.DataFrame({
    'Failures': x_hypothetical_noise3_2,
    'Number of observed features': y_hypothetical_noise3_2
})
table_hypothetical_noise3_2.to_csv('Hypothetical_approach_Loi_Hybride_70_30.csv', index=False)

# Créer une figure pour la loi binomiale
fig, ax_binomial = plt.subplots()
plot_interpolated_curve(ax_binomial, x_classical, y_classical, label='C-CBR', color='orange')
plot_interpolated_curve(ax_binomial, x_hypothetical2, y_hypothetical2, label='PH-CBR_Binomial Dis_(ON=70%,OFF=30%)', color='#12223e')
plot_interpolated_curve(ax_binomial, x_hypothetical_noise2, y_hypothetical_noise2, label='PH-CBR_Binomial Dis_(ON=90%,OFF=10%)', color='#add151')
plot_interpolated_curve(ax_binomial, x_hypothetical_noise2_2, y_hypothetical_noise2_2, label='PH-CBR_Binomial Dis_(ON=99%,OFF=1%)', color='#52b5da')
ax_binomial.set_xlabel('Failures')
ax_binomial.set_ylabel('Number of observed features')
ax_binomial.set_title('C-CBR Vs PH-CBR_Binomial Dis_All Configurations')
ax_binomial.legend()

# Créer une figure pour la loi normale
fig, ax_normal = plt.subplots()
plot_interpolated_curve(ax_normal, x_classical, y_classical, label='C-CBR', color='orange')
plot_interpolated_curve(ax_normal, x_hypothetical1, y_hypothetical1, label='PH-CBR_Normal Dis_(µ,σ)', color='#12223e')
plot_interpolated_curve(ax_normal, x_hypothetical_noise1, y_hypothetical_noise1, label=' PH-CBR_Normal Dis_(µ,2σ)', color='#add151')
plot_interpolated_curve(ax_normal, x_hypothetical_noise1_2, y_hypothetical_noise1_2, label='PH-CBR_Normal Dis_Dis_(µ,3σ)', color='#52b5da')
ax_normal.set_xlabel('Failures')
ax_normal.set_ylabel('Number of observed features')
ax_normal.set_title('C-CBR Vs PH-CBR_Normal Dis_All Configurations')
ax_normal.legend()

# Créer une figure pour la loi hybride
fig, ax_hybrid = plt.subplots()
plot_interpolated_curve(ax_hybrid, x_classical, y_classical, label='C-CBR', color='orange')
plot_interpolated_curve(ax_hybrid, x_hypothetical3, y_hypothetical3, label='PH-CBR_Hybrid Dis_ (Mu,Sigma)OR( ON=70%,OFF=30%)', color='#12223e')
plot_interpolated_curve(ax_hybrid, x_hypothetical_noise3, y_hypothetical_noise3, label=' PH-CBR_Hybrid Dis_ (Mu,2Sigma)OR( ON=90%,OFF=10%)', color='#add151')
plot_interpolated_curve(ax_hybrid, x_hypothetical_noise3_2, y_hypothetical_noise3_2, label='PH-CBR_Hybrid Dis_ (Mu,3Sigma)OR( ON=99%,OFF=1%)', color='#52b5da')
ax_hybrid.set_xlabel('Failures')
ax_hybrid.set_ylabel('Number of observed features')
ax_hybrid.set_title('C-CBR Vs PH-CBR_Hybrid Dis_All Configurations')
ax_hybrid.legend()








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










plt.show()
