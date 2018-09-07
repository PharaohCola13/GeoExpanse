# A Octohedron, brought to you by PharaohCola13

import mpl_toolkits.mplot3d.axes3d as p3
import matplotlib.pyplot as plt

from mpl_toolkits.mplot3d.art3d import *
from matplotlib.animation import *
from matplotlib import *
from numpy import *


option = int(input('Run? (0) Yes, (1) No\n>> '))

while option == 0:

# Points on the object
p = (1 + sqrt(5))/2
	points = array([
					[0,0,0],			#0
					[0, 0, 2*p**2], 	#1
					[p**2, 0, p**3], 	#2
					[p, p**2, p**3],	#3
					[0, p, p**3],		#4
					[-p, p**2, p**3],	#5
					[-p**2, 0, p**3], 	#6
					[-p, -p**2, p**3],	#7
					[0, -p, p**3], 		#8
					[p, -p**2, p**3], 	#9
					[p**3, p, p**2],	#10
					[p**2, p**2, p**2], #11
					[0, p**3, p**2],	#12
					[-p**2, p**2, p**2],#13
					[-p**3, p, p**2], 	#14
					[-p**3, -p, p**2], 	#15
					[-p**2, -p**2, p**2],#16
					[0, -p**3, p**2],	#17
					[p**2, -p**2, p**2], #18
					[p**3, -p, p**2], 	#19
					[p**3, 0, p],		#20
					[p**2, p**3, p],	#21
					[-p**2, p**3, p],	#22
					[-p**3, 0, p],		#23
					[-p**2, -p**3, p],	#24
					[p**2, -p**3, p],	#25
					[2*p**2, 0, 0],		#26					
					[p**3, p**2, 0],	#27
					[p, p**3, 0],		#28
					[0, 2*p**2, 0],		#29
					[-p, p**3, 0],		#30					
					[-p**3, -p**2,0],	#31
					[-2*p**2, 0, 0],	#32
					[-p**3, -p**2, 0],	#33
					[-p, -p**3,	0],		#34				
					[0, -2*p**2, 0],	#35
					[p, -p**3, 0], 		#36
					[p**3, -p**2, 0],	#37
					[p**3, 0, -p],		#38					
					[p**2, p**3, -p], 	#39
					[-p**2, p**3, -p],	#40
					[-p**3, 0, -p],		#41
					[-p**2,-p**3, -p],	#42 					
					[p**2, -p**3, -p],	#43
					[p**3, p, -p**2],	#44
					[p**2, p**2, -p**2],#45
					[0, p**3, -p**2],	#46
					[-p**2, p**2. -p**2],#47
					[-p**3, p, -p**2],	#48					
					[-p**3, -p, -p**2],	#49					
					[-p**2, -p**2, -p**2],#50					
					[0, -p**3, -p**2],	#51					
					[p**2, -p**2, -p**2],#52					
					[p**3, -p, -p**2],	#53					
					[p**2, 0, -p**3],	#54					
					[p, p**2, -p**3],	#55
					[0,p, -p**3],		#56
					[-p, p**2, -p**3],	#57					
					[-p**2,	0, -p**3],	#58			
					[-p, -p**2, -p**3],	#59					
					[0, -p, -p**3],		#60				
					[p,	-p**2, -p**3],	#61				
					[0, 0, -2 * p**2], 	#62					
				   ])

# Scaling Matricies
# 100%
	P = [
		[1, 0, 0],
	    [0, 1, 0],
	    [0, 0, 1]
		]

	J = zeros((62,3))


	for i in range(62):
		J[i,:] = dot(points[i,:],P)

# Figure Properties
	fig = plt.figure(figsize=(8,8))

	ax = p3.Axes3D(fig)
	ax.set_facecolor('black') # Figure background turns black
	
# Axis Properties
	plt.axis('off') # Turns off the axis grid
	plt.axis('equal')

# Axis Limits
	ax.set_xlim(-1, 1)
	ax.set_ylim(-1, 1)
	ax.set_zlim(-1, 1)

# Radius
	r = [-1 ,1]

# Definition of x and y
	X, Y = np.meshgrid(r, r)

# The edges of the object
	verts = [
			[J[1], J[2], J[4]],
			[J[2], J[3], J[4]],
			[J[2], J[20], J[10]],
			[J[2], J[10], J[11]],
			[J[2], J[11], J[3]],
			[J[3], J[11], J[12]],
			[J[3], J[12], J[4]],
			[J[20], J[26], J[27]],
			[J[20], J[27], J[10]],
			[J[10], J[27], J[11]],
			[J[11], J[27], J[21]],
			[J[11], J[21], J[12]],
			[J[21], J[27], J[28]],
			[J[12], J[21], J[28]],
			[J[12], J[28], J[29]],
			[J[1], J[4], J[6]],
			[J[4], J[12], J[5]],
			[J[4], J[5], J[6]],
			[J[5], J[12], J[13]],
			[J[5], J[13], J[6]],
			[J[6], J[13], J[14]],
			[J[6], J[14], J[23]],
			[J[12], J[29], J[30]],
			[J[12], J[30], J[22]],
			[J[12], J[22], J[13]],
			[J[13], J[22], J[31]],
			[J[22], J[30], J[31]],
			[J[13], J[31], J[14]],
			[J[14], J[31], J[23]],
			[J[23], J[31], J[32]],
			[J[1], J[6], J[8]],
			[J[6], J[23], J[15]],
			[J[6], J[15], J[16]],
			[J[6], J[16], J[7]],
			[J[6], J[7], J[8]],
			[J[8], J[7], J[17]],
			[J[7], J[16], J[17]],
			[J[23], J[32], J[32]],
			[J[15], J[23], J[23]],
			[J[16], J[15], J[15]],
			[J[24], J[
			[J[34], J[
			[J[17], J[
			[J[17], J[
			[J[17], J[
			[J[1], J[
			[J[8], J[
			[J[8], J[
			[J[9], J[
			[J[9], J[
			[J[2], J[
			[J[2], J[
			[J[17], J[
			[J[17], J[
			[J[17], J[
			[J[18], J[
			[J[27], J[

			
			]

# Surface plot
	octa = Poly3DCollection(verts)

	octa.set_edgecolor('blue')
	octa.set_linewidth(2)
	octa.set_alpha(0.3)
	octa.set_facecolor('skyblue')

	octahedron = ax.add_collection3d(octa)


# Defintions for animations
	def init():
	    return octahedron,

	def animate(i):
# azimuth angle : 0 deg to 360 deg
# elev = i * n --> rotates object about the xy-plane with a magnitude of n
# azim = i * n --> rotates object around the z axis with a magnitude of n
# For top view elev = 90
# For side view elev = 0

	    ax.view_init(elev=0, azim= 4 * i)
	    return octahedron,

# Smooth-ish transition @ elev=90+i, azim=4 * 1, .., frames=550

# Animate
	#ani = FuncAnimation(fig, animate, init_func=init,
	#                   frames=550, interval=2, blit=False, repeat=True)

#Saving to Octahedron.mp4

	# Writer = writers['ffmpeg']
	# writer = Writer(fps=15, bitrate=1800)

	# ani.save('Octahedron.mp4', writer=writer)

	plt.show() # Shows Figure
	option = int(input('Run again? (0) Yes, (1) No\n>> '))

