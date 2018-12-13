# A Snub Dodecahedron

import mpl_toolkits.mplot3d.axes3d as p3
import matplotlib.pyplot as plt
from matplotlib import *
from numpy import *
from mpl_toolkits.mplot3d.art3d import *
from matplotlib.animation import *

name = "Truncated Octahedron"

C0 = sqrt(2)/2
C1 = sqrt(2)

points = array([

[ C0, 0.0,  C1],
[ C0, 0.0, -C1],
[-C0, 0.0,  C1],
[-C0, 0.0, -C1],
[ C1,  C0, 0.0],
[ C1, -C0, 0.0],
[-C1,  C0, 0.0],
[-C1, -C0, 0.0],
[0.0,  C1,  C0],
[0.0,  C1, -C0],
[0.0, -C1,  C0],
[0.0, -C1, -C0],
[0.0,  C0,  C1],
[0.0,  C0, -C1],
[0.0, -C0,  C1],
[0.0, -C0, -C1],
[ C1, 0.0,  C0],
[ C1, 0.0, -C0],
[-C1, 0.0,  C0],
[-C1, 0.0, -C0],
[ C0,  C1, 0.0],
[ C0, -C1, 0.0],
[-C0,  C1, 0.0],
[-C0, -C1, 0.0],
])

P = [[1, 0, 0],
	 [0, 1, 0],
	 [0, 0, 1]
	 ]
Z = zeros((24,3))

for i in range(24):
	Z[i, :] = dot(points[i, :], P)


fig = plt.figure(figsize=(8,8))
ax = p3.Axes3D(fig)
ax.set_facecolor("black")

plt.axis("off")


verts = [
[Z[0], Z[14], Z[10], Z[21], Z[5], Z[16]],
[Z[1], Z[13], Z[9], Z[20], Z[4], Z[17]],
[Z[2], Z[12], Z[8], Z[22], Z[6], Z[18]],
[Z[3], Z[15], Z[11], Z[23], Z[7], Z[19]],
[Z[4], Z[20], Z[8], Z[12], Z[0], Z[16]],
[Z[5], Z[21], Z[11], Z[15], Z[1], Z[17]],
[Z[7], Z[23], Z[10], Z[14], Z[2], Z[18]],
[Z[6], Z[22], Z[9], Z[13], Z[3], Z[19]],
[Z[0], Z[12], Z[2], Z[14]],
[Z[1], Z[15], Z[3], Z[13]],
[Z[4], Z[16], Z[5], Z[17]],
[Z[6], Z[19], Z[7], Z[18]],
[Z[8], Z[20], Z[9], Z[22]],
[Z[10], Z[23], Z[11], Z[21]],
]

fc = ["white" if i in range(0, 8) else "crimson" for i in range(len(verts))]

sdode = Poly3DCollection(verts)

sdode.set_edgecolor("gold")
sdode.set_linewidth(1)
sdode.set_alpha(0.5)
sdode.set_facecolor(fc)

ax.add_collection3d(sdode)

plt.show() 























