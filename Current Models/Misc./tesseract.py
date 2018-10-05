# A Tesseract, brought to you by PharaohCola13

import mpl_toolkits.mplot3d.axes3d as p3
import matplotlib.pyplot as plt
from matplotlib import *
from numpy import *
from mpl_toolkits.mplot3d.art3d import *
from matplotlib.animation import *

name = "Tesseract"

def shape(fig, alpha, color, edge_c, edge_w, grid, radius, color2):
# Points on the object
	points = array([
				   [-1,	-1,	-1],
    	           [ 1,	-1, -1],
    	           [ 1,	 1, -1],
    	           [-1,	 1, -1],
    	           [-1, -1,  1],
    	           [ 1,	-1,  1],
    	           [ 1,  1,  1],
    	           [-1,	 1,	 1]
				   ])
 
# Scaling Matricies
# 200%
	P = [
		[2, 0, 0],
		[0, 2, 0],
		[0, 0, 2]
		]

# 100%
	Q = [
		[1, 0, 0],
		[0, 1, 0],
		[0, 0, 1]
		]

	Z = zeros((8,3))
	
	V = zeros((8,3))

	for i in range(8):
		Z[i,:] = dot(points[i,:],P)

	for i in range(8):
		V[i,:] = dot(points[i,:],Q)

# Figure Properties
	ax = p3.Axes3D(fig)
	ax.set_facecolor('black')

	plt.axis(grid)
	plt.axis('equal')

	ax.set_xlim(-4,4)
	ax.set_ylim(-4,4)
	ax.set_zlim(-4,4)

# Radius
	r = radius
	r = [-1 * r,r]

# Definition of x and y
	X, Y = np.meshgrid(r, r)

# Outer Region Configuration
	verts_outer = [
				  [Z[0], V[0], V[1], Z[1]],
				  [Z[1], V[1], V[5], Z[5]], 
				  [Z[0], V[0], V[4], Z[4]], 
				  [Z[4], V[4], V[5], Z[5]], 
				  [Z[5], V[5], V[6], Z[6]],
				  [Z[1], V[1], V[2], Z[2]], 
				  [Z[2], V[2], V[6], Z[6]],
				  [Z[2], V[2], V[3], Z[3]],
				  [Z[6], V[6], V[7], Z[7]],
				  [Z[7], V[7], V[3], Z[3]],
				  [Z[0], V[0], V[3], Z[3]],
				  [Z[4], V[4], V[7], Z[7]]
				  ]

# Inner Cube Configuration	
	verts_inner = [
			 	  [V[0],V[1],V[2],V[3]],
				  [V[4],V[5],V[6],V[7]],
				  [V[0],V[4],V[5],V[1]],
				  [V[1],V[5],V[6],V[2]],
				  [V[2],V[6],V[7],V[3]],
				  [V[3],V[7],V[4],V[0]]
				  ]

# Outside Region
	outer_region = Poly3DCollection(verts_outer)

	outer_region.set_edgecolor(edge_c)
	outer_region.set_linewidth(edge_w)
	outer_region.set_alpha(alpha)	
	outer_region.set_facecolor(color)

# Inside Region
	inner_region = Poly3DCollection(verts_inner)

	inner_region.set_edgecolor(edge_c)
	inner_region.set_linewidth(edge_w)
	inner_region.set_alpha(alpha)
	inner_region.set_facecolor(color2)


# Plot Surfaces
	out = ax.add_collection3d(outer_region)
	inn = ax.add_collection3d(inner_region)
