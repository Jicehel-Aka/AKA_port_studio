# pokitto_compat

Couche de compatibilite source Pokitto -> AKA (voir docs/POKITTO_COMPAT_SPEC.md).

## Etat V0.1 (valide sur Kong-II)

| Module | Etat |
|---|---|
| Pokitto::Core | Supported |
| Pokitto::Buttons | Supported (API reelle : `pressed()`/`repeat()`, pas seulement `aBtn()`) |
| Pokitto::Display | Wrapped (viewport 220x176 centre, palette indexee, `drawBitmap` 4bpp -- ATTENTION alignement par ligne, cf. plus bas) |
| Pokitto::Sound | Partial (SFX + amorcage du lecteur audio OK ; streaming musique SD pas teste) |
| Pokitto::Cookie | Wrapped (signature reelle a 3 arguments) |
| Sprites | Manual (non requis par Kong-II, pas encore implemente) |

## Deux pieges critiques (trouves seulement au test sur materiel reel)

1. **`drawBitmap`** : chaque ligne du format 4bpp est alignee sur un octet
   entier (`rowBytes = (W+1)/2`), ce n'est PAS un flux continu de nibbles.
   Pour une largeur impaire, un decodage "flux continu" cisaille l'image en
   diagonale (bug reel trouve sur le splash screen). Voir
   `PokittoDisplay.cpp::drawBitmap` pour le decodage correct.
2. **Audio** : declarer des `gb_audio_track_wav` et appeler
   `playSFX()`/`playMusicStream()` NE SUFFIT PAS. Sans `Sound::begin()`
   (enregistrement aupres de `gb_audio_player` + tache de mixage dediee),
   le jeu tourne silencieusement, sans aucune erreur. `Sound::begin()` est
   appele automatiquement par `Core::begin()`.

Compat AVR/Arduino additionnelle (indispensable, non prevue dans le
brouillon initial) : `PROGMEM`, `pgm_read_byte`, `random()`. Voir
`AvrCompat.h` et docs/POKITTO_COMPAT_SPEC.md ("Addendum V0.1" et
"Addendum V0.1.1").

## Detail

Voir `compatibility_db/compatibility_db.json` pour l'etat exact, symbole par
symbole, avec notes techniques.

## Emplacement

`components/pokitto_compat/` (sous `components/` — voir docs/DECISIONS.md).
