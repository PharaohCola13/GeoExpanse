# Something, brought to you by PharaohCola13

import mpl_toolkits.mplot3d.axes3d as p3
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import *
from matplotlib.animation import *
from matplotlib import *
from numpy import *
import warnings
import time
import sys

name = " "


def shape(fig, alpha, color, edge_c, edge_w, grid, sides, edges,
		  multi_pi, figcolor, rotation, rotmagt, rotmagp, save):
	plt.clf()
	def x_(u,v):
		x = cos(u) * sin(v)
		return x

	def y_(u,v):
		y = sin(u) * sin(v)
		return y

	def z_(u,v):
		z = cos(v) + log1p(tan(2+v)**2)
		return z

	u = linspace(0.001,multi_pi * pi, 1 + sides)
	v = linspace(0, multi_pi * pi, edges)

	u, v = meshgrid(u, v)

	x = x_(u,v)
	y = y_(u,v)
	z = z_(u,v)

	#fig = plt.figure(figsize=(8, 8), facecolor="black", edgecolor="white")
	ax = p3.Axes3D(fig)
	ax.set_facecolor(figcolor)

	plt.axis(grid)
	plt.axis('equal')

	# Surface Plot
	test = ax.plot_surface(x, y, z)

	test.set_alpha(alpha)
	test.set_edgecolor(edge_c)
	test.set_linewidth(edge_w)
	test.set_facecolor(color)

	def rot_on():
		def animate(i):
			ax.view_init(azim=rotmagt * i, elev=rotmagp * i)

		if save == "MP4":
			# Animate
			ani = FuncAnimation(fig, animate, frames=500,
								interval=100, save_count=50)  # frames=100)#, repeat=True)

			Writer = writers['ffmpeg']
			writer = Writer(fps=30, bitrate=1800)
			ani.save('Test.mp4', writer=writer)
		else:
			#save = None
			# Animate
			ani = FuncAnimation(fig, animate,
								interval=1, save_count=50)  # frames=100)#, repeat=True)
			pass


		plt.ion()
		plt.show()
		time.sleep(0)
		plt.close()

	if rotation == "On":
		rot_on()
	elif rotation == "Off":
		pass



#	def save_mp4():
#		def animate(i):
#			ax.view_init(elev=i, azim=i)

# 	# 	# Animate
#		ani = FuncAnimation(fig, animate, init_func=init,
#					interval=1, frames=500, repeat=True)


#		plt.ion()
#		time.sleep(0)
#		plt.close()
#
#	if save == "mp4":
#		print("Welp")	
#	save_mp4()
#	if rot == "off":
#		rot_off()

# # # Saving to testing.mp4
# #
# # #Writer = writers['ffmpeg']
# # #writer = Writer(fps=25, bitrate=1800)
# #
# # #ani.save('testing.mp4', writer=writer)
# #
#plt.show()
