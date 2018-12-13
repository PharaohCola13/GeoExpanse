# A Truncated Cuboctahedron

import mpl_toolkits.mplot3d.axes3d as p3
import matplotlib.pyplot as plt
from matplotlib import *
from numpy import *
from mpl_toolkits.mplot3d.art3d import *
from matplotlib.animation import *

name = "Truncated Cuboctahedron"

C0 = (1 + sqrt(2))/2
C1 = (1 + 2 * sqrt(2)) / 2

points = array([
[  C0,  0.5,   C1],
[  C0,  0.5,  -C1],
[  C0, -0.5,   C1],
[  C0, -0.5,  -C1],
[ -C0,  0.5,   C1],
[ -C0,  0.5,  -C1],
[ -C0, -0.5,   C1],
[ -C0, -0.5,  -C1],
[  C1,   C0,  0.5],
[  C1,   C0, -0.5],
[  C1,  -C0,  0.5],
[  C1,  -C0, -0.5],
[ -C1,   C0,  0.5],
[ -C1,   C0, -0.5],
[ -C1,  -C0,  0.5],
[ -C1,  -C0, -0.5],
[ 0.5,   C1,   C0],
[ 0.5,   C1,  -C0],
[ 0.5,  -C1,   C0],
[ 0.5,  -C1,  -C0],
[-0.5,   C1,   C0],
[-0.5,   C1,  -C0],
[-0.5,  -C1,   C0],
[-0.5,  -C1,  -C0],
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
[-C0,  -C1, -0.5],
])

P = [[1, 0, 0],
	 [0, 1, 0],
	 [0, 0, 1]
	 ]
Z = zeros((48,3))

for i in range(48):
	Z[i, :] = dot(points[i, :], P)


fig = plt.figure(figsize=(8,8))
ax = p3.Axes3D(fig)
ax.set_facecolor("black")

plt.axis("off")


verts = [
[Z[ 0], Z[24], Z[28], Z[ 4], Z[ 6], Z[30], Z[26], Z[ 2]],
[Z[ 1], Z[ 3], Z[27], Z[31], Z[ 7], Z[ 5], Z[29], Z[25]],
[Z[ 8], Z[32], Z[34], Z[10], Z[11], Z[35], Z[33], Z[ 9]],
[Z[12], Z[13], Z[37], Z[39], Z[15], Z[14], Z[38], Z[36]],
[Z[16], Z[40], Z[41], Z[17], Z[21], Z[45], Z[44], Z[20]],
[Z[18], Z[22], Z[46], Z[47], Z[23], Z[19], Z[43], Z[42]],
[Z[ 0], Z[32], Z[ 8], Z[40], Z[16], Z[24]],
[Z[ 1], Z[25], Z[17], Z[41], Z[ 9], Z[33]],
[Z[ 2], Z[26], Z[18], Z[42], Z[10], Z[34]],
[Z[ 3], Z[35], Z[11], Z[43], Z[19], Z[27]],
[Z[ 4], Z[28], Z[20], Z[44], Z[12], Z[36]],
[Z[ 5], Z[37], Z[13], Z[45], Z[21], Z[29]],
[Z[ 6], Z[38], Z[14], Z[46], Z[22], Z[30]],
[Z[ 7], Z[31], Z[23], Z[47], Z[15], Z[39]],
[Z[ 0], Z[ 2], Z[34], Z[32]],
[Z[ 1], Z[33], Z[35], Z[ 3]],
[Z[ 4], Z[36], Z[38], Z[ 6]],
[Z[ 5], Z[ 7], Z[39], Z[37]],
[Z[ 8], Z[ 9], Z[41], Z[40]],
[Z[10], Z[42], Z[43], Z[11]],
[Z[12], Z[44], Z[45], Z[13]],
[Z[14], Z[15], Z[47], Z[46]],
[Z[16], Z[20], Z[28], Z[24]],
[Z[17], Z[25], Z[29], Z[21]],
[Z[18], Z[26], Z[30], Z[22]],
[Z[19], Z[23], Z[31], Z[27]],
]

fc = []

for i in range(len(verts)):
	if i in range(0,6):
		fc.append("white")
	elif i in range(6,14):
		fc.append("crimson")
	else:
		fc.append("orange")

sdode = Poly3DCollection(verts)

sdode.set_edgecolor("gold")
sdode.set_linewidth(1)
sdode.set_alpha(0.5)
sdode.set_facecolor(fc)

ax.add_collection3d(sdode)

plt.show() 























