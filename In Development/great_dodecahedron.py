# A Cube, brought to you by PharaohCola13

import mpl_toolkits.mplot3d.axes3d as p3
import matplotlib.pyplot as plt
from matplotlib import *
from numpy import *
from mpl_toolkits.mplot3d.art3d import *
from matplotlib.animation import *

name = "Cube"


points = array([[0,0,0],
                [0,                         0, -5/(sqrt(50 - (10 * sqrt(5))))],
                [0,                         0, 5/(sqrt(50 - (10 * sqrt(5))))],
                [-sqrt(2/(5 - sqrt(5))),    0, -1/sqrt(10 - (2 * sqrt(5)))],
                [sqrt(2/(5 - sqrt(5))),     0, 1/sqrt(10 - (2 * sqrt(5)))],

                [-(-1 + sqrt(5))/(2 * sqrt(10 - (2 * sqrt(5)))), -0.5 * sqrt((5 + sqrt(5))/(5 - sqrt(5))), -1/sqrt(10 - (2 * sqrt(5)))],
                [-(-1 + sqrt(5))/(2 * sqrt(10 - (2 * sqrt(5)))),  0.5 * sqrt((5 + sqrt(5))/(5 - sqrt(5))), -1/sqrt(10 - (2 * sqrt(5)))],
                [(-1 + sqrt(5))/(2 * sqrt(10 - (2 * sqrt(5)))),  -0.5 * sqrt((5 + sqrt(5))/(5 - sqrt(5))), 1/sqrt(10 - (2 * sqrt(5)))],
                [(-1 + sqrt(5))/(2 * sqrt(10 - (2 * sqrt(5)))),   0.5 * sqrt((5 + sqrt(5))/(5 - sqrt(5))), 1/sqrt(10 - (2 * sqrt(5)))],

                [-(1 + sqrt(5))/(2 * sqrt(10 - (2 * sqrt(5)))),  -0.5, 1/sqrt(10 - (2 * sqrt(5)))],
                [-(1 + sqrt(5))/(2 * sqrt(10 - (2 * sqrt(5)))),   0.5, 1/sqrt(10 - (2 * sqrt(5)))],
                [(1 + sqrt(5))/(2 * sqrt(10 - (2 * sqrt(5)))),   -0.5, -1/sqrt(10 - (2 * sqrt(5)))],
                [(1 + sqrt(5))/(2 * sqrt(10 - (2 * sqrt(5)))),    0.5, -1/sqrt(10 - (2 * sqrt(5)))]
                ])

# Scaling Matricies
P = [[1, 0, 0],
     [0, 1, 0],
     [0, 0, 1]]

Z = zeros((13, 3))

for i in range(13):
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
verts_cube = [[Z[7], Z[9], Z[3], Z[1], Z[11]],
              [Z[1], Z[3], Z[10], Z[8], Z[12]],
              [Z[11], Z[1], Z[6], Z[8], Z[4]],
              [Z[7], Z[5], Z[1], Z[12], Z[4]],
              [Z[1], Z[5], Z[9], Z[10], Z[6]],
              [Z[8], Z[6], Z[3], Z[9], Z[2]],
              [Z[7], Z[2], Z[10], Z[3], Z[5]],
              [Z[4], Z[2], Z[9], Z[5], Z[11]],
              [Z[4], Z[12], Z[6], Z[10], Z[2]],
              [Z[8], Z[2], Z[7], Z[11], Z[12]],
              [Z[5], Z[3], Z[6], Z[12], Z[11]],
              [Z[4], Z[8], Z[10], Z[9], Z[7]]

              ]

cube = Poly3DCollection(verts_cube)

cube.set_edgecolor("white")
cube.set_linewidth(0.5)
cube.set_alpha(0.5)
cube.set_facecolor("blue")

# Plot Surfaces
ax.add_collection3d(cube)

plt.show()
