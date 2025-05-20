# hooks/hook-yt_dlp.py
from PyInstaller.utils.hooks import collect_submodules

# collect *all* yt_dlp submodules (incl. compat & utils._deprecated)
hiddenimports = collect_submodules('yt_dlp')
