import matplotlib
matplotlib.use('TkAgg')
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
import mpl_toolkits.mplot3d.axes3d as p3
from matplotlib.animation import *
from numpy import *
from matplotlib.figure import Figure
import Tkinter as tk  # python 2.7
import ttk            # python 2.7
import sys

import interesting

root = tk.Tk()

fig = plt.figure(figsize=(8,8))


root.title("Geometric Models")
# Vars

grid_axis = tk.StringVar()

# Functions

def axi():
		plt.axis(str(grid_axis.get()))

def quit():
		global root
		root.quit()
		root.destroy()

# Rotational Widgets

tk.Label(root, text="XY-rotation").grid(row=2, column=0, pady=0)
scroll_elev 	= tk.Scale(root, from_=-50, to=50, width=40, orient=tk.HORIZONTAL)
scroll_elev.grid(row=3, column=0, sticky="nsew")

tk.Label(root, text="Z-rotation").grid(row=4, column=0, pady=0)
scroll_azim 	= tk.Scale(root, from_=-50, to=50, width=40, orient=tk.HORIZONTAL)
scroll_azim.grid(row=5, column=0, sticky="nsew")

# Grid Functions

grid_on 		= tk.Radiobutton(root, text="On", variable=grid_axis, value='on', command=axi)
grid_on.grid(row=0, column=1, sticky='n')

grid_off 		= tk.Radiobutton(root, text='Off', variable=grid_axis, value='off', command=axi)
grid_off.grid(row=0, column=2, sticky='n')

# Transparency

a_entry_label 	= tk.Label(root, text="Transparency").grid(row=0, column=1, sticky='nw', pady=265)
a_entry 		= tk.Scale(root, from_=0, to=1, resolution=0.1, orient=tk.HORIZONTAL)
a_entry.grid(row=0, column=2, sticky='nw', pady=250)

# Edge Width

ew_entry_label 	= tk.Label(root, text="Edge Width").grid(row=0, column=1, sticky='nw', pady=350)
ew_entry       	= tk.Scale(root, from_=0, to=5, resolution=0.5, orient=tk.HORIZONTAL)
ew_entry.grid(row=0, column=2, sticky='nw', pady=335)

# Face color

c_entry_label 	= tk.Label(root, text="Face Color").grid(row=0, column=1, sticky='nw', pady=30, padx=20)

c_entry = tk.Listbox(root, exportselection=0, width=15) 
c_entry.insert(1, 'gold')
c_entry.insert(2, 'teal')
c_entry.insert(3, 'white')
c_entry.insert(4, 'red')
c_entry.insert(5, 'blue')
c_entry.insert(6, 'fuchsia')
c_entry.insert(7, 'green')
c_entry.insert(8, 'lime')
c_entry.insert(9, 'paleturquoise')
c_entry.insert(10, 'orange')
c_entry.insert(11, 'lightgray')
c_entry.insert(12, 'black')
c_entry.insert(13, 'coral')
c_entry.insert(14, 'deepskyblue')

c_entry.grid(row=0, column=1, sticky='n', pady=50)

# Edge Color

tk.Label(root, text="Edge Color").grid(row=0, column=2, sticky='nw', pady=30, padx=20)
ec_entry = tk.Listbox(root, exportselection=0, width=15)
ec_entry.insert(1, 'gold')
ec_entry.insert(2, 'teal')
ec_entry.insert(3, 'white')
ec_entry.insert(4, 'red')
ec_entry.insert(5, 'blue')
ec_entry.insert(6, 'fuchsia')
ec_entry.insert(7, 'green')
ec_entry.insert(8, 'lime')
ec_entry.insert(9, 'paleturquoise')
ec_entry.insert(10, 'orange')
ec_entry.insert(11, 'lightgray')
ec_entry.insert(12, 'black')
ec_entry.insert(13, 'coral')
ec_entry.insert(14, 'deepskyblue')
ec_entry.grid(row=0, column=2, sticky='nw', pady=50)

tk.Button(root, text="Quit", command=quit).grid(row=5, column=1, columnspan=2, sticky='nsew')

class Geometry(tk.Frame):
	global fig, scroll_elev, scroll_azim, c_entry, ec_entry, a_entry, ew_entry

	def __init__(self, master=None):
		tk.Frame.__init__(self,master)
		self.createWidgets()

	def createWidgets(self):
		ax = p3.Axes3D(fig)
		ax.set_facecolor('black')
		plt.axis('off')
		canvas = FigureCanvasTkAgg(fig,root)
		canvas.get_tk_widget().grid(row=0,column=0)
		canvas.draw()

		self.plotbutton=tk.Button(root, text="Render", command=lambda: self.plot(canvas,ax))
		self.plotbutton.grid(row=1,column=0, sticky="nsew")

	def plot(self,canvas,ax):	
		global fig, scroll_azim, scroll_elev, c_entry, ec_entry, a_entry, grid_axis, ew_entry
		
		ax.clear()
		edge_c 		= ec_entry.get(ec_entry.curselection()[0]) 
		color 		= c_entry.get(c_entry.curselection()[0])
		rot_azim 	= scroll_azim.get()
		rot_elev 	= scroll_elev.get()
		alpha		= a_entry.get()
		grid		= grid_axis.get()
		edge_w		= ew_entry.get()

		def x_(u,v):
			x = cos(u) * sin(v)
			return x

		def y_(u,v):
			y = sin(u) * sin(v)
			return y

		def z_(u,v):
			z = cos(v) + log1p(tan(2 + v)**2)
			return z
		u = linspace(0.001, 2 * pi, 25)
		v = linspace(0, 2 * pi, 25)

		u, v = meshgrid(u, v)

		x = x_(u,v)
		y = y_(u,v)
		z = z_(u,v)

		plt.axis(grid)
		interest = ax.plot_surface(x, y, z)

		interest.set_alpha(alpha)
		interest.set_edgecolor(edge_c)
		interest.set_linewidth(edge_w)
		interest.set_facecolor(color)
		def animate(i):
	#     # azimuth angle : 0 deg to 360 deg
	#     # elev = i * n --> rotates object about the xy-plane with a magnitude of n
	#     # azim = i * n --> rotates object around the z axis with a magnitude of n
	#     # For top view elev = 90
	#     # For side view elev = 0
	#
			ax.view_init(elev=(rot_elev * i), azim=(rot_azim * i))

		ani = FuncAnimation(fig, animate,
		   	 frames=550, interval=2, blit=False, repeat=True)
		canvas.draw()

	def test(self, canvas, ax):
		global fig, scroll_azim, scroll_elev, c_entry, ec_entry, a_entry,grid_axis
		
		ax.clear()
		edge_c 		= ec_entry.get(ec_entry.curselection()[0]) 
		color 		= c_entry.get(c_entry.curselection()[0])
		rot_azim 	= scroll_azim.get()
		rot_elev 	= scroll_elev.get()
		alpha		= a_entry.get()
		grid 		= grid_axis.get()
		
		interesting.shape(fig, alpha, color, edge_c, rot_elev, rot_azim, grid)

		def animate(i):
	#     # azimuth angle : 0 deg to 360 deg
	#     # elev = i * n --> rotates object about the xy-plane with a magnitude of n
	#     # azim = i * n --> rotates object around the z axis with a magnitude of n
	#     # For top view elev = 90
	#     # For side view elev = 0
	#
			ax.view_init(elev=(rot_elev * i), azim=(rot_azim * i))

		ani = FuncAnimation(fig, animate,
		   	 frames=550, interval=2, blit=False, repeat=True)
		canvas.draw()



geo=Geometry(master=root)
geo.mainloop()
