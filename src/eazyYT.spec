# -*- mode: python ; coding: utf-8 -*-

import os
import sys
from PyInstaller.utils.hooks import collect_data_files

pathex = [r'.']

# Localização do ffmpeg.exe dentro do repositório
ffmpeg_src = os.path.abspath(os.path.join('ffmpeg', 'ffmpeg.exe'))

a = Analysis(
    ['eazyYT.py'],
    pathex=['.'],
    binaries=[('ffmpeg/ffmpeg.exe', '.')],
    datas=collect_data_files('customtkinter', subdir='assets'),
    hiddenimports=['yt_dlp', 'customtkinter'],
    hookspath=[],
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=None,
    noarchive=False,
)

pyz = PYZ(
    a.pure,
    a.zipped_data,
    cipher=None
)

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

coll = COLLECT(
    exe,
    a.binaries,
    a.zipfiles,
    a.datas,
    strip=False,
    upx=True,
    name='eazyYT'
)
