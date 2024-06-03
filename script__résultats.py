import random
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import pandas as pd

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
    "Pan": range(1, num_pannes + 1),
    "Hypothetical-Approach_Time(s)": execution_times_variable,
    "Classical-Approach_Time(s)": execution_times_fixed
}
comparison_df = pd.DataFrame(comparison_table)
print(comparison_df)

# Courbe pour comparer le temps d'exécution
fig = plt.figure(figsize=(10, 6))
ax = fig.add_subplot(111, projection='3d')

# Liaison entre les points et utilisation des couleurs rose, vert et orange
ax.plot(range(1, num_pannes + 1), num_features_fixed, execution_times_fixed, label='Classical-Approach', c='orange', marker='o', linestyle='-', linewidth=2)
ax.plot(range(1, num_pannes + 1), num_features_variable, execution_times_variable, label='Hypothetical-Approach', c='green', marker='o', linestyle='-', linewidth=2)

ax.set_xlabel('Pan Number', fontsize=14)
ax.set_ylabel('Number of Primitives Analyzed', fontsize=14)
ax.set_zlabel('Execution Time (seconds)', fontsize=14)
ax.legend(fontsize=14)
plt.title('Classical-Approach Vs Hypothetical-Approach')
plt.show()
