#!/usr/bin/env bash

#cp ./geo_gui.spec ./compile_space/
#cp ./icon.ico ./compile_space/
#cp ./geo_gui.py ./compile_space/
cp ../../Current\ Models/Archimedean/*.py ./compile_space/
cp ../../Current\ Models/Hyperbolic/*.py ./compile_space/
cp ../../Current\ Models/Misc./*.py ./compile_space/
cp ../../Current\ Models/Platonic\ Solids/*.py ./compile_space/
cp ../../Current\ Models/Surfaces/*.py ./compile_space/
cp ../../Current\ Models/Topological/*.py ./compile_space/
cp ../../Current\ Models/Two\ Space/*.py ./compile_space/
cp ../../In\ Development/*.py ./compile_space/

pyinstaller geo_gui.spec --clean

#mv ./build/ ./compile_space/

#rm ./compile_space/*.py
#rm ./compile_space/geo_gui.spec
#rm ./compile_space/icon.ico
#rm -r ./compile_space/__pycache__
#rm -r ./compile_space/build/