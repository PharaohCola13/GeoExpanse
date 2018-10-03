# A Cube, brought to you by PharaohCola13

import mpl_toolkits.mplot3d.axes3d as p3
import matplotlib.pyplot as plt
from matplotlib import *
from numpy import *
from mpl_toolkits.mplot3d.art3d import *
from matplotlib.animation import *

name = "Great Rombicosidodecahedron"

def shape(fig, alpha, color, edge_c, edge_w, grid, sides,
				   edges, multi_pi, radius):

	points = array([[0,0,0],
					[-1, 	0.25 * (-3 - sqrt(5)), 0.25 * (-7 - (3 * sqrt(5)))],
					[-1, 	0.25 * (-3 - sqrt(5)), 0.25 * (7 + (3 * sqrt(5)))],
					[-1, 	0.25 * (3 + sqrt(5)), 	0.25 * (-7 - (3 * sqrt(5)))],
					[-1, 	0.25 * (3 + sqrt(5)), 	0.25 * (7 + (3 * sqrt(5)))],

					[-0.5, 	-0.5, 					-1.5 - sqrt(5)],
					[-0.5, 	-0.5, 					1.5 + sqrt(5)],
					[-0.5, 	0.5, 					-1.5 - sqrt(5)],
					[-0.5, 	0.5, 					1.5 + sqrt(5)],
					[-0.5, -1.5 - sqrt(5),		-0.5],
					[-0.5, -1.5 - sqrt(5),		0.5],
					[-0.5, -1 - (sqrt(5)/2),		-2 - (sqrt(5)/2)],
					[-0.5, -1 - (sqrt(5)/2), 		0.5 * (4 + sqrt(5))],
					[-0.5, 1.5 + sqrt(5), 		-0.5],
					[-0.5, 1.5 + sqrt(5), 		0.5],
					[-0.5, (0.5) * (2 + sqrt(5)), 	-2 - (sqrt(5)/2)],
					[-0.5, (0.5) * (2 + sqrt(5)), 	(0.5) * (4 + sqrt(5))],

					[0.5, -0.5, 					-1.5 - sqrt(5)],
					[0.5, -0.5, 					1.5 + sqrt(5)],
					[0.5, 0.5, 						-1.5 - sqrt(5)],
					[0.5, 0.5, 						1.5 + sqrt(5)],
					[0.5, -1.5 - sqrt(5), 			-0.5],
					[0.5, -1.5 - sqrt(5), 			0.5],
					[0.5, -1 - sqrt(5)/2, 			-2 - (sqrt(5)/2)],
					[0.5, -1 - sqrt(5)/2, 			0.5 * (4 + sqrt(5))],
					[0.5, 1.5 + sqrt(5), 			-0.5],
					[0.5, 1.5 + sqrt(5), 			0.5],
					[0.5, 0.5 * (2 + sqrt(5)), 		-2 - (sqrt(5)/2)],
					[0.5, 0.5 * (2 + sqrt(5)), 		0.5 * (4 + sqrt(5))],

					[1, 0.25 * (-3 - sqrt(5)), 		0.25 * (-7 - (3 * sqrt(5)))],
					[1, 0.25 * (-3 - sqrt(5)), 		0.25 * (7 + (3 * sqrt(5)))],
					[1, 0.25 * (3 + sqrt(5)), 		0.25 * (-7 - (3 * sqrt(5)))],
					[1, 0.25 * (3 + sqrt(5)),		0.25 * (7 + (3 * sqrt(5)))],

					[0.25 * (-7 - (3 * sqrt(5))), -1,  0.25 * (-3 - sqrt(5))],
					[0.25 * (-7 - (3 * sqrt(5))), -1,  0.25 * (3 + sqrt(5))],
					[0.25 * (-7 - (3 * sqrt(5))), 1,  0.25 * (-3 - sqrt(5))],
					[0.25 * (-7 - (3 * sqrt(5))), 1,  0.25 * (3 + sqrt(5))],

					[0.25 * (-5 - (3 * sqrt(5))), 0.25 * (-5 - sqrt(5)), 0.5 * (-1 - sqrt(5))],
					[0.25 * (-5 - (3 * sqrt(5))), 0.25 * (-5 - sqrt(5)), 0.5 * (1 + sqrt(5))],
					[0.25 * (-5 - (3 * sqrt(5))), 0.25 * (5 + sqrt(5)), 0.5 * (-1 - sqrt(5))],
					[0.25 * (-5 - (3 * sqrt(5))), 0.25 * (5 + sqrt(5)), 0.5 * (1 + sqrt(5))],

					[0.25 * (-5 - sqrt(5)), 0.5 * (-1 - sqrt(5)), 0.25 * (-5 - (3 * sqrt(5)))],
					[0.25 * (-5 - sqrt(5)), 0.5 * (-1 - sqrt(5)), 0.25 * (5 + (3 * sqrt(5)))],
					[0.25 * (-5 - sqrt(5)), 0.5 * (1 + sqrt(5)), 0.25 * (-5 - (3 * sqrt(5)))],
					[0.25 * (-5 - sqrt(5)), 0.5 * (1 + sqrt(5)), 0.25 * (5 + (3 * sqrt(5)))],

					[0.25 * (-3 - sqrt(5)), 0.25 * (-7 - (3 * sqrt(5))), -1],
					[0.25 * (-3 - sqrt(5)), 0.25 * (-7 - (3 * sqrt(5))), 1],
					[0.25 * (-3 - sqrt(5)), -0.75 * (1 + sqrt(5)), 0.5 * (-3 - sqrt(5))],
					[0.25 * (-3 - sqrt(5)), -0.75 * (1 + sqrt(5)), 0.5 * (3 + sqrt(5))],
					[0.25 * (-3 - sqrt(5)), 0.75 * (1 + sqrt(5)), 0.5 * (-3 - sqrt(5))],
					[0.25 * (-3 - sqrt(5)), 0.75 * (1 + sqrt(5)), 0.5 * (3 + sqrt(5))],
					[0.25 * (-3 - sqrt(5)), 0.25 * (7 + (3 * sqrt(5))), -1],
					[0.25 * (-3 - sqrt(5)), 0.25 * (7 + (3 * sqrt(5))), 1],

					[0.5 * (-3 - sqrt(5)), 0.25 * (-3 - sqrt(5)), -0.75 * (1 + sqrt(5))],
					[0.5 * (-3 - sqrt(5)), 0.25 * (-3 - sqrt(5)), 0.75 * (1 + sqrt(5))],
					[0.5 * (-3 - sqrt(5)), 0.25 * (3 + sqrt(5)), -0.75 * (1 + sqrt(5))],
					[0.5 * (-3 - sqrt(5)), 0.25 * (3 + sqrt(5)), 0.75 * (1 + sqrt(5))],

					[-1.5 - sqrt(5), -0.5, -0.5],
					[-1.5 - sqrt(5), -0.5, 0.5],
					[-1.5 - sqrt(5), 0.5, -0.5],
					[-1.5 - sqrt(5), 0.5, 0.5],

					[0.5 * (-1 - sqrt(5)), 0.25 * (-5 - (3 * sqrt(5))), 0.25 * (-5 - sqrt(5))],
					[0.5 * (-1 - sqrt(5)), 0.25 * (-5 - (3 * sqrt(5))), 0.25 * (5 + sqrt(5))],
					[0.5 * (-1 - sqrt(5)), 0.25 * (5 + (3 * sqrt(5))), 0.25 * (-5 - sqrt(5))],
					[0.5 * (-1 - sqrt(5)), 0.25 * (5 + (3 * sqrt(5))), 0.25 * (5 + sqrt(5))],

					[-2 - (sqrt(5)/2), -0.5, -1 - (sqrt(5)/2)],
					[-2 - (sqrt(5)/2), -0.5, 0.5 * (2 + sqrt(5))],
					[-2 - (sqrt(5)/2), 0.5, -1 - (sqrt(5)/2)],
					[-2 - (sqrt(5)/2), 0.5, 0.5 * (2 + sqrt(5))],

					[-1 - (sqrt(5)/2), -2 - (sqrt(5)/2), -0.5],
					[-1 - (sqrt(5)/2), -2 - (sqrt(5)/2), 0.5],
					[-1 - (sqrt(5)/2), 0.5 * (4 + sqrt(5)), -0.5],
					[-1 - (sqrt(5)/2), 0.5 * (4 + sqrt(5)), 0.5],

					[-0.75 * (1 + sqrt(5)), 0.5 * (-3 - sqrt(5)), 0.25 * (-3 - sqrt(5))],
					[-0.75 * (1 + sqrt(5)), 0.5 * (-3 - sqrt(5)), 0.25 * (3 + sqrt(5))],
					[-0.75 * (1 + sqrt(5)), 0.5 * (3 + sqrt(5)), 0.25 * (-3 - sqrt(5))],
					[-0.75 * (1 + sqrt(5)), 0.5 * (3 + sqrt(5)), 0.25 * (3 + sqrt(5))],

					[0.5 * (1 + sqrt(5)), 0.25 * (-5 - (3 * sqrt(5))), 0.25 * (-5 - sqrt(5))],
					[0.5 * (1 + sqrt(5)), 0.25 * (-5 - (3 * sqrt(5))), 0.25 * (5 + sqrt(5))],
					[0.5 * (1 + sqrt(5)), 0.25 * (5 + (3 * sqrt(5))), 0.25 * (-5 - sqrt(5))],
					[0.5 * (1 + sqrt(5)), 0.25 * (5 + (3 * sqrt(5))), 0.25 * (5 + sqrt(5))],

					[0.75 * (1 + sqrt(5)), 0.5 * (-3 - sqrt(5)), 0.25 * (-3 - sqrt(5))],
					[0.75 * (1 + sqrt(5)), 0.5 * (-3 - sqrt(5)), 0.25 * (3 + sqrt(5))],
					[0.75 * (1 + sqrt(5)), 0.5 * (3 + sqrt(5)), 0.25 * (-3 - sqrt(5))],
					[0.75 * (1 + sqrt(5)), 0.5 * (3 + sqrt(5)), 0.25 * (3 + sqrt(5))],

					[1.5 + sqrt(5), -0.5, -0.5],
					[1.5 + sqrt(5), -0.5, 0.5],
					[1.5 + sqrt(5), 0.5, -0.5],
					[1.5 + sqrt(5), 0.5, 0.5],

					[0.5 * (2 + sqrt(5)), -2 - (sqrt(5)/2), -0.5],
					[0.5 * (2 + sqrt(5)), -2 - (sqrt(5)/2), 0.5],
					[0.5 * (2 + sqrt(5)), 0.5 * (4 + sqrt(5)), -0.5],
					[0.5 * (2 + sqrt(5)), 0.5 * (4 + sqrt(5)), 0.5],

					[0.25 * (3 + sqrt(5)), 0.25 * (-7 - (3 * sqrt(5))), -1],
					[0.25 * (3 + sqrt(5)), 0.25 * (-7 - (3 * sqrt(5))), 1],
					[0.25 * (3 + sqrt(5)), -0.75 * (1 + sqrt(5)), 0.5 * (-3 - sqrt(5))],
					[0.25 * (3 + sqrt(5)), -0.75 * (1 + sqrt(5)), 0.5 * (3 + sqrt(5))],
					[0.25 * (3 + sqrt(5)), 0.75 * (1 + sqrt(5)), 0.5 * (-3 - sqrt(5))],
					[0.25 * (3 + sqrt(5)), 0.75 * (1 + sqrt(5)), 0.5 * (3 + sqrt(5))],
					[0.25 * (3 + sqrt(5)), 0.25 * (7 + (3 * sqrt(5))),-1],
					[0.25 * (3 + sqrt(5)), 0.25 * (7 + (3 * sqrt(5))),1],

					[0.5 * (3 + sqrt(5)), 0.25 * (-3 - sqrt(5)), -0.75 * (1 + sqrt(5))],
					[0.5 * (3 + sqrt(5)), 0.25 * (-3 - sqrt(5)), 0.75 * (1 + sqrt(5))],
					[0.5 * (3 + sqrt(5)), 0.25 * (3 + sqrt(5)), -0.75 * (1 + sqrt(5))],
					[0.5 * (3 + sqrt(5)), 0.25 * (3 + sqrt(5)), 0.75 * (1 + sqrt(5))],

					[0.5 * (4 + sqrt(5)), -0.5, -1 - (sqrt(5)/2)],
					[0.5 * (4 + sqrt(5)), -0.5, 0.5 * (2 + sqrt(5))],
					[0.5 * (4 + sqrt(5)), 0.5, -1 - (sqrt(5)/2)],
					[0.5 * (4 + sqrt(5)), 0.5, 0.5 * (2 + sqrt(5))],

					[0.25 * (5 + sqrt(5)), 0.5 * (-1 - sqrt(5)), 0.25 * (-5 - (3 * sqrt(5)))],
					[0.25 * (5 + sqrt(5)), 0.5 * (-1 - sqrt(5)), 0.25 * (5 + (3 * sqrt(5)))],
					[0.25 * (5 + sqrt(5)), 0.5 * (1 + sqrt(5)), 0.25 * (-5 - (3 * sqrt(5)))],
					[0.25 * (5 + sqrt(5)), 0.5 * (1 + sqrt(5)), 0.25 * (5 + (3 * sqrt(5)))],

					[0.25 * (5 + (3 * sqrt(5))), 0.25 * (-5 -sqrt(5)), 0.5 * (-1 - sqrt(5))],
					[0.25 * (5 + (3 * sqrt(5))), 0.25 * (-5 -sqrt(5)), 0.5 * (1 + sqrt(5))],
					[0.25 * (5 + (3 * sqrt(5))), 0.25 * (5 + sqrt(5)), 0.5 * (-1 - sqrt(5))],
					[0.25 * (5 + (3 * sqrt(5))), 0.25 * (5 + sqrt(5)), 0.5 * (1 + sqrt(5))],

					[0.25 * (7 + (3 * sqrt(5))), -1, 0.25 * (-3 - sqrt(5))],
					[0.25 * (7 + (3 * sqrt(5))), -1, 0.25 * (3 + sqrt(5))],
					[0.25 * (7 + (3 * sqrt(5))), 1, 0.25 * (-3 - sqrt(5))],
					[0.25 * (7 + (3 * sqrt(5))), 1, 0.25 * (3 + sqrt(5))],
									 ])

	# Scaling Matricies
	P = [[1, 0, 0],
		 [0, 1, 0],
		 [0, 0, 1]]

	Z = zeros((121, 3))

	for i in range(121):
		Z[i, :] = dot(points[i, :], P)

	# Figure Properties
	#fig = plt.figure(figsize=(8, 8))
	ax = p3.Axes3D(fig)
	ax.set_facecolor('black')

	plt.axis(grid)
	plt.axis('equal')

	ax.set_xlim(-4, 4)
	ax.set_ylim(-4, 4)
	ax.set_zlim(-4, 4)

	# Interval
	r = [-10, 10]

	X, Y = np.meshgrid(r, r)


	verts_cube = [ [Z[2],Z[6],Z[8],Z[4],Z[44],Z[56],Z[68],Z[66],Z[54],Z[42]], #
				  [Z[109],Z[29],Z[17],Z[19],Z[31],Z[111],Z[103],Z[107],Z[105],Z[101]], #
				  [Z[24],Z[30],Z[18],Z[6],Z[2],Z[12]], #
				  [Z[7],Z[3],Z[15],Z[27],Z[31],Z[19]], #
				  [Z[58],Z[57],Z[33],Z[37],Z[73],Z[69],Z[70],Z[74],Z[38],Z[34]], #
				  [Z[84],Z[116],Z[120],Z[88],Z[87],Z[119],Z[115],Z[83],Z[91],Z[92]], #
				  [Z[90],Z[89],Z[81],Z[113],Z[117],Z[85],Z[86],Z[118],Z[114],Z[82]], #
				  [Z[36],Z[40],Z[76],Z[72],Z[71],Z[75],Z[39],Z[35],Z[59],Z[60]],#
				  [Z[5],Z[17],Z[29],Z[23],Z[11],Z[1]],#
				  [Z[4],Z[8],Z[20],Z[32],Z[28],Z[16]],#
				  [Z[67],Z[55],Z[43],Z[3],Z[7],Z[5],Z[1],Z[41],Z[53],Z[65]],#
				  [Z[18],Z[30],Z[110],Z[102],Z[106],Z[108],Z[104],Z[112],Z[32],Z[20]],#
				  [Z[79],Z[83],Z[115],Z[103],Z[111],Z[97]],
				  [Z[38],Z[74],Z[62],Z[48],Z[42],Z[54]],
				  [Z[4], Z[16],Z[50],Z[44]],
				  [Z[23],Z[29],Z[109],Z[95]],
				  [Z[96],Z[110],Z[30],Z[24]],
				  [Z[43],Z[49],Z[15],Z[3]],
				  [Z[53],Z[41],Z[47],Z[61],Z[73],Z[37]],
				  [Z[98],Z[112],Z[104],Z[116],Z[84],Z[80]],
				  [Z[69],Z[45],Z[9],Z[10],Z[46],Z[70]],
				  [Z[26],Z[100],Z[92],Z[91],Z[99],Z[25]],
				  [Z[82],Z[114],Z[102],Z[110],Z[96],Z[78]],
				  [Z[55],Z[39],Z[75],Z[63],Z[49],Z[43]],
				  [Z[1], Z[11],Z[47],Z[41]],
				  [Z[28],Z[32],Z[112],Z[98]],
				  [Z[61],Z[47],Z[11],Z[23],Z[95],Z[77],Z[93],Z[21],Z[9],Z[45]],
				  [Z[50],Z[16],Z[28],Z[98],Z[80],Z[100],Z[26],Z[14],Z[52],Z[64]],
				  [Z[97],Z[111],Z[31],Z[27]],
				  [Z[42],Z[48],Z[12],Z[2]],
				  [Z[44],Z[50],Z[64],Z[76],Z[40],Z[56]],
				  [Z[77],Z[95],Z[109],Z[101],Z[113],Z[81]],
				  [Z[63],Z[51],Z[13],Z[25],Z[99],Z[79],Z[97],Z[27],Z[15],Z[49]],
				  [Z[46],Z[10],Z[22],Z[94],Z[78],Z[96],Z[24],Z[12],Z[48],Z[62]],
				  [Z[52],Z[14],Z[13],Z[51],Z[71],Z[72]],
				  [Z[22],Z[21],Z[93],Z[89],Z[90],Z[94]],
				  [Z[115],Z[119],Z[107],Z[103]],
				  [Z[34],Z[38],Z[54],Z[66]],
				  [Z[71],Z[51],Z[63],Z[75]],
				  [Z[94],Z[90],Z[82],Z[78]],
				  [Z[114],Z[118],Z[106],Z[102]],
				  [Z[35],Z[39],Z[55],Z[67]],
				  [Z[70],Z[46],Z[62],Z[74]],
				  [Z[99],Z[91],Z[83],Z[79]],
				  [Z[65],Z[53],Z[37],Z[33]],
				  [Z[104],Z[108],Z[120],Z[116]],
				  [Z[77],Z[81],Z[89],Z[93]],
				  [Z[76],Z[64],Z[52],Z[72]],
				  [Z[59],Z[35],Z[67],Z[65],Z[33],Z[57]],
				  [Z[106],Z[118],Z[86],Z[88],Z[120],Z[108]],
				  [Z[68],Z[56],Z[40],Z[36]],
				  [Z[101],Z[105],Z[117],Z[113]],
				  [Z[80],Z[84],Z[92],Z[100]],
				  [Z[73],Z[61],Z[45],Z[69]],
				  [Z[34],Z[66],Z[68],Z[36],Z[60],Z[58]],
				  [Z[105],Z[107],Z[119],Z[87],Z[85],Z[117]],
				  [Z[7],Z[19],Z[17],Z[5]],
				  [Z[6],Z[18],Z[20],Z[8]],
				  [Z[14],Z[26],Z[25],Z[13]],
				  [Z[9],Z[21],Z[22],Z[10]],
				  [Z[58],Z[60],Z[59],Z[57]],
				  [Z[85],Z[87],Z[88],Z[86]]
	]

	cube = Poly3DCollection(verts_cube)

	cube.set_edgecolor(edge_c)
	cube.set_linewidth(edge_w)
	cube.set_alpha(alpha)
	cube.set_facecolor(color)

	# Plot Surfaces
	ax.add_collection3d(cube)
