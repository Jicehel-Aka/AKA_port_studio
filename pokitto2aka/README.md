# pokitto2aka

Convertisseur automatique Pokitto -> AKA (voir docs/CONVERTER_SPEC.md).

## Etat V0.3 : premier MVP fonctionnel de l'analyseur

`src/analyzer.py` est un premier prototype REEL (pas un squelette) qui,
pour un depot de jeu Pokitto deja clone localement, produit :

- `analysis.json` — fichiers sources, lignes de code, detection "est-ce
  vraiment un projet Pokitto ?"
- `api_usage.json` — frequence d'appel de chaque API Pokitto detectee
- `assets.json` — images/sons/musiques/polices
- `compatibility_report.md` — croise l'usage reel avec `compatibility_db.json`

Usage :

```
python3 src/analyzer.py <depot_clone> <compatibility_db.json> <dossier_sortie> [nom_du_jeu]
```

Valide sur 6 depots (voir `docs/game_analysis/`) : 4 vrais jeux Pokitto
(FireWorks, MineSweeper, ButtonsTrail, LeWord) + 2 faux-positifs detectes
et correctement rejetes (Karateka/KaratekaFX, en realite Arduboy/Arduboy FX).

## Limites connues (V0.3)

- Le detecteur d'API ne suit qu'un seul niveau de chainage (`PC::buttons.pressed`
  fonctionne, une chaine plus longue non testee).
- La correspondance avec `compatibility_db.json` est une recherche de
  sous-chaine simple, pas une analyse syntaxique complete.
- Pas encore de `cli.py`/`repository.py` (clonage automatique depuis une URL
  GitHub) -- le depot doit etre deja clone/extrait localement.

## Prochaine etape (Sprint 1, cf. docs/ANALYZER_SPEC.md a rediger)

`repository.py` (clonage automatique depuis une URL) + `cli.py`
(`pokitto2aka analyze <url>`), pour eliminer l'etape manuelle de
telechargement/extraction.
