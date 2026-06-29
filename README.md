# knapsack-problem

# 🎒 Problème du Sac à Dos — Résolution par Programmation Linéaire

Mini-projet d'algorithmique et recherche opérationnelle réalisé dans le cadre
du cursus DA2I (S4).

## 📋 Description

Résolution du problème d'optimisation combinatoire du **sac à dos 0/1**
en utilisant la programmation linéaire en nombres entiers (ILP) avec la
bibliothèque PuLP.

**Problème :** Sélectionner un sous-ensemble d'objets maximisant la valeur
totale sans dépasser la capacité du sac.

## 🧮 Données du problème

| Objet | Poids (kg) | Valeur |
|-------|-----------|--------|
| A     | 2         | 3      |
| B     | 3         | 4      |
| C     | 4         | 5      |
| D     | 5         | 8      |
| E     | 9         | 10     |

**Capacité maximale :** 15 kg

## ⚙️ Approche

- Modélisation en **problème de maximisation linéaire** (ILP)
- Variables de décision **binaires** (prendre ou non chaque objet)
- Résolution via le solveur **CBC** intégré à PuLP

## 🛠️ Technologies

- **Python 3**
- **PuLP** — bibliothèque d'optimisation linéaire

## 🚀 Installation & Exécution

```bash
# Installer la dépendance
pip install pulp

# Lancer le programme
python sac_dos.py
```

## 📤 Résultat attendu

Prendre l'objet A

Prendre l'objet B

Prendre l'objet D

Prendre l'objet E

## 👤 Auteur

**Mamadou Abou Ba** — Étudiant DA2I 
🔗 [GitHub](https://github.com/Mohamadou2)

