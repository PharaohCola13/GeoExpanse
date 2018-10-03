# A Cube, brought to you by PharaohCola13

import mpl_toolkits.mplot3d.axes3d as p3
import matplotlib.pyplot as plt
from matplotlib import *
from numpy import *
from mpl_toolkits.mplot3d.art3d import *
from matplotlib.animation import *

name = "Cube"


points = array([[0,0,0],
				[-0.5, 0.5 + 1/(sqrt(2)), 0.5 +1/(sqrt(2))],
				[-0.5, 0.5 + 1/(sqrt(2)), 1/(2 - (2 *sqrt(2)))],
				[-0.5, 1/(2 - (2 *sqrt(2))), 0.5 + 1/sqrt(2)],
				[-0.5, 1/(2 - (2 *sqrt(2))), 1/(2 - (2 *sqrt(2)))],

				[0.5, 0.5 + 1/sqrt(2), 0.5 + 1/sqrt(2)],
				[0.5, 0.5 + 1/sqrt(2), 1/(2 - (2 *sqrt(2)))],
				[0.5, 1/(2 - (2 *sqrt(2))), 0.5 +1/sqrt(2)],
				[0.5, 1/(2 - (2 *sqrt(2))),1/(2 - (2 *sqrt(2)))],

				[0.5 + 1/sqrt(2), -0.5, 0.5 +1/sqrt(2)],
				[0.5 + 1/sqrt(2), -0.5, 1/(2 - (2 *sqrt(2)))],
				[0.5 + 1/sqrt(2), 0.5, 0.5 + 1/sqrt(2)],
				[0.5 + 1/sqrt(2), 0.5, 1/(2 - (2 * sqrt(2)))],
				[0.5 + 1/sqrt(2), 0.5 + 1/sqrt(2), -0.5],
				[0.5 + 1/sqrt(2), 0.5 + 1/sqrt(2), 0.5],
				[0.5 + 1/sqrt(2), 1/(2 - (2 * sqrt(2))), -0.5],
				[0.5 + 1/sqrt(2), 1/(2 - (2 * sqrt(2))), 0.5],

				[1/(2 - (2 * sqrt(2))), -0.5, 0.5 +1/sqrt(2)],
				[1/(2 - (2 * sqrt(2))), -0.5, 1/(2 - (2 * sqrt(2)))],
				[1/(2 - (2 * sqrt(2))), 0.5, 0.5 + 1/sqrt(2)],
				[1/(2 - (2 * sqrt(2))), 0.5, 1/(2 - (2 * sqrt(2)))],
				[1/(2 - (2 * sqrt(2))), 0.5 + 1/sqrt(2), -0.5],
				[1/(2 - (2 * sqrt(2))), 0.5 + 1/sqrt(2), 0.5],
				[1/(2 - (2 * sqrt(2))), 1/(2 - (2 * sqrt(2))), -0.5],
				[1/(2 - (2 * sqrt(2))), 1/(2 - (2 * sqrt(2))), 0.5],
				])

# Scaling Matricies
P = [[1, 0, 0],
	 [0, 1, 0],
	 [0, 0, 1]]

Z = zeros((25, 3))

for i in range(25):
	Z[i, :] = dot(points[i, :], P)

# Figure Properties
fig = plt.figure(figsize=(8, 8))
ax = p3.Axes3D(fig)
ax.set_facecolor('black')

plt.axis("off")
plt.axis('equal')

ax.set_xlim(-4, 4)
ax.set_ylim(-4, 4)
ax.set_zlim(-4, 4)

# Interval
r = [-1, 1]

X, Y = np.meshgrid(r, r)

# Side Configuration for Cube
# Cube Properties
verts_cube = [[Z[6],Z[12],Z[10],Z[8],Z[4],Z[18],Z[20],Z[2]],
			[Z[1],Z[19],Z[17],Z[3],Z[7],Z[9],Z[11],Z[5]],
			[Z[3],Z[24],Z[23],Z[4],Z[8],Z[15],Z[16],Z[7]],
			[Z[5],Z[14],Z[13],Z[6],Z[2],Z[21],Z[22],Z[1]],
			[Z[9],Z[16],Z[15],Z[10],Z[12],Z[13],Z[14],Z[11]],
			[Z[19],Z[22],Z[21],Z[20],Z[18],Z[23],Z[24],Z[17]],
			[Z[16],Z[9],Z[7]],
			[Z[5],Z[11],Z[14]],
			[Z[3],Z[17],Z[24]],
			[Z[22],Z[19],Z[1]],
			[Z[8],Z[10],Z[15]],
			[Z[13],Z[12],Z[6]],
			[Z[23],Z[18],Z[4]],
			[Z[2],Z[20],Z[21]],
			  ]

cube = Poly3DCollection(verts_cube)

cube.set_edgecolor("white")
cube.set_linewidth(0.5)
cube.set_alpha(0.5)
cube.set_facecolor("blue")

# Plot Surfaces
ax.add_collection3d(cube)

plt.show()
