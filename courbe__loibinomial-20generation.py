import matplotlib.pyplot as plt
import numpy as np

# Créer les données pour la courbe "Classical CBR-approach"
pn = ['p{}'.format(i) for i in range(1, 12)]
x_classical = np.array(pn)
y_classical = np.ones(len(x_classical))*30

# Créer les données pour les courbes "Hypothetical approach-config: 70%, 30%" avec 20 variations
x_hypothetical = x_classical.copy()
y_hypothetical_variations = []
for i in range(20):
    y_hypothetical = np.random.randint(0, 15, size=len(x_hypothetical))
    while ( (np.sum(y_hypothetical<5) == 0) or (np.sum(y_hypothetical>17) == 0) ) :
        y_hypothetical = np.random.randint(0, 15, size=len(x_hypothetical))
    y_hypothetical_variations.append(y_hypothetical + i*0.001)

# Créer les données pour les courbes "Hypothetical approach-config: 70%, 30% avec bruit" avec 20 variations
x_hypothetical_noise = x_hypothetical.copy()
y_hypothetical_noise_variations = []
for i in range(20):
    binomial = np.random.binomial(scale=0.2, size=len(x_hypothetical))
    y_hypothetical_noise = y_hypothetical + binomial + i * 0.001
    y_hypothetical_noise_variations.append(y_hypothetical_noise)

# Créer les données pour les courbes "Hypothetical approach-config: 70%, 30% avec bruit 2" avec 20 variations
x_hypothetical_noise2 = x_hypothetical.copy()
y_hypothetical_noise2_variations = []
for i in range(20):
    y_hypothetical_noise2 = y_hypothetical + np.random.binomial(scale=0.8, size=len(x_hypothetical)) + i*0.001
    y_hypothetical_noise2_variations.append(y_hypothetical_noise2)

# Créer une figure pour chaque courbe comparée à la classique
fig1, ax1 = plt.subplots()
ax1.plot(x_classical, y_classical, marker='o', linestyle='--', label='Classical CBR-approach', color='orange')
for y_hypothetical in y_hypothetical_variations:
    ax1.plot(x_hypothetical, y_hypothetical, marker='o', linestyle='-', color='blue', alpha=0.3)
ax1.set_xlabel('Failures')
ax1.set_ylabel('Number of observed features')
binomial = 'Normal'
ax1.set_title(('Classical-CBR Approach Vs H-CBR Approach_Config:Loi ' + binomial + ':-50%, 50%'))
ax1.legend()

fig2, ax2 = plt.subplots()
ax2.plot(x_classical, y_classical, marker='o', linestyle='--', label='Classical CBR-approach', color='orange')
for y_hypothetical_noise in y_hypothetical_noise_variations:
    ax2.plot(x_hypothetical_noise, y_hypothetical_noise, marker='o', linestyle='-', color='green', alpha=0.3)
ax2.set_xlabel('Failures')
ax2.set_ylabel('Number of observed features')
ax2.set_title(('Classical-CBR Approach Vs H-CBR Approach_Config:Loi ' + binomial + ':90%, 10%'))
ax2.legend()

fig3, ax3 = plt.subplots()
ax3.plot(x_classical, y_classical, marker='o', linestyle='--', label='Classical CBR-approach', color='orange')
for y_hypothetical_noise2 in y_hypothetical_noise2_variations:
    ax3.plot(x_hypothetical_noise2, y_hypothetical_noise2, marker='o', linestyle='-', color='purple', alpha=0.3)
ax3.set_xlabel('Failures')
ax3.set_ylabel('Number of observed features')
ax3.set_title(('Classical-CBR Approach Vs H-CBR Approach_Config:Loi ' + binomial + ':70%, 30%'))
ax3.legend()

# Créer une figure pour la fusion des 3 courbes avec la classique
fig4, ax4 = plt.subplots()
ax4.plot(x_classical, y_classical, marker='o', linestyle='--', label='Classical CBR-approach', color='orange')
ax4.plot(x_hypothetical, y_hypothetical, marker='o', linestyle='-', label=(
            'H-CBR Approach_Config:Loi ' + binomial + ':50%, 50%'), color='#1f77b4')
ax4.plot(x_hypothetical_noise, y_hypothetical_noise, marker='o', linestyle='-', label=(
            'H-CBR Approach_Config:Loi ' + binomial + ':90%, 10%'), color='#add151')
ax4.plot(x_hypothetical_noise2, y_hypothetical_noise2, marker='o', linestyle='-', label=(
            'H-CBR Approach_Config:Loi ' + binomial + ':70%, 30%'), color='#52b5da')
ax4.set_xlabel('Failures')
ax4.set_ylabel('Number of observed features')
ax4.set_title('Classical-CBR Approach Vs H-CBR Approach_Config:Loi %s' % binomial)
ax4.legend()

# Afficher les figures
plt.show()