# Something, brought to you by PharaohCola13

import mpl_toolkits.mplot3d.axes3d as p3
import matplotlib.pyplot as plt

from mpl_toolkits.mplot3d.art3d import *
from matplotlib.animation import *
from matplotlib import *
from numpy import *
import time

name = "Testing"

def shape(fig, alpha, color, edge_c, edge_w, grid, sides, edges, multi_pi, radiusm, radiusa, color2, color3, height):
	def x_(u,v):
		x = cos(u) * sin(v)
		return x

	def y_(u,v):
		y = sin(u) * sin(v)
		return y

	def z_(u,v):
		z = cos(v) + log1p(tan(2+v)**2)
		return z

	u = linspace(0.001, multi_pi * pi, 1 + sides)
	v = linspace(0, 2 * pi, edges)

	u, v = meshgrid(u, v)

	x = x_(u,v)
	y = y_(u,v)
	z = z_(u,v)

	ax = p3.Axes3D(fig)
	ax.set_facecolor('black')

#	ax1 = p3.Axes3D(fig1)
#	ax1.set_facecolor('black')

#	plt.figure(1)
	plt.axis("off")
	plt.axis('equal')

#	plt.figure(2)
#	plt.axis("off")
#	plt.axis("equal")
#	# Figure Properties
	#ax.set_xlim(-1,1)
	#ax.set_ylim(-1,1)
	#ax.set_zlim(-1,1)

	# Surface Plot

	test = ax.plot_surface(x, y, z)
#	test1 = ax1.plot_surface(x, y, z)

	test.set_alpha(alpha)
	test.set_edgecolor(edge_c)
	test.set_linewidth(edge_w)
	test.set_facecolor(color)

#	test1.set_alpha(alpha)#
#	test1.set_edgecolor(edge_c)
#	test1.set_linewidth(edge_w)
#	test1.set_facecolor(color)

# 	def rot_on():
#
# 		plt.axis("off")
# 		ax.set_facecolor('black')
# 		ax.grid(False)
# 		ax.axis('off')
# 		ax.set_xticks([])
# 		ax.set_yticks([])
# 		ax.set_zticks([])
#
# 		plt.axis('off')
# 		plt.axis('equal')
# 		def init():
# 			return test,
#
# 		def animate(i):
# 			ax.view_init(elev=45, azim=i)
# 			return test
#
# 		# Animate
# 		ani = FuncAnimation(fig, animate, init_func=init,
# 							interval=1, frames=500, repeat=True)
#
# 		plt.ion()
# 		plt.show()
# 		time.sleep(0)
# 		plt.close()
# 		#ax.clear()
# 		#plt.cla()
# 		#plt.clf()
#
# 	# def save_mp4():
# 	# 	plt.axis("off")
# 	# 	ax.set_facecolor('black')
# 	# 	ax.grid(False)
# 	# 	ax.axis('off')
# 	# 	ax.set_xticks([])
# 	# 	ax.set_yticks([])
# 	# 	ax.set_zticks([])
# 	#
# 	# 	plt.axis('off')
# 	# 	plt.axis('equal')
# 	# 	def init():
# 	# 		return test,
# 	#
# 	# 	def animate(i):
# 	# 		ax.view_init(elev=i, azim=i)
# 	# 		return test
# 	#
# 	# 	# Animate
# 	# 	ani = FuncAnimation(fig, animate, init_func=init,
# 	# 						interval=1, frames=500, repeat=True)
# 	#
# 	# 	Writer = writers['ffmpeg']
# 	#
# 	# 	writer = Writer(fps=15, bitrate=1800)
# 	# #
# 	# 	ani.save('{}.mp4'.format(name),writer=writer)
# 	#
# 	# 	plt.ion()
# 	# 	plt.show()
# 	# 	time.sleep(0)
# 	# 	plt.close()
# 	#
#
# 	def rot_off():
# 		ax.set_facecolor('black')
# 		ax.grid(False)
# 		ax.axis('off')
# 		ax.set_xticks([])
# 		ax.set_yticks([])
# 		ax.set_zticks([])
#
# 		plt.axis('off')
# 		plt.axis('equal')
#
# 		plt.ion()
# 		plt.show()
# 		time.sleep(0)
# 		plt.close()
# 		#plt.draw()
#
# 	if rot == "on":
# 		rot_on()
#
# 	#if save == "mp4":
# 		#save_mp4()
#
# 	if rot == "off":
# 		rot_off()
#
# # # Definitions for animation
# # def init():
# #  	return test,
# # #
# # def animate(i):
# # #     # azimuth angle : 0 deg to 360 deg
# # #     # elev = i * n --> rotates object about the xy-plane with a magnitude of n
# # #     # azim = i * n --> rotates object around the z axis with a magnitude of n
# # #     # For top view elev = 90
# # #     # For side view elev = 0
# # #
# #     ax.view_init(elev=20, azim=i*4)
# #     return test
# #
# # # Animate
# # #ani = FuncAnimation(fig, animate, init_func=init,
# # #                  frames=200, interval=50, blit=False, repeat=True)
# #
# # # Saving to testing.mp4
# #
# # #Writer = writers['ffmpeg']
# # #writer = Writer(fps=25, bitrate=1800)
# #
# # #ani.save('testing.mp4', writer=writer)
# #
# # plt.show()
