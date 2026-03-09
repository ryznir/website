# Gallery generator

This repository includes a small generator script that scans the `photos/` folder
and emits `gallery_data.json` which `gallery.html` will load to render albums
and images dynamically.

How to use (Windows PowerShell):

1. Make sure you have Python installed and `python` is on your PATH.
2. From the repository root (where `gallery.html` lives) run:

```powershell
python .\generate_gallery.py
```

3. This will create `gallery_data.json` with entries for each subfolder in
   `photos/`. Open `gallery.html` in a browser (or serve the folder with a
   simple static server) to view the galleries.

Notes:
- The script finds files under `photos/<album>/` with common image extensions
  (.jpg, .png, .webp, etc.) and writes relative paths that work from the
  `gallery.html` page.
- If you add/remove photos, re-run the script to refresh `gallery_data.json`.
