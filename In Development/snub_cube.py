# A Cube, brought to you by PharaohCola13

import mpl_toolkits.mplot3d.axes3d as p3
import matplotlib.pyplot as plt
from matplotlib import *
from numpy import *
from mpl_toolkits.mplot3d.art3d import *
from matplotlib.animation import *

name = "Cube"

C0 = sqrt(3 * (4 - cbrt(17 + 3*sqrt(33)) - cbrt(17 - 3*sqrt(33)))) / 6
C1 = sqrt(3 * (2 + cbrt(17 + 3*sqrt(33)) + cbrt(17 - 3*sqrt(33)))) / 6
C2 = sqrt(3 * (4 + cbrt(199 + 3*sqrt(33)) + cbrt(199 - 3*sqrt(33)))) / 6

points = array([[C1,   C0,  C2], #0
                [C1,  -C0, -C2], #1
                [-C1, -C0,  C2], #2
                [-C1,  C0, -C2], #3
                [C2,   C1,  C0], #4
                [C2,  -C1, -C0], #5
                [-C2, -C1,  C0], #6
                [-C2,  C1, -C0], #7
                [C0,   C2,  C1], #8
                [C0,  -C2, -C1], #9
                [-C0, -C2,  C1], #10
                [-C0,  C2, -C1], #11
                [C0,  -C1,  C2], #12
                [C0,   C1, -C2], #13
                [-C0,  C1,  C2], #14
                [-C0, -C1, -C2], #15
                [C2,  -C0,  C1], #16
                [C2,   C0, -C1], #17
                [-C2,  C0,  C1], #18
                [-C2, -C0, -C1], #19
                [C1,  -C2,  C0], #20
                [C1,   C2, -C0], #21
                [-C1,  C2,  C0], #22
                [-C1, -C2, -C0], #23
                ])
# Scaling Matricies
P = [[1, 0, 0],
     [0, 1, 0],
     [0, 0, 1]]

Z = zeros((24, 3))

for i in range(24):
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
verts_cube = [[Z[2],Z[12],Z[0],Z[14]],
                [Z[3],Z[13],Z[1],Z[15]],
                [Z[4],Z[16],Z[5],Z[17]],
                [Z[7],Z[19],Z[6],Z[18]],
                [Z[8],Z[21],Z[11],Z[22]],
                [Z[9],Z[20],Z[10],Z[23]],
                [Z[0],Z[8],Z[14]],
                [Z[1],Z[9],Z[15]],
                [Z[2],Z[10],Z[12]],
                [Z[3],Z[11],Z[13]],
                [Z[4],Z[0],Z[16]],
                [Z[5],Z[1],Z[17]],
                [Z[6],Z[2],Z[18]],
                [Z[7],Z[3],Z[19]],
                [Z[8],Z[4],Z[21]],
                [Z[9],Z[5],Z[20]],
                [Z[10],Z[6],Z[23]],
                [Z[11],Z[7],Z[22]],
                [Z[12],Z[16],Z[0]],
                [Z[13],Z[17],Z[1]],
                [Z[14],Z[18],Z[2]],
                [Z[15],Z[19],Z[3]],
                [Z[16],Z[20],Z[5]],
                [Z[17],Z[21],Z[4]],
                [Z[18],Z[22],Z[7]],
                [Z[19],Z[23],Z[6]],
                [Z[20],Z[12],Z[10]],
                [Z[21],Z[13],Z[11]],
                [Z[22],Z[14],Z[8]],
                [Z[23],Z[15],Z[9]],
                [Z[8],Z[0],Z[4]],
                [Z[9],Z[1],Z[5]],
                [Z[10],Z[2],Z[6]],
                [Z[11],Z[3],Z[7]],
                [Z[12],Z[20],Z[16]],
                [Z[13],Z[21],Z[17]],
                [Z[14],Z[22],Z[18]],
                [Z[15],Z[23],Z[19]],
               ]

for n in range(0, 38):
    print(len(verts_cube[n]))

    if len(verts_cube[n]) == 3:
        cube = Poly3DCollection(verts_cube[3])

        cube.set_edgecolor("white")
        cube.set_linewidth(0.5)
        cube.set_alpha(0.5)
        cube.set_facecolor("blue")
    elif len(verts_cube[n]) == 4:
        cube = Poly3DCollection(verts_cube[10])

        cube.set_edgecolor("white")
        cube.set_linewidth(0.5)
        cube.set_alpha(0.5)
        cube.set_facecolor("yellow")

# Plot Surfaces
ax.add_collection3d(cube)

plt.show()
