# -*- mode: python -*-

block_cipher = None


a = Analysis(['geo_windows.py'],
           #pathex=['C:\\tools\\cygwin\\home\\900335362\\GeoExpanse-master\\src\\GUI\\compile_space'],
           pathex=['~/PycharmProjects/Research/GeoExpanse/src/GUI/compile_space'],
             binaries=[],
             datas=[],
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
          name='GeoExpanse_wind',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          runtime_tmpdir=None,
          console=False, icon="icon.ico")
