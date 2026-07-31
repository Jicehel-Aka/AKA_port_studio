# AKA Port Studio
# Port Manifest Specification

Version : 1.0

---

# Objectif

Le fichier `port_manifest.json` décrit un portage.

Il constitue le contrat officiel entre :

- aka_runtime
- pokitto2aka
- compatibility_db
- le launcher AKA
- les outils de build

Chaque portage doit contenir un manifest unique.

---

# Emplacement

```text
project_root/

├── port_manifest.json
├── LICENSE.original
├── README.port.md
└── ...
```

---

# Exemple minimal

```json
{
  "id": "kong2",
  "title": "Kong II",
  "platform": "Pokitto",
  "author": "Press Play On Tape",
  "license": "BSD-3-Clause",
  "source_repository": "https://github.com/Press-Play-On-Tape/Kong-II-Pokitto"
}
```

---

# Exemple complet

```json
{
  "schema_version": 1,

  "id": "kong2",

  "title": "Kong II",

  "version": "1.0.0",

  "platform": "Pokitto",

  "port_level": "raw",

  "author": "Press Play On Tape",

  "porter": "AKA Port Studio",

  "license": "BSD-3-Clause",

  "copyright": "Press Play On Tape",

  "source_repository":
  "https://github.com/Press-Play-On-Tape/Kong-II-Pokitto",

  "description":
  "Pokitto to AKA port",

  "supports_save": true,

  "supports_screenshot": true,

  "supports_languages": true,

  "supports_pause": true,

  "save_directory":
  "/sdcard/kong2/",

  "license_file":
  "LICENSE.original",

  "credits_file":
  "CREDITS.md"
}
```

---

# Champs obligatoires

## id

Identifiant unique.

Exemple :

```json
"id":"kong2"
```

Contraintes :

- minuscules
- chiffres autorisés
- pas d'espace
- stable dans le temps

Utilisé pour :

```text
/sdcard/kong2/
```

---

## title

Nom affiché.

Exemple :

```json
"title":"Kong II"
```

---

## platform

Plateforme d'origine.

Valeurs possibles :

```text
Pokitto
Arduboy
GamebuinoMETA
Custom
```

---

## author

Auteur original.

Exemple :

```json
"author":"Press Play On Tape"
```

---

## license

Licence originale.

Exemple :

```json
"license":"BSD-3-Clause"
```

---

## source_repository

URL officielle du projet d'origine.

Exemple :

```json
"source_repository":
"https://github.com/Press-Play-On-Tape/Kong-II-Pokitto"
```

---

# Champs recommandés

## porter

Auteur du portage.

Exemple :

```json
"porter":"Jean-Charles Lebeau"
```

---

## version

Version du portage.

Exemple :

```json
"version":"1.0.0"
```

---

## description

Description courte.

Exemple :

```json
"description":
"Classic arcade platform game"
```

---

# Port Level

## raw

Portage fidèle.

Objectifs :

- gameplay inchangé
- interface inchangée
- contrôles inchangés

---

## enhanced

Portage enrichi.

Ajouts possibles :

- informations dans les bordures
- options AKA
- améliorations ergonomiques

---

## native

Réécriture importante.

Le jeu reste inspiré de la version originale mais exploite pleinement l'AKA.

---

# Fonctionnalités

## supports_save

```json
"supports_save":true
```

---

## supports_screenshot

```json
"supports_screenshot":true
```

---

## supports_languages

```json
"supports_languages":true
```

---

## supports_pause

```json
"supports_pause":true
```

---

# Contrôles

Optionnel.

Exemple :

```json
{
  "controls":
  {
    "a":"Jump",
    "b":"Fire",
    "c":"Action",
    "d":"Pause"
  }
}
```

Utilisé dans l'écran Informations.

---

# Extensions AKA

Optionnel.

Exemple :

```json
{
  "aka_features":
  [
    "pause_button",
    "system_menu",
    "screenshots"
  ]
}
```

---

# Validation

Le manifest est invalide si :

- id absent
- title absent
- author absent
- license
