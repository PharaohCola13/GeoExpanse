# A Scutoid, brought to you by PharaohCola13

import mpl_toolkits.mplot3d.axes3d as p3
import matplotlib.pyplot as plt
from matplotlib import cm
import numpy as np
from numpy import pi, linspace, cos, sin
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
from matplotlib.animation import FuncAnimation
from matplotlib.animation import writers


hexa = np.array([[-2,0,1],
				 [-1.5, 0.866, 1],
				 [-0.5, 0.866, 1],
				 [0.0, 0, 1],
				 [-0.5, -0.866, 1],
				 [-1.5, -0.866, 1]])

penta = np.array([[-2,0,0],
				  [-1.5,0.866,0],
				  [-0.5, 0.866,0],
				  [0.0, 0, 0],
				  [-1, -0.866, 0]])

cent = np.array([[-1.5, -0.866, 1],
				 [-1, -1.266, 0.5],
				 [-0.5, -0.866, 1]])


ahexa = np.array([[0,0,0],
				 [-1, -0.866, 0],
				 [-0.75, -1.866, 0],
				 [0.25, -2.166, 0],
				 [1.05, -1.466, 0],
				 [1, -0.434, 0]])

apenta = np.array([[0.0,0,1],
				  [1, -0.434,1],
				  [1.05, -1.466, 1],
				  [0, -1.7, 1],
					[-0.5,-0.866,1]])

acent = np.array([[-1, -0.866, 0],
				 [-1, -1.266, 0.5],
				 [-0.75, -1.866, 0]])


N = [[1,0,0],
	 [0,1,0],
	 [0,0,1]]

aN = [[1,0,0],
	 [0,1,0],
	 [0,0,1]]

M = np.zeros((6,3))
P = np.zeros((5,3))
Q = np.zeros((3,3))

aM = np.zeros((6,3))
aP = np.zeros((5,3))
aQ = np.zeros((3,3))

for i in range(6):
	M[i,:] = np.dot(hexa[i,:],N)

for i in range(5):
	P[i,:] = np.dot(penta[i,:],N)

for i in range(3):
	Q[i,:] = np.dot(cent[i,:],N)


for i in range(6):
	aM[i,:] = np.dot(ahexa[i,:],aN)

for i in range(5):
	aP[i,:] = np.dot(apenta[i,:],aN)

for i in range(3):
	aQ[i,:] = np.dot(acent[i,:],aN)




fig = plt.figure(figsize=(8,8))
ax = p3.Axes3D(fig)
ax.set_facecolor('black')

plt.axis('off')
plt.axis('equal')
 
ax.set_xlim(-2,2)
ax.set_ylim(-2,2)
ax.set_zlim(0,1)

r = [-2, 2]

X,Y = np.meshgrid(r,r)

top_hex = [[M[0], M[1], M[2], M[3], M[4], M[5]]]

bottom_pent = [[P[0], P[1], P[2], P[3], P[4]]]

sides = [[P[0], M[0], M[1], P[1]],
				 [P[1], M[1], M[2], P[2]],
				 [P[2], M[2], M[3], P[3]],
				 [P[3], P[4], Q[1], Q[2], M[4], M[3]],
				 [P[4], Q[1], Q[0], M[5], M[0], P[0]]

]

verts_cent = [[Q[0], Q[1], Q[2]]]

##

bottom_hex = [[aM[0], aM[1], aM[2], aM[3], aM[4], aM[5]]]

top_pent = [[aP[1], aP[2], aP[3], aP[4], aP[0]]]

alt_sides = [[aP[0], aM[0], aM[5], aP[1]],
				[aP[1], aM[5], aM[4], aP[2]],
				[aP[2], aM[4], aM[3], aP[3]],
				[aP[3], aM[3], aQ[2], aQ[1], aP[4]] 

]

verts_acent = [[aQ[0], aQ[1], aQ[2], aQ[0]]]



scu_top_hex = Poly3DCollection(top_hex)

scu_top_hex.set_edgecolor('black')
scu_top_hex.set_facecolor('green')
scu_top_hex.set_linewidth(2)
scu_top_hex.set_alpha(1)


scu_bottom_pent = Poly3DCollection(bottom_pent)

scu_bottom_pent.set_edgecolor('black')
scu_bottom_pent.set_facecolor('green')
scu_bottom_pent.set_linewidth(2)
scu_bottom_pent.set_alpha(1)

scu_sides = Poly3DCollection(sides)

scu_sides.set_edgecolor('black')
scu_sides.set_linewidth(2)
scu_sides.set_facecolor('green')
scu_sides.set_alpha(1)

scu_cent = Poly3DCollection(verts_cent)

scu_cent.set_edgecolor('black')
scu_cent.set_linewidth(2)
scu_cent.set_facecolor('green')
scu_cent.set_alpha(1)

##

scu_bottom_hex = Poly3DCollection(bottom_hex)

scu_bottom_hex.set_edgecolor('black')
scu_bottom_hex.set_facecolor('yellow')
scu_bottom_hex.set_linewidth(2)
scu_bottom_hex.set_alpha(1)


scu_top_pent = Poly3DCollection(top_pent)

scu_top_pent.set_edgecolor('black')
scu_top_pent.set_facecolor('yellow')
scu_top_pent.set_linewidth(2)
scu_top_pent.set_alpha(1)

scu_alt_sides = Poly3DCollection(alt_sides)

scu_alt_sides.set_edgecolor('black')
scu_alt_sides.set_linewidth(2)
scu_alt_sides.set_facecolor('yellow')
scu_alt_sides.set_alpha(1)

scu_acent = Poly3DCollection(verts_acent)

scu_acent.set_edgecolor('black')
scu_acent.set_linewidth(2)
scu_acent.set_facecolor('yellow')
scu_acent.set_alpha(1)

sth = ax.add_collection(scu_top_hex)
sbp = ax.add_collection(scu_bottom_pent)
ss = ax.add_collection(scu_sides)
sc = ax.add_collection(scu_cent)

##

sbh = ax.add_collection(scu_bottom_hex)
stp = ax.add_collection(scu_top_pent)
sas = ax.add_collection(scu_alt_sides)
sa = ax.add_collection(scu_acent)

# Defintions for animations
def init():
    return sth,

def animate(i):
    # azimuth angle : 0 deg to 360 deg
    # elev = i * n --> rotates object about the xy-plane with a magnitude of n
    # azim = i * n --> rotates object around the z axis with a magnitude of n
    # For top view elev = 90
    # For side view elev = 0

    ax.view_init(elev=14, azim=-147)
    return sth,

# Animate
ani = FuncAnimation(fig, animate, init_func=init,
                   frames=88, interval=1, blit=False, repeat=True)

#Saving to Tesseract.mp4

#Writer = writers['ffmpeg']
#writer = Writer(fps=15, bitrate=1800)

#ani.save('Tesseract.mp4', writer=writer)




plt.show()
