# Rapport de compatibilite -- Karateka_Pokitto

## Resume

- **SUPPORTED** : 14 symbole(s)
- **WRAPPED** : 2 symbole(s)
- **PARTIAL** : 3 symbole(s)
- **MANUAL** : 2 symbole(s)

## Detail par symbole

| Symbole | Appels | Etat | Notes |
|---|---|---|---|
| `Pokitto::Display::drawBitmap` | 163 | WRAPPED | Format reel observe (Kong-II) : entete [W,H] uint8 puis donnees 4bpp. BUG CRITIQ... |
| `Pokitto::Core::pressed` | 84 | SUPPORTED |  |
| `Pokitto::Display::print` | 28 | SUPPORTED |  |
| `Pokitto::Core::repeat` | 24 | PARTIAL | Auto-repeat approxime a partir de holdStart[]/frameInterval, pas la temporisatio... |
| `Pokitto::Display::setCursor` | 22 | SUPPORTED |  |
| `Pokitto::Display::drawLine` | 19 | SUPPORTED | Algorithme de Bresenham reimplemente (l'AKA n'a pas de primitive ligne generique... |
| `Pokitto::Display::setColor` | 17 | SUPPORTED |  |
| `Pokitto::Display::directBitmap` | 14 | MANUAL | Trouve par analyse automatique (Karateka_Pokitto, 14 appels). Non implemente -- ... |
| `Pokitto::Core::frameCount` | 10 | SUPPORTED |  |
| `Pokitto::Core::setFrameRate` | 4 | SUPPORTED |  |
| `Pokitto::Core::update` | 2 | SUPPORTED | Cadence via setFrameRate(). Presente la frame precedente (Display::present) avan... |
| `Pokitto::Display::clearLCD` | 2 | MANUAL | Trouve par analyse automatique (Karateka_Pokitto, 2 appels). Variante de clear()... |
| `Pokitto::Core::getTime` | 2 | SUPPORTED | Deja implemente depuis la V0.1 (retourne le temps ecoule en ms) mais jamais docu... |
| `Pokitto::Core::begin` | 1 | SUPPORTED |  |
| `Pokitto::Display::loadRGBPalette` | 1 | SUPPORTED | Absent du brouillon initial de la spec mais indispensable : tous les jeux 'index... |
| `Pokitto::Display::persistence` | 1 | PARTIAL | Champ accepte mais ignore : le renderer AKA redessine tout chaque frame (pas de ... |
| `Pokitto::Display::setInvisibleColor` | 1 | SUPPORTED |  |
| `Pokitto::Display::setFont` | 1 | PARTIAL | fontC64 (comme palettePico) est fournie par le vrai SDK Pokitto, ABSENTE des sou... |
| `Pokitto::Core::isRunning` | 1 | SUPPORTED |  |
| `Pokitto::Display::clear` | 1 | SUPPORTED |  |
| `Pokitto::Core::pollButtons` | 1 | WRAPPED | No-op : le sondage reel se fait dans Core::update() via input_poll(g_keys), une ... |
