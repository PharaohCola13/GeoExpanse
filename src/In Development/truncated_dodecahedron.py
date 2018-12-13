# A Truncated Icosahedron

import mpl_toolkits.mplot3d.axes3d as p3
import matplotlib.pyplot as plt
from matplotlib import *
from numpy import *
from mpl_toolkits.mplot3d.art3d import *
from matplotlib.animation import *

name = "Truncated Icosahedron"

C0 = (3 + sqrt(5)) / 4
C1 = (1 + sqrt(5)) / 2
C2 = (2 + sqrt(5)) / 2
C3 = (3 + sqrt(5)) / 2
C4 = (5 + 3 * sqrt(5)) / 4

points = array([
[ 0.0,  0.5,   C4],
[ 0.0,  0.5,  -C4],
[ 0.0, -0.5,   C4],
[ 0.0, -0.5,  -C4],
[  C4,  0.0,  0.5],
[  C4,  0.0, -0.5],
[ -C4,  0.0,  0.5],
[ -C4,  0.0, -0.5],
[ 0.5,   C4,  0.0],
[ 0.5,  -C4,  0.0],
[-0.5,   C4,  0.0],
[-0.5,  -C4,  0.0],
[ 0.5,   C0,   C3],
[ 0.5,   C0,  -C3],
[ 0.5,  -C0,   C3],
[ 0.5,  -C0,  -C3],
[-0.5,   C0,   C3],
[-0.5,   C0,  -C3],
[-0.5,  -C0,   C3],
[-0.5,  -C0,  -C3],
[  C3,  0.5,   C0],
[  C3,  0.5,  -C0],
[  C3, -0.5,   C0],
[  C3, -0.5,  -C0],
[ -C3,  0.5,   C0],
[ -C3,  0.5,  -C0],
[ -C3, -0.5,   C0],
[ -C3, -0.5,  -C0],
[  C0,   C3,  0.5],
[  C0,   C3, -0.5],
[  C0,  -C3,  0.5],
[  C0,  -C3, -0.5],
[ -C0,   C3,  0.5],
[ -C0,   C3, -0.5],
[ -C0,  -C3,  0.5],
[ -C0,  -C3, -0.5],
[  C0,   C1,   C2],
[  C0,   C1,  -C2],
[  C0,  -C1,   C2],
[  C0,  -C1,  -C2],
[ -C0,   C1,   C2],
[ -C0,   C1,  -C2],
[ -C0,  -C1,   C2],
[ -C0,  -C1,  -C2],
[  C2,   C0,   C1],
[  C2,   C0,  -C1],
[  C2,  -C0,   C1],
[  C2,  -C0,  -C1],
[ -C2,   C0,   C1],
[ -C2,   C0,  -C1],
[ -C2,  -C0,   C1],
[ -C2,  -C0,  -C1],
[  C1,   C2,   C0],
[  C1,   C2,  -C0],
[  C1,  -C2,   C0],
[  C1,  -C2,  -C0],
[ -C1,   C2,   C0],
[ -C1,   C2,  -C0],
[ -C1,  -C2,   C0],
[ -C1,  -C2,  -C0],
])

P = [[1,0,0],
	 [0,1,0],
	 [0,0,1]
	 ]
Z = zeros((60,3))

for i in range(60):
	Z[i,:] = dot(points[i,:],P)


fig = plt.figure(figsize=(8,8))
ax = p3.Axes3D(fig)
ax.set_facecolor("black")

plt.axis("off")


verts = [
[Z[ 0], Z[ 2], Z[14], Z[38], Z[46], Z[22], Z[20], Z[44], Z[36], Z[12]],
[Z[ 1], Z[ 3], Z[19], Z[43], Z[51], Z[27], Z[25], Z[49], Z[41], Z[17]],
[Z[ 2], Z[ 0], Z[16], Z[40], Z[48], Z[24], Z[26], Z[50], Z[42], Z[18]],
[Z[ 3], Z[ 1], Z[13], Z[37], Z[45], Z[21], Z[23], Z[47], Z[39], Z[15]],
[Z[ 4], Z[ 5], Z[21], Z[45], Z[53], Z[29], Z[28], Z[52], Z[44], Z[20]],
[Z[ 5], Z[ 4], Z[22], Z[46], Z[54], Z[30], Z[31], Z[55], Z[47], Z[23]],
[Z[ 6], Z[ 7], Z[27], Z[51], Z[59], Z[35], Z[34], Z[58], Z[50], Z[26]],
[Z[ 7], Z[ 6], Z[24], Z[48], Z[56], Z[32], Z[33], Z[57], Z[49], Z[25]],
[Z[ 8], Z[10], Z[32], Z[56], Z[40], Z[16], Z[12], Z[36], Z[52], Z[28]],
[Z[ 9], Z[11], Z[35], Z[59], Z[43], Z[19], Z[15], Z[39], Z[55], Z[31]],
[Z[10], Z[ 8], Z[29], Z[53], Z[37], Z[13], Z[17], Z[41], Z[57], Z[33]],
[Z[11], Z[ 9], Z[30], Z[54], Z[38], Z[14], Z[18], Z[42], Z[58], Z[34]],
[Z[ 0], Z[12], Z[16]],
[Z[ 1], Z[17], Z[13]],
[Z[ 2], Z[18], Z[14]],
[Z[ 3], Z[15], Z[19]],
[Z[ 4], Z[20], Z[22]],
[Z[ 5], Z[23], Z[21]],
[Z[ 6], Z[26], Z[24]],
[Z[ 7], Z[25], Z[27]],
[Z[ 8], Z[28], Z[29]],
[Z[ 9], Z[31], Z[30]],
[Z[10], Z[33], Z[32]],
[Z[11], Z[34], Z[35]],
[Z[36], Z[44], Z[52]],
[Z[37], Z[53], Z[45]],
[Z[38], Z[54], Z[46]],
[Z[39], Z[47], Z[55]],
[Z[40], Z[56], Z[48]],
[Z[41], Z[49], Z[57]],
[Z[42], Z[50], Z[58]],
[Z[43], Z[59], Z[51]],
]

fc = ["white" if i in range(0,12) else "crimson" for i in range(len(verts))]

sdode = Poly3DCollection(verts)

sdode.set_edgecolor("gold")
sdode.set_linewidth(1)
sdode.set_alpha(0.5)
sdode.set_facecolor(fc)

ax.add_collection3d(sdode)

plt.show() 























