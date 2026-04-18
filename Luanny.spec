# -*- mode: python ; coding: utf-8 -*-

from pathlib import Path


ROOT_DIR = Path.cwd().resolve()
SRC_DIR = ROOT_DIR / 'src'


a = Analysis(
    [str(SRC_DIR / 'luanny' / 'cli.py')],
    pathex=[str(SRC_DIR)],
    binaries=[],
    datas=[(str(SRC_DIR / 'luanny'), 'luanny')],
    hiddenimports=['playwright.sync_api', 'dotenv', 'rich', 'structlog'],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=['nltk', 'scipy', 'matplotlib', 'PyQt5', 'PyQt6', 'tkinter'],
    noarchive=False,
    optimize=0,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='Luanny',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon=None,
)
coll = COLLECT(
    exe,
    a.binaries,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='Luanny',
)
