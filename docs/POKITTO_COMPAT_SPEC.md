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
