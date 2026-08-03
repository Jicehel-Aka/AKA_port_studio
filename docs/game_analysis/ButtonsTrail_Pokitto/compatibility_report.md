# Rapport de compatibilite -- ButtonsTrail_Pokitto

## Resume

- **SUPPORTED** : 15 symbole(s)
- **WRAPPED** : 2 symbole(s)
- **PARTIAL** : 3 symbole(s)
- **UNKNOWN** : 3 symbole(s)

## Detail par symbole

| Symbole | Appels | Etat | Notes |
|---|---|---|---|
| `Pokitto::Display::drawBitmap` | 97 | WRAPPED | Format reel observe (Kong-II) : entete [W,H] uint8 puis donnees 4bpp. BUG CRITIQ... |
| `Pokitto::Core::pressed` | 27 | SUPPORTED |  |
| `Pokitto::Core::frameCount` | 25 | SUPPORTED |  |
| `Pokitto::Display::setCursor` | 25 | SUPPORTED |  |
| `Pokitto::Display::print` | 25 | SUPPORTED |  |
| `Pokitto::Display::setColor` | 17 | SUPPORTED |  |
| `Pokitto::Display::fillRectangle` | 3 | UNKNOWN |  |
| `Pokitto::Core::repeat` | 3 | PARTIAL | Auto-repeat approxime a partir de holdStart[]/frameInterval, pas la temporisatio... |
| `Pokitto::Display::setFont` | 2 | PARTIAL | fontC64 (comme palettePico) est fournie par le vrai SDK Pokitto, ABSENTE des sou... |
| `Pokitto::Core::begin` | 1 | SUPPORTED |  |
| `Pokitto::Display::loadRGBPalette` | 1 | SUPPORTED | Absent du brouillon initial de la spec mais indispensable : tous les jeux 'index... |
| `Pokitto::Display::persistence` | 1 | PARTIAL | Champ accepte mais ignore : le renderer AKA redessine tout chaque frame (pas de ... |
| `Pokitto::Display::setInvisibleColor` | 1 | SUPPORTED |  |
| `Pokitto::Core::setFrameRate` | 1 | SUPPORTED |  |
| `Pokitto::Display::textWrap` | 1 | UNKNOWN |  |
| `Pokitto::Core::isRunning` | 1 | SUPPORTED |  |
| `Pokitto::Core::update` | 1 | SUPPORTED | Cadence via setFrameRate(). Presente la frame precedente (Display::present) avan... |
| `Pokitto::Cookie::begin` | 1 | SUPPORTED |  |
| `Pokitto::Display::fillScreen` | 1 | SUPPORTED |  |
| `Pokitto::Display::drawPixel` | 1 | SUPPORTED |  |
| `Pokitto::Display::drawRectangle` | 1 | UNKNOWN |  |
| `Pokitto::Display::clear` | 1 | SUPPORTED |  |
| `Pokitto::Core::pollButtons` | 1 | WRAPPED | No-op : le sondage reel se fait dans Core::update() via input_poll(g_keys), une ... |

## A investiguer en priorite (symboles inconnus de la DB)

- `Pokitto::Display::fillRectangle` (3 appels)
- `Pokitto::Display::textWrap` (1 appels)
- `Pokitto::Display::drawRectangle` (1 appels)