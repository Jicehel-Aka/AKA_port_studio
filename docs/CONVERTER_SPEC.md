# AKA Port Studio
# Pokitto Converter Specification

Version : 0.1

---

# Objectif

Le convertisseur `pokitto2aka` est le cœur d'AKA Port Studio.

Il prend un projet Pokitto et génère un projet AKA compilable.

Le convertisseur doit être :

- non destructif ;
- reproductible ;
- traçable ;
- automatisable.

---

# Philosophie

Le projet source n'est jamais modifié.

Principe :

```text
Projet Pokitto
      ↓
Analyse
      ↓
Conversion
      ↓
Nouveau projet AKA
```

Le répertoire source reste intact.

---

# Entrées

Le convertisseur doit accepter :

## Dossier local

```bash
pokitto2aka ./Kong-II-Pokitto
```

---

## Archive ZIP

```bash
pokitto2aka ./Kong-II.zip
```

---

## Dépôt Git

```bash
pokitto2aka \
  https://github.com/.../Kong-II-Pokitto
```

---

# Sorties

Projet complet :

```text
Kong-II-AKA/

├── main/
├── components/
├── assets/
├── docs/

├── port_manifest.json

├── LICENSE.original
├── README.original

├── README.port.md

└── compatibility_report.json
```

---

# Pipeline

## Phase 1

Import

```text
Projet détecté
```

Extraction :

- nom
- licence
- README
- structure

---

## Phase 2

Analyse

Scan :

```cpp
Pokitto::
Sprites::
```

Inventaire :

```json
{
  "apis": [
    "Pokitto::Display",
    "Pokitto::Buttons",
    "Sprites"
  ]
}
```

---

## Phase 3

Compatibilité

Consultation :

```text
compatibility_db.json
```

Production :

```text
SUPPORTED
PARTIAL
MANUAL
UNSUPPORTED
```

---

## Phase 4

Analyse assets

Détection :

```text
PNG
BMP
JPG
RAW
H
C
CPP
```

contenant des ressources.

---

## Phase 5

Conversion assets

Génération :

```text
assets_original/
assets_aka/
```

Le projet d'origine est conservé.

---

## Phase 6

Réécriture source

Transformation :

```cpp
#include <Pokitto.h>
```

↓

```cpp
#include <pokitto_compat/Pokitto.h>
```

---

## Phase 7

Génération du manifest

```json
port_manifest.json
```

---

## Phase 8

Génération documentation

Création :

```text
README.port.md

compatibility_report.json

compatibility_report.md
```

---

# Analyseur C/C++

## Objectif

Identifier automatiquement :

```cpp
Pokitto::Display::drawBitmap
Sprites::drawPlusMask
```

sans compilation.

---

## Résultat

```json
{
  "symbols":
  [
    {
      "name":
      "Pokitto::Display::drawBitmap",

      "count":
      47
    }
  ]
}
```

---

# Rapport de compatibilité

Exemple :

```json
{
  "project":"Kong II",

  "compatibility":92,

  "supported":145,

  "wrapped":18,

  "partial":4,

  "manual":2,

  "unsupported":0
}
```

---

# Rapport Markdown

```text
Compatibility Report

Project :
Kong II

Global Score :
92 %

Supported :
145

Wrapped :
18

Partial :
4

Manual :
2
```

---

# Génération README.port.md

Contenu :

- jeu original ;
- auteur original ;
- licence ;
- dépôt source ;
- informations de conversion.

---

# Génération licence

Copie automatique :

```text
LICENSE
```

↓

```text
LICENSE.original
```

---

# Génération crédits

Création automatique :

```text
CREDITS.md
```

---

# Détection du niveau de portage

## RAW

Peu de modifications.

```json
"port_level":"raw"
```

---

## ENHANCED

Ajouts spécifiques AKA.

```json
"port_level":"enhanced"
```

---

## NATIVE

Adaptation importante.

```json
"port_level":"native"
```

---

# Validation

Le convertisseur vérifie :

## Obligatoire

- auteur détecté
- licence détectée
- titre détecté
- dépôt source détecté

---

## Avertissement

API partiellement supportées.

---

## Erreur

API incompatibles.

---

# Ligne de commande

## Analyse seule

```bash
pokitto2aka analyse projet/
```

---

## Conversion seule

```bash
pokitto2aka convert projet/
```

---

## Rapport

```bash
pokitto2aka report projet/
```

---

## Conversion complète

```bash
pokitto2aka build projet/
```

---

# Mode batch

```bash
pokitto2aka batch ./ports
```

Convertit plusieurs projets.

---

# Cache

Répertoire :

```text
.cache/
```

Utilisé pour :

- rapports
- assets convertis
- analyses

---

# Critères de succès V0.1

Le convertisseur doit être capable de :

✅ analyser Kong-II

✅ générer un rapport

✅ générer un manifest

✅ générer un projet AKA

✅ produire un projet compilable

✅ préserver auteurs et licence

✅ préserver le dépôt source

✅ fonctionner sans modifier les sources originales

---

# Vision V1.0

Objectif final :

```text
URL GitHub
      ↓
Analyse
      ↓
Conversion
      ↓
Compilation
      ↓
Projet AKA prêt à lancer
```

avec un minimum d'intervention humaine.
``
