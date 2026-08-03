#!/usr/bin/env python3
"""
pokitto2aka.generators.launcher_assets — genere les 2 fichiers attendus par
le launcher AKA dans le dossier SD de chaque jeu (/sdcard/<gameId>/) :

  - screen.bmp  (160x120, 24 bits) : vignette affichee dans le launcher
  - meta.json   : {title, description, author, version, date}

Strategie screen.bmp (V0.3, automatisable sans materiel) :
  Les jeux Pokitto ont quasi tous une banniere promotionnelle 200x80 (le
  format standard des fichiers .POP Pokitto), reperable par un nom de
  fichier contenant "banner" (insensible a la casse), typiquement dans
  Assets/, distributable/ ou un dossier "Banner and Icons". On la
  redimensionne SANS DEFORMATION (facteur uniforme) puis on la centre sur
  un fond noir 160x120. Evite d'avoir besoin d'une vraie capture d'ecran
  materielle des la conversion (utilisable des l'etape d'analyse, avant
  meme la compilation).

  Amelioration future possible : remplacer par une vraie capture
  gameplay (takeScreenshot(), 320x240) redimensionnee en 160x120, une
  fois le jeu teste sur materiel reel -- plus fidele mais necessite d'avoir
  deja flashe/joue.

Usage :
    python3 launcher_assets.py <repo_clone> <port_manifest.json> <sortie_dir>
"""
import json
import sys
import datetime
from pathlib import Path
from PIL import Image

BANNER_HINTS = ["popbanner", "banner"]
EXCLUDE_HINTS = ["icon", "screenshot", "screenhot"]
IMAGE_EXTS = {".png", ".jpg", ".jpeg", ".bmp"}


def find_best_banner(repo_path: Path):
    candidates = []
    for p in repo_path.rglob("*"):
        if not p.is_file() or p.suffix.lower() not in IMAGE_EXTS:
            continue
        name = p.name.lower()
        if any(h in name for h in EXCLUDE_HINTS):
            continue
        if any(h in name for h in BANNER_HINTS):
            try:
                im = Image.open(p)
                candidates.append((im.size[0] * im.size[1], p))
            except Exception:
                continue
    if not candidates:
        return None
    candidates.sort(reverse=True)   # prefere la plus grande banniere trouvee
    return candidates[0][1]


def make_screen_bmp(banner_path: Path, out_path: Path, size=(160, 120), bg=(0, 0, 0)):
    src = Image.open(banner_path).convert("RGB")
    canvas = Image.new("RGB", size, bg)
    scale = min(size[0] / src.width, size[1] / src.height)
    new_w, new_h = int(src.width * scale), int(src.height * scale)
    resized = src.resize((new_w, new_h), Image.LANCZOS)
    ox, oy = (size[0] - new_w) // 2, (size[1] - new_h) // 2
    canvas.paste(resized, (ox, oy))
    canvas.save(out_path, "BMP")
    return canvas.size


def make_meta_json(manifest: dict, out_path: Path, repo_path: Path):
    """
    'Automatise' ne veut pas dire deviner a la place de l'utilisateur -- ca
    veut dire le GUIDER (poser les bonnes questions) et VERIFIER que les
    elements importants (licence, auteur d'origine, depot source) sont bien
    presents avant de considerer le portage pret. La description n'a pas de
    source fiable et automatisable dans ce corpus (cf. recherche -- ni
    description GitHub, ni README exploitable) : c'est une VRAIE question a
    poser a l'utilisateur au moment de la reprise, pas un texte a generer
    silencieusement a sa place.
    """
    questions_for_user = []
    checklist = {}

    description = manifest.get("description")
    if not description:
        questions_for_user.append(
            "description : aucune source fiable trouvee (pas de description "
            "GitHub, README non exploitable) -- a demander a l'utilisateur."
        )
        description = None  # laisse explicitement vide plutot que de deviner

    # Verifications des elements importants (pas seulement la description)
    has_license_file = any(repo_path.glob("LICENSE*")) or any(repo_path.glob("license*"))
    checklist["license_file_present"] = bool(has_license_file)
    if not has_license_file:
        questions_for_user.append("licence : aucun fichier LICENSE trouve dans le depot -- a demander/verifier.")

    author = manifest.get("author")
    checklist["author_present"] = bool(author)
    if not author:
        questions_for_user.append("auteur original : non renseigne dans le manifest -- obligatoire (respect de l'auteur).")

    source_repo = manifest.get("source_repository")
    checklist["source_repository_present"] = bool(source_repo)
    if not source_repo:
        questions_for_user.append("depot source : URL d'origine non renseignee -- a demander.")

    meta = {
        "title": manifest.get("title", manifest.get("id", "Unknown")),
        "description": description,
        "author": author or "A_COMPLETER",
        "version": manifest.get("version", "1.0"),
        "date": datetime.date.today().isoformat(),
    }
    out_path.write_text(json.dumps(meta, indent=2, ensure_ascii=False), encoding="utf-8")
    return meta, questions_for_user, checklist


def generate(repo_path: str, manifest_path: str, out_dir: str):
    repo_path = Path(repo_path)
    out_dir = Path(out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)
    manifest = json.loads(Path(manifest_path).read_text(encoding="utf-8"))

    banner = find_best_banner(repo_path)
    result = {"banner_found": str(banner) if banner else None}
    if banner:
        size = make_screen_bmp(banner, out_dir / "screen.bmp")
        result["screen_bmp"] = str(out_dir / "screen.bmp")
        result["screen_size"] = size
    else:
        result["warning"] = "aucune banniere trouvee -- screen.bmp non genere, a fournir manuellement"

    meta, questions_for_user, checklist = make_meta_json(manifest, out_dir / "meta.json", repo_path)
    result["meta"] = meta
    result["checklist"] = checklist
    result["questions_for_user"] = questions_for_user
    return result


if __name__ == "__main__":
    if len(sys.argv) < 4:
        print("usage: launcher_assets.py <repo_clone> <port_manifest.json> <sortie_dir>")
        sys.exit(1)
    r = generate(sys.argv[1], sys.argv[2], sys.argv[3])
    print(json.dumps(r, indent=2, ensure_ascii=False))
