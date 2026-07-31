# AKA Port Studio
# Compatibility Database Specification

Version : 1.0

---

# Objectif

La Compatibility Database (compatibility_db) décrit
l'état de compatibilité entre l'API source et l'API AKA.

Elle est utilisée par :

- pokitto2aka
- l'analyseur source
- les rapports de conversion
- la documentation
- les futures interfaces graphiques

---

# Principe

Chaque symbole identifié dans le code source reçoit un état.

Exemple :

```cpp
Pokitto::Display::drawBitmap()
```

↓

```json
{
  "symbol": "Pokitto::Display::drawBitmap",
  "status": "SUPPORTED"
}
```

---

# Etats possibles

## SUPPORTED

Support complet.

Aucune intervention nécessaire.

Exemple :

```cpp
Pokitto::Buttons::aBtn()
```

---

## WRAPPED

Supporté par une couche de compatibilité.

Exemple :

```cpp
Pokitto::Display::print()
```

converti via :

```cpp
pokitto_compat
```

---

## PARTIAL

Support partiel.

Certaines fonctionnalités peuvent manquer.

Exemple :

```cpp
Pokitto::Sound::playMusicStream()
```

---

## MANUAL

Intervention humaine nécessaire.

Exemple :

```cpp
Direct Framebuffer Access
```

---

## UNSUPPORTED

Aucune solution connue.

Le projet ne peut pas être converti automatiquement.

---

# Structure du fichier

Fichier :

```text
compatibility_db/
compatibility_db.json
```

---

# Exemple

```json
{
  "schema_version": 1,

  "symbols":
  [
    {
      "symbol":
      "Pokitto::Core::begin",

      "status":
      "SUPPORTED",

      "since":
      "0.1"
    },

    {
      "symbol":
      "Pokitto::Display::drawBitmap",

      "status":
      "WRAPPED",

      "since":
      "0.1"
    },

    {
      "symbol":
      "Sprites::drawPlusMask",

      "status":
      "PARTIAL",

      "since":
      "0.1"
    },

    {
      "symbol":
      "DirectFramebufferAccess",

      "status":
      "MANUAL"
    }
  ]
}
```

---

# Catégories

Chaque symbole appartient à une catégorie.

Exemples :

```json
{
  "category":"display"
}
```

Valeurs possibles :

```text
core
display
buttons
sound
sprites
storage
file
system
other
```

---

# Niveau de confiance

Optionnel.

```json
{
  "confidence":100
}
```

Valeurs :

```text
0 à 100
```

Exemple :

```json
{
  "symbol":
  "Pokitto::Buttons::aBtn",

  "status":
  "SUPPORTED",

  "confidence":
  100
}
```

---

# Notes techniques

Optionnel.

```json
{
  "notes":
  "Reimplemented in pokitto_compat"
}
```

---

# Règles de détection

Le moteur d'analyse utilise :

```json
{
  "patterns":
  [
    "Pokitto::Display::",
    "Pokitto::Sound::",
    "Sprites::"
  ]
}
```

pour détecter automatiquement les API.

---

# Score de compatibilité

Le convertisseur génère un score.

Formule initiale :

SUPPORTED   = 100%

WRAPPED     = 90%

PARTIAL     = 50%

MANUAL      = 10%

UNSUPPORTED = 0%
```

---

## Exemple

Projet :

```text
100 symboles détectés

80 supported
10 wrapped
5 partial
5 manual
```

Score :

```text
89 %
```

---

# Rapport de conversion

Exemple :

```text
Compatibility Report

Project :
Kong II

Display :
SUPPORTED

Buttons :
SUPPORTED

Core :
SUPPORTED

Sprites :
PARTIAL

Sound :
WRAPPED

Global score :
92%
```

---

# Règles V0.1

Toute API nécessaire à la compilation de Kong-II
doit être ajoutée dans la base de compatibilité.

Les projets suivants :

- Kong-II
- Trials Of Astarok
- Galaxy Fighter

servent de référence pour étendre progressivement
la couverture.

---

# Objectif long terme

Permettre à pokitto2aka d'estimer automatiquement :

- le taux de conversion
- les fichiers à modifier
- les risques de portage
- le travail manuel restant

avant même la génération du projet AKA.
