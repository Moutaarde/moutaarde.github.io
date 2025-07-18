import matplotlib.pyplot as plt
import numpy as np
import random

# Paramètres de la population et sélection
population_total = 3523
selection_count = 12
rang_moyen = 2226
rang_median = 2237
depth = 100

def generer_rangs_realistes(moyenne, mediane, n, rang_min=1, rang_max=3523):
    decalage = moyenne - mediane
    
    # Génère moitié des valeurs en dessous de la médiane
    dessous = sorted([random.randint(max(rang_min, mediane - 100), mediane) for _ in range(n // 2)])
    
    # Génère le reste au-dessus de la médiane, plus dispersé si la moyenne est plus haute
    au_dessus = sorted([random.randint(mediane, min(rang_max, mediane + 100 + abs(decalage))) for _ in range(n - len(dessous))])
    
    return sorted(dessous + au_dessus)

# Générer les rangs simulés
#selection_rangs = generer_rangs_realistes(rang_moyen, rang_median, selection_count)

selection_rangs = [0]*selection_count
ensemble_selections_rangs = []

for i in range(depth):
    ensemble_selections_rangs.append(generer_rangs_realistes(rang_moyen, rang_median, selection_count))

for i in range(selection_count):
    total = 0
    for j in range(depth):
        total += ensemble_selections_rangs[j][i]
    moy = total / depth
    selection_rangs[i] = moy

# Visualisation
fig, ax = plt.subplots(figsize=(10, 2))

ax.hlines(y=1, xmin=selection_rangs[0]-100, xmax=selection_rangs[-1]+100, color='lightgray', linewidth=4)
ax.plot(selection_rangs, [1]*selection_count, 'o', color='blue', label='Rangs sélectionnés')
ax.axvline(x=rang_moyen, color='orange', linestyle='--', label=f'Moyenne ({rang_moyen})')
ax.axvline(x=rang_median, color='green', linestyle='--', label=f'Médiane ({rang_median})')

ax.set_yticks([])
ax.set_xlim(selection_rangs[0]-100, selection_rangs[-1]+100)
ax.set_xlabel("Rang")
ax.set_title("Répartition simulée autour de la moyenne et médiane")
ax.legend(loc='upper right')
plt.tight_layout()
plt.show()

# Afficher les rangs générés
print("Rangs générés :", selection_rangs)
