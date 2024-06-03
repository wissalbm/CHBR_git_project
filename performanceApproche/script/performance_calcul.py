def precision(correctly_identified, total_identified):
    return correctly_identified / total_identified

def recall(correctly_identified, total_actual):
    return correctly_identified / total_actual

def f1_score(precision_value, recall_value):
    return 2 * (precision_value * recall_value) / (precision_value + recall_value)

# Valeurs pour une seule configuration
correctly_identified_hyp_single = 930  # Nombre de pannes correctement identifiées par approche hypothétique pour une configuration
correctly_identified_classical_single = 890  # Nombre de pannes correctement identifiées par approche classique pour une configuration
total_identified_single = 1000  # Nombre total de pannes identifiées pour une configuration
total_actual_single = 1000  # Nombre total de pannes réelles pour une configuration

# Nombre de configurations et de générations
num_configurations = 9
num_generations = 20

# Calcul des valeurs totales pour toutes les configurations et générations
correctly_identified_hyp_total = correctly_identified_hyp_single * num_configurations * num_generations
correctly_identified_classical_total = correctly_identified_classical_single * num_configurations * num_generations
total_identified_total = total_identified_single * num_configurations * num_generations
total_actual_total = total_actual_single * num_configurations * num_generations

# Calcul des métriques pour l'approche hypothétique
precision_hyp = precision(correctly_identified_hyp_total, total_identified_total)
recall_hyp = recall(correctly_identified_hyp_total, total_actual_total)
f1_score_hyp = f1_score(precision_hyp, recall_hyp)

# Calcul des métriques pour l'approche classique
precision_classical = precision(correctly_identified_classical_total, total_identified_total)
recall_classical = recall(correctly_identified_classical_total, total_actual_total)
f1_score_classical = f1_score(precision_classical, recall_classical)

# Affichage des résultats
print("Approche Hypothétique :")
print(f"Nombre de pannes correctement identifiées: {correctly_identified_hyp_total}")
print(f"Nombre total de pannes identifiées: {total_identified_total}")
print(f"Nombre total de pannes réelles: {total_actual_total}")
print(f"Précision: {precision_hyp:.2f}")
print(f"Rappel: {recall_hyp:.2f}")
print(f"Score F1: {f1_score_hyp:.2f}\n")

print("Approche Classique :")
print(f"Nombre de pannes correctement identifiées: {correctly_identified_classical_total}")
print(f"Nombre total de pannes identifiées: {total_identified_total}")
print(f"Nombre total de pannes réelles: {total_actual_total}")
print(f"Précision: {precision_classical:.2f}")
print(f"Rappel: {recall_classical:.2f}")
print(f"Score F1: {f1_score_classical:.2f}")
