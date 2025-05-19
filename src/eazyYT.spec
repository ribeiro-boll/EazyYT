import sys
from PyInstaller.utils.hooks import collect_submodules

# Inclua o diretório do projeto
pathex = [r'.']

# Análise do script
a = Analysis(
    ['eazyYT.py'],
    pathex=pathex,
    binaries=[],
    datas=[],
    hiddenimports=[],
    hookspath=[],
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=None,
    noarchive=False,
)

# Compacta o código puro
pyz = PYZ(
    a.pure,
    a.zipped_data,
    cipher=None
)

# Cria o executável (onefile sem coleta separada)
exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='eazyYT',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=True
)

# Coleta os binários, zipfiles e dados
coll = COLLECT(
    exe,
    a.binaries,
    a.zipfiles,
    a.datas,
    strip=False,
    upx=True,
    name='eazyYT'
)
