# Rapport de compatibilite -- FireWorks_Pokitto

## Resume

- **SUPPORTED** : 14 symbole(s)
- **WRAPPED** : 2 symbole(s)
- **PARTIAL** : 3 symbole(s)
- **UNKNOWN** : 4 symbole(s)

## Detail par symbole

| Symbole | Appels | Etat | Notes |
|---|---|---|---|
| `Pokitto::Display::drawBitmap` | 75 | WRAPPED | Format reel observe (Kong-II) : entete [W,H] uint8 puis donnees 4bpp. BUG CRITIQ... |
| `Pokitto::Core::frameCount` | 46 | SUPPORTED |  |
| `Pokitto::Core::pressed` | 26 | SUPPORTED |  |
| `Pokitto::Display::setColor` | 22 | SUPPORTED |  |
| `Pokitto::Display::drawFastHLine` | 12 | UNKNOWN |  |
| `Pokitto::Core::setFrameRate` | 6 | SUPPORTED |  |
| `Pokitto::Core::repeat` | 2 | PARTIAL | Auto-repeat approxime a partir de holdStart[]/frameInterval, pas la temporisatio... |
| `Pokitto::Core::begin` | 1 | SUPPORTED |  |
| `Pokitto::Display::loadRGBPalette` | 1 | SUPPORTED | Absent du brouillon initial de la spec mais indispensable : tous les jeux 'index... |
| `Pokitto::Display::persistence` | 1 | PARTIAL | Champ accepte mais ignore : le renderer AKA redessine tout chaque frame (pas de ... |
| `Pokitto::Display::setInvisibleColor` | 1 | SUPPORTED |  |
| `Pokitto::Display::setFont` | 1 | PARTIAL | fontC64 (comme palettePico) est fournie par le vrai SDK Pokitto, ABSENTE des sou... |
| `Pokitto::Display::adjustCharStep` | 1 | UNKNOWN |  |
| `Pokitto::Display::textWrap` | 1 | UNKNOWN |  |
| `Pokitto::Core::isRunning` | 1 | SUPPORTED |  |
| `Pokitto::Core::update` | 1 | SUPPORTED | Cadence via setFrameRate(). Presente la frame precedente (Display::present) avan... |
| `Pokitto::Cookie::begin` | 1 | SUPPORTED |  |
| `Pokitto::Display::drawPixel` | 1 | SUPPORTED |  |
| `Pokitto::Display::fillCircle` | 1 | UNKNOWN |  |
| `Pokitto::Display::clear` | 1 | SUPPORTED |  |
| `Pokitto::Core::pollButtons` | 1 | WRAPPED | No-op : le sondage reel se fait dans Core::update() via input_poll(g_keys), une ... |
| `Pokitto::Display::drawLine` | 1 | SUPPORTED | Algorithme de Bresenham reimplemente (l'AKA n'a pas de primitive ligne generique... |
| `Pokitto::Display::fillRect` | 1 | SUPPORTED |  |

## A investiguer en priorite (symboles inconnus de la DB)

- `Pokitto::Display::drawFastHLine` (12 appels)
- `Pokitto::Display::adjustCharStep` (1 appels)
- `Pokitto::Display::textWrap` (1 appels)
- `Pokitto::Display::fillCircle` (1 appels)