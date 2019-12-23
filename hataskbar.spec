# -*- mode: python ; coding: utf-8 -*-

import os

block_cipher = None


a = Analysis(['src/main.py'],
             pathex=[os.path.abspath(SPECPATH)],
             binaries=[],
             datas=[('src/assets/tray.ico','assets')],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='hataskbar',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=False,
          icon='src/assets/tray.ico' )
