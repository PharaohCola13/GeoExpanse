import matplotlib
matplotlib.use('TkAgg')
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
import mpl_toolkits.mplot3d.axes3d as p3
from matplotlib.animation import *
from numpy import *
from matplotlib.figure import Figure
import tkinter as tk  # python 2.7
import PIL
from PIL import ImageTk
#import ttk            # python 2.7
import sys
import threading
#import interesting

sys.path.insert(0, './In Development/')

sys.path.insert(0, './Current Models/')
sys.path.insert(0, './Current Models/Hyperbolic')
sys.path.insert(0, './Current Models/Misc.')
sys.path.insert(0, './Current Models/Platonic Solids')
sys.path.insert(0, './Current Models/Surfaces')
sys.path.insert(0, './Current Models/Topological')

sys.path.insert(0, './Scutoid Research/')

## Current Models
# import prism 			 	 as pris
# import pyramid				 as pyra
# import sphere				 as sphe
#
# # Hyperbolic
# import hyperbolic_octahedron as hyoc
# import hyperbolic_paraboloid as hypa
# import one_sheet_hyperboloid as oshy
#
# # Misc.
# import three_dodecahedron	 as tdod
# import cressant				 as cres
# import funnel				 as funn
# import gabriel_horn			 as horn
# import rose_spiral			 as rose
# import shell				 as shel
# import tesseract			 as tess
#
# # Surfaces
# #import boys_surface			 as boys
# #import breather_surface		 as brea
# #import kuen_surface			 as kuen
# #import steiner_surface		 as stei
#import roman_surface		 as roma
#
# # Platonic Surfaces
# import cube					 as cube
# import dodecahedron			 as dode
# import icosahedron			 as icos
# import octahedron			 as octa
#
# # Topological
# #import cross_cap			 as cros
# #import klein				 as klei
# #import mobius				 as mobi
import torus				 as toru
#
# ## In Development
# import interesting			 as rile
# import polyhedron			 as poly
# #import hyperbolic_cylinder	 as hycl
# #import dini_surface			 as disu
# #import knot					 as knot
# #import neat					 as neat
# #import spiral				 as spir
# #import testing				 as test
# #import vase					 as vase


root = tk.Tk()

root.title("Geometric Models")

root.geometry("750x800")


class Geometry(tk.Frame):
	def __init__(self, master=None):
		tk.Frame.__init__(self,master)
		self.createWidgets()

	def createWidgets(self):
		self.fig = plt.figure(figsize=(5, 5))
		ax = p3.Axes3D(self.fig)
		ax.set_facecolor('black')
		plt.axis('off')
		canvas = FigureCanvasTkAgg(self.fig,root)
		canvas.get_tk_widget().grid(row=0,column=0, sticky='new')
		root.update_idletasks()
		canvas.draw()

		# Vars

		self.grid_axis = tk.StringVar()
		
		#self.alpha	   = tk.StringVar()
		
		self.axis_limits = tk.StringVar()

		#self.		= 

		# Functions

		def axi():
			plt.axis(str(self.grid_axis.get()))

		def zoo():
			self.plt.xlim(-1 * self.axis_zoom.get(), self.axis_zoom.get())
			self.plt.ylim(-1 * self.axis_zoom.get(), self.axis_zoom.get())

		def quit():
			global root
			root.quit()
			root.destroy()

		# Ploting plot
		tk.Button(root, text="Render Plot", command=lambda: self.plot
		(canvas,ax), height=4).grid(row=0, column=1, sticky="new", pady=500)

		# Ploting test
		tk.Button(root, text="Render Test", command=lambda: self.test
		(canvas,ax), height=4).grid(row=0, column=1,  sticky="new", pady=585)

		tk.Button(root, text="Quit", command=quit, height=10).grid(row=0, column=2, rowspan=1, sticky='new', pady=500)

		# Rotational functions
		tk.Label(root, text="XY-rotation").grid(row=0, column=0, sticky='new', pady=510)
		self.scroll_elev = tk.Scale(root, from_=-50, to=50, width=40, orient=tk.HORIZONTAL)
		self.scroll_elev.grid(row=0, column=0, sticky="nsew", pady=530)

		tk.Label(root, text="Z-rotation").grid(row=0, column=0, sticky="new", pady=610, )
		self.scroll_azim = tk.Scale(root, from_=-50, to=50, width=40, orient=tk.HORIZONTAL)
		self.scroll_azim.grid(row=0, column=0, sticky="nsew", pady=630)

		# Changing axis limits
		tk.Label(root, text="Axis Limits").grid(row=0, column=0, sticky="new", pady=710)
		self.axis_zoom = tk.Scale(root, from_=1, to=100, width=40, orient=tk.HORIZONTAL)
		self.axis_zoom.grid(row=0, column=0, sticky="nsew", pady=730)

		# Grid Functions (on/off)
		self.grid_on = tk.Radiobutton(root, text="Grid On", variable=self.grid_axis, value='on', command=axi)
		self.grid_on.grid(row=0, column=1, sticky='n')

		self.grid_off = tk.Radiobutton(root, text='Grid Off', variable=self.grid_axis, value='off', command=axi)
		self.grid_off.grid(row=0, column=2, sticky='n')
		self.grid_axis.set('off')

		# Transparency
		tk.Label(root, text="Transparency").grid(row=0, column=1, sticky='nw', pady=225)
		self.a_entry = tk.Scale(root, from_=0, to=1, resolution=0.1, orient=tk.HORIZONTAL)
		self.a_entry.grid(row=0, column=2, sticky='nw', pady=210)
		self.a_entry.set(0.4)

		# Entry of the number of sides
		self.si_entry_label = tk.Label(root, text="Number of Sides").grid(row=0, column=1, sticky='nw', pady=270)
		self.si_entry = tk.Scale(root, from_=1, to=100, resolution=1, orient=tk.HORIZONTAL)
		self.si_entry.grid(row=0, column=2, sticky='nw', pady=250)
		self.si_entry.set(20)

		# Entry of the number of edges
		tk.Label(root, text="Number of edges").grid(row=0, column=1, sticky='nw', pady=310)
		self.ed_entry = tk.Scale(root, from_=1, to=100, resolution=1, orient=tk.HORIZONTAL)
		self.ed_entry.grid(row=0, column=2, sticky='nw', pady=290)
		self.ed_entry.set(20)

		tk.Label(root, text="Multiple of pi").grid(row=0, column=1, sticky='nw', pady=390)
		self.pi_entry = tk.Scale(root, from_=1, to=100, resolution=1, orient=tk.HORIZONTAL)
		self.pi_entry.grid(row=0, column=2, sticky='nw', pady=370)

		tk.Label(root, text="Radius").grid(row=0, column=1, sticky='nw', pady=430)
		self.ra_entry = tk.Scale(root, from_=1, to=100, resolution=1, orient=tk.HORIZONTAL)
		self.ra_entry.grid(row=0, column=2, sticky='nw', pady=410)

		# Edge Width

		tk.Label(root, text="Edge Width").grid(row=0, column=1, sticky='nw', pady=350)
		self.ew_entry = tk.Scale(root, from_=0, to=5, resolution=0.5, orient=tk.HORIZONTAL)
		self.ew_entry.grid(row=0, column=2, sticky='nw', pady=330)

		self.ew_entry.set(1)

		# Face color
		tk.Label(root, text="Face Color").grid(row=0, column=1, sticky='nw', pady=30, padx=20)
		self.c_entry = tk.Listbox(root, exportselection=0, width=15)
		self.c_entry.insert(1, 'red')
		self.c_entry.insert(2, 'orange')
		self.c_entry.insert(3, 'yellow')
		self.c_entry.insert(4, 'green')
		self.c_entry.insert(5, 'blue')
		self.c_entry.insert(6, 'purple')
		self.c_entry.insert(7, 'gold')
		self.c_entry.insert(8, 'fuchsia')
		self.c_entry.insert(9, 'turquoise')
		self.c_entry.insert(10, 'silver')
		self.c_entry.insert(11, 'black')
		self.c_entry.insert(12, 'white')
		# c_entry.insert(13, colorset)
		self.c_entry.grid(row=0, column=1, sticky='n', pady=50)
		self.c_entry.select_set(9)

		self.c_scroll = tk.Scrollbar(root, orient=tk.VERTICAL, width=15)
		self.c_scroll.grid(row=0, column=1, sticky='ne', pady=52)
		self.c_scroll.config(command=self.c_entry.yview)

		self.c_entry.configure(yscrollcommand=self.c_scroll.set)

		# Edge Color
		tk.Label(root, text="Edge Color").grid(row=0, column=2, sticky='nw', pady=30, padx=20)
		self.ec_entry = tk.Listbox(root, exportselection=0, width=15)
		self.ec_entry.insert(1, 'red')
		self.ec_entry.insert(2, 'orange')
		self.ec_entry.insert(3, 'yellow')
		self.ec_entry.insert(4, 'green')
		self.ec_entry.insert(5, 'blue')
		self.ec_entry.insert(6, 'purple')
		self.ec_entry.insert(7, 'gold')
		self.ec_entry.insert(8, 'fuchsia')
		self.ec_entry.insert(9, 'turquoise')
		self.ec_entry.insert(10, 'silver')
		self.ec_entry.insert(11, 'black')
		self.ec_entry.insert(12, 'white')
		self.ec_entry.grid(row=0, column=2, sticky='nw', pady=50)
		self.ec_entry.select_set(6)

		self.ec_scroll = tk.Scrollbar(root, orient=tk.VERTICAL, width=15)
		self.ec_scroll.grid(row=0, column=2, sticky='ne', pady=52)
		self.ec_scroll.config(command=self.ec_entry.yview)

		self.ec_entry.configure(yscrollcommand=self.ec_scroll.set)

	def plot(self,canvas, ax):
		ax.clear()
		name = "Unk Surface"

		root.title("Geometric Models ({})".format(name))

		edge_c 		= self.ec_entry.get(self.ec_entry.curselection()[0])
		color 		= self.c_entry.get(self.c_entry.curselection()[0])
		#rot_azim 	= self.scroll_azim.get()
		#rot_elev 	= self.scroll_elev.get()
		#alpha 		= self.a_entry.get()
		grid 		= self.grid_axis.get()
		edge_w 		= self.ew_entry.get()
		zoom 		= self.axis_zoom.get()
		edges		= self.ed_entry.get()
		sides 		= self.si_entry.get()
		multi_pi	= self.pi_entry.get()
		zoom 		= self.axis_zoom.get()

		def x_(u, v):
			x = cos(u) * sin(v)
			return x

		def y_(u, v):
			y = sin(u) * sin(v)
			return y

		def z_(u, v):
			z = cos(v) + log1p(tan(2 + v) ** 2)
			return z

		u = linspace(0.001, 2 * pi, self.si_entry.get())
		v = linspace(0, 2 * pi, self.ed_entry.get())

		u, v = meshgrid(u, v)

		x = x_(u, v)
		y = y_(u, v)
		z = z_(u, v)

		#plt.xlim(-1 * self.axis_zoom.get(),self.axis_zoom.get())
		#plt.ylim(-1 * self.axis_zoom.get(), self.axis_zoom.get())
		#ax.set_zlim(-5, 5)

		plt.axis(self.grid_axis.get())
		# plt.xlim(-1 * zoom, zoom)
		# plt.ylim(-1 * zoom, zoom)
		# ax.set_zlim(-2, 2)

		interest = ax.plot_surface(x, y, z)

		interest.set_alpha(self.a_entry.get())
		interest.set_edgecolor(self.ec_entry.get(self.ec_entry.curselection()[0]))
		interest.set_linewidth(self.ew_entry.get())
		interest.set_facecolor(self.c_entry.get(self.c_entry.curselection()[0]))

		def init():
			return interest,

		def animate(i):
			#     # azimuth angle : 0 deg to 360 deg
			#     # elev = i * n --> rotates object about the xy-plane with a magnitude of n
			#     # azim = i * n --> rotates object around the z axis with a magnitude of n
			#     # For top view elev = 90
			#     # For side view elev = 0
			#
			ax.view_init(elev=self.scroll_elev.get(), azim=self.scroll_azim.get())
			return interest

		# Animate
		ani = FuncAnimation(self.fig, animate, init_func=init,
							interval=1, frames=500, blit=False, repeat=True)
		canvas.draw()	

	def test(self, canvas, ax):
		root.title("Geometric Models ({})".format(toru.name))

		ax.clear()
		edge_c 		= self.ec_entry.get(self.ec_entry.curselection()[0])
		color 		= self.c_entry.get(self.c_entry.curselection()[0])
		rot_azim 	= self.scroll_azim.get()
		rot_elev 	= self.scroll_elev.get()
		alpha 		= self.a_entry.get()
		grid 		= self.grid_axis.get()
		edge_w 		= self.ew_entry.get()
		zoom 		= self.axis_zoom.get()
		edges		= self.ed_entry.get()
		sides 		= self.si_entry.get()
		multi_pi	= self.pi_entry.get()
		zoom 		= self.axis_zoom.get()
		radius		= self.ra_entry.get()

		toru.shape(self.fig, alpha, color, edge_c, edge_w, grid, sides,
				   edges, multi_pi, zoom, rot_elev, rot_azim, radius)
		canvas.draw()

img = ImageTk.PhotoImage(file='penrose_icon.png')
root.tk.call('wm', 'iconphoto', root._w, img)

root.update()
root.update_idletasks()

geo = Geometry(master=root)
geo.mainloop()
