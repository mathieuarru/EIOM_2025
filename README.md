# EIOM 2025 — Ateliers de modélisation statistique

[![Quarto Publish](https://img.shields.io/badge/Quarto-publish-blue)](https://quarto.org/)  
Site en ligne 👉 [aureliennicosiaulaval.github.io/EIOM_2025](https://aureliennicosiaulaval.github.io/EIOM_2025/)

---

## 📚 Présentation

Ce dépôt contient le matériel pédagogique des **ateliers EIOM 2025**, centrés sur l’introduction à la **régression linéaire multiple** et à la **régression logistique**.

Les ateliers sont conçus pour un public universitaire et visent à combiner **théorie**, **expérimentation** et **discussion critique**.

---

## 🗂 Structure du dépôt

```
EIOM_2025/
├── _quarto.yml         # Configuration du site Quarto
├── index.qmd           # Page d'accueil
├── slides/             # Diapositives (Atelier 1 et 2)
├── missions/           # Missions pratiques (QMD)
├── utils/              # Fichiers utilitaires (CSS, requirements, etc.)
└── README.md           # Ce fichier
```

---

## 🎯 Objectifs pédagogiques

- **Atelier 1 — Régression linéaire multiple**
  - Comprendre la formulation du modèle.
  - Apprendre à lire/interpréter les coefficients.
  - Vérifier les hypothèses via diagnostics.
  - Expérimenter à travers des missions guidées.

- **Atelier 2 — Régression logistique**
  - Introduire la régression pour une réponse binaire.
  - Interpréter en termes de logit / odds ratio.
  - Évaluer les modèles : confusion, sens/spéc, ROC, AUC, calibration.
  - Discuter du choix de seuils selon le contexte.

---

## 🚀 Installation locale

Pour reproduire les ateliers sur votre machine :

```bash
# Cloner le dépôt
git clone https://github.com/AurelienNicosiaULaval/EIOM_2025.git
cd EIOM_2025

# Lancer le site localement
quarto preview
```

### 📦 Dépendances R

Dans R / RStudio, installer les librairies nécessaires :

```r
install.packages(c(
  "tidyverse", "ggplot2", "dplyr", "broom", "janitor",
  "GGally", "car", "performance", "pROC",
  "AmesHousing", "titanic", "scales"
))
```

---

## 🌐 Site en ligne

Le site est publié automatiquement via **GitHub Pages** :  
👉 [aureliennicosiaulaval.github.io/EIOM_2025](https://aureliennicosiaulaval.github.io/EIOM_2025/)

---

## 👤 Auteur

**Aurélien Nicosia**  
Chargé d’enseignement, Université Laval  
📧 [aurelien.nicosia@mat.ulaval.com](mailto:aurelien.nicosia@mat.ulaval.com)  
🌐 [GitHub](https://github.com/AurelienNicosiaULaval)


---

## 📜 Licence

Ce matériel pédagogique est distribué sous licence **MIT** (libre d’utilisation, modification et distribution avec attribution).
