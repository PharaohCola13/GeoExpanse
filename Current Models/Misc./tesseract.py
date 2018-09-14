# A Tesseract, brought to you by PharaohCola13

import sys
sys.path.insert(0,'./parse.py')
from  parse import *

name = "Tesseract"

if args.run:
# Points on the object
	points = array([
				   [-1,	-1,	-1],
    	           [ 1,	-1, -1],
    	           [ 1,	 1, -1],
    	           [-1,	 1, -1],
    	           [-1 	-1,  1],
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
	fig = plt.figure(figsize=(8,8))
	
	ax = p3.Axes3D(fig)
	ax.set_facecolor('black')

	plt.axis('off')
	plt.axis('equal')

	ax.set_xlim(-4,4)
	ax.set_ylim(-4,4)
	ax.set_zlim(-4,4)

# Radius
	radius = float(input('What is the radius?\n>> '))
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

	outer_region.set_edgecolor('white')
	outer_region.set_linewidth(1)
	outer_region.set_alpha(0.2)	
	outer_region.set_facecolor('blue')

# Inside Region
	inner_region = Poly3DCollection(verts_inner)

	inner_region.set_edgecolor('white')
	inner_region.set_linewidth(1)
	inner_region.set_alpha(0.5)
	inner_region.set_facecolor('purple')


# Plot Surfaces
	out = ax.add_collection3d(outer_region)
	inn = ax.add_collection3d(inner_region)

	if args.rotate:
# Defintions for animations

		def animate(i):
	# azimuth angle : 0 deg to 360 deg
	# elev = i * n --> rotates object about the xy-plane with a magnitude of n
	# azim = i * n --> rotates object around the z axis with a magnitude of n
	# For top view elev = 90
	# For side view elev = 0

		    ax.view_init(elev=i, azim= 4 * i)
		    return out,

	# Animate
		ani = FuncAnimation(fig, animate,
				   frames=88, interval=1, blit=False, repeat=True)
		if args.save:
#Saving to Tesseract.mp4

			Writer = writers['ffmpeg']
			writer = Writer(fps=15, bitrate=1800)

			ani.save('../Samples/%s.mp4' % name, writer=writer)

	
	plt.show() # Shows Figure
