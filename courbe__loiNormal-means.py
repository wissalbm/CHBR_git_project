import matplotlib.pyplot as plt
import numpy as np

# Créer les données pour la courbe "Classical CBR-approach"
pn = ['p{}'.format(i) for i in range(1, 12)]
x_classical = np.array(pn)
y_classical = np.ones(len(x_classical))*30

# Créer les données pour la courbe "Hypothetical approach-config: 70%, 30%"
x_hypothetical = x_classical.copy()
y_hypothetical = np.random.randint(0, 20, size=len(x_hypothetical))

# S'assurer qu'il y ait des valeurs <5 et >17 dans y_hypothetical
while ( (np.sum(y_hypothetical<5) == 0) or (np.sum(y_hypothetical>17) == 0) ) :
    y_hypothetical = np.random.randint(0, 20, size=len(x_hypothetical))

# Créer les données pour la courbe "Hypothetical approach-config: 70%, 30% avec bruit"
x_hypothetical_noise = x_hypothetical.copy()
y_hypothetical_noise = y_hypothetical + np.random.normal(scale=0.2, size=len(x_hypothetical))

# Créer les données pour la courbe "Hypothetical approach-config: 70%, 30% avec bruit 2"
x_hypothetical_noise2 = x_hypothetical.copy()
y_hypothetical_noise2 = y_hypothetical + np.random.normal(scale=0.8, size=len(x_hypothetical))

# Créer une figure pour chaque courbe comparée à la classique
fig1, ax1 = plt.subplots()
ax1.plot(x_classical, y_classical, marker='o', linestyle='--', label='Classical CBR-approach', color='orange')
ax1.plot(x_hypothetical, y_hypothetical, marker='o', linestyle='-', label='H-CBR Approach_Config:Loi Normal:Means50%, 50%', color='blue')
ax1.set_xlabel('Failures')
ax1.set_ylabel('Number of observed features')
ax1.set_title('Classical-CBR Approach Vs H-CBR Approach_Config:Loi Normal:Means-50%, 50%')
ax1.legend()

fig2, ax2 = plt.subplots()
ax2.plot(x_classical, y_classical, marker='o', linestyle='--', label='Classical CBR-approach', color='orange')
ax2.plot(x_hypothetical_noise, y_hypothetical_noise, marker='o', linestyle='-', label='H-CBR Approach_Config:Loi Normal:90%, 10%', color='green')
ax2.set_xlabel('Failures')
ax2.set_ylabel('Number of observed features')
ax2.set_title('Classical-CBR Approach Vs H-CBR Approach_Config:Loi Normal:90%, 10%')
ax2.legend()

fig3, ax3 = plt.subplots()
ax3.plot(x_classical, y_classical, marker='o', linestyle='--', label='Classical CBR-approach', color='orange')
ax3.plot(x_hypothetical_noise2, y_hypothetical_noise2, marker='o', linestyle='-', label='H-CBR Approach_Config:Loi Normal:70%, 30%', color='purple')
ax3.set_xlabel('Failures')
ax3.set_ylabel('Number of observed features')
ax3.set_title('Classical-CBR Approach Vs H-CBR Approach_Config:Loi Normal:70%, 30%')
ax3.legend()

# Créer une figure pour la fusion des 3 courbes avec la classique
fig4, ax4 = plt.subplots()
ax4.plot(x_classical, y_classical, marker='o', linestyle='--', label='Classical CBR-approach', color='orange')
ax4.plot(x_hypothetical, y_hypothetical, marker='o', linestyle='-', label='H-CBR Approach_Config:Loi Normal:50%, 50%', color='blue')
ax4.plot(x_hypothetical_noise, y_hypothetical_noise, marker='o', linestyle='-', label='H-CBR Approach_Config:Loi Normal:90%, 10%', color='green')
ax4.plot(x_hypothetical_noise2, y_hypothetical_noise2, marker='o', linestyle='-', label='H-CBR Approach_Config:Loi Normal:70%, 30%', color='purple')
ax4.set_xlabel('Failures')
ax4.set_ylabel('Number of observed features')
ax4.set_title('Classical-CBR Approach Vs H-CBR Approach_Config:Loi Normal')
ax4.legend()

# Afficher les figures
plt.show()
