# aka_runtime

Socle commun a tous les jeux portes (voir docs/RUNTIME_SPEC.md).

## Etat V0.1 (portage Kong-II)

Implemente :
- `AkaRuntime::begin(gameId)` — monte l'arborescence SD (`/sdcard/AKA/`,
  `/sdcard/<gameId>/`).
- `AkaRuntime::update(keys)` — declenche la capture ecran sur MENU maintenu
  ~500ms (voir ci-dessous). Le menu systeme complet reste a faire.
- `AkaRuntime::takeScreenshot()` — capture BMP 24 bits reelle (portee du
  projet GnW_AKA), enregistree sous `/sdcard/AKA/screenshots/<gameId>_NNNN.BMP`.
  Indispensable : c'est cette fonction qui a permis de diagnostiquer le bug
  de cisaillement diagonal dans `Pokitto::Display::drawBitmap` (voir
  compatibility_db) -- a implementer tres tot dans tout nouveau portage.
- `gamePath()` / `settingsPath()` / `screenshotPath()`.
- `returnToLoader()` (bascule OTA vers la partition loader).
- Sondage boutons/joystick partage (`core/input.h`, deplace ici depuis
  `main/` — voir docs/DECISIONS.md, "Code partage entre composants").

Pas encore implemente (cf. compatibility_db) :
- Menu systeme complet (Reprendre/Volume/Langue/Informations/Credits/Licence).
- Lecture/ecriture reelle de `settings.json` (langue/volumes en memoire
  uniquement pour l'instant).
- Notifications visuelles.

## Emplacement

`components/aka_runtime/` (sous `components/`, pas a la racine — voir
docs/DECISIONS.md pour la raison : decouverte du build ESP-IDF).
