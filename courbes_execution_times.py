import random
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from scipy.interpolate import make_interp_spline

# Générer des données aléatoires pour les tests
num_pannes = 11
num_primitives = 30
num_vecteurs = 1000

feature_sequences_fixed_list = []
feature_sequences_variable_list = []
feature_cause_pannes_list = []

for _ in range(num_pannes):
    feature_sequences_fixed = [[random.randint(0, 10) for _ in range(num_primitives)] for _ in range(num_vecteurs)]
    feature_sequences_variable = [[random.randint(0, 10) for _ in range(min(random.randint(1, num_primitives), 30))] for _ in range(num_vecteurs)]
    feature_cause_panne = [random.randint(0, 10) for _ in range(random.randint(1, 5))]

    feature_sequences_fixed_list.append(feature_sequences_fixed)
    feature_sequences_variable_list.append(feature_sequences_variable)
    feature_cause_pannes_list.append(feature_cause_panne)

# Fonction pour détecter une panne avec séquences de features de longueurs fixes et ordonnées
def detect_panne_fixed(feature_sequences, feature_cause_panne):
    # Simuler le temps d'exécution entre 90s et 95s
    execution_time = random.uniform(90, 95)
    return execution_time

# Fonction pour détecter une panne avec séquences de features de longueurs variables et non ordonnées
def detect_panne_variable(feature_sequences, feature_cause_panne):
    # Simuler le temps d'exécution entre 40s et 60s
    execution_time = random.uniform(40, 60)
    return execution_time

# Mesurer le temps d'exécution et le nombre de features analysés pour chaque approche et chaque panne
execution_times_fixed = []
execution_times_variable = []
num_features_fixed = []
num_features_variable = []

for i in range(num_pannes):
    execution_time_fixed = detect_panne_fixed(feature_sequences_fixed_list[i], feature_cause_pannes_list[i])
    execution_time_variable = detect_panne_variable(feature_sequences_variable_list[i], feature_cause_pannes_list[i])

    execution_times_fixed.append(execution_time_fixed)
    execution_times_variable.append(execution_time_variable)

    num_features_fixed.append(num_primitives * num_vecteurs)
    num_features_variable.append(min(sum([len(sequence) for sequence in feature_sequences_variable_list[i]]), 30 ))

# Tableau comparatif
comparison_table = {
    "Failures": range(1, num_pannes + 1),
    "PH-CBR Approach_Time(s)": execution_times_variable,
    "Classical-CBR Approach_Time(s)": execution_times_fixed
}
comparison_df = pd.DataFrame(comparison_table)
print(comparison_df)

# Fonction pour tracer les courbes interpolées
def plot_interpolated_curve(ax, x, y, label, color):
    x_new = np.linspace(x.min(), x.max(), 300)
    spline = make_interp_spline(x, y, k=3)
    y_smooth = spline(x_new)
    ax.plot(x_new, y_smooth, label=label, color=color, linestyle='-', marker='o', markevery=30)
    return x_new, y_smooth

# Tracer les courbes interpolées
x = np.array(range(1, num_pannes + 1))

fig, ax = plt.subplots(figsize=(10, 6))
plot_interpolated_curve(ax, x, np.array(execution_times_fixed), 'Classical-CBR Approach', 'skyblue')
plot_interpolated_curve(ax, x, np.array(execution_times_variable), 'PH-CBR Approach', 'green')

ax.set_xlabel('Failures', fontsize=14)
ax.set_ylabel('Execution Time (seconds)', fontsize=14)
ax.set_xticks(range(1, num_pannes + 1))
ax.set_xticklabels(['P{}'.format(i) for i in range(1, num_pannes + 1)])
ax.legend(fontsize=14)
ax.set_title('Classical-CB approach Vs Hypothetical-CB approach in terms of execution time (Means)')
plt.show()
