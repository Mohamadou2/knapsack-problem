from pulp import LpMaximize, LpProblem, LpVariable, lpSum

# Données
objets = ['A', 'B', 'C', 'D', 'E']
poids = {'A': 2, 'B': 3, 'C': 4, 'D': 5, 'E': 9}
valeurs = {'A': 3, 'B': 4, 'C': 5, 'D': 8, 'E': 10}
capacite = 15

# Modèle
model = LpProblem(name="sac-a-dos", sense=LpMaximize)
x = {i: LpVariable(name=i, cat='Binary') for i in objets}

# Fonction objectif
model += lpSum(valeurs[i] * x[i] for i in objets), "ValeurTotale"

# Contrainte de capacité
model += lpSum(poids[i] * x[i] for i in objets) <= capacite, "ContraintePoids"

# Résolution
model.solve()

# Résultats
for i in objets:
    if x[i].value() == 1:
        print(f"Prendre l'objet {i}")