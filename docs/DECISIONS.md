# AKA Port Studio

## Historique des réflexions et décisions

Ce document conserve les choix techniques et architecturaux effectués durant la conception du projet.

---

# Philosophie générale

## Objectif

Créer un système permettant de convertir des jeux Pokitto vers la Gamebuino AKA avec un minimum d'intervention humaine.

Le projet doit conserver :

- le gameplay original ;
- les auteurs ;
- les licences ;
- le dépôt source original.

---

# Émulation ou portage

## Décision retenue

✅ Portage vers une application AKA native.

## Solutions rejetées

❌ Émulation Pokitto complète.

❌ Reproduction du matériel Pokitto.

### Raisons

- meilleures performances ;
- intégration native au système AKA ;
- maintenance plus simple ;
- compatibilité à long terme.

---

# Couche de compatibilité

## Décision retenue

Création d'une bibliothèque :

```text
pokitto_compat
```

Objectif :

```cpp
#include <Pokitto.h>
```

↓

```cpp
#include <pokitto_compat/Pokitto.h>
```

Le code métier doit rester le plus proche possible de l'original.

---

# Runtime commun

## Décision retenue

Créer un composant partagé :

```text
aka_runtime
```

Tous les ports l'utilisent.

### Fonctions fournies

- Menu système
- Gestion volume
- Gestion langues
- Captures écran
- Retour loader
- Gestion SD
- Informations
- Crédits
- Licence

---

# Menu système standard

## Décision retenue

MENU appui court :

```text
Reprendre

Volume

Langue

Informations

Crédits

Licence

Retour Loader
```

### Motivation

Offrir une expérience utilisateur homogène sur tous les portages.

---

# Capture écran

## Décision retenue

Commande :

```text
MENU maintenu
```

Stockage :

```text
/sdcard/AKA/screenshots/
```

### Motivation

Fonctionnalité système disponible dans tous les jeux.

---

# Retour au loader

## Décision retenue

Commande :

```text
RUN + MENU maintenus
```

### Motivation

Comportement identique sur tous les ports.

---

# Sauvegardes

Deux solutions ont été étudiées :

### Solution 1

```text
NVS
```

### Solution 2

```text
Carte SD
```

## Décision retenue

✅ Carte SD.

## Solution rejetée

❌ NVS.

### Raisons

- visibilité des données ;
- sauvegarde facile ;
- transfert simple ;
- débogage facilité ;
- extensibilité.

---

# Organisation de la carte SD

## Décision retenue

Répertoire global :

```text
/sdcard/AKA/
```

Contient :

```text
settings.json
screenshots/
lang/
```

---

## Répertoire spécifique à chaque jeu

Exemple :

```text
/sdcard/kong2/
```

Contient :

```text
save.dat
config.json
highscores.dat
replay.dat
mods/
```

### Motivation

Chaque jeu reste autonome.

La sauvegarde complète d'un jeu revient à copier un seul dossier.

---

# Préférences globales

## Décision retenue

Fichier :

```text
/sdcard/AKA/settings.json
```

Contient :

```json
{
  "language": "fr",
  "music_volume": 80,
  "sfx_volume": 70
}
```

### Portée

Paramètres partagés par tous les jeux.

---

# Respect des auteurs

## Décision retenue

Chaque port doit contenir :

- Auteur original
- Licence originale
- Référence du dépôt source
- Auteur du portage

Ces informations doivent être accessibles dans le jeu.

---

# Modes d'affichage

## Décision retenue

Un seul mode d'affichage est supporté.

Le rendu Pokitto est toujours affiché dans un viewport
220x176 centré sur l'écran AKA.

Aucun redimensionnement n'est effectué.

Aucune déformation n'est autorisée.

Les zones libres de l'écran AKA peuvent être utilisées
pour afficher des informations complémentaires propres
à la plateforme :

- état du système ;
- rappels des commandes ;
- score ;
- statistiques ;
- indicateurs ;
- options supplémentaires.

---

# Contrôles

## Boutons réservés au système

MENU
RUN

Ces boutons ne doivent jamais être utilisés
par le jeu.

Ils sont gérés exclusivement par aka_runtime.

## Mapping Pokitto

Pokitto A → AKA A
Pokitto B → AKA B
Pokitto C → AKA C

## Extensions AKA

AKA D
AKA L1
AKA R1

peuvent être utilisés pour des fonctionnalités
supplémentaires sans modifier le gameplay original.

# Extensions spécifiques Kong II
 
## Décision retenue
 
Aucune extension gameplay.
 
Le gameplay Pokitto est conservé à l'identique.
 
## Bouton supplémentaire utilisé
 
AKA D → Pause
 
## Boutons non utilisés
 
AKA L1
AKA R1
 
## Motivation
 
- Respect maximal du jeu original
- Simplicité du portage
- Aucun risque de modifier l'équilibrage
- Comportement identique à la version Pokitto

# Politique des extensions AKA
 
Les boutons supplémentaires AKA ne doivent pas être utilisés
sans justification.
 
Par défaut :
 
- A, B, C → mapping Pokitto
- D, L1, R1 → non affectés
 
L'utilisation de D, L1 ou R1 doit apporter une fonctionnalité
claire et utile.
 
L'absence d'utilisation est préférable à une fonctionnalité
artificielle.

---

# Gestion des licences

## Décision retenue

Le convertisseur récupère automatiquement :

```text
LICENSE
README
```

quand ils existent.

Le port généré intègre :

- les crédits ;
- la licence originale ;
- l'URL du projet.

---

## Motivation

- respect du pixel-art original ;
- rendu identique à la Pokitto ;
- absence d'artefacts de mise à l'échelle ;
- comportement cohérent sur tous les portages.

# Jeux de validation

## Ordre retenu

### Premier jeu

```text
Kong-II
```

### Puis

```text
Trials Of Astarok
Galaxy Fighter
```

### But

Construire progressivement la compatibilité Pokitto à partir de cas réels.

---

# Compatibilité ciblée V0.1

```cpp
Pokitto::Core
Pokitto::Display
Pokitto::Buttons
Pokitto::Sound
Pokitto::Cookie
Sprites
```

Tout nouvel élément requis par un jeu de référence est ajouté au périmètre officiel.

---

# Vision long terme

Objectif final :

```text
URL GitHub
     ↓
Analyse automatique
     ↓
Conversion automatique
     ↓
Compilation AKA
     ↓
Projet prêt à exécuter
```

avec :

- menu standard AKA ;
- captures écran ;
- retour loader ;
- volume global ;
- langues ;
- sauvegarde SD ;
- crédits ;
- licence ;
- traçabilité complète du projet d'origine.

---

# Principe directeur

AKA Port Studio doit privilégier :

1. La conservation du code métier.
2. L'automatisation.
3. La simplicité pour l'utilisateur.
4. Le respect des auteurs.
5. La maintenabilité à long terme.
