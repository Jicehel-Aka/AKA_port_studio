# Compatibility Matrix

Etat reel constate lors du portage de Kong-II (V0.1). Voir
`compatibility_db/compatibility_db.json` pour le detail symbole par symbole.

| API | Etat |
|-------|-------|
| Pokitto::Core | Supported |
| Pokitto::Display | Wrapped |
| Pokitto::Buttons | Supported |
| Pokitto::Sound | Partial |
| Pokitto::Cookie | Wrapped |
| Sprites | Manual (non requis par Kong-II) |
| PROGMEM / pgm_read_byte (AVR compat) | Wrapped |
| random() / abs() (Arduino compat) | Wrapped |

## Légende

Supported — fonctionne tel quel, aucune particularite.
Wrapped — fonctionne via pokitto_compat, avec un ecart de signature/comportement documente.
Partial — fonctionne partiellement ; limitation connue non testee ou non implementee.
Manual — necessite une intervention humaine, pas encore couvert par pokitto_compat.
Unsupported — aucune solution connue.
