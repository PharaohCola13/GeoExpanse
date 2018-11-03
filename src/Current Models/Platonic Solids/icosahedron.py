# A Icosahedron, brought to you by PharaohCola13

import mpl_toolkits.mplot3d.axes3d as p3
import matplotlib.pyplot as plt
from matplotlib import *
from numpy import *
from mpl_toolkits.mplot3d.art3d import *
from matplotlib.animation import *

name = "Icosahedron"

def shape(fig, alpha, color, edge_c, edge_w, grid, figcolor):

# Points on the object
	p = (1 + sqrt(5))/2
	points = array([
					[p**2, 0, p**3], 	#2		#0 
					[-p**2, 0, p**3],	#6		#1 
					[0, p**3,  p**2],	#12		#2 
					[0, -p**3, p**2], 	#17		#3 
					[p**3, p**2, 0], 	# 27	#4 #
					[-p**3, p**2, 0], 	# 31	#5
					[-p**3, -p**2, 0], 	# 33	#6
					[p**3, -p**2, 0], 	# 37	#7
					[0, p**3, -p**2],	# 46	#8 
					[0, -p**3, -p**2], 	# 51	#9 
					[p**2, 0, -p**3], 	# 54	#10 
					[-p**2, 0, -p**3], 	#58		#11 
])

# Scaling Matricies
# 100%
	P = [
		[1, 0, 0],
		[0, 1, 0],
		[0, 0, 1]
		]

	I = zeros((12,3))

	for i in range(12):
		I[i,:] = dot(points[i,:],P)

# Figure Properties
	ax = p3.Axes3D(fig)
	ax.set_facecolor(figcolor) # Figure background turns black
	
# Axis Properties
	plt.axis(grid) # Turns off the axis grid
	plt.axis('equal')

# Axis Limits
	ax.set_xlim(-5, 5)
	ax.set_ylim(-5, 5)
	ax.set_zlim(-5, 5)

# The edges of the object
	verts = [
			[I[0], I[1], I[3]],
			[I[0], I[2], I[1]],
			[I[0], I[3], I[7]],
			[I[0], I[7], I[4]],
			[I[0], I[4], I[2]],
			[I[7], I[10], I[4]],
			[I[4], I[10], I[8]],
			[I[4], I[8], I[2]],
			[I[2], I[8], I[5]],
			[I[2], I[5], I[1]],
			[I[1], I[5], I[6]],
			[I[1], I[6], I[3]],
			[I[3], I[6], I[9]],
			[I[7], I[9], I[10]],
			[I[11], I[10], I[9]],
			[I[11], I[8], I[10]],
			[I[11], I[5], I[8]],
			[I[11], I[6], I[5]],
			[I[11],	I[9], I[6]],
			[I[3], I[9], I[7]],
			]

# Surface plot
	icosa = Poly3DCollection(verts)

	icosa.set_edgecolor(edge_c)
	icosa.set_linewidth(edge_w)
	icosa.set_alpha(alpha)
	icosa.set_facecolor(color)

	icosahedron = ax.add_collection3d(icosa)
