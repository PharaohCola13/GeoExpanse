# A Scutoid, brought to you by PharaohCola13

import mpl_toolkits.mplot3d.axes3d as p3
import matplotlib.pyplot as plt
from matplotlib import cm
import numpy as np
from numpy import pi, linspace, cos, sin
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
from matplotlib.animation import FuncAnimation
from matplotlib.animation import writers


hex_top = np.array([[cos(pi/3),sin(pi/3),1],
		    [cos(2*pi/3),sin(2*pi/3), 1],
		    [cos(pi), sin(pi), 1],
		    [cos(4*pi/3), sin(4*pi/3), 1],
		    [cos(5*pi/3), sin(5*pi/3), 1],
		    [cos(2*pi), sin(2*pi), 1]])

pent_bottom = np.array([[0,1,0],
			[-sin(2*pi/5),cos(2*pi/5),0],
			[-sin(pi/5),-cos(pi/5),0],
			[sin(pi/5),-cos(pi/5), 0],
			[sin(2*pi/5),cos(2*pi/5), 0]])

cent = np.array([[0.5, 0.866, 1],
		 [0, 1, 0.5],
		 [-0.5, 0.866, 1]])


hex_bottom = np.array([[0,0,0],
		       [-1, -0.866, 0],
		       [-0.75, -1.866, 0],
		       [0.25, -2.166, 0],
		       [1.05, -1.466, 0],
		       [1, -0.434, 0]])

pent_top = np.array([[0.0,0,1],
		     [1, -0.434,1],
		     [1.05, -1.466, 1],
		     [0, -1.7, 1],
		     [-0.5,-0.866,1]])

cent_alt = np.array([[-1, -0.866, 0],
		     [-1, -1.266, 0.5],
		     [-0.75, -1.866, 0]])


# Scaling Matricies
N = [[1,0,0],
     [0,1,0],
     [0,0,1]]

L = [[1,0,0],
     [0,1,0],
     [0,0,1]]

M = np.zeros((6,3))
P = np.zeros((5,3))
Q = np.zeros((3,3))

R = np.zeros((6,3))
S = np.zeros((5,3))
T = np.zeros((3,3))

for i in range(6):
	M[i,:] = np.dot(hex_top[i,:],N)

for i in range(5):
	P[i,:] = np.dot(pent_bottom[i,:],N)

for i in range(3):
	Q[i,:] = np.dot(cent[i,:],N)


for i in range(6):
	R[i,:] = np.dot(hex_bottom[i,:],L)

for i in range(5):
	S[i,:] = np.dot(pent_top[i,:],L)

for i in range(3):
	T[i,:] = np.dot(cent_alt[i,:],L)
	
# Figure Properties
fig = plt.figure(figsize=(10,10))
ax = p3.Axes3D(fig)
ax.set_facecolor('black')

plt.axis('off')
plt.axis('equal')
 
ax.set_xlim(-1.5,1.5)
ax.set_ylim(-1.5,1.5)
ax.set_zlim(0,1)

# Radius
r = [-2, 2]

X,Y = np.meshgrid(r,r)

# Edges for the Scutoid with a Hexagon on top
top_hex = [[M[0], M[1], M[2], M[3], M[4], M[5]]]

bottom_pent = [[P[0], P[1], P[2], P[3], P[4]]]

sides = [[P[1], M[2], M[3], P[2]],
		 [P[2], M[3], M[4], P[3]],
		 [P[3], M[4], M[5], P[4]],
	 	 [P[4], P[0], Q[1], Q[0], M[0], M[5]],
	 	 [P[0], Q[1], M[1], M[2], P[1]]
]

verts_cent = [[Q[0], Q[1], Q[2]]]

# Edges for the Scutoid with a Pentagon on top

bottom_hex = [[R[0], R[1], R[2], R[3], R[4], R[5]]]

top_pent = [[S[1], S[2], S[3], S[4], S[0]]]

alt_sides = [[S[0], R[0], R[5], S[1]],
	     [S[1], R[5], R[4], S[2]],
	     [S[2], R[4], R[3], S[3]],
	     [S[3], R[3], T[2], T[1], S[4]]]

verts_acent = [[T[0], T[1], T[2], T[0]]]

# Suface Properties (Scutoid with Hexagon on top)
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

# Surface Properties (Scutoid with Pentagon on top)

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

# Surface Plot (Scutoid with Hexagon on top)
sth = ax.add_collection(scu_top_hex)
sbp = ax.add_collection(scu_bottom_pent)
ss = ax.add_collection(scu_sides)
sc = ax.add_collection(scu_cent)

# Surface Plot (Scutoid with Pentagon on top)

#sbh = ax.add_collection(scu_bottom_hex)
#stp = ax.add_collection(scu_top_pent)
#sas = ax.add_collection(scu_alt_sides)
#sa = ax.add_collection(scu_acent)

# Defintions for animations
def init():
    return sth,

def animate(i):
    # azimuth angle : 0 deg to 360 deg
    # elev = i * n --> rotates object about the xy-plane with a magnitude of n
    # azim = i * n --> rotates object around the z axis with a magnitude of n
    # For top view elev = 90
    # For side view elev = 0

    ax.view_init(elev=0, azim=i)
    return sth,

# Animate
#ani = FuncAnimation(fig, animate, init_func=init,
#                   frames=450, interval=10, blit=False, repeat=True)

#Saving to Scutoid.mp4

#Writer = writers['ffmpeg']
#writer = Writer(fps=15, bitrate=1800)

#ani.save('Scutoid.mp4', writer=writer)

plt.show()
