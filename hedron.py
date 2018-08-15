# A Dodecahedron, brought to you by PharaohCola13

import mpl_toolkits.mplot3d.axes3d as p3
import matplotlib.pyplot as plt
from matplotlib import cm
import numpy as np
from numpy import pi, linspace, cos, sin
from mpl_toolkits.mplot3d.art3d import Poly3DCollection, Line3DCollection
from matplotlib.animation import FuncAnimation
from matplotlib.animation import writers


points = np.array([[1.21412, 0, 1.58931],				#0
					[0.375185, 1.1547, 1.58931],		#1
					[-0.982247, 0.713644, 1.58931],		#2
					[-0.982247, -0.713644, 1.58931],	#3
					[0.375185, -1.1547, 1.58931],		#4
					[1.96449, 0, 0.375185],				#5
					[0.607062, 1.86835, 0.375185],		#6
					[-1.58931, 1.1547, 0.375185],		#7
					[-1.58931, -1.1547, 0.375185],		#8
					[0.607062, -1.86835, 0.375185],		#9
					[1.58931, 1.1547, -0.375185],		#10
					[-0.607062, 1.86835, -0.375185],	#11
					[-1.96449, 0, -0.375185],			#12
					[-0.607062, -1.86835, -0.375185],	#13
					[1.58931, -1.1547, -0.375185],		#14
					[0.982247, 0.713644, -1.58931],		#15
					[-0.375185, 1.1547, -1.58931],		#16
					[-1.21412, 0, -1.58931],			#17
					[-0.375185, -1.1547, -1.58931],		#18
					[0.982247, -0.713644, -1.58931]		#19
])
					
P = [[1, 0, 0],
	 [0, 1, 0],
	 [0, 0, 1]]

Q = [[0.5, 0, 0],
	 [0, 0.5, 0],
	 [0, 0, 0.5]]


Z = np.zeros((20,3))

M = np.zeros((20,3))


for i in range(20):
	Z[i,:] = np.dot(points[i,:],P)


for i in range(20):
	M[i,:] = np.dot(points[i,:],Q)


# Figure Properties
fig = plt.figure(figsize=(8,8))

ax = p3.Axes3D(fig)
ax.set_facecolor('black')

plt.axis('off')
plt.axis('equal')

ax.set_xlim(-4,4)
ax.set_ylim(-4,4)
ax.set_zlim(-4,4)

# Radius
r = [-1,1]

X, Y = np.meshgrid(r, r)

verts = [[Z[0], Z[1], Z[2], Z[3], Z[4]], 
         [Z[0], Z[5], Z[10], Z[6], Z[1]],
         [Z[1], Z[6], Z[11], Z[7], Z[2]],
         [Z[2], Z[7], Z[12], Z[8], Z[3]],
         [Z[3], Z[8], Z[13], Z[9], Z[4]],
      	 [Z[4], Z[9], Z[14], Z[5], Z[0]],
      	 [Z[15], Z[10], Z[5], Z[14], Z[19]],
      	 [Z[16], Z[11], Z[6], Z[10], Z[15]],
      	 [Z[17], Z[12], Z[7], Z[11], Z[16]],
      	 [Z[18], Z[13], Z[8], Z[12], Z[17]],
      	 [Z[19], Z[14], Z[9], Z[13], Z[18]],
      	 [Z[19], Z[18], Z[17], Z[16], Z[15]]
]

averts = [[M[0], M[1], M[2], M[3], M[4]], 
         [M[0], M[5], M[10], M[6], M[1]],
         [M[1], M[6], M[11], M[7], M[2]],
         [M[2], M[7], M[12], M[8], M[3]],
         [M[3], M[8], M[13], M[9], M[4]],
      	 [M[4], M[9], M[14], M[5], M[0]],
      	 [M[15], M[10], M[5], M[14], M[19]],
      	 [M[16], M[11], M[6], M[10], M[15]],
      	 [M[17], M[12], M[7], M[11], M[16]],
      	 [M[18], M[13], M[8], M[12], M[17]],
      	 [M[19], M[14], M[9], M[13], M[18]],
      	 [M[19], M[18], M[17], M[16], M[15]]
]


# Outside Region
dodeca = Poly3DCollection(verts)

dodeca.set_edgecolor('white')
dodeca.set_linewidth(1)
dodeca.set_alpha(0.1)
dodeca.set_facecolor('purple')


adodeca = Poly3DCollection(averts)

adodeca.set_edgecolor('white')
adodeca.set_linewidth(1)
adodeca.set_alpha(0.2)
adodeca.set_facecolor('purple')


hedron = ax.add_collection3d(dodeca)

ahedron = ax.add_collection3d(adodeca)

# Defintions for animations
def init():
    return hedron,

def animate(i):
    # azimuth angle : 0 deg to 360 deg
    # elev = i * n --> rotates object about the xy-plane with a magnitude of n
    # azim = i * n --> rotates object around the z axis with a magnitude of n
    # For top view elev = 90
    # For side view elev = 0

    ax.view_init(elev=i, azim= 4 * i)
    return hedron,

# Animate
ani = FuncAnimation(fig, animate, init_func=init,
                   frames=88, interval=1, blit=False, repeat=True)

#Saving to Tesseract.mp4

#3Writer = writers['ffmpeg']
#writer = Writer(fps=15, bitrate=1800)

#ani.save('Tesseract.mp4', writer=writer)



plt.show()
