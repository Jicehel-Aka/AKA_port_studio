# Rapport de compatibilite -- MineSweeper_Pokitto

## Resume

- **SUPPORTED** : 15 symbole(s)
- **WRAPPED** : 2 symbole(s)
- **PARTIAL** : 2 symbole(s)

## Detail par symbole

| Symbole | Appels | Etat | Notes |
|---|---|---|---|
| `Pokitto::Display::drawBitmap` | 29 | WRAPPED | Format reel observe (Kong-II) : entete [W,H] uint8 puis donnees 4bpp. BUG CRITIQ... |
| `Pokitto::Display::setColor` | 22 | SUPPORTED |  |
| `Pokitto::Core::pressed` | 20 | SUPPORTED |  |
| `Pokitto::Display::print` | 18 | SUPPORTED |  |
| `Pokitto::Core::repeat` | 6 | PARTIAL | Auto-repeat approxime a partir de holdStart[]/frameInterval, pas la temporisatio... |
| `Pokitto::Display::setCursor` | 4 | SUPPORTED |  |
| `Pokitto::Display::clear` | 3 | SUPPORTED |  |
| `Pokitto::Display::drawPixel` | 3 | SUPPORTED |  |
| `Pokitto::Display::fillRect` | 2 | SUPPORTED |  |
| `Pokitto::Core::begin` | 1 | SUPPORTED |  |
| `Pokitto::Display::loadRGBPalette` | 1 | SUPPORTED | Absent du brouillon initial de la spec mais indispensable : tous les jeux 'index... |
| `Pokitto::Display::persistence` | 1 | PARTIAL | Champ accepte mais ignore : le renderer AKA redessine tout chaque frame (pas de ... |
| `Pokitto::Display::setInvisibleColor` | 1 | SUPPORTED |  |
| `Pokitto::Core::setFrameRate` | 1 | SUPPORTED |  |
| `Pokitto::Core::isRunning` | 1 | SUPPORTED |  |
| `Pokitto::Core::update` | 1 | SUPPORTED | Cadence via setFrameRate(). Presente la frame precedente (Display::present) avan... |
| `Pokitto::Cookie::begin` | 1 | SUPPORTED |  |
| `Pokitto::Core::pollButtons` | 1 | WRAPPED | No-op : le sondage reel se fait dans Core::update() via input_poll(g_keys), une ... |
| `Pokitto::Display::fillScreen` | 1 | SUPPORTED |  |
