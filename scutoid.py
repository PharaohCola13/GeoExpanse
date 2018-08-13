# A Scutoid, brought to you by PharaohCola13

import mpl_toolkits.mplot3d.axes3d as p3
import matplotlib.pyplot as plt
from matplotlib import cm
import numpy as np
from numpy import pi, linspace, cos, sin
from mpl_toolkits.mplot3d.art3d import Poly3DCollection, Line3DCollection
from matplotlib.animation import FuncAnimation
from matplotlib.animation import writers


hexa = np.array([[0,0,1],
				 [0.5, 0.866, 1],
				 [1.5, 0.866, 1],
				 [2.0, 0, 1],
				 [1.5, -0.866, 1],
				 [0.5, -0.866, 1]])

penta = np.array([[0,0,0],
				  [0.5,0.866,0],
				  [1.5, 0.866,0],
				  [2.0, 0, 0],
				  [1, -0.866, 0]])

cent = np.array([[0.5, -0.866, 1],
				 [1, -0.866, 0.5],
				 [1.5, -0.866, 1]])


ahexa = np.array([[0,0,-1],
				 [0.5, 0.866, -1],
				 [1.5, 0.866, -1],
				 [2.0, 0, -1],
				 [1.5, -0.866, -1],
				 [0.5, -0.866, -1]])

apenta = np.array([[0,0,0],
				  [0.5,0.866,0],
				  [1.5, 0.866,0],
				  [2.0, 0, 0],
				  [1, -0.866, 0]])

acent = np.array([[0.5, -0.866, -1],
				 [1, -0.866, -0.5],
				 [1.5, -0.866, -1]])


N = [[1,0,0],
	 [0,1,0],
	 [0,0,1]]

aN = [[-1,0,0],
	 [0,-1,0],
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
#plt.axis('equal')
 
ax.set_xlim(0,2)
ax.set_ylim(-1,1)
ax.set_zlim(0,1)

r = [-0.866, 0.866]

X,Y = np.meshgrid(r,r)

verts_hex = [[M[0], M[1], M[2], M[3], M[4], M[5]]]

verts_pent = [[P[0], P[1], P[2], P[3], P[4]]]

verts_sides = [[P[0], M[0], M[1], P[1]],
				 [P[1], M[1], M[2], P[2]],
				 [P[2], M[2], M[3], P[3]],
				 [P[3], P[4], Q[1], Q[2], M[4], M[3]],
				 [P[4], Q[1], Q[0], M[5], M[0], P[0]]

]

verts_cent = [[Q[0], Q[1], Q[2]]]

##

verts_ahex = [[aM[0], aM[1], aM[2], aM[3], aM[4], aM[5]]]

verts_apent = [[aP[0], aP[1], aP[2], aP[3], aP[4]]]

verts_asides = [[aP[0], aM[0], aM[1], aP[1]],
				 [aP[1], aM[1], aM[2], aP[2]],
				 [aP[2], aM[2], aM[3], aP[3]],
				 [aP[3], aP[4], aQ[1], aQ[2], aM[4], aM[3]],
				 [aP[4], aQ[1], aQ[0], aM[5], aM[0], aP[0]]

]

verts_acent = [[aQ[0], aQ[1], aQ[2]]]



scu_hex = Poly3DCollection(verts_hex)

scu_hex.set_edgecolor('blue')
scu_hex.set_facecolor('white')
scu_hex.set_linewidth(1)
scu_hex.set_alpha(1)


scu_pent = Poly3DCollection(verts_pent)

scu_pent.set_edgecolor('blue')
scu_pent.set_facecolor('white')
scu_pent.set_linewidth(1)
scu_pent.set_alpha(1)

scu_sides = Poly3DCollection(verts_sides)

scu_sides.set_edgecolor('blue')
scu_sides.set_linewidth(1)
scu_sides.set_facecolor('white')
scu_sides.set_alpha(1)

scu_cent = Poly3DCollection(verts_cent)

scu_cent.set_edgecolor('blue')
scu_cent.set_linewidth(1)
scu_cent.set_facecolor('white')
scu_cent.set_alpha(1)

##

scu_ahex = Poly3DCollection(verts_ahex)

scu_ahex.set_edgecolor('blue')
scu_ahex.set_facecolor('white')
scu_ahex.set_linewidth(1)
scu_ahex.set_alpha(1)


scu_apent = Poly3DCollection(verts_apent)

scu_apent.set_edgecolor('blue')
scu_apent.set_facecolor('white')
scu_apent.set_linewidth(1)
scu_apent.set_alpha(1)

scu_asides = Poly3DCollection(verts_asides)

scu_asides.set_edgecolor('blue')
scu_asides.set_linewidth(1)
scu_asides.set_facecolor('white')
scu_asides.set_alpha(1)

scu_acent = Poly3DCollection(verts_acent)

scu_acent.set_edgecolor('blue')
scu_acent.set_linewidth(1)
scu_acent.set_facecolor('white')
scu_acent.set_alpha(1)

ax.add_collection(scu_hex)
ax.add_collection(scu_pent)
ax.add_collection(scu_sides)
ax.add_collection(scu_cent)

ax.add_collection(scu_ahex)
ax.add_collection(scu_apent)
ax.add_collection(scu_asides)
ax.add_collection(scu_acent)


plt.show()

