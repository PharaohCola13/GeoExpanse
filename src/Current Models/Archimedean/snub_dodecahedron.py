# A Snub Dodecahedron, brought to you by PharaohCola13

import mpl_toolkits.mplot3d.axes3d as p3
import matplotlib.pyplot as plt
from matplotlib import *
from numpy import *
from mpl_toolkits.mplot3d.art3d import *
from matplotlib.animation import *
from matplotlib.text import Annotation
from mpl_toolkits.mplot3d.proj3d import proj_transform


name = "Snub Dodecahedron"

def shape(fig, alpha, color, edge_c, edge_w, grid, color2, figcolor, rotation, rotmagt, rotmagp, save):
	plt.clf()

	C0  = 0.192893711352359022108262546061
	C1  = 0.330921024729844230963655269187
	C2  = 0.374821658114562295266609516608
	C3  = 0.567715369466921317374872062669
	C4  = 0.643029605914072573107464141441
	C5  = 0.728335176957191477360671629838
	C6  = 0.847550046789060797396217956030
	C7  = 1.103156835071753772627281146446
	C8  = 1.24950378846302719500774109632
	C9  = 1.41526541625598211477109001870
	C10 = 1.45402422933801541929649491091
	C11 = 1.64691794069037444140475745697
	C12 = 1.74618644098582634573474528789
	C13 = 1.97783896542021867236841272616
	C14 = 2.097053835252087992403959052348

	points = array([
					[  C2,   C1,  C14],
					[  C2,  -C1, -C14],
					[ -C2,  -C1,  C14],
					[ -C2,   C1, -C14],
					[ C14,   C2,   C1],
					[ C14,  -C2,  -C1],
					[-C14,  -C2,   C1],
					[-C14,   C2,  -C1],
					[  C1,  C14,   C2],
					[  C1, -C14,  -C2],
					[ -C1, -C14,   C2],
					[ -C1,  C14,  -C2],
					[  C3,  -C4,  C13],
					[  C3,   C4, -C13],
					[ -C3,   C4,  C13],
					[ -C3,  -C4, -C13],
					[ C13,  -C3,   C4],
					[ C13,   C3,  -C4],
					[-C13,   C3,   C4],
					[-C13,  -C3,  -C4],
					[  C4, -C13,   C3],
					[  C4,  C13,  -C3],
					[ -C4,  C13,   C3],
					[ -C4, -C13,  -C3],
					[  C0,   C8,  C12],
					[  C0,  -C8, -C12],
					[ -C0,  -C8,  C12],
					[ -C0,   C8, -C12],
					[ C12,   C0,   C8],
					[ C12,  -C0,  -C8],
					[-C12,  -C0,   C8],
					[-C12,   C0,  -C8],
					[  C8,  C12,   C0],
					[  C8, -C12,  -C0],
					[ -C8, -C12,   C0],
					[ -C8,  C12,  -C0],
					[  C7,   C6,  C11],
					[  C7,  -C6, -C11],
					[ -C7,  -C6,  C11],
					[ -C7,   C6, -C11],
					[ C11,   C7,   C6],
					[ C11,  -C7,  -C6],
					[-C11,  -C7,   C6],
					[-C11,   C7,  -C6],
					[  C6,  C11,   C7],
					[  C6, -C11,  -C7],
					[ -C6, -C11,   C7],
					[ -C6,  C11,  -C7],
					[  C9,  -C5,  C10],
					[  C9,   C5, -C10],
					[ -C9,   C5,  C10],
					[ -C9,  -C5, -C10],
					[ C10,  -C9,   C5],
					[ C10,   C9,  -C5],
					[-C10,   C9,   C5],
					[-C10,  -C9,  -C5],
					[  C5, -C10,   C9],
					[  C5,  C10,  -C9],
					[ -C5,  C10,   C9],
					[ -C5, -C10,  -C9],
	])

	P = [[1, 0, 0],
		 [0, 1, 0],
		 [0, 0, 1]
		 ]
	Z = zeros((60,3))

	for i in range(60):
		Z[i, :] = dot(points[i, :], P)

	ax = p3.Axes3D(fig)
	ax.set_facecolor(figcolor)

	plt.axis(grid)

	ax.set_xlim(-2, 2)
	ax.set_ylim(-2, 2)
	ax.set_zlim(-2, 2)


	verts = [
			[Z[ 0], Z[12], Z[48], Z[28], Z[36]],
			[Z[ 1], Z[13], Z[49], Z[29], Z[37]],
			[Z[ 2], Z[14], Z[50], Z[30], Z[38]],
			[Z[ 3], Z[15], Z[51], Z[31], Z[39]],
			[Z[ 4], Z[17], Z[53], Z[32], Z[40]],
			[Z[ 5], Z[16], Z[52], Z[33], Z[41]],
			[Z[ 6], Z[19], Z[55], Z[34], Z[42]],
			[Z[ 7], Z[18], Z[54], Z[35], Z[43]],
			[Z[ 8], Z[22], Z[58], Z[24], Z[44]],
			[Z[ 9], Z[23], Z[59], Z[25], Z[45]],
			[Z[10], Z[20], Z[56], Z[26], Z[46]],
			[Z[11], Z[21], Z[57], Z[27], Z[47]],
			[Z[ 0], Z[14], Z[ 2]],
			[Z[ 1], Z[15], Z[ 3]],
			[Z[ 2], Z[12], Z[ 0]],
			[Z[ 3], Z[13], Z[ 1]],
			[Z[ 4], Z[16], Z[ 5]],
			[Z[ 5], Z[17], Z[ 4]],
			[Z[ 6], Z[18], Z[ 7]],
			[Z[ 7], Z[19], Z[ 6]],
			[Z[ 8], Z[21], Z[11]],
			[Z[ 9], Z[20], Z[10]],
			[Z[10], Z[23], Z[ 9]],
			[Z[11], Z[22], Z[ 8]],
			[Z[12], Z[56], Z[48]],
			[Z[13], Z[57], Z[49]],
			[Z[14], Z[58], Z[50]],
			[Z[15], Z[59], Z[51]],
			[Z[16], Z[48], Z[52]],
			[Z[17], Z[49], Z[53]],
			[Z[18], Z[50], Z[54]],
			[Z[19], Z[51], Z[55]],
			[Z[20], Z[52], Z[56]],
			[Z[21], Z[53], Z[57]],
			[Z[22], Z[54], Z[58]],
			[Z[23], Z[55], Z[59]],
			[Z[24], Z[36], Z[44]],
			[Z[25], Z[37], Z[45]],
			[Z[26], Z[38], Z[46]],
			[Z[27], Z[39], Z[47]],
			[Z[28], Z[40], Z[36]],
			[Z[29], Z[41], Z[37]],
			[Z[30], Z[42], Z[38]],
			[Z[31], Z[43], Z[39]],
			[Z[32], Z[44], Z[40]],
			[Z[33], Z[45], Z[41]],
			[Z[34], Z[46], Z[42]],
			[Z[35], Z[47], Z[43]],
			[Z[36], Z[24], Z[ 0]],
			[Z[37], Z[25], Z[ 1]],
			[Z[38], Z[26], Z[ 2]],
			[Z[39], Z[27], Z[ 3]],
			[Z[40], Z[28], Z[ 4]],
			[Z[41], Z[29], Z[ 5]],
			[Z[42], Z[30], Z[ 6]],
			[Z[43], Z[31], Z[ 7]],
			[Z[44], Z[32], Z[ 8]],
			[Z[45], Z[33], Z[ 9]],
			[Z[46], Z[34], Z[10]],
			[Z[47], Z[35], Z[11]],
			[Z[48], Z[16], Z[28]],
			[Z[49], Z[17], Z[29]],
			[Z[50], Z[18], Z[30]],
			[Z[51], Z[19], Z[31]],
			[Z[52], Z[20], Z[33]],
			[Z[53], Z[21], Z[32]],
			[Z[54], Z[22], Z[35]],
			[Z[55], Z[23], Z[34]],
			[Z[56], Z[12], Z[26]],
			[Z[57], Z[13], Z[27]],
			[Z[58], Z[14], Z[24]],
			[Z[59], Z[15], Z[25]],
			[Z[24], Z[14], Z[ 0]],
			[Z[25], Z[15], Z[ 1]],
			[Z[26], Z[12], Z[ 2]],
			[Z[27], Z[13], Z[ 3]],
			[Z[28], Z[16], Z[ 4]],
			[Z[29], Z[17], Z[ 5]],
			[Z[30], Z[18], Z[ 6]],
			[Z[31], Z[19], Z[ 7]],
			[Z[32], Z[21], Z[ 8]],
			[Z[33], Z[20], Z[ 9]],
			[Z[34], Z[23], Z[10]],
			[Z[35], Z[22], Z[11]],
			[Z[36], Z[40], Z[44]],
			[Z[37], Z[41], Z[45]],
			[Z[38], Z[42], Z[46]],
			[Z[39], Z[43], Z[47]],
			[Z[48], Z[56], Z[52]],
			[Z[49], Z[57], Z[53]],
			[Z[50], Z[58], Z[54]],
			[Z[51], Z[59], Z[55]],
	]

	fc = [color if i in range(0, 11) else color2 for i in range(len(verts))]

	sdode = Poly3DCollection(verts)

	sdode.set_edgecolor(edge_c)
	sdode.set_linewidth(edge_w)
	sdode.set_alpha(alpha)
	sdode.set_facecolor(fc)

	ax.add_collection3d(sdode)


	def rot_on():
		def animate(i):
			ax.view_init(azim=rotmagt * i, elev=rotmagp * i)

		if save == "MP4":
			# Animate
			ani = FuncAnimation(fig, animate, frames=500,
								interval=100, save_count=50)  # frames=100)#, repeat=True)

			Writer = writers['ffmpeg']
			writer = Writer(fps=30, bitrate=1800)
			ani.save('{}.mp4'.format(name), writer=writer)
		else:
			# save = None
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