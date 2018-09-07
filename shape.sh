#!/usr/bin

echo -n "Object: "
read shape

echo "Rendering a ${shape}."

if [ "${shape}" = "cube" ]; then

   echo $(./Platonic Solids/cube.py)
   
elif [ "${shape}" = "sphere" ]; then
   echo $(./sphere.py)
   
elif [ "${shape}" = "prism" ]; then
   echo $(./prism.py)

elif [ "${shape}" = "pyramid" ]; then 
   echo $(./pyramid.py)
   
elif [ "${shape}" = "boy's surface" ]; then
   echo $(./Current Models/Surfaces/boys_surface.py)
