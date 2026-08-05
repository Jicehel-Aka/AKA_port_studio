# AKA Port Studio
# Runtime Specification

Version : 0.1

---

# Objectif

aka_runtime est le socle commun de tous les jeux portés.

Il fournit :

- menu système
- captures d'écran
- gestion des langues
- gestion du volume
- chargement du manifest
- crédits
- licence
- retour au loader
- accès aux chemins SD

Les jeux n'ont pas besoin de réimplémenter ces fonctionnalités.

---

# Architecture

```text
Jeu
 │
 ▼
aka_runtime
 │
 ▼
Gamebuino AKA SDK
```

---

# Cycle de vie

## Initialisation

```cpp
akaRuntime.begin();
```

Charge :

- settings.json
- port_manifest.json

Initialise :

- langue
- volume
- système de captures

---

## Boucle principale

```cpp
akaRuntime.update();
```

Doit être appelée une fois par frame.

Responsabilités :

- surveiller MENU
- surveiller RUN
- gérer les raccourcis système
- gérer les notifications

---

# Contrôles système

## MENU

### Appui court

Ouvre le menu système.

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

### Appui long

Déclenche :

```text
Capture écran
```

---

## RUN + MENU

### Appui long

Déclenche :

```text
Retour Loader
```

---

# Captures d'écran

API :

```cpp
akaRuntime.takeScreenshot();
```

Répertoire (V0.4 : reorganise, un dossier par jeu -- cf. addendum DECISIONS.md) :

```text
/sdcard/<gameId>/screenshots/
```

Nommage (V0.4 : plus de prefixe du jeu dans le nom -- le dossier l'indique deja) :

```text
0001.BMP
KONG2_0002.BMP
```

---

# Gestion du volume

API :

```cpp
akaRuntime.getMusicVolume();

akaRuntime.setMusicVolume();

akaRuntime.getSfxVolume();

akaRuntime.setSfxVolume();
```

Stockage :

```text
/sdcard/AKA/settings.json
```

---

# Gestion des langues

API :

```cpp
akaRuntime.getLanguage();

akaRuntime.setLanguage();

akaRuntime.translate("KEY");
```

Fichiers (V0.4 : deux niveaux -- commun + specifique au jeu, cf. addendum DECISIONS.md) :

```text
/sdcard/AKA/lang/<code>.json          -- commun (libelles du menu systeme, partage par tous les jeux)
/sdcard/<gameId>/lang/<code>.json     -- specifique au jeu (commandes, etc.), prioritaire en cas de cle en double
```

Exemple :

```text
fr.json
en.json
de.json
es.json
it.json
```

---

# Informations

Lecture depuis :

```text
port_manifest.json
```

Affiche :

- titre
- auteur
- licence
- version
- plateforme d'origine

---

# Crédits

Affichage obligatoire.

Informations minimales :

- auteur original
- porteur
- framework

---

# Licence

Lecture automatique :

```text
LICENSE.original
```

---

# Accès aux chemins

```cpp
akaRuntime.gamePath();

akaRuntime.settingsPath();

akaRuntime.screenshotPath();
```

Exemple :

```cpp
std::string saveFile =
    akaRuntime.gamePath() +
    "/save.dat";
```

---

# Notifications

Exemples :

```text
Capture enregistrée

Sauvegarde effectuée

Volume modifié
```

Affichage temporaire.

---

# Portabilité

Aucun code du jeu ne doit dépendre directement :

- du menu système
- des captures écran
- du retour loader

Ces fonctionnalités appartiennent exclusivement au runtime.

