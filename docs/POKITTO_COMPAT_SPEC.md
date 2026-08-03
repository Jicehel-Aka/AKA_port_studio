# AKA Port Studio
# Pokitto Compatibility Layer Specification

Version : 0.1

---

# Objectif

La bibliothèque `pokitto_compat` fournit une couche de compatibilité
entre les projets Pokitto et la plateforme Gamebuino AKA.

L'objectif principal est de permettre la réutilisation maximale du code
source Pokitto sans modification importante.

Philosophie :

```text
Code Pokitto
        ↓
pokitto_compat
        ↓
AKA Runtime
        ↓
SDK AKA
```

---

# Principes

## Compatibilité source

Objectif :

```cpp
#include <Pokitto.h>
```

↓

```cpp
#include <pokitto_compat/Pokitto.h>
```

---

## Compatibilité progressive

Les API sont implémentées en fonction :

- des besoins réels ;
- des jeux de référence ;
- des cas observés.

---

# Jeux de référence

V0.1

```text
Kong II
```

V0.2

```text
Trials Of Astarok
Galaxy Fighter
```

---

# Namespace principal

```cpp
namespace Pokitto
{

}
```

---

# Core

Fichier :

```cpp
PokittoCore.h
```

---

## Classe

```cpp
namespace Pokitto
{

class Core
{
public:

    void begin();

    bool update();

    bool isRunning();

    void setFrameRate(uint8_t fps);

    uint32_t getTime();

};

}
```

---

## Etat

```text
SUPPORTED
```

---

## Mapping AKA

```cpp
gb_begin()
gb_update()
```

---

# Display

Fichier :

```cpp
PokittoDisplay.h
```

---

## Classe

```cpp
namespace Pokitto
{

class Display
{
public:

    void clear();

    void fillScreen(uint16_t color);

    void drawPixel(
        int16_t x,
        int16_t y
    );

    void drawLine(
        int16_t x0,
        int16_t y0,
        int16_t x1,
        int16_t y1
    );

    void drawRect(
        int16_t x,
        int16_t y,
        int16_t w,
        int16_t h
    );

    void fillRect(
        int16_t x,
        int16_t y,
        int16_t w,
        int16_t h
    );

    void drawBitmap(
        int16_t x,
        int16_t y,
        const uint8_t* bitmap
    );

    void setCursor(
        int16_t x,
        int16_t y
    );

    void print(
        const char*
    );

    void println(
        const char*
    );

};

}
```

---

## Etat

```text
SUPPORTED
```

---

## Coordonnées

Les coordonnées restent exprimées
dans l'espace Pokitto :

```text
220 x 176
```

Le runtime applique automatiquement :

```text
Offset X = 50
Offset Y = 32
```

---

# Buttons

Fichier :

```cpp
PokittoButtons.h
```

---

## Classe

```cpp
namespace Pokitto
{

class Buttons
{
public:

    bool aBtn();

    bool bBtn();

    bool cBtn();

    bool upBtn();

    bool downBtn();

    bool leftBtn();

    bool rightBtn();
};

}
```

---

## Mapping

```text
Pokitto A → AKA A
Pokitto B → AKA B
Pokitto C → AKA C
```

```text
UP    → UP
DOWN  → DOWN
LEFT  → LEFT
RIGHT → RIGHT
```

---

## Etat

```text
SUPPORTED
```

---

# Sound

Fichier :

```cpp
PokittoSound.h
```

---

## V0.1

```cpp
namespace Pokitto
{

class Sound
{
public:

    void playTone(
        uint16_t frequency,
        uint16_t duration
    );

    void stopTone();
};

}
```

---

## Etat

```text
WRAPPED
```

---

## V0.2

Ajout prévu :

```cpp
playMusic()
stopMusic()
```

---

# Cookie

Fichier :

```cpp
PokittoCookie.h
```

---

## Objectif

Compatibilité sauvegarde.

Implémentation AKA :

```text
Carte SD
```

---

## Classe

```cpp
namespace Pokitto
{

class Cookie
{
public:

    bool begin();

    bool loadCookie();

    bool saveCookie();
};

}
```

---

## Emplacement

```text
/sdcard/<game_id>/save.dat
```

---

## Etat

```text
WRAPPED
```

---

# File

Fichier :

```cpp
PokittoFile.h
```

---

## Classe

```cpp
namespace Pokitto
{

class File
{
public:

    bool open();

    void close();

    int read();

    int write();

    bool exists();
};

}
```

---

## Etat

```text
PARTIAL
```

---

# Sprites

Fichier :

```cpp
PokittoSprites.h
```

---

## Classe

```cpp
class Sprites
{
public:

    static void drawOverwrite();

    static void drawSelfMasked();

    static void drawPlusMask();
};
```

---

## Priorité

Très élevée.

La majorité des jeux utilisent
ces fonctions.

---

## Etat V0.1

```text
PARTIAL
```

---

# API AKA supplémentaires

Ces fonctions n'existent pas
dans Pokitto.

Elles sont optionnelles.

---

## Pause

```text
AKA D
```

Exemple :

```text
Kong II
```

↓

```text
D = Pause
```

---

## Boutons réservés

Utilisation interdite
par les jeux.

```text
MENU
RUN
```

Réservés à :

```text
aka_runtime
```

---

# Coordonnées écran

Toutes les API Pokitto continuent
à croire que l'écran mesure :

```text
220 x 176
```

Le développeur n'a pas à gérer :

```text
320 x 240
```

---

# Viewport

Règle officielle.

```text
Largeur  : 220
Hauteur  : 176

Position X : 50
Position Y : 32
```

---

# Mise à l'échelle

Aucune.

Décision officielle :

```text
Pas d'upscale

Pas de fullscreen

Pas de stretching
```

Le pixel-art original est conservé.

---

# Extensions AKA

Les marges peuvent être utilisées
par le runtime ou les portages
enhanced.

Exemples :

```text
Informations

Contrôles

Etat système

Notifications
```

---

# Dépendances

La couche de compatibilité ne doit
jamais accéder directement :

- au menu système ;
- au loader ;
- aux captures d'écran.

Ces fonctionnalités appartiennent
uniquement à :

```text
aka_runtime
```

---

# Critère de validation V0.1

La bibliothèque est considérée
fonctionnelle lorsque :

✅ Kong II compile

✅ Kong II démarre

✅ Kong II est jouable

✅ Sauvegardes SD fonctionnelles

✅ Menu système fonctionnel

✅ Capture écran fonctionnelle

✅ Retour loader fonctionnel

✅ Crédits et licence affichables

---

# Addendum V0.1 — écarts constatés sur Kong-II (jeu de référence)

Le portage effectif de Kong-II a révélé plusieurs écarts entre ce brouillon
de spec (rédigé avant tout portage réel) et l'API réellement utilisée par un
jeu Pokitto de référence. Ce document reste la cible V0.1, mais les points
suivants doivent être lus en priorité par quiconque implémente
`pokitto_compat` :

## Buttons — API réelle différente du brouillon

Le brouillon documentait `aBtn()`, `bBtn()`, etc. Kong-II (et vraisemblablement
la plupart des jeux Pokitto réels) utilise en fait :

```cpp
PC::buttons.pressed(BTN_LEFT)
PC::buttons.repeat(BTN_LEFT, 1)
```

Une classe `Buttons` avec des méthodes génériques `pressed(btn)` /
`repeat(btn, frames)` / `released(btn)`, plus des constantes `BTN_*`. Les deux
API (`aBtn()` et `pressed()`) doivent être fournies ; `pressed()`/`repeat()`
est la plus utilisée en pratique.

`pollButtons()` est aussi appelée explicitement par certains jeux
(`Game::loop()` de Kong-II) — à fournir en no-op si le sondage réel se fait
ailleurs (ex. dans `Core::update()`).

---

## Sound — bien plus riche que prévu

Le brouillon V0.1 ne prévoyait que `playTone()`/`stopTone()`. Kong-II
nécessite :

```cpp
PS::playSFX(const uint8_t* data, uint32_t length);       // PCM 8-bit embarque
PS::playMusicStream(const char* path, uint8_t loop);      // flux depuis la SD
PS::sfxDataPtr / PS::sfxEndPtr;                            // etat "en cours" (comparaison de pointeurs)
```

Sur l'AKA, `gb_audio_track_wav` (composant `gamebuino`) fournit tout ce qu'il
faut :
- `play_raw(const int16_t*, size_t)` pour des échantillons PCM en mémoire
  (idéal pour `playSFX`, après conversion 8-bit non signé → 16-bit signé) ;
- `play_wav(const char*)` pour un fichier WAV (RIFF) sur la SD (pour
  `playMusicStream`, après avoir enveloppé les `.raw` d'origine dans un
  en-tête WAV valide — travail de conversion d'assets à prévoir dans
  `pokitto2aka`).

`playTone()`/`stopTone()` (le brouillon initial) ne sont en pratique jamais
appelées par un jeu réel constaté à ce jour.

---

## Cookie — signature réelle à 3 arguments

Le brouillon documentait `bool begin();`. La réalité :

```cpp
cookie.begin("KONGII", sizeof(cookie), (char*)&cookie);
```

`bool begin(const char* name, int size, char* data);` — le nom sert
d'identifiant, `size`/`data` décrivent le blob à charger/sauvegarder tel
quel (correspond à `/sdcard/<game_id>/save.dat`).

---

## Display::drawBitmap — format réel + piège de performance

Format constaté (assets Kong-II, ex. `Kong_FacingRight_F1.h`) :

```cpp
const uint8_t Nom[] = { W, H, <données 4bpp, 2 pixels/octet, ligne par ligne> };
```

**Piège important** : ne JAMAIS implémenter `drawBitmap` avec un `fillRect`
appelé pixel par pixel — un sprite Kong-II courant fait des centaines de
pixels, dessinés plusieurs fois par frame ; c'est bien trop lent pour un jeu
à défilement. Décoder dans un buffer temporaire (PSRAM) puis faire **un
seul** appel `drawImage()`/blit rapide.

Deux jeux référence testés utilisent aussi `drawBitmap(x, y, bitmap, flipX,
flipY)` (2 booléens de retournement) — prévoir la surcharge dès le départ.

---

## Macros/fonctions Arduino-AVR indispensables

Aucune des specs V0.1 initiales ne mentionnait ce point, pourtant il bloque
la compilation de **tous** les fichiers d'assets si absent :

```cpp
#define PROGMEM                                   // vide sur ESP32 (tout le const est deja en flash)
#define pgm_read_byte(addr) (*(const uint8_t*)(addr))
inline long random(long max);
inline long random(long min, long max);
```

`PROGMEM` non défini casse le *parsing* (pas juste la sémantique) des
déclarations `const uint8_t PROGMEM Nom[] = {...}`, ce qui produit une
cascade d'erreurs « n'est pas membre de » sans rapport apparent avec la
vraie cause. À fournir dès la V0.1, avant même le premier jeu de test.

---

## palettePico — absente des sources de jeu

`PD::loadRGBPalette(palettePico)` est appelé par Kong-II sans que
`palettePico` soit défini nulle part dans son dépôt : c'est une constante du
vrai SDK Pokitto (PokittoLib), pas du jeu. `pokitto_compat` (ou le projet
généré) doit la fournir — palette PICO-8 standard (16 couleurs).

---

## Addendum V0.1.1 — deux pièges critiques trouvés après premiers tests sur matériel réel

Ces deux bugs ne sont apparus qu'une fois Kong-II compilé et lancé sur la
console (invisibles à la simple lecture du code) — à vérifier en priorité
sur tout futur portage.

### drawBitmap — alignement des lignes sur l'octet (piège majeur)

Le format 4bpp de Kong-II n'est **pas** un flux continu de nibbles sur toute
l'image : **chaque ligne est alignée sur un octet entier**
(`rowBytes = (W+1)/2`, pas `W*H/2` réparti en continu). Pour une image de
largeur **impaire**, traiter les données comme un flux continu décale
progressivement chaque ligne d'un demi-octet de plus que la précédente —
l'image entière apparaît cisaillée en diagonale.

Confirmé sur `Ppot_Full.h` (131×68, largeur impaire) : 4488 octets de données
réelles = 66 octets/ligne (arrondi) × 68 lignes, alors qu'un flux continu en
donnerait 4454.

Symptôme observé : le logo/texte du splash screen "Press Play On Tape"
rendu de travers, ainsi que des artefacts sur les bords en mode "vue large"
(même cause probable : autres sprites à largeur impaire).

```cpp
int rowBytes = (w + 1) / 2;               // JAMAIS w*h/2 en continu
for (int row = 0; row < h; ++row) {
    const uint8_t* rowPx = px + row * rowBytes;   // repart d'un octet neuf a chaque ligne
    for (int col = 0; col < w; ++col) {
        uint8_t b = rowPx[col >> 1];
        uint8_t idx = (col & 1) ? (b & 0x0F) : (b >> 4);
        // ...
    }
}
```

### Audio — l'amorçage du lecteur est une étape à part entière

Déclarer des `gb_audio_track_wav` et appeler `playSFX()`/`playMusicStream()`
ne suffit **pas** : sur l'AKA, aucun son ne sort tant que (1) les pistes ne
sont pas enregistrées auprès d'un `gb_audio_player` via `add_track()`, et
(2) une tâche dédiée n'appelle pas `player.pool()` en boucle (~2ms) pour
alimenter le FIFO I2S. Sans cette étape, le jeu tourne normalement mais reste
**totalement silencieux**, sans aucune erreur de compilation ni de log.

À fournir dès la V0.1 (`Pokitto::Sound::begin()`, appelé automatiquement
depuis `Pokitto::Core::begin()`) — pas quelque chose à découvrir jeu par
jeu.

---

# Addendum V0.2.1 — framebuffer non initialise (trouve sur Galaxy Fighter)

`heap_caps_malloc()` (PSRAM, ESP-IDF) ne met JAMAIS a zero la memoire
allouee. Le vrai Pokitto demarre avec un framebuffer physiquement a zero.
Certains jeux (Galaxy Fighter) ne font JAMAIS `PD::clear()` eux-memes au
demarrage -- ils comptent sur ce zero initial, exactement comme sur le
materiel d'origine.

**Consequence si on l'oublie** : le tout premier ecran affiche du bruit
colore aleatoire (les residus de la PSRAM, decodes via la palette) au lieu
d'un fond noir propre -- visible typiquement sur l'ecran de demarrage/logo.

**A appliquer systematiquement** : tout buffer PSRAM qu'un jeu peut lire
avant de l'avoir lui-meme rempli (screenbuffer, mais potentiellement
d'autres a l'avenir) doit etre explicitement mis a zero (`memset`) juste
apres l'allocation, jamais suppose "propre par defaut".
