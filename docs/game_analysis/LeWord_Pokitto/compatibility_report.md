# Rapport de compatibilite -- LeWord_Pokitto

## Resume

- **SUPPORTED** : 17 symbole(s)
- **WRAPPED** : 2 symbole(s)
- **PARTIAL** : 2 symbole(s)
- **UNKNOWN** : 5 symbole(s)

## Detail par symbole

| Symbole | Appels | Etat | Notes |
|---|---|---|---|
| `Pokitto::Display::drawBitmap` | 47 | WRAPPED | Format reel observe (Kong-II) : entete [W,H] uint8 puis donnees 4bpp. BUG CRITIQ... |
| `Pokitto::Display::setColor` | 29 | SUPPORTED |  |
| `Pokitto::Core::pressed` | 24 | SUPPORTED |  |
| `Pokitto::Display::print` | 17 | SUPPORTED |  |
| `Pokitto::Display::fillRect` | 13 | SUPPORTED |  |
| `Pokitto::Core::frameCount` | 9 | SUPPORTED |  |
| `Pokitto::Display::setCursor` | 9 | SUPPORTED |  |
| `Pokitto::Core::repeat` | 7 | PARTIAL | Auto-repeat approxime a partir de holdStart[]/frameInterval, pas la temporisatio... |
| `Pokitto::Core::pollButtons` | 3 | WRAPPED | No-op : le sondage reel se fait dans Core::update() via input_poll(g_keys), une ... |
| `Pokitto::Display::drawRect` | 3 | SUPPORTED |  |
| `Pokitto::Core::released` | 2 | SUPPORTED |  |
| `Pokitto::Display::drawFastHLine` | 2 | UNKNOWN |  |
| `Pokitto::Display::drawFastVLine` | 2 | UNKNOWN |  |
| `Pokitto::Display::drawPixel` | 2 | SUPPORTED |  |
| `Pokitto::Core::begin` | 1 | SUPPORTED |  |
| `Pokitto::Display::loadRGBPalette` | 1 | SUPPORTED | Absent du brouillon initial de la spec mais indispensable : tous les jeux 'index... |
| `Pokitto::Display::persistence` | 1 | PARTIAL | Champ accepte mais ignore : le renderer AKA redessine tout chaque frame (pas de ... |
| `Pokitto::Display::setInvisibleColor` | 1 | SUPPORTED |  |
| `Pokitto::Core::setFrameRate` | 1 | SUPPORTED |  |
| `Pokitto::Display::textWrap` | 1 | UNKNOWN |  |
| `Pokitto::Display::adjustCharStep` | 1 | UNKNOWN |  |
| `Pokitto::Core::isRunning` | 1 | SUPPORTED |  |
| `Pokitto::Core::update` | 1 | SUPPORTED | Cadence via setFrameRate(). Presente la frame precedente (Display::present) avan... |
| `Pokitto::Cookie::begin` | 1 | SUPPORTED |  |
| `Pokitto::Core::held` | 1 | UNKNOWN |  |
| `Pokitto::Display::clear` | 1 | SUPPORTED |  |

## A investiguer en priorite (symboles inconnus de la DB)

- `Pokitto::Display::drawFastHLine` (2 appels)
- `Pokitto::Display::drawFastVLine` (2 appels)
- `Pokitto::Display::textWrap` (1 appels)
- `Pokitto::Display::adjustCharStep` (1 appels)
- `Pokitto::Core::held` (1 appels)