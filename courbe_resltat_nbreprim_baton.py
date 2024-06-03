import time
import random
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

# Générer des données aléatoires pour les tests
num_pannes = 11
num_primitives = 30
num_vecteurs = 1000

feature_sequences_fixed_list = []
feature_sequences_variable_list = []
feature_cause_pannes_list = []

for _ in range(num_pannes):
    feature_sequences_fixed = [[random.randint(0, 10) for _ in range(num_primitives)] for _ in range(num_vecteurs)]
    feature_sequences_variable = [[random.randint(0, 10) for _ in range(random.randint(2, 25))] for _ in range(num_vecteurs)]
    feature_cause_panne = [random.randint(0, 10) for _ in range(random.randint(1, 5))]

    feature_sequences_fixed_list.append(feature_sequences_fixed)
    feature_sequences_variable_list.append(feature_sequences_variable)
    feature_cause_pannes_list.append(feature_cause_panne)

# Fonction pour détecter une panne avec séquences de features de longueurs fixes et ordonnées
def detect_panne_fixed(feature_sequences, feature_cause_panne):
    for sequence in feature_sequences:
        for feature in sequence:
            if feature in feature_cause_panne:
                return True
    return False

# Fonction pour détecter une panne avec séquences de features de longueurs variables et non ordonnées
def detect_panne_variable(feature_sequences, feature_cause_panne):
    feature_cause_set = set(feature_cause_panne)
    for sequence in feature_sequences:
        if feature_cause_set.intersection(set(sequence)):
            return True
    return False

# Mesurer le temps d'exécution et le nombre de features analysés pour chaque approche et chaque panne
execution_times_fixed = []
execution_times_variable = []
num_features_fixed = []
num_features_variable = []

for i in range(num_pannes):
    start_time_fixed = time.time()
    result_fixed = detect_panne_fixed(feature_sequences_fixed_list[i], feature_cause_pannes_list[i])
    end_time_fixed = time.time()

    start_time_variable = time.time()
    result_variable = detect_panne_variable(feature_sequences_variable_list[i], feature_cause_pannes_list[i])
    end_time_variable = time.time()

    execution_times_fixed.append(end_time_fixed - start_time_fixed)
    execution_times_variable.append(end_time_variable - start_time_variable)

    num_features_fixed.append(num_primitives * num_vecteurs)
    num_features_variable.append(sum([len(sequence) for sequence in feature_sequences_variable_list[i]]))

pan_labels = ['P{}'.format(i) for i in range(1, num_pannes + 1)]

# Diagramme en bâtons pour comparer le nombre de primitives analysées
plt.figure(figsize=(10, 6))
plt.bar(pan_labels, num_features_fixed, width=0.35, label='Classical-CBR Approach', color='skyblue')
plt.bar([x + 0.35 for x in range(len(pan_labels))], num_features_variable, width=0.35, label='PH-CBR Approach', color='orange')
plt.xlabel('Failures', fontsize=14)
plt.ylabel('Number of observed features', fontsize=14)
plt.xticks(rotation=45)
plt.legend(fontsize=14)
plt.title('Classical-CB approach Vs Hypothetical-CB approach in terms of the number of observed features analyzed')
plt.show()
