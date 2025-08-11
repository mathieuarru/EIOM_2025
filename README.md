# Ateliers EIOM — Régression linéaire multiple & logistique

## Public
Étudiant·es gradués à l'aise avec R, bases en statistiques abordées de façon opérationnelle.

## Prérequis
- R (≥ 4.3), RStudio récent
- Internet actif (les données proviennent de paquets CRAN)

## Installation rapide
1. Ouvrez `utils/setup-packages.qmd` et exécutez le bloc d’installation
2. Lancez les slides :
   - `atelier1_reg_lin/slides_atelier1.qmd`
   - `atelier2_reg_log/slides_atelier2.qmd`

## Données utilisées
- **Ames** : `AmesHousing::make_ames()` (prix de maisons)
- **Titanic** : `titanic::titanic_train`
- **Default (ISLR)** : `ISLR::Default` (challenge logistique)

## Organisation des missions
Chaque mission est **guidée** (énoncé, étapes, questions) et se conclut par des **points de discussion** pour le retour en groupe. Les **corrigés** proposent une solution commentée.

## Notes pédagogiques
- Les slides incluent un **minuteur** et un **sommaire latéral**.
- Les encarts **Pièges fréquents** facilitent le débrief.
- Tout repose sur `lm()` / `glm()` + tidyverse (`broom`, `yardstick`, etc.).