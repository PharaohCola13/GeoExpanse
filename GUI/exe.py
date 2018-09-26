import sys
import os
from cx_Freeze import setup, Executable

includes = []
excludes = []
packages = []

filename = "gui_final.py"
base = None
setup(
    name = 'Geometry',
    version = '0.1',
    description = 'Models geometric surfaces',
    author = 'no',
    author_email = 'spencerriley620@gmail.com',
    options = {'build_exe': {'excludes':excludes,'packages':packages,'includes':includes}},
    executables = [Executable(filename, base = base, icon = "penrose_icon.png")])