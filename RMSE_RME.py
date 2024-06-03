import random
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Définir le nombre de pannes
num_pannes = 11

# Valeurs prédites et réelles pour l'approche Classical-CBR
predicted_values_fixed = np.array([random.uniform(40, 100) for _ in range(num_pannes)])
real_values_fixed = np.array([random.uniform(0, 50) for _ in range(num_pannes)])

# Valeurs prédites et réelles pour l'approche PH-CBR
predicted_values_variable = np.array([random.uniform(0, 50) for _ in range(num_pannes)])
real_values_variable = np.array([random.uniform(0, 50) for _ in range(num_pannes)])

# Calcul de RMSE
def rmse(predicted, real):
    return np.sqrt(np.mean((predicted - real)**2))

rmse_fixed = rmse(predicted_values_fixed, real_values_fixed)
rmse_variable = rmse(predicted_values_variable, real_values_variable)

# Calcul de MAE
def mae(predicted, real):
    return np.mean(np.abs(predicted - real))

mae_fixed = mae(predicted_values_fixed, real_values_fixed)
mae_variable = mae(predicted_values_variable, real_values_variable)

# Tableau comparatif
comparison_table = {
    "Errors": ['RMSE', 'MAE'],
    "Classical-CBR Approach": [rmse_fixed, mae_fixed],
    "PH-CBR Approach": [rmse_variable, mae_variable]
}
comparison_df = pd.DataFrame(comparison_table)
print(comparison_df)

# Courbe pour comparer RMSE
plt.figure(figsize=(10, 6))
plt.bar(['Classical-CBR Approach', 'PH-CBR Approach'], [rmse_fixed, rmse_variable], label='RMSE', color=['skyblue', 'green'])
plt.xlabel('Approaches', fontsize=14)
plt.ylabel('RMSE', fontsize=14)
plt.legend(fontsize=14)
plt.title('RMSE comparison')
plt.show()

# Courbe pour comparer MAE
plt.figure(figsize=(10, 6))
plt.bar(['Classical-CBR Approach', 'PH-CBR Approach'], [mae_fixed, mae_variable], label='MAE', color=['skyblue', 'green'])
plt.xlabel('Approaches', fontsize=14)
plt.ylabel('MAE', fontsize=14)
plt.legend(fontsize=14)
plt.title('MAE comparison')
plt.show()
