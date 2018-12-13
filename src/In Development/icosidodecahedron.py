# A Icosidodecahedron

import mpl_toolkits.mplot3d.axes3d as p3
import matplotlib.pyplot as plt
from matplotlib import *
from numpy import *
from mpl_toolkits.mplot3d.art3d import *
from matplotlib.animation import *

name = "Icosidodecahedron"

C0 = (1 + sqrt(5))/4
C1 = (3 + sqrt(5))/4
C2 = (1 + sqrt(5))/2

points = array([

[ 0.0,  0.0,   C2],
[ 0.0,  0.0,  -C2],
[  C2,  0.0,  0.0],
[ -C2,  0.0,  0.0],
[ 0.0,   C2,  0.0],
[ 0.0,  -C2,  0.0],
[ 0.5,   C0,   C1],
[ 0.5,   C0,  -C1],
[ 0.5,  -C0,   C1],
[ 0.5,  -C0,  -C1],
[-0.5,   C0,   C1],
[-0.5,   C0,  -C1],
[-0.5,  -C0,   C1],
[-0.5,  -C0,  -C1],
[  C1,  0.5,   C0],
[  C1,  0.5,  -C0],
[  C1, -0.5,   C0],
[  C1, -0.5,  -C0],
[ -C1,  0.5,   C0],
[ -C1,  0.5,  -C0],
[ -C1, -0.5,   C0],
[ -C1, -0.5,  -C0],
[  C0,   C1,  0.5],
[  C0,   C1, -0.5],
[  C0,  -C1,  0.5],
[  C0,  -C1, -0.5],
[ -C0,   C1,  0.5],
[ -C0,   C1, -0.5],
[ -C0,  -C1,  0.5],
[ -C0,  -C1, -0.5],
])

P = [[1, 0, 0],
	 [0, 1, 0],
	 [0, 0, 1]
	 ]
Z = zeros((30,3))

for i in range(30):
	Z[i, :] = dot(points[i, :], P)


fig = plt.figure(figsize=(8,8))
ax = p3.Axes3D(fig)
ax.set_facecolor("black")

plt.axis("off")


verts = [
[Z[0], Z[ 8], Z[16], Z[14], Z[ 6]],
[Z[0], Z[10], Z[18], Z[20], Z[12]],
[Z[1], Z[ 7], Z[15], Z[17], Z[ 9]],
[Z[1], Z[13], Z[21], Z[19], Z[11]],
[Z[2], Z[15], Z[23], Z[22], Z[14]],
[Z[2], Z[16], Z[24], Z[25], Z[17]],
[Z[3], Z[18], Z[26], Z[27], Z[19]],
[Z[3], Z[21], Z[29], Z[28], Z[20]],
[Z[4], Z[23], Z[ 7], Z[11], Z[27]],
[Z[4], Z[26], Z[10], Z[ 6], Z[22]],
[Z[5], Z[24], Z[ 8], Z[12], Z[28]],
[Z[5], Z[29], Z[13], Z[ 9], Z[25]],
[Z[0], Z[ 6], Z[10]],
[Z[0], Z[12], Z[ 8]],
[Z[1], Z[ 9], Z[13]],
[Z[1], Z[11], Z[ 7]],
[Z[2], Z[14], Z[16]],
[Z[2], Z[17], Z[15]],
[Z[3], Z[19], Z[21]],
[Z[3], Z[20], Z[18]],
[Z[4], Z[22], Z[23]],
[Z[4], Z[27], Z[26]],
[Z[5], Z[25], Z[24]],
[Z[5], Z[28], Z[29]],
[Z[6], Z[14], Z[22]],
[Z[7], Z[23], Z[15]],
[Z[8], Z[24], Z[16]],
[Z[9], Z[17], Z[25]],
[Z[10], Z[26], Z[18]],
[Z[11], Z[19], Z[27]],
[Z[12], Z[20], Z[28]],
[Z[13], Z[29], Z[21]],
]

fc = ["white" if i in range(0, 12) else "crimson" for i in range(len(verts))]

sdode = Poly3DCollection(verts)

sdode.set_edgecolor("gold")
sdode.set_linewidth(1)
sdode.set_alpha(0.5)
sdode.set_facecolor(fc)

ax.add_collection3d(sdode)

plt.show() 























