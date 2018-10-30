# A pen_tri, brought to you by PharaohCola13

import mpl_toolkits.mplot3d.axes3d as p3
import matplotlib.pyplot as plt
from matplotlib import *
from numpy import *
from mpl_toolkits.mplot3d.art3d import *
from matplotlib.animation import *

name = "Penrose Triangle"


def shape(fig, edge_c, edge_w, grid):
	plt.clf()
	points_x = [0.09, -2.66, 3.284, 6.315, -1.505, -8.328, 9.254, 10.685, 1.227, -1.563, -9.804, -3.916]
	points_y = [2.761, -2.19, -2.19, -2.189, 5.229, -6.883, -6.89, -4.45, 10.022, 10.022, -4.602, -4.449]


	edges = [(1, 3), (3,9), (9,10), (5,6), (7,8), (2,4), (4,5), (0,11), (11,7), (8,9), (10,5), (6,7)]

	lines_xy = list(zip(points_x, points_y))
	segments = [(lines_xy[s], lines_xy[t]) for s, t in edges]

	# Figure Properties
	ax = plt.subplot(111)
	ax.patch.set_facecolor("black")
	ax.xaxis.set_tick_params(color="white", labelcolor="white")
	ax.yaxis.set_tick_params(color="white", labelcolor="white")

	plt.axis(grid)
	plt.axis('equal')


	plt.scatter(points_x, points_y,
			   s        =   0,
			   )

	pen_tri = LineCollection(segments)
	pen_tri.set_linewidth(edge_w)
	pen_tri.set_color(edge_c)

	# Plot Surfaces
	ax.add_collection(pen_tri)
