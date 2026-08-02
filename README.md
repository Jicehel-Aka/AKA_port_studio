# AKA Port Studio

AKA Port Studio est un framework et un ensemble d'outils destinés à faciliter le portage de jeux Pokitto vers la console Gamebuino AKA.

L'objectif du projet est de conserver le maximum du code source original tout en générant des applications AKA natives intégrées aux standards de la plateforme.

---

# Principes

AKA Port Studio repose sur cinq principes fondamentaux :

- Préserver le gameplay original.
- Réutiliser le maximum du code source.
- Respecter les auteurs originaux.
- Respecter les licences d'origine.
- Automatiser le plus possible le processus de portage.

Le projet ne cherche pas à émuler la Pokitto.

Le projet cherche à convertir un jeu Pokitto en application AKA native.

---

# Architecture

```text
Projet Pokitto
      │
      ▼
pokitto2aka
      │
      ▼
Projet AKA
      │
      ├── aka_runtime
      ├── pokitto_compat
      └── code converti
      │
      ▼
Compilation ESP-IDF
      │
      ▼
Application AKA
```

---

# Composants du projet

## aka_runtime

Runtime partagé par tous les jeux portés.

Fonctionnalités :

- Menu système
- Gestion du volume
- Gestion des langues
- Captures d'écran
- Retour au loader
- Gestion SD
- Écran informations
- Écran crédits
- Écran licence

---

## pokitto_compat

Couche de compatibilité Pokitto.

Objectif :

```cpp
#include <Pokitto.h>
```

↓

```cpp
#include <pokitto_compat/Pokitto.h>
```

Compatibilité prévue :

```cpp
Pokitto::Core
Pokitto::Display
Pokitto::Buttons
Pokitto::Sound
Pokitto::Cookie
Sprites
```

---

## pokitto2aka

Convertisseur automatique.

Fonctions :

- Analyse du projet source
- Détection des API Pokitto
- Extraction des métadonnées
- Extraction des licences
- Conversion des assets
- Génération du projet AKA
- Rapport de compatibilité

Exemple :

```bash
pokitto2aka Kong-II-Pokitto/
```

---

## compatibility_db

Base de connaissance utilisée par le convertisseur.

Permet de suivre :

- API supportées
- API partiellement supportées
- API nécessitant une intervention manuelle

---

# Fonctionnalités système standard

Tous les jeux portés bénéficient automatiquement des fonctions suivantes.

## MENU (appui court)

```text
Reprendre

Volume

Langue

Informations

Crédits

Licence

Retour Loader
```

---

## MENU (appui long)

```text
Capture écran
```

---

## RUN + MENU (appui long)

```text
Retour Loader
```

---

# Organisation de la carte SD

## Répertoire global AKA

```text
/sdcard/AKA/
```

Contenu :

```text
settings.json
screenshots/
lang/
```

---

## Répertoire d'un jeu

Exemple :

```text
/sdcard/kong2/
```

Contenu :

```text
save.dat
config.json
highscores.dat
replay.dat
mods/
```

---

# Respect des auteurs

Chaque portage doit obligatoirement conserver :

- l'auteur original
- la licence originale
- le dépôt source original
- les informations du porteur

Ces informations restent accessibles dans le menu système.

---

# Jeux de validation

## V0.1

- Kong II

## V0.2

- Trials Of Astarok
- Galaxy Fighter

Ces projets servent de base pour étendre progressivement la compatibilité de la couche `pokitto_compat`.

---

# Feuille de route

## V0.1

- Runtime AKA (fondation : SD, chemins, retour loader — menu systeme complet a venir)
- Compatibilite Pokitto minimale (Core/Buttons/Display/Sound/Cookie, valides sur Kong-II)
- Analyseur de projet (a faire — le portage V0.1 a ete fait manuellement, cf. compatibility_db pour les constats a automatiser)
- Convertisseur basique (a faire)
- Portage pilote : Kong II (code source compile ; execution/jouabilite sur materiel reel a confirmer)

## V0.2

- Audio avancé
- Tilemaps
- Assistant graphique
- Amélioration de la conversion automatique

## V1.0

Objectif :

```text
URL GitHub
     ↓
Analyse
     ↓
Conversion
     ↓
Compilation
     ↓
Projet AKA compilable
```

---

# Contribuer

Les contributions sont les bienvenues.

Les priorités actuelles sont :

- aka_runtime
- pokitto_compat
- compatibility_db
- pokitto2aka
- Jeux de validation

---

# Licence

Ce projet est distribué sous licence Apache License 2.0.

Voir le fichier LICENSE.
