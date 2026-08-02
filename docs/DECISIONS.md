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

---

# Addendum — retour d'expérience portage Kong-II (V0.1)

Décisions/constats issus du premier portage réel, à connaître avant
d'implémenter `pokitto2aka` (l'automatisation) ou de porter un second jeu.

## Placement physique des composants ESP-IDF

## Constat

Le schéma d'architecture montre `aka_runtime` et `pokitto_compat` comme
dossiers frères à la racine du projet. **En pratique**, le système de build
ESP-IDF ne scanne par défaut que `components/` et `main/` — des composants
placés à la racine ne sont pas découverts sans `EXTRA_COMPONENT_DIRS`.

## Décision retenue

✅ Placer `aka_runtime/` et `pokitto_compat/` sous `components/`, au même
niveau que le SDK `gamebuino` (`components/aka_runtime`,
`components/pokitto_compat`). La séparation **logique** décrite dans
l'architecture reste inchangée ; seule l'imbrication physique diffère d'un
niveau, ce qui est la convention standard ESP-IDF.

## Alternative rejetée

❌ `EXTRA_COMPONENT_DIRS` pointant vers les dossiers racine — techniquement
possible mais sémantique ambiguë (dossier unique vs dossier conteneur de
plusieurs composants) et donc plus risqué à générer automatiquement dans
`pokitto2aka`.

---

## Code partagé entre composants (ex. lecture des boutons)

## Constat

Un composant ESP-IDF ne voit **que** les `INCLUDE_DIRS` publics des
composants qu'il déclare dans `REQUIRES` — jamais l'inverse. Du code
partagé par plusieurs composants (ex. `core/input.h`, la lecture des
boutons/joystick) ne doit donc **pas** vivre dans `main/`, sinon
`aka_runtime` et `pokitto_compat` (qui en ont besoin) ne peuvent pas le
voir.

## Décision retenue

✅ Tout code d'infrastructure partagé (lecture des boutons, etc.) vit dans
`aka_runtime` (le composant "socle commun" déjà conçu pour ça), jamais dans
`main`. `main` peut dépendre de tout ; rien ne doit dépendre de `main`.

---

## Audio : primitive PCM directe disponible dans le SDK

## Constat

Le SDK partagé (`components/gamebuino`) fournit déjà
`gb_audio_track_wav::play_raw(const int16_t*, size_t)` — lecture
d'échantillons PCM 16 bits directement depuis la mémoire, sans encapsulage
WAV. C'est la primitive idéale pour `Pokitto::Sound::playSFX` (échantillons
embarqués courts) ; `play_wav(chemin)` convient pour `playMusicStream`
(streaming SD, nécessite un fichier avec en-tête RIFF/WAVE valide).

## Décision retenue

✅ `pokitto_compat` s'appuie directement sur `gb_audio_track_wav`, pas besoin
d'un nouveau sous-système audio.

---

## Jeu de validation V0.1 (Kong-II) : bilan

## Constat

Une fois la fondation (`pokitto_compat` + `aka_runtime` + macros AVR)
posée, la quasi-totalité des ~50 fichiers sources de Kong-II a compilé sans
modification du code métier — conforme à l'objectif "conservation du code
métier". Les seules interventions sur le code source du jeu ont été :

- reformatage des `#include "Pokitto.h"` → `#include "pokitto_compat/Pokitto.h"` ;
- un `-Wno-error` supplémentaire pour une ligne de code mort préexistante
  (`return X; Y;`) dans le jeu d'origine — corrigé côté flags de
  compilation plutôt que dans le fichier vendu, pour rester fidèle au
  principe de conservation.

## Confirme

Le principe directeur "conservation du code métier + couche de
compatibilité" fonctionne comme prévu pour ce premier cas réel.

---

## Addendum — bugs trouves uniquement sur materiel reel (premier test Kong-II)

Deux bugs graves ont echappe a la revue de code et n'ont ete decouverts
qu'au premier lancement sur console. A retenir pour le processus de
validation de tout futur portage :

## Constat

- Le bug d'alignement des lignes `drawBitmap` (cisaillement diagonal) ne se
  voit QUE visuellement, sur ecran reel -- rien dans les logs de compilation
  ne le signale.
- Le silence audio total ne produit aucune erreur ni warning -- le code
  playSFX/playMusicStream s'execute "normalement" sans jamais rien produire.

## Decision retenue

✅ Le processus V1.0 de `pokitto2aka` doit prevoir une etape de **validation
visuelle et audio sur materiel reel** (ou emulateur fidele), pas seulement
"le projet compile". Deux verifications minimales a automatiser/documenter
pour tout nouveau portage :
1. Capturer un ecran (splash + un ecran avec du texte/UI) et verifier
   l'absence de cisaillement sur les sprites a largeur impaire.
2. Confirmer qu'au moins un son (SFX de menu) est audible des le premier
   lancement.

✅ La fonction de capture d'ecran (`AkaRuntime::takeScreenshot()`, appui
long sur MENU) doit etre implementee et testee **avant** tout autre travail
de portage sur un nouveau jeu -- c'est elle qui a permis de diagnostiquer
precisement le bug `drawBitmap` sans elle, on aurait devine a l'aveugle.

---

# Addendum — 2e jeu de reference (Galaxy Fighter) : validation croisee

Premiere vraie validation de la methode sur un jeu DIFFERENT de Kong-II.
Resultat global : la fondation (Core/Buttons/Cookie/Sound/macros AVR)
s'est reutilisee sans modification. Un point a force une evolution
architecturale du module Display.

## Constat

Galaxy Fighter accede DIRECTEMENT au framebuffer (`PD::screenbuffer`,
memset brut), lit `PD::width`/`PD::height` comme des champs simples, et
assigne `PD::invisiblecolor` directement (pas seulement via une methode).
Le modele V0.1 ("chaque primitive blitte immediatement vers l'ecran reel")
ne pouvait pas satisfaire cet acces direct.

## Decision retenue

✅ `Pokitto::Display` gere desormais un vrai **framebuffer indexe
persistant** (220x176, 4 bits/pixel, 2 pixels/octet) — exactement comme le
Pokitto reel. Toutes les primitives (drawPixel, fillRect, drawBitmap,
drawColumn...) ECRIVENT dans ce framebuffer ; `present()` (appele une fois
par frame) decode l'integralite du buffer via la palette et fait un seul
blit vers l'ecran AKA. C'est un changement d'architecture (V0.1 -> V0.2),
mais **retro-compatible a 100% avec Kong-II** (verifie : Kong-II n'utilise
aucune des nouvelles API, aucune regression).

## A retenir pour la suite

Cette architecture (framebuffer persistant + present() unique) est
desormais la reference pour `pokitto_compat`, pas seulement un cas
particulier pour Galaxy Fighter. Tout nouveau jeu qui accederait au
framebuffer autrement (ex. mode graphique different, double-buffering
explicite) devra etre etudie au cas par cas.

## My_settings.h : lecture automatique a prevoir

Confirme sur ce 2e jeu : `My_settings.h` de CHAQUE jeu Pokitto definit
reellement `INCLUDE_SOUND`/`INCLUDE_SOUND_FROM_SD` (et d'autres flags
`PROJ_*`). Le convertisseur `pokitto2aka` (non encore implemente) devrait
PARSER ce fichier et reporter automatiquement ses `#define` pertinents,
plutot que de les decouvrir manuellement jeu par jeu (a coute plusieurs
allers-retours de debogage sur Kong-II, ou l'absence d'INCLUDE_SOUND
causait un silence total sans la moindre erreur de compilation).

## Police : aucune police Pokitto reelle disponible

Comme `palettePico`, les polices nommees (`fontC64`, etc.) sont fournies
par le vrai SDK Pokitto et absentes des depots de jeux portes. Une police
5x7 maison a ete generee par rendu programmatique (voir
`pokitto_compat/Font5x7.h`) plutot que de tenter de reconstituer la police
d'origine a la main.
