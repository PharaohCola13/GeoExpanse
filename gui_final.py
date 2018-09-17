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
#import ttk            # python 2.7
#import sys
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
import prism 			 	 as pris
import pyramid				 as pyra
import sphere				 as sphe 

# Hyperbolic
import hyperbolic_octahedron as hyoc
import hyperbolic_paraboloid as hypa
import one_sheet_hyperboloid as oshy

# Misc.
import three_dodecahedron	 as tdod
import cressant				 as cres
import funnel				 as funn
import gabriel_horn			 as horn
import rose_spiral			 as rose
import shell				 as shel
import tesseract			 as tess

# Surfaces
#import boys_surface			 as boys
#import breather_surface		 as brea
#import kuen_surface			 as kuen
#import steiner_surface		 as stei

# Platonic Surfaces
import cube					 as cube 
import dodecahedron			 as dode
import icosahedron			 as icos
import octahedron			 as octa

# Topological
#import cross_cap			 as cros
#import klein				 as klei
#import mobius				 as mobi
#import torus				 as toru

## In Development
import interesting			 as rile
import polyhedron			 as poly
#import hyperbolic_cylinder	 as hycl
#import dini_surface			 as disu
#import knot					 as knot
#import neat					 as neat
#import spiral				 as spir
#import testing				 as test
#import vase					 as vase


root = tk.Tk()

fig = plt.figure(figsize=(8,8))

#root.geometry("1050x965")
# Vars

grid_axis = tk.StringVar()

shape = tk.StringVar()
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


si_entry_label 	= tk.Label(root, text="Sides").grid(row=0, column=1, sticky='nw', pady=465)
si_entry 		= tk.Scale(root, from_=1, to=1000, resolution=1, orient=tk.HORIZONTAL)
si_entry.grid(row=0, column=2, sticky='nw', pady=450)


# Shape name

#shape_name_label 	= tk.Label(root, text="Shape").grid(row=0, column=1, sticky='nw', pady=465)
#shape_name 		= tk.Entry(root, textvariable=shape, width=10)
#shape_name.grid(row=0, column=2, sticky='nw', pady=450)
#

#shapeobj = shape_name.get()

# Edge Width

ew_entry_label 	= tk.Label(root, text="Edge Width").grid(row=0, column=1, sticky='nw', pady=350)
ew_entry       	= tk.Scale(root, from_=0, to=5, resolution=0.5, orient=tk.HORIZONTAL)
ew_entry.grid(row=0, column=2, sticky='nw', pady=335)

# Face color

c_entry_label 	= tk.Label(root, text="Face Color").grid(row=0, column=1, sticky='nw', pady=30, padx=20)

c_entry = tk.Listbox(root, exportselection=0, width=15) 
c_entry.insert(1, 'red')
c_entry.insert(2, 'orange')
c_entry.insert(3, 'yellow')
c_entry.insert(4, 'green')
c_entry.insert(5, 'blue')
c_entry.insert(6, 'purple')
c_entry.insert(7, 'gold')
c_entry.insert(8, 'fuchsia')
c_entry.insert(9, 'turquoise')
c_entry.insert(10, 'silver')
c_entry.insert(11, 'black')
c_entry.insert(12, 'white')
#c_entry.insert(13, colorset)

c_entry.grid(row=0, column=1, sticky='n', pady=50)

# Edge Color

tk.Label(root, text="Edge Color").grid(row=0, column=2, sticky='nw', pady=30, padx=20)
ec_entry = tk.Listbox(root, exportselection=0, width=15)
ec_entry.insert(1, 'red')
ec_entry.insert(2, 'orange')
ec_entry.insert(3, 'yellow')
ec_entry.insert(4, 'green')
ec_entry.insert(5, 'blue')
ec_entry.insert(6, 'purple')
ec_entry.insert(7, 'gold')
ec_entry.insert(8, 'fuchsia')
ec_entry.insert(9, 'turquoise')
ec_entry.insert(10, 'silver')
ec_entry.insert(11, 'black')
ec_entry.insert(12, 'white')
ec_entry.grid(row=0, column=2, sticky='nw', pady=50)

tk.Button(root, text="Quit", command=quit).grid(row=5, column=1, rowspan=2, columnspan=2, sticky='nsew')

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

		self.plotbutton=tk.Button(root, text="Render", command=lambda: self.test(canvas,ax))
		self.plotbutton.grid(row=3, column=1, rowspan=2, columnspan=2, sticky="nsew")

	def plot(self,canvas,ax):	
		global fig, scroll_azim, scroll_elev, c_entry, ec_entry, ew_entry, a_entry, grid_axis
		
		ax.clear()
		name 		= "Unknown Object"	
		root.title("Geometric Models ({})".format(name))	
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
		global fig, scroll_azim, scroll_elev, c_entry, ec_entry, a_entry, grid_axis, si_entry

		#ax.clear()
		edge_c 		= ec_entry.get(ec_entry.curselection()[0]) 
		color 		= c_entry.get(c_entry.curselection()[0])
		rot_azim 	= scroll_azim.get()
		rot_elev 	= scroll_elev.get()
		alpha		= a_entry.get()
		grid 		= grid_axis.get()
		edge_w		= ew_entry.get()
		sides		= si_entry.get()
		
		sphe.shape(fig, alpha, color, edge_c, edge_w, rot_elev, rot_azim, grid, sides)

	#	def animate(i):
	#     # azimuth angle : 0 deg to 360 deg
	#     # elev = i * n --> rotates object about the xy-plane with a magnitude of n
	#     # azim = i * n --> rotates object around the z axis with a magnitude of n
	#     # For top view elev = 90
	#     # For side view elev = 0
	#
	#		ax.view_init(elev=(rot_elev * i), azim=(rot_azim * i))

	#	ani = FuncAnimation(fig, animate,
	#	   	 frames=1000000, interval=1000, blit=False, repeat=True)
		#root.title("Geometric Models ({})".format(name))
		canvas.draw()


geo=Geometry(master=root)
geo.mainloop()