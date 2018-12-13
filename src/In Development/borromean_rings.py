# Borromean Rings

import mpl_toolkits.mplot3d.axes3d as p3
import matplotlib.pyplot as plt
from matplotlib import *
from numpy import *
from mpl_toolkits.mplot3d.art3d import *
from matplotlib.animation import *

name = "Borromean Rings"
points = array([
[ 0,  3,  5],
[ 0,  3, -5],
[ 0, -3,  5],
[ 0, -3, -5],
[ 1,  2,  4],
[ 1,  2, -4],
[ 1, -2,  4],
[ 1, -2, -4],
[-1,  2,  4],
[-1,  2, -4],
[-1, -2,  4],
[-1, -2, -4],
[ 3,  5,  0],
[ 3, -5,  0],
[-3,  5,  0],
[-3, -5,  0],
[ 2,  4,  1],
[ 2, -4,  1],
[-2,  4,  1],
[-2, -4,  1],
[ 2,  4, -1],
[ 2, -4, -1],
[-2,  4, -1],
[-2, -4, -1],
[ 5,  0,  3],
[-5,  0,  3],
[ 5,  0, -3],
[-5,  0, -3],
[ 4,  1,  2],
[-4,  1,  2],
[ 4,  1, -2],
[-4,  1, -2],
[ 4, -1,  2],
[-4, -1,  2],
[ 4, -1, -2],
[-4, -1, -2],

])

P = [[1,0,0],
	 [0,1,0],
	 [0,0,1]
	 ]
Z = zeros((36,3))

for i in range(36):
	Z[i,:] = dot(points[i,:],P)


fig = plt.figure(figsize=(8,8))
ax = p3.Axes3D(fig)
ax.set_facecolor("black")

plt.axis("off")


verts = [
[Z[ 0], Z[ 2], Z[ 6], Z[ 4]],
[Z[ 0], Z[ 4], Z[ 5], Z[ 1]],
[Z[ 0], Z[ 1], Z[ 9], Z[ 8]],
[Z[ 0], Z[ 8], Z[10], Z[ 2]],
[Z[ 3], Z[ 2], Z[10], Z[11]],
[Z[ 3], Z[11], Z[ 9], Z[ 1]],
[Z[ 3], Z[ 1], Z[ 5], Z[ 7]],
[Z[ 3], Z[ 7], Z[ 6], Z[ 2]],
[Z[ 4], Z[ 6], Z[10], Z[ 8]],
[Z[ 4], Z[ 8], Z[ 9], Z[ 5]],
[Z[ 7], Z[ 5], Z[ 9], Z[11]],
[Z[ 7], Z[11], Z[10], Z[ 6]],
[Z[12], Z[14], Z[18], Z[16]],
[Z[12], Z[16], Z[17], Z[13]],
[Z[12], Z[13], Z[21], Z[20]],
[Z[12], Z[20], Z[22], Z[14]],
[Z[15], Z[14], Z[22], Z[23]],
[Z[15], Z[23], Z[21], Z[13]],
[Z[15], Z[13], Z[17], Z[19]],
[Z[15], Z[19], Z[18], Z[14]],
[Z[16], Z[18], Z[22], Z[20]],
[Z[16], Z[20], Z[21], Z[17]],
[Z[19], Z[17], Z[21], Z[23]],
[Z[19], Z[23], Z[22], Z[18]],
[Z[24], Z[26], Z[30], Z[28]],
[Z[24], Z[28], Z[29], Z[25]],
[Z[24], Z[25], Z[33], Z[32]],
[Z[24], Z[32], Z[34], Z[26]],
[Z[27], Z[26], Z[34], Z[35]],
[Z[27], Z[35], Z[33], Z[25]],
[Z[27], Z[25], Z[29], Z[31]],
[Z[27], Z[31], Z[30], Z[26]],
[Z[28], Z[30], Z[34], Z[32]],
[Z[28], Z[32], Z[33], Z[29]],
[Z[31], Z[29], Z[33], Z[35]],
[Z[31], Z[35], Z[34], Z[30]],
]

fc = []

for i in range(len(verts)):
	if i in range(0, 12):
		fc.append("white")
	elif i in range(12, 24):
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























