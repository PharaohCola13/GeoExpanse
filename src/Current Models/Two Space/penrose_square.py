# A pen_tri, brought to you by PharaohCola13

import mpl_toolkits.mplot3d.axes3d as p3
import matplotlib.pyplot as plt
from matplotlib import *
from numpy import *
from mpl_toolkits.mplot3d.art3d import *
from matplotlib.animation import *
from matplotlib.text import Annotation

name = "Penrose Square"


def shape(fig, edge_c, edge_w, grid, figcolor):
	plt.clf()

	points_x = [-1.56,  -10,  -10.024,  -1.524, 	  1.225,	10, 	10.02, 1.2,	 1.544, 	-5.3, 	-6.9, 0, -1.78, 5.3, 6.9, 0 ]
	points_y = [10.024, 1.2,  -1.56,   -10.024, 	-10.024,	-1.6, 	1.28, 10.024, 6.9, 		0, 		1.64, -5.3,-7.02, 0, -1.6, 5.3]

	edges = [(0,1), (1,2), (2,3),(3,4), (4,5), (5,6),(6,7), (7,0), (8,9),  (10,11), (12,13),  (14,15), (14,3), (12,1), (10,7), (8,5)]

	lines_xy = list(zip(points_x, points_y))
	segments = [(lines_xy[s], lines_xy[t]) for s, t in edges]

	# Figure Properties
	ax = plt.subplot(111)
	ax.patch.set_facecolor("white")
	ax.set_facecolor(figcolor) # Figure background turns black
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
	if grid == "on":
		labels = ['({}, {})'.format(round(i,2), round(j,2)) for i in points_x for j in points_y]

		for label, x, y in zip(labels, points_x, points_y):
		   plt.annotate(label,
					  # s                    =   label,
					   xy                   =   (x,y),
					   fontsize             =   8,
					   color				=   edge_c,
					   xytext               =   (-3,3),
					   textcoords           =   'offset points',
					   horizontalalignment  =   'right',
					   verticalalignment    =   'bottom',
					   #arrowprops           =   dict(arrowstyle='<-', connectionstyle="arc3, rad=0.5")
					        )
