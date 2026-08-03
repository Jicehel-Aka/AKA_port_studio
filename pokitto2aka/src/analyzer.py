#!/usr/bin/env python3
"""
pokitto2aka.analyzer — MVP de l'analyseur de projets Pokitto.

Premiere version fonctionnelle (pas un squelette) : scanne un depot de jeu
Pokitto deja clone localement et produit :
  - analysis.json          (fichiers sources, taille du projet)
  - api_usage.json         (frequence d'appel de chaque API Pokitto)
  - assets.json            (images/sons/musiques/polices detectes)
  - compatibility_report.md (croise api_usage avec compatibility_db.json)

Usage :
    python3 analyzer.py <chemin_du_depot_clone> <chemin_vers_compatibility_db.json> <dossier_sortie>
"""
import json
import os
import re
import sys
from collections import Counter
from pathlib import Path

SOURCE_EXTS = {".cpp", ".c", ".hpp", ".h", ".ino"}
IMAGE_EXTS  = {".png", ".bmp", ".jpg", ".jpeg"}
SOUND_EXTS  = {".raw", ".wav", ".ogg"}
FONT_HINTS  = {"font", "Font"}

# Alias courts -> prefixe complet utilise dans compatibility_db.json
ALIAS = {
    "PD::": "Pokitto::Display::",
    "PC::": "Pokitto::Core::",
    "PS::": "Pokitto::Sound::",
    "Sprites::": "Sprites::",
}

API_CALL_RE = re.compile(r'\b(PD|PC|PS|Sprites)::([A-Za-z_][A-Za-z0-9_]*)(\.[A-Za-z_][A-Za-z0-9_]*)?')
COOKIE_RE   = re.compile(r'\b(cookie|Cookie)\s*\.\s*(begin|loadCookie|saveCookie)\b')


def detect_is_pokitto(files):
    """Verifie que le depot est bien un projet Pokitto avant d'aller plus loin
    -- certains depots au nom proche (ex: Karateka / KaratekaFX) sont en
    realite des jeux Arduboy/Arduboy FX sans aucun rapport avec Pokitto.
    Signal fiable : presence d'un #include "Pokitto.h" (ou variante)."""
    for p in files:
        try:
            text = p.read_text(encoding="utf-8", errors="ignore")
        except Exception:
            continue
        if re.search(r'#include\s*[<"]Pokitto\.h[>"]', text):
            return True
        if "PokittoCookie.h" in text or "Pokitto::Core" in text:
            return True
    return False


def scan_sources(repo_path: Path):
    files = []
    for p in repo_path.rglob("*"):
        if p.is_file() and p.suffix in SOURCE_EXTS:
            files.append(p)
    by_ext = Counter(p.suffix.lstrip(".") for p in files)
    total_lines = 0
    for p in files:
        try:
            total_lines += sum(1 for _ in p.open(encoding="utf-8", errors="ignore"))
        except Exception:
            pass
    return files, {
        "total_files": len(files),
        "by_extension": dict(by_ext),
        "total_lines": total_lines,
    }


def scan_api_usage(files):
    counter = Counter()
    raw_symbols = Counter()
    for p in files:
        try:
            text = p.read_text(encoding="utf-8", errors="ignore")
        except Exception:
            continue
        for m in API_CALL_RE.finditer(text):
            prefix, method, chained = m.group(1), m.group(2), m.group(3)
            if chained:
                method = chained.lstrip(".")   # ex: PC::buttons.pressed -> "pressed"
            full = ALIAS.get(prefix + "::", prefix + "::") + method
            counter[full] += 1
            raw_symbols[f"{prefix}::{method}"] += 1
        for m in COOKIE_RE.finditer(text):
            counter[f"Pokitto::Cookie::{m.group(2)}"] += 1
    return counter, raw_symbols


def scan_assets(repo_path: Path):
    images, sounds, music, fonts = [], [], [], []
    for p in repo_path.rglob("*"):
        if not p.is_file():
            continue
        ext = p.suffix.lower()
        rel = str(p.relative_to(repo_path))
        if ext in IMAGE_EXTS:
            images.append(rel)
        elif ext in SOUND_EXTS:
            if "music" in rel.lower():
                music.append(rel)
            else:
                sounds.append(rel)
        if any(h in p.name for h in FONT_HINTS):
            fonts.append(rel)
    return {
        "images": len(images),
        "sounds": len(sounds),
        "music": len(music),
        "fonts": len(fonts),
        "images_sample": images[:5],
        "music_sample": music[:5],
    }


def load_compat_db(path: Path):
    d = json.loads(path.read_text(encoding="utf-8"))
    return d.get("symbols", [])


def match_compat(symbol_full: str, db_symbols):
    """Cherche si un symbole detecte correspond a une entree de la DB.
    La DB regroupe parfois plusieurs methodes dans un seul champ 'symbol'
    (ex: 'Pokitto::Display::setCursor/print/println') -- on decoupe sur '/'."""
    method = symbol_full.rsplit("::", 1)[-1]
    for entry in db_symbols:
        parts = entry["symbol"].replace(" ", "").split("/")
        for part in parts:
            if part.endswith(method) or method in part:
                return entry
    return None


def build_compatibility_report(game_name, api_counter, db_symbols):
    lines = [f"# Rapport de compatibilite -- {game_name}", ""]
    status_counts = Counter()
    rows = []
    for symbol, count in api_counter.most_common():
        entry = match_compat(symbol, db_symbols)
        status = entry["status"] if entry else "UNKNOWN"
        status_counts[status] += 1
        rows.append((symbol, count, status, entry.get("notes", "") if entry else ""))

    lines.append("## Resume")
    lines.append("")
    for status in ("SUPPORTED", "WRAPPED", "PARTIAL", "MANUAL", "UNSUPPORTED", "UNKNOWN"):
        if status_counts.get(status):
            lines.append(f"- **{status}** : {status_counts[status]} symbole(s)")
    lines.append("")
    lines.append("## Detail par symbole")
    lines.append("")
    lines.append("| Symbole | Appels | Etat | Notes |")
    lines.append("|---|---|---|---|")
    for symbol, count, status, notes in rows:
        note_short = (notes[:80] + "...") if len(notes) > 80 else notes
        lines.append(f"| `{symbol}` | {count} | {status} | {note_short} |")
    lines.append("")
    unknown = [r for r in rows if r[2] == "UNKNOWN"]
    if unknown:
        lines.append("## A investiguer en priorite (symboles inconnus de la DB)")
        lines.append("")
        for symbol, count, _, _ in unknown:
            lines.append(f"- `{symbol}` ({count} appels)")
    return "\n".join(lines), status_counts


def analyze(repo_path: str, compat_db_path: str, out_dir: str, game_name: str):
    repo_path = Path(repo_path)
    out_dir = Path(out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)

    files, analysis = scan_sources(repo_path)
    is_pokitto = detect_is_pokitto(files)
    analysis["is_pokitto_project"] = is_pokitto

    if not is_pokitto:
        (out_dir / "analysis.json").write_text(json.dumps(analysis, indent=2, ensure_ascii=False))
        warning = (f"# Rapport de compatibilite -- {game_name}\n\n"
                   "**ATTENTION : ce depot ne semble PAS etre un projet Pokitto** "
                   "(aucun #include \"Pokitto.h\" / Pokitto::Core detecte). "
                   "C'est probablement une version Arduboy / Arduboy FX ou autre "
                   "plateforme. Analyse arretee ici -- verifier le bon depot avant "
                   "de poursuivre.")
        (out_dir / "compatibility_report.md").write_text(warning, encoding="utf-8")
        return {"game": game_name, "is_pokitto_project": False, "analysis": analysis}

    api_counter, raw_symbols = scan_api_usage(files)
    assets = scan_assets(repo_path)
    db_symbols = load_compat_db(Path(compat_db_path))
    report_md, status_counts = build_compatibility_report(game_name, api_counter, db_symbols)

    (out_dir / "analysis.json").write_text(json.dumps(analysis, indent=2, ensure_ascii=False))
    (out_dir / "api_usage.json").write_text(json.dumps(dict(api_counter.most_common()), indent=2, ensure_ascii=False))
    (out_dir / "assets.json").write_text(json.dumps(assets, indent=2, ensure_ascii=False))
    (out_dir / "compatibility_report.md").write_text(report_md, encoding="utf-8")

    return {
        "game": game_name,
        "is_pokitto_project": True,
        "analysis": analysis,
        "assets": assets,
        "api_symbol_count": len(api_counter),
        "status_counts": dict(status_counts),
    }


if __name__ == "__main__":
    if len(sys.argv) < 4:
        print("usage: analyzer.py <repo_path> <compatibility_db.json> <out_dir> [game_name]")
        sys.exit(1)
    repo_path, db_path, out_dir = sys.argv[1:4]
    game_name = sys.argv[4] if len(sys.argv) > 4 else Path(repo_path).name
    summary = analyze(repo_path, db_path, out_dir, game_name)
    print(json.dumps(summary, indent=2, ensure_ascii=False))
