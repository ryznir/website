"""
generate_gallery.py

Scans the local `photos/` directory for subfolders and image files and writes
`gallery_data.json` mapping album names -> ordered list of relative image paths.

Run:
  python generate_gallery.py

This script is intentionally simple and safe for static sites. It includes
common image extensions and preserves relative paths suitable for linking
from `gallery.html`.
"""
from pathlib import Path
import json

IMG_EXTS = {'.jpg', '.jpeg', '.png', '.gif', '.webp', '.bmp', '.tiff'}

ROOT = Path(__file__).parent
PHOTOS_DIR = ROOT / 'photos'
OUT_FILE = ROOT / 'gallery_data.json'

def make_gallery_data(photos_dir: Path):
    data = {}
    if not photos_dir.exists():
        print(f"Photos directory not found: {photos_dir}")
        return data
    for child in sorted(photos_dir.iterdir()):
        if child.is_dir():
            imgs = []
            for p in sorted(child.rglob('*')):
                if p.suffix.lower() in IMG_EXTS and p.is_file():
                    # produce a path relative to the site root, suitable for <img src="...">
                    rel = p.relative_to(ROOT).as_posix()
                    imgs.append(rel)
            if imgs:
                data[child.name] = imgs
    return data


def main():
    data = make_gallery_data(PHOTOS_DIR)
    if not data:
        print('No galleries found or no images in photos/.')
    else:
        with OUT_FILE.open('w', encoding='utf-8') as f:
            json.dump(data, f, indent=2)
        print(f'Wrote {OUT_FILE} with {len(data)} galleries.')

if __name__ == '__main__':
    main()
