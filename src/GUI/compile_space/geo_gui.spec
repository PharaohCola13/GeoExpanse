# -*- mode: python -*-

block_cipher = None


a = Analysis(['../geo_gui.py', '../../Current Models/*.py', '../../Current Models/Archimedean/*.py', '../../Current Models/Hyperbolic/*.py', '../../Current Models/Misc./*.py', '../../Current Models/Surfaces/*.py', '../../Current Models/Platonic Solids/*.py', '../../Current Models/Topological/*.py', '../../Current Models/Two Space/*.py'],
             pathex=['/home/pharaohcola13/PycharmProjects/Research/GeoMetrics/GUI/compile'],
             binaries=[],
             datas=None,
             hiddenimports=['PIL._tkinter_finder', 'matplotlib'],
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
          name='GeoExpanse',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          runtime_tmpdir=None,
          console=False, icon='icon.ico')
