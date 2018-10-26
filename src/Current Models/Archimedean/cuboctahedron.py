# A Cuboctahedron, brought to you by PharaohCola13

import mpl_toolkits.mplot3d.axes3d as p3
import matplotlib.pyplot as plt
from matplotlib import *
from numpy import *
from mpl_toolkits.mplot3d.art3d import *
from matplotlib.animation import *
from matplotlib.text import Annotation
from mpl_toolkits.mplot3d.proj3d import proj_transform

# Used to generate the labels
class Annotation3D(Annotation):
    '''Annotate the point xyz with text s'''

    def __init__(self, s, xyz, *args, **kwargs):
        Annotation.__init__(self,s, xy=(0,0), *args, **kwargs)
        self._verts3d = xyz

    def draw(self, renderer):
        xs3d, ys3d, zs3d = self._verts3d
        xs, ys, zs = proj_transform(xs3d, ys3d, zs3d, renderer.M)
        self.xy=(xs,ys)
        Annotation.draw(self, renderer)

def annotate3D(ax, s, *args, **kwargs):
    '''add anotation text s to to Axes3d ax'''

    tag = Annotation3D(s, *args, **kwargs)
    ax.add_artist(tag)

name = "Cuboctahedron"

def shape(fig, alpha, color, edge_c, edge_w, grid, color2):


	points = array([[0,0,0],
					[-1, 0, 0],
					[-0.5, -0.5, -1/sqrt(2)],
					[-0.5, -0.5, 1/sqrt(2)],
					[-0.5, 0.5, -1/sqrt(2)],
					[-0.5, 0.5, 1/sqrt(2)],
					[0, -1, 0],
					[0,1,0],
					[0.5, -0.5, -1/sqrt(2)],
					[0.5, -0.5, 1/sqrt(2)],
					[0.5, 0.5, -1/sqrt(2)],
					[0.5, 0.5, 1/sqrt(2)],
					[1, 0, 0]
					])

	# Scaling Matricies
	P = [[1, 0, 0],
		 [0, 1, 0],
		 [0, 0, 1]]

	Z = zeros((13, 3))

	for i in range(13):
		Z[i, :] = dot(points[i, :], P)

	# Figure Properties
	#fig = plt.figure(figsize=(8,8))
	ax = p3.Axes3D(fig)
	ax.set_facecolor('black')

	plt.axis(grid)
	plt.axis('equal')

	ax.set_xlim(-1, 1)
	ax.set_ylim(-1, 1)
	ax.set_zlim(-1, 1)

	verts_cuboc = [[Z[4], Z[10], Z[8],  Z[2]],
				  [Z[3],  Z[9],  Z[11], Z[5]],
				  [Z[9],  Z[6],  Z[8],  Z[12]],
				  [Z[3],  Z[1],  Z[2],  Z[6]],
				  [Z[5],  Z[7],  Z[4],  Z[1]],
				  [Z[11], Z[12], Z[10], Z[7]],
				]
	cuboc_three = [
				  [Z[12], Z[11], Z[9]],
				  [Z[3],  Z[5],  Z[1]],
				  [Z[6],  Z[9],  Z[3]],
				  [Z[5],  Z[11], Z[7]],
				  [Z[8],  Z[10], Z[12]],
				  [Z[1],  Z[4],  Z[2]],
				  [Z[2],  Z[8],  Z[6]],
				  [Z[7],  Z[10], Z[4]]
				  ]

	cuboc = Poly3DCollection(verts_cuboc)

	cuboc.set_edgecolor("white")
	cuboc.set_linewidth(1)
	cuboc.set_alpha(0.5)
	cuboc.set_facecolor("deepskyblue")

	cuboc1 = Poly3DCollection(cuboc_three)

	cuboc1.set_edgecolor("white")
	cuboc1.set_linewidth(1)
	cuboc1.set_alpha(0.5)
	cuboc1.set_facecolor("deepskyblue")

	# Plot Surfaces
	ax.add_collection3d(cuboc)
	ax.add_collection3d(cuboc1)

	if grid == "on":
		# Produces the labels and arrows of the Hexagonal Face
		for j, xyz_ in enumerate(points):
		   hex = annotate3D(ax,
				       s                    =   (j),
				       xyz                  =   xyz_,
				       fontsize             =   13,
				       xytext               =   (-3,3),
				       textcoords           =   'offset points',
				       horizontalalignment  =   'right',
				       verticalalignment    =   'bottom',
				       arrowprops           =   dict(arrowstyle='<-', connectionstyle="arc3, rad=0.5")
				            )
		if grid == "off":
			ax.clear()
