## General Information

__author__ = "Spencer Riley"
__title__  = "GeoExpanse"

__platform__= "None (Development)"

## Imports
import matplotlib
matplotlib.use('tkagg')
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import mpl_toolkits.mplot3d.axes3d as p3
from matplotlib.animation import *
#from PIL import ImageTk
from PIL import Image
import sys
from time import sleep

try:
	import tkinter as tk
	from tkinter.colorchooser import askcolor
except ImportError:
	import Tkinter as tk
	from tkColorChooser import askcolor

sys.path.append('../In Development/')

sys.path.append('../Current Models/')
sys.path.append('../Current Models/Hyperbolic/')
sys.path.append('../Current Models/Misc./')
sys.path.append('../Current Models/Platonic Solids/')
sys.path.append('../Current Models/Surfaces/')
sys.path.append('../Current Models/Topological/')
sys.path.append('../Current Models/Two Space/')
sys.path.append('../Current Models/Archimedean/')

import prism, pyramid, sphere, billion, general_3d,hyperbolic_octahedron, hyperbolic_paraboloid, one_sheet_hyperboloid,\
	hyperbolic_helicoid, hyperbolic_cylinder, three_dodecahedron, crescent, funnel, gabriel_horn, rose_spiral, shell, \
	tesseract, spiral, seashell, steinbach_screw, breather_surface, kuen_surface, steiner_surface, boys_surface, \
	roman_surface, sine_surface, henneberg_surface, unk_surface, dini_surface, enneper_surface, corkscrew_surface, \
	shoe_surface, cube, dodecahedron, icosahedron, octahedron, tetrahemihexahedron, truncated_tetrahedron, cross_cap, \
	klein, mobius, torus, neat, testing, vase, something_strange, great_dodecahedron, great_stellated_dodecahedron, \
	cuboctahedron, great_rombicosidodecahedron, snub_cube, truncated_cube, disdyakis_triacontahedron, great_icosahedron,\
	small_stellated_dodecahedron, isohedral_toroid, knotted_dodecahedron, klein_map, deltoid, log_spiral, parabola, \
	penrose_square, penrose_circle, line, penrose_triangle, polygon, ellipse, fermat_sprial, borromean_rings, \
	truncated_cuboctahedron, truncated_dodecahedron, truncated_icosahedron, truncated_octahedron, snub_dodecahedron,\
	icosidodecahedron, poweroid, hyperbolic_tetrahedron

## Geometry Dictionary
s = {	 "Prism"					: prism,
		 "Pyramid"					: pyramid,
		 "Sphere"					: sphere,
		 "Hyperbolic Octahedron"	: hyperbolic_octahedron,
		 "Hyperbolic Paraboloid"	: hyperbolic_paraboloid,
		 "One Sheet Hyperboloid"	: one_sheet_hyperboloid,
		 "Hyperbolic Cylinder"		: hyperbolic_cylinder,
		 "Hyperbolic Helicoid"		: hyperbolic_helicoid,
		 "Three Dodecahedron"		: three_dodecahedron,
		 "Crescent"					: crescent,
		 "Funnel"					: funnel,
		 "Gabriel's Horn"			: gabriel_horn,
		 "Rose Spiral"				: rose_spiral,
		 "Shell"					: shell,
		 "Tesseract"				: tesseract,
		 "Spiral"					: spiral,
		 "Seashell"					: seashell,
		 "Steinbach Screw"			: steinbach_screw,
		 "Breather's Surface"		: breather_surface,
		 "Kuen Surface"				: kuen_surface,
		 "Steiner's Surface"		: steiner_surface,
		 "Boy's Surface"			: boys_surface,
		 "Roman Surface"			: roman_surface,
		 "Sine Surface"				: sine_surface,
		 "Henneberg's Surface"		: henneberg_surface,
		 "Dini's Surface"			: dini_surface,
		 "Enneper's Surface"		: enneper_surface,
		 "Corkscrew Surface"		: corkscrew_surface,
		 "Shoe Surface"				: shoe_surface,
		 "Unk Surface"				: unk_surface,
		 "Cube"						: cube,
		 "Dodecahedron"				: dodecahedron,
		 "Icosahedron"				: icosahedron,
		 "Octahedron"				: octahedron,
		 "Cross Cap"				: cross_cap,
		 "Klein Bottle"				: klein,
		 "Mobius Strip"				: mobius,
		 "Torus"					: torus,
		 #"Neat"						: neat,
		 #"Great Dodecahedron"		: great_dodecahedron,
		 "Vase"						: vase,
		 #"Something Strange"		: something_strange,
		 "Cuboctahedron"			: cuboctahedron,
		 "Disdyakis Triacontahedron": disdyakis_triacontahedron,
		 "Great Rombicosidodecahedron": great_rombicosidodecahedron,
		 "Snub Cube"				: snub_cube,
		 "Truncated Cube"			: truncated_cube,
		 "Great Icosahedron"		: great_icosahedron,
		 "Line"						: line,
		 "Deltoid"					: deltoid,
		 "Log Spiral"				: log_spiral,
		 "Parabola"					: parabola,
		 "Penrose Circle"			: penrose_circle,
		 "Penrose Square"			: penrose_square,
		 "Penrose Triangle"			: penrose_triangle,
		 "Polygons"				 	: polygon,
		 "Ellipse"					: ellipse,
		 "Fermat Spiral"			: fermat_sprial,
		  ""						: testing,
		 # "General"					: general_3d,
		 "Small Stellated Dodecahedron" : small_stellated_dodecahedron,
		 "Great Stellated Dodecahedron" : great_stellated_dodecahedron,
		 "Tetrahemihexahedron"		: tetrahemihexahedron,
		 "Truncated Tetrahedron"	: truncated_tetrahedron,
		 #"Geodesic Icosahedron Pattern 222": billion,
		 "Isohedral Toroid"			: isohedral_toroid,
 		 "Knotted Dodecahedron"		: knotted_dodecahedron,
		 "Klein Map"				: klein_map,
		 "Borromean Rings"			: borromean_rings,
		 "Snub Dodecahedron"		: snub_dodecahedron,
		 "Truncated Icosahedron"	: truncated_icosahedron,
		 "Truncated Octahedron"		: truncated_octahedron,
		 "Truncated Cuboctahedron"	: truncated_cuboctahedron,
		 "Truncated Dodecahedron"	: truncated_dodecahedron,
		 "Icosidodecahedron"		: icosidodecahedron,
		 "Poweroid"					: poweroid,
		 "Hyperbolic Tetrahedron"	: hyperbolic_tetrahedron,
}

gen 	= ["Prism", "Pyramid", "Sphere"]
hyper	= ["Hyperbolic Octahedron", "Hyperbolic Paraboloid", "One Sheet Hyperboloid", "Hyperbolic Cylinder",
			"Hyperbolic Helicoid", "Hyperbolic Tetrahedron"]
misc 	= ["Three Dodecahedron", "Crescent", "Funnel", "Gabriel's Horn",
		   "Rose Spiral", "Shell", "Tesseract", "Spiral", "Seashell", "Steinbach Screw",
		   "Isohedral Toroid", "Knotted Dodecahedron", "Klein Map", "Borromean Rings", "Vase"]
surf 	= ["Breather's Surface", "Kuen Surface", "Steiner's Surface", "Boy's Surface",
		   "Roman Surface", "Sine Surface", "Henneberg's Surface", "Dini's Surface",
		   "Enneper's Surface", "Corkscrew Surface", "Shoe Surface", "Unk Surface", "Poweroid"]
topo 	= ["Cross Cap", "Klein Bottle", "Mobius Strip", "Torus"]
#deve 	= ["Neat", "", "Great Dodecahedron", "Vase", "Something Strange",  "Geodesic Icosahedron Pattern 222",  "General"]
arch 	= ["Cuboctahedron", "Disdyakis Triacontahedron", "Great Rombicosidodecahedron",
		   "Snub Cube", "Truncated Cube", "Tetrahemihexahedron", "Truncated Tetrahedron", "Snub Dodecahedron", "Truncated Icosahedron",
		   "Truncated Octahedron", "Truncated Cuboctahedron", "Truncated Dodecahedron", "Icosidodecahedron"]
plat    = ["Cube", "Dodecahedron", "Octahedron", "Icosahedron"]
two 	= ["Line", "Deltoid", "Log Spiral", "Parabola", "Polygons", "Ellipse", "Fermat Spiral"]
pen		= ["Penrose Circle", "Penrose Triangle", "Penrose Square"]
kepl	= ["Great Icosahedron","Great Dodecahedron", "Small Stellated Dodecahedron", "Great Stellated Dodecahedron"]
dim = "#303030"  #   Background
dimf = "#00C0FF"  #   Font Color
disa = "#d400ff" #   Disabled Text

day = '#c6dcff'
dayf = '#008721'
days = '#e500ff'


root_width = 920
root_height = 530
## Start of Application
class Geometry(tk.Frame):
	def __init__(self, master):
		tk.Frame.__init__(self ,master)
		self.createWidgets(master)

	def createWidgets(self, master):

## Vars
		self.grid_axis 		= tk.StringVar()
		self.axis_limits 	= tk.StringVar()
		self.scroll			= tk.DoubleVar()
		self.shape_set 		= tk.StringVar()
		self.alpha 			= tk.StringVar()
		self.two_three 		= tk.StringVar()
		self.rotation 		= tk.StringVar()
		self.format_save 	= tk.StringVar()
		self.figcolor		= tk.StringVar()
		self.size			= tk.StringVar()

		self.rotation.set("Off")


## Fig Props
		self.fig = plt.figure(figsize=(5, 5), facecolor='black', edgecolor="white")
		ax = p3.Axes3D(self.fig)
		ax.set_facecolor('black')
		plt.axis("off")

		canvas = FigureCanvasTkAgg(self.fig ,master)
		canvas.get_tk_widget().grid(row=0 ,column=0, sticky='new')
		master.update_idletasks()
		canvas.draw()

## Functions
		def axi():
			plt.axis(str(self.grid_axis.get()))
			plt.xlabel("X-Axis", color="white")
			plt.ylabel("Y-Axis", color="white")
			ax.set_zlabel("Z-Axis", color="white")
			plt.xticks(color="white")
			plt.yticks(color="white")
	#	#
		def space():
			plt.figure(1)
			plt.gca()
#			ax.set_facecolor(self.figcolor)
			plt.axis('on')
	#

		initcolor 	= []
		initcolor2 	= []
		initcolor3	= []
		initcolore	= []

		initcolor.append("#00acff")
		initcolor2.append("#000000")
		initcolor3.append("#000000")
		initcolore.append("#ffffff")


		def FaceColor(self):
			for i in initcolor:
				self.c_entry = askcolor(initialcolor=i, title="Face Color")
				if len(initcolor) < 2:
					initcolor[:] = []
					initcolor.append(self.c_entry[1])
					break
			self.fck.config(bg=self.c_entry[1], width=200000000)
			return self.c_entry[1]

		#	#
		def FaceColor2(self):
			for i in initcolor2:
				self.c_entry2 = askcolor(initialcolor=i, title="Secondary Face Color")
				if len(initcolor2) < 2:
					initcolor2[:] = []
					initcolor2.append(self.c_entry2[1])
					break
			self.f2.config(bg=self.c_entry2[1], width=200000000)
			return self.c_entry2[1]

		#	#
		def FaceColor3(self):
			for i in initcolor3:
				self.c_entry3 = askcolor(initialcolor=i, title="Tertiary Face Color")
				if len(initcolor3) < 2:
					initcolor3[:] = []
					initcolor3.append(self.c_entry3[1])
					break
			self.f3.config(bg=self.c_entry3[1], width=200000000)
			return self.c_entry3[1]

		#	#
		def EdgeColor(self):
			for i in initcolore:
				self.ec_entry = askcolor(initialcolor=i, title="Edge Color")
				if len(initcolore) < 2:
					initcolore[:] = []
					initcolore.append(self.ec_entry[1])
					break
			self.eck.config(bg=self.ec_entry[1], width=200000000)
			return self.ec_entry[1]

## Popups
	#	#
		def popup_save():
			top = tk.Toplevel(self)
			top.title("Save Figure")

			top.tk.call('wm', 'iconphoto', top._w, icon)
			top.config(background=dim)
			#top_width = 337
			#top_height = 83
			#top.geometry(str(top_width) + "x" + str(top_height))
			#top.maxsize(str(top_width), str(top_height))
			#top.minsize(str(top_width), str(top_height))
			self.format_save = tk.StringVar()

			def pop():
				top.destroy()
				self.format_save.set(None)
				self.plot(canvas, ax, s[self.shape_set.get()])

			wid = ["PNG", "JPG", "SVG", "EPS", "MP4"]

			pop = tk.Button(top, text="POP!", command=pop)
			pop.grid(row=0, column=0, columnspan=1, sticky='nsew')
			pop.config(bg=dim, fg=dimf, activebackground=dim, highlightbackground=dimf, activeforeground=dimf)

			for n in range(0,5):
				tk.Radiobutton(top, text=str(wid[n]), variable=self.format_save, value=str(wid[n]), width=5, bg=dim,
							   fg=dimf, activebackground=dim, highlightthickness=0, activeforeground=dimf,
							   selectcolor=dim).grid(row=n+1, column=0, sticky='nw')


			save_img = tk.Button(top, text="Save (Opaque)", width=15)
			save_img.grid(row=0, column=2, rowspan=2, sticky='nsew')
			save_img.config(bg=dim, fg=dimf, activebackground=dim, highlightbackground=dimf, activeforeground=dimf,
							command=lambda: plt.savefig("{}.{}".format(str(s[self.shape_set.get()].name), str(self.format_save.get())),
								transparent=False))

			save_img1 = tk.Button(top, text="Save (Transparent)", width=15)
			save_img1.grid(row=2, column=2, rowspan=2, sticky='nsew')
			save_img1.config(bg=dim, fg=dimf, activebackground=dim, highlightbackground=dimf, activeforeground=dimf,
							 command=lambda: plt.savefig("{}.{}".format(str(s[self.shape_set.get()].name), str(self.format_save.get())),
								 transparent=True))

			save_vid = tk.Button(top, text="Save Video", width=15, command=lambda: self.plot(canvas, ax, s[self.shape_set.get()]))
			save_vid.grid(row=4, column=2, rowspan=2, sticky='nsew')
			save_vid.config(bg=dim, fg=dimf, activebackground=dim, highlightbackground=dimf, activeforeground=dimf)
	#	#	
		def popup_about():
			top = tk.Toplevel(self)
			top.title("About")
			top.tk.call('wm', 'iconphoto', top._w, icon)

			top_width = 220
			top_height = 175
			top.geometry(str(top_width) + "x" + str(top_height))
			top.maxsize(str(top_width), str(top_height))
			top.minsize(str(top_width), str(top_height))
			top.config(background=dim)

			pop = tk.Button(top, text="POP!", command=top.destroy)
			pop.grid(row=0, column=0, sticky='new')
			pop.config(bg=dim, fg=dimf, activebackground=dim, highlightbackground=dimf, activeforeground=dimf)

			about = tk.Message(top, text="This software was developed by Spencer Alexander Riley, a undergraduate Physics major and Math minor at New Mexico Tech.\n"
															"--------------------------------------------------\n"
															"This is an open-source educational application to allow students or interested parties to examine and study a great variety of geometric structures.")
			about.grid(row=1, column=0, rowspan=3, columnspan=1)
			about.config(bg=dim, fg=dimf)
	#	#
		def popup_shape():
			self.rotation.set("Off")
			self.format_save.set(None)
			top = tk.Toplevel(self)
			top.tk.call('wm', 'iconphoto', top._w, icon)
			top.focus_set()
			top.grab_set()

			top.title("Shapes")
			top.config(background=dim)

			pop = tk.Button(top, text="POP!", command=top.destroy)
			pop.grid(row=0, column=0, sticky='new')
			pop.config(bg=dim,fg=dimf, activebackground=dim, highlightbackground=dimf, activeforeground=dimf)

			plotter = tk.Button(top, text="Plot", command=lambda: self.plot(canvas, ax, s[self.shape_set.get()]))
			plotter.grid(row=0, column=1, sticky="new")
			plotter.config(bg=dim,fg=dimf, activebackground=dim, highlightbackground=dimf, activeforeground=dimf)

			if self.two_three.get() == "3d":
				self.shape_set.set("Unk Surface")
				##
				for n in range(len(gen)):
					tk.Radiobutton(top, text= gen[n], variable=self.shape_set, value= gen[n], bg=dim, fg=dimf, activebackground=dim, highlightthickness=0, activeforeground=dimf,selectcolor=dim)\
						.grid(row=n+1, column=0, sticky='w')
				##
				platonic = tk.Label(top, text="--- Platonic Solids ---", font=('Times', 12, 'bold'), bg=dim, fg=dimf, activebackground=dim)\
					.grid(row=4, column=0, sticky='nsew')
				for n in range(len(plat)):
					tk.Radiobutton(top, text=plat[n], variable=self.shape_set, value= plat[n], bg=dim, fg=dimf, activebackground=dim, highlightthickness=0, activeforeground=dimf,selectcolor=dim)\
						.grid(row=n+5, column=0, sticky='w')

				##
				topological = tk.Label(top, text="--- Topological ---", font=('Times', 12, 'bold'), bg=dim, fg=dimf, activebackground=dim)\
					.grid(row=9, column=0, sticky='nsew')
				for n in range(len(topo)):
					tk.Radiobutton(top, text= topo[n], variable=self.shape_set, value= topo[n], bg=dim, fg=dimf, activebackground=dim, highlightthickness=0, activeforeground=dimf,selectcolor=dim)\
						.grid(row=n+10, column=0, sticky='w')

				##
				hyperbolic = tk.Label(top, text="--- Hyperbolic Objects ---", font=('Times', 12, 'bold'), bg=dim, fg=dimf, activebackground=dim)\
					.grid(row=1, column=1, sticky="nsew")

				for n in range(len( hyper)):
					tk.Radiobutton(top, text= hyper[n], variable=self.shape_set, value= hyper[n], bg=dim, fg=dimf, activebackground=dim, highlightthickness=0, activeforeground=dimf,selectcolor=dim)\
						.grid(row=n+2, column=1, sticky='w')

				##
				miscellaneous = tk.Label(top, text="--- Miscellaneous ---", font=('Times', 12, 'bold'), bg=dim, fg=dimf, activebackground=dim)\
					.grid(row=1, column=2, sticky='nsew')

				for n in range(len( misc)):
					tk.Radiobutton(top, text= misc[n], variable=self.shape_set, value= misc[n], bg=dim, fg=dimf, activebackground=dim, highlightthickness=0, activeforeground=dimf,selectcolor=dim)\
						.grid(row=n+2, column=2, sticky='w')

				##
				surface = tk.Label(top, text="--- Surfaces ---", font=('Times', 12, 'bold'), bg=dim, fg=dimf, activebackground=dim)\
					.grid(row=1, column=3, sticky='new')
				for n in range(len( surf)):
					tk.Radiobutton(top, text= surf[n], variable=self.shape_set, value= surf[n], bg=dim, fg=dimf, activebackground=dim, highlightthickness=0, activeforeground=dimf,selectcolor=dim)\
						.grid(row=n+2, column=3, sticky='w')

				##
				kepler = tk.Label(top, text="--- Kepler-Poinsot Solids ---", font=('Times', 12, 'bold'), bg=dim, fg=dimf, activebackground=dim)\
					.grid(row=1, column=4, sticky='nsew')
				for n in range(len( kepl)):
					tk.Radiobutton(top, text= kepl[n], variable=self.shape_set, value= kepl[n], bg=dim, fg=dimf, activebackground=dim, highlightthickness=0, activeforeground=dimf,selectcolor=dim)\
						.grid(row=n+2, column=4, sticky='w')


				##
				archimedean = tk.Label(top, text="--- Archimedean Solids ---", font=('Times', 12, 'bold'), bg=dim, fg=dimf, activebackground=dim)\
					.grid(row=6, column=4, sticky='nsew')
				for n in range(len( arch)):
					tk.Radiobutton(top, text= arch[n], variable=self.shape_set, value= arch[n], bg=dim, fg=dimf, activebackground=dim, highlightthickness=0, activeforeground=dimf,selectcolor=dim)\
						.grid(row=n+7, column=4, sticky='w')

			##
			elif self.two_three.get() == "2d":
				self.shape_set.set("Penrose Circle")
				for n in range(len( two)):
					tk.Radiobutton(top, text= two[n], variable=self.shape_set, value= two[n], bg=dim, fg=dimf, activebackground=dim, highlightthickness=0, activeforeground=dimf,selectcolor=dim)\
						.grid(row=n+1, column=0, sticky='w')

				penrose = tk.Label(top, text="--- Penrose Projections ---", font=('Times', 12, 'bold'), bg=dim, fg=dimf, activebackground=dim)\
					.grid(row=1, column=2, sticky='nsew')
				for n in range(len( pen)):
					tk.Radiobutton(top, text= pen[n], variable=self.shape_set, value= pen[n], bg=dim, fg=dimf, activebackground=dim, highlightthickness=0, activeforeground=dimf,selectcolor=dim)\
						.grid(row=n+2, column=2, sticky='w')
		#
## Menus	
	#	#
		menu = tk.Menu(master)
		master.config(menu=menu)

		filemenu = tk.Menu(menu)
		menu.add_cascade(label="File", menu=filemenu)

		figmenu = tk.Menu(menu)
		menu.add_cascade(label='Configure', menu=figmenu)

		filemenu.add_command(label="Save", command=popup_save)
		filemenu.add_separator()
		filemenu.add_command(label="About", command=popup_about)
		filemenu.add_command(label="Quit <Esc>", command=master.destroy)
		
		figmenu.add_radiobutton(label="Figure",variable=self.size, value="Figure", command=lambda:master.geometry(str(500) + "x" + str(500)), selectcolor=dimf)
		figmenu.add_radiobutton(label="Full", variable= self.size, value="All", command=lambda: master.geometry(str(root_width) + "x" + str(root_height)), selectcolor=dimf)
		self.size.set("All")

		figmenu.add_radiobutton(label="Dark", value='#000000', selectcolor=dimf, variable=self.figcolor)

		figmenu.add_radiobutton(label="Light", value='#ffffff', selectcolor=dimf, variable=self.figcolor)
		# For website display
		#self.figcolor.set('#252525')
		self.figcolor.set('#000000')

		figmenu.add_radiobutton(label="Rotation On", variable=self.rotation, value="On", selectcolor=dimf)
		figmenu.add_radiobutton(label="Rotation Off", variable=self.rotation, value="Off", selectcolor=dimf)

## Widgets
	# 	# Transparency
		self.a_label = tk.Label(master, text="Transparency")
		self.a_label.grid(row=0, column=1, sticky='new', pady=110)
		self.a_entry = tk.Scale(master, from_=0, to=1, resolution=0.1, orient=tk.HORIZONTAL)
		self.a_entry.grid(row=0, column=2, sticky='new', pady=90)
		self.a_entry.set(0.4)
	
	# 	# Height
		self.h_label = tk.Label(master, text="Height")
		self.h_label.grid(row=0, column=3, sticky='new', pady=110, padx=10)
		self.h_entry = tk.Scale(master, from_=1, to=50, resolution=1, orient=tk.HORIZONTAL)
		self.h_entry.grid(row=0, column=4, sticky='new', pady=90)
		self.h_entry.set(1)
	
	# 	# Entry of the number of sides
		self.si_label = tk.Label(master, text="Number of Sides")
		self.si_label.grid(row=0, column=1, sticky='new', pady=150)
		self.si_entry = tk.Scale(master, from_=1, to=100, resolution=1, orient=tk.HORIZONTAL)
		self.si_entry.grid(row=0, column=2, sticky='new', pady=130)
		self.si_entry.set(20)
	
	# 	# Entry of the number of edges
		self.ed_label = tk.Label(master, text="Number of Edges")
		self.ed_label.grid(row=0, column=1, sticky='new', pady=190)
		self.ed_entry = tk.Scale(master, from_=1, to=100, resolution=1, orient=tk.HORIZONTAL)
		self.ed_entry.grid(row=0, column=2, sticky='new', pady=170)
		self.ed_entry.set(2)

	# 	# Multiple of Pi
		self.pi_label = tk.Label(master, text=r"Multiple of " u'\u03C0' + " ("u'\u03C6'")")
		self.pi_label.grid(row=0, column=1, sticky='new', pady=270)
		self.pi_entry = tk.Scale(master, from_=1, to=100, resolution=1, orient=tk.HORIZONTAL)
		self.pi_entry.grid(row=0, column=2, sticky='new', pady=250)
		self.pi_entry.set(2)

	# 	# Multiple of Pi
		self.pi_label2 = tk.Label(master, text=r"Multiple of " u'\u03C0' + " ("u'\u03B8'")")
		self.pi_label2.grid(row=0, column=3, sticky='new', pady=270)
		self.pi_entry2 = tk.Scale(master, from_=1, to=100, resolution=1, orient=tk.HORIZONTAL)
		self.pi_entry2.grid(row=0, column=4, sticky='new', pady=250)
		self.pi_entry2.set(2)
	
	# 	# Edge Width
		self.ew_label = tk.Label(master, text="Edge Width")
		self.ew_label.grid(row=0, column=1, sticky='new', pady=230)
		self.ew_entry = tk.Scale(master, from_=0, to=10, resolution=0.5, orient=tk.HORIZONTAL)
		self.ew_entry.grid(row=0, column=2, sticky='new', pady=210)
		self.ew_entry.set(1)
	
	# 	# Radius
		self.ram_label = tk.Label(master, text="Radius (Main)")
		self.ram_label.grid(row=0, column=3, sticky='new', pady=150, padx=10)
		self.ram_entry = tk.Scale(master, from_=1, to=50, resolution=1, orient=tk.HORIZONTAL)
		self.ram_entry.grid(row=0, column=4, sticky='new', pady=130)
	
	# 	# Radius
		self.raa_label = tk.Label(master, text="Radius (Alt)")
		self.raa_label.grid(row=0, column=3, sticky='new', pady=190, padx=10)
		self.raa_entry = tk.Scale(master, from_=1, to=50, resolution=1, orient=tk.HORIZONTAL)
		self.raa_entry.grid(row=0, column=4, sticky='new', pady=170)

	#	# Edge Color
		self.edge = tk.Button(master, text="Edge Color", command=lambda: EdgeColor(self), state=tk.NORMAL)
		self.edge.grid(row=0, column=1, sticky='new', pady=30, padx=0)

		self.eck = tk.Message(master,borderwidth=5, relief=tk.GROOVE)
		self.eck.grid(row=0, column=1, sticky='new', pady=60)

	#	# Face Color
		self.face = tk.Button(master, text="Face Color", command=lambda: FaceColor(self), state=tk.NORMAL)
		self.face.grid(row=0, column=2, sticky='new', pady=30, padx=0)
		
		self.fck = tk.Message(master, borderwidth=5, relief=tk.GROOVE)
		self.fck.grid(row=0, column=2, sticky='new', pady=60, padx=0)
#	# Edge Color
		self.face2 = tk.Button(master, text="Face Color 2", command=lambda: FaceColor2(self), state=tk.NORMAL)
		self.face2.grid(row=0, column=3, sticky='new', pady=30, padx=0)

		self.f2 = tk.Message(master,borderwidth=5, relief=tk.GROOVE)
		self.f2.grid(row=0, column=3, sticky='new', pady=60, padx=0)

	#	# Face Color
		self.face3 = tk.Button(master, text="Face Color 3", command=lambda: FaceColor3(self), state=tk.NORMAL)
		self.face3.grid(row=0, column=4, sticky='new', pady=30, padx=0)

		self.f3 = tk.Message(master, borderwidth=5, relief=tk.GROOVE)
		self.f3.grid(row=0, column=4, sticky='new', pady=60, padx=0)

	#	# Plotting,
		self.plotting = tk.Button(master, text="Update", command=lambda: self.plot(canvas, ax, s[self.shape_set.get()]), height=4)
		self.plotting.grid(row=0, column=1, columnspan=2, sticky="new", pady=430)# pady=730)

	# 	# Grid Functions (on/off)
		self.grid_on = tk.Radiobutton(master, text="Grid On", variable=self.grid_axis, value='on', command=axi)
		self.grid_on.grid(row=0, column=1, sticky='new')

		self.grid_off = tk.Radiobutton(master, text='Grid Off', variable=self.grid_axis, value='off', command=axi)
		self.grid_off.grid(row=0, column=2, sticky='new')
		self.grid_axis.set('off')
	
	# 	# 2D or 3D
		self.two_space = tk.Radiobutton(master, text="2D Objects", variable=self.two_three, value='2d', command=space)
		self.two_space.grid(row=0, column=3, sticky='new')

		self.three_space = tk.Radiobutton(master, text="3D Objects", variable=self.two_three, value='3d', command=space)
		self.three_space.grid(row=0, column=4, sticky='new')
		self.two_three.set('3d')


		self.romt_label = tk.Label(master, text="Rotation\n Magnitude"+ " ("u'\u03B8'")")
		self.romt_label.grid(row=0, column=1, sticky='new', pady=301, padx=0)
		self.romt_entry = tk.Scale(master, from_=0, to=10, resolution=1, orient=tk.HORIZONTAL)
		self.romt_entry.grid(row=0, column=2, sticky='new', pady=300)


		self.romp_label = tk.Label(master, text="Rotation\n Magnitude" + " ("u'\u03C6'")")
		self.romp_label.grid(row=0, column=3, sticky='new', pady=301, padx=0)
		self.romp_entry = tk.Scale(master, from_=0, to=10, resolution=1, orient=tk.HORIZONTAL)
		self.romp_entry.grid(row=0, column=4, sticky='new', pady=300)

# self.x_label = tk.Label(master, text="X = ")
		# self.x_label.grid(row=0, column=1, sticky='new', pady=301)
		# self.x_entry = tk.Entry(master, text="X = ", width=2, textvariable=self.x)
		# self.x_entry.grid(row=0, column=2, sticky='new', pady=300)
		# self.x.set("u**2")
		#
		# self.y_label = tk.Label(master, text="Y = ")
		# self.y_label.grid(row=0, column=1, sticky='new', pady=326)
		# self.y_entry = tk.Entry(master, text="Y = ", width=2, textvariable=self.y)
		# self.y_entry.grid(row=0, column=2, sticky='new', pady=325)
		# self.y.set("v**2")
		#
		# self.z_label = tk.Label(master, text="Z = ")
		# self.z_label.grid(row=0, column=1, sticky='new', pady=351)
		# self.z_entry = tk.Entry(master, text="Z = ", width=2, textvariable=self.z)
		# self.z_entry.grid(row=0, column=2, sticky='new', pady=350)
		#

# 	# Shape Popup
		self.shapes = tk.Button(master, text="Shapes", command=popup_shape, height=4)
		self.shapes.grid(row=0, column=3, columnspan=2, sticky='new', pady=430)#pady=730)


		self.scales = [self.a_entry, self.h_entry, self.si_entry, self.ed_entry, self.pi_entry, self.ew_entry,
				  self.ram_entry, self.raa_entry, self.pi_entry2, self.romt_entry, self.romp_entry]

		self.labels = [self.a_label, self.h_label, self.si_label, self.ed_label, self.pi_label, self.ew_label,
				  self.ram_label, self.raa_label, self.pi_label2, self.romt_label, self.romp_label]

		self.radio = [self.grid_on, self.grid_off, self.two_space, self.three_space]

		self.button = [self.plotting, self.face, self.face2, self.face3, self.edge, self.shapes]

		self.menus = [menu, filemenu, figmenu]


		def dark(self):
			master.config(background=dim)
			for m in self.scales:
				m.config(bg=dim, fg=dimf, activebackground=dim, highlightthickness=0, troughcolor=dimf)
			for n in self.labels:
				n.config(bg=dim, fg=dimf, activebackground=dim)
			for o in self.radio:
				o.config(bg=dim, fg=dimf, activebackground=dim, highlightthickness=0, activeforeground=dimf,
						 selectcolor=dim)
			for p in self.button:
				p.config(bg=dim, fg=dimf, activebackground=dim, highlightbackground=dimf, activeforeground=dimf)
			for q in self.menus:
				q.config(bg=dim, fg=dimf, activebackground=dim, activeforeground=dimf)
		return dark(self)

	## PlOt ThE pLoTs
	def plot(self, canvas, ax, shape_obj):
		col_lab = [self.fck, self.f2, self.f3]
		try:
			root.title("GeoExpanse ({})".format(shape_obj.name))
		except:
			pass
		try:
			edge_c = self.ec_entry[1]
		except AttributeError:
			edge_c = "#ffffff"
			self.eck.config(bg=edge_c, width=200000000)
		try:
			color = self.c_entry[1]
		except AttributeError:
			color = "#00acff"
			self.fck.config(bg=color, width=200000000)
		try:
			color2 = self.c_entry2[1]
		except AttributeError:
			color2 = dim
			self.f2.config(bg=color2, width=200000000)
		try:
			color3 = self.c_entry3[1]
		except AttributeError:
			color3 = dim
			self.f3.config(bg=color3, width=200000000)

		#	#
		alpha 		= self.a_entry.get()
		grid 		= self.grid_axis.get()
		edge_w 		= self.ew_entry.get()
		edges 		= self.ed_entry.get()
		sides 		= self.si_entry.get()
		multi_pi 	= self.pi_entry.get()
		radiusa 	= self.raa_entry.get()
		radiusm 	= self.ram_entry.get()
		height 		= self.h_entry.get()
		multi_pi2 	= self.pi_entry2.get()
		figcolor	= self.figcolor.get()
		rotation 	= self.rotation.get()
		rotmagt		= self.romt_entry.get()
		rotmagp		= self.romp_entry.get()
		save		= self.format_save.get()

		ax.clear()
		plt.cla()
		plt.clf()

		def disable(*off):
			for m in off:
				if m in self.scales:
					m.config(state=tk.DISABLED, bg=dim, fg=dim, activebackground=dim, troughcolor=dim)
				elif m in self.labels:
					m.config(fg=disa)
				elif m in self.button:
					m.config(state=tk.DISABLED, highlightbackground=disa)
				elif m in col_lab:
					m.config(bg=dim, fg=dim, relief=tk.RIDGE)

		def activate(*on):
			for m in on:
				if m in self.scales:
					m.config(state=tk.ACTIVE, bg=dim, fg=dimf, activebackground=dim, troughcolor=dimf)
				elif m in self.labels:
					m.config(fg=dimf)
				elif m in self.button:
					m.config(state=tk.ACTIVE, highlightbackground=dimf)
				elif m in col_lab:
					m.config(relief=tk.GROOVE)
		args = shape_obj.shape.__code__.co_varnames

		if args[1:17] == (
			'alpha', 'color', 'edge_c', 'edge_w', 'grid', 'sides', 'edges', 'multi_pi', 'radiusm', 'radiusa', 'height', 'figcolor', 'rotation', 'rotmagt', 'rotmagp', 'save'):

			self.raa_label.config(text="Radius (Alt)")
			self.raa_entry.config(from_=1, to=50, resolution=1)
			self.pi_label.config(text=r"Multiple of " u'\u03C0' + " ("u'\u03C6'")")
			self.pi_entry.config(from_=1)
			self.ram_label.config(text="Radius (Main)")
			self.ram_entry.config(from_=1)
			shape_obj.shape(self.fig, alpha, color, edge_c, edge_w, grid, sides, edges, multi_pi, radiusm, radiusa,
							height, figcolor, rotation, rotmagt, rotmagp, save)

			activate(self.face, self.fck,
					 self.a_entry, self.h_entry, self.si_entry, self.ed_entry, self.pi_entry, self.ram_entry,
					 self.raa_entry,
					 self.a_label, self.h_label, self.si_label, self.ed_label, self.pi_label, self.ram_label,
					 self.raa_label)

			disable(self.face2, self.face3, self.f2, self.f3, self.pi_label2, self.pi_entry2)

		elif args[1:16] == (
			'alpha', 'color', 'edge_c', 'edge_w', 'grid', 'sides', 'edges',  'x_entry', 'y_entry', 'z_entry', 'figcolor', 'rotation', 'rotmagt', 'rotmagp', 'save'):
			self.raa_label.config(text="Radius (Alt)")
			self.raa_entry.config(from_=1, to=50, resolution=1)
			self.pi_label.config(text=r"Multiple of " u'\u03C0' + " ("u'\u03C6'")")
			self.pi_entry.config(from_=1)
			self.ram_label.config(text="Radius (Main)")
			self.ram_entry.config(from_=1)
			shape_obj.shape(self.fig, alpha, color, edge_c, edge_w, grid, sides, edges, x_entry, y_entry, z_entry, figcolor, rotation, rotmagt, rotmagp, save)

			activate(self.face, self.fck,
					 self.a_entry, self.si_entry, self.ed_entry,
					 self.a_label, self.si_label, self.ed_label)

			disable(self.face2, self.face3, self.f2, self.f3,
					self.raa_entry, self.raa_label, self.pi_entry2, self.pi_label2, self.pi_label, self.ram_label, self.pi_entry, self.ram_entry, self.h_label, self.h_entry)


		elif args[1:16] == (
			'alpha', 'color', 'edge_c', 'edge_w', 'grid', 'sides', 'edges', 'multi_pi', 'radiusm', 'height', 'figcolor', 'rotation', 'rotmagt', 'rotmagp', 'save'):
			self.raa_label.config(text="Radius (Alt)")
			self.raa_entry.config(from_=1, to=50, resolution=1)
			self.pi_label.config(text=r"Multiple of " u'\u03C0' + " ("u'\u03C6'")")
			self.pi_entry.config(from_=1)
			self.ram_label.config(text="Radius (Main)")
			self.ram_entry.config(from_=1)
			shape_obj.shape(self.fig, alpha, color, edge_c, edge_w, grid, sides, edges, multi_pi, radiusm, height, figcolor, rotation, rotmagt, rotmagp, save)

			activate(self.face, self.fck,
					 self.a_entry, self.h_entry, self.si_entry, self.ed_entry, self.pi_entry, self.ram_entry,
					 self.a_label, self.h_label, self.si_label, self.ed_label, self.pi_label, self.ram_label, )

			disable(self.face2, self.face3, self.f2, self.f3,
					self.raa_entry, self.raa_label, self.pi_entry2, self.pi_label2)

		elif args[1:15] == (
			'alpha', 'color', 'edge_c', 'edge_w', 'grid', 'sides', 'edges', 'radiusm', 'height', 'figcolor', 'rotation', 'rotmagt', 'rotmagp', 'save'):
			self.raa_label.config(text="Radius (Alt)")
			self.raa_entry.config(from_=1, to=50, resolution=1)
			self.pi_label.config(text=r"Multiple of " u'\u03C0' + " ("u'\u03C6'")")
			self.pi_entry.config(from_=1)
			self.ram_label.config(text="Radius (Main)")
			self.ram_entry.config(from_=1)
			shape_obj.shape(self.fig, alpha, color, edge_c, edge_w, grid, sides, edges, radiusm, height, figcolor, rotation, rotmagt, rotmagp, save)

			activate(self.face, self.fck,
					 self.a_entry, self.si_entry, self.ed_entry, self.ram_entry, self.h_entry,
					 self.a_label, self.si_label, self.ed_label, self.ram_label, self.h_label)

			disable(self.face2, self.face3, self.f2, self.f3,
					self.raa_entry, self.raa_label, self.pi_entry2, self.pi_label2, self.pi_entry, self.pi_label)

		elif args[1:15] == ('alpha', 'color', 'edge_c', 'edge_w', 'grid', 'sides', 'edges', 'multi_pi', 'radiusm', 'figcolor', 'rotation', 'rotmagt', 'rotmagp', 'save'):
			self.raa_label.config(text="Radius (Alt)")
			self.raa_entry.config(from_=1, to=50, resolution=1)
			self.pi_label.config(text=r"Multiple of " u'\u03C0' + " ("u'\u03C6'")")
			self.pi_entry.config(from_=1)
			self.ram_label.config(text="Radius (Main)")
			self.ram_entry.config(from_=1)
			shape_obj.shape(self.fig, alpha, color, edge_c, edge_w, grid, sides, edges, multi_pi, radiusm, figcolor, rotation, rotmagt, rotmagp, save)
			activate(self.face, self.fck,
					 self.a_entry, self.si_entry, self.ed_entry, self.pi_entry, self.ram_entry,
					 self.a_label, self.si_label, self.ed_label, self.pi_label, self.ram_label)

			disable(self.face2, self.face3, self.f2, self.f3,
					self.raa_entry, self.h_entry, self.raa_label, self.h_label, self.pi_entry2, self.pi_label2)

		elif args[1:14] == ('alpha', 'color', 'edge_c', 'edge_w', 'grid', 'sides', 'edges', 'multi_pi', 'figcolor', 'rotation', 'rotmagt', 'rotmagp', 'save'):
			self.raa_label.config(text="Radius (Alt)")
			self.raa_entry.config(from_=1, to=50, resolution=1)
			self.pi_label.config(text=r"Multiple of " u'\u03C0' + " ("u'\u03C6'")")
			self.pi_entry.config(from_=1)
			self.ram_label.config(text="Radius (Main)")
			self.ram_entry.config(from_=1)
			shape_obj.shape(self.fig, alpha, color, edge_c, edge_w, grid, sides, edges, multi_pi, figcolor, rotation, rotmagt, rotmagp, save)

			activate(self.face, self.fck,
					 self.a_entry, self.si_entry, self.ed_entry, self.pi_entry,
					 self.a_label, self.si_label, self.ed_label, self.pi_label)

			disable(self.face2, self.face3, self.f2, self.f3,
					self.raa_entry, self.h_entry, self.ram_entry, self.pi_entry2,
					self.raa_label, self.h_label, self.ram_label, self.pi_label2)

		elif args[1:14] == ('alpha', 'color', 'edge_c', 'edge_w', 'grid', 'sides', 'edges', 'multi_pi', 'figcolor', 'rotation', 'rotmagt', 'rotmagp', 'save'):
			self.raa_label.config(text="Radius (Alt)")
			self.raa_entry.config(from_=1, to=50, resolution=1)
			self.pi_label.config(text=r"Multiple of " u'\u03C0' + " ("u'\u03C6'")")
			self.pi_entry.config(from_=1)
			self.ram_label.config(text="Radius (Main)")
			self.ram_entry.config(from_=1)
			shape_obj.shape(self.fig, alpha, color, edge_c, edge_w, grid, sides, edges, multi_pi, figcolor, rotation, rotmagt, rotmagp, save)

			activate(self.face, self.fck,
					 self.a_entry, self.si_entry, self.ed_entry, self.pi_entry,
					 self.a_label, self.si_label, self.ed_label, self.pi_label)

			disable(self.face2, self.face3, self.f2, self.f3,
					self.raa_entry, self.h_entry, self.ram_entry, self.pi_entry2,
					self.raa_label, self.h_label, self.ram_label, self.pi_label2)

		elif args[1:12] == ('alpha', 'color', 'edge_c', 'edge_w', 'grid', 'radiusm', 'color2', 'figcolor', 'rotation', 'rotmagt', 'rotmagp', 'save'):
			self.raa_label.config(text="Radius (Alt)")
			self.raa_entry.config(from_=1, to=50, resolution=1)
			self.pi_label.config(text=r"Multiple of " u'\u03C0' + " ("u'\u03C6'")")
			self.pi_entry.config(from_=1)
			self.ram_label.config(text="Radius (Main)")
			self.ram_entry.config(from_=1)
			shape_obj.shape(self.fig, alpha, color, edge_c, edge_w, grid, radiusm, color2, figcolor, rotation, rotmagt, rotmagp, save)

			activate(self.face, self.fck,
					 self.a_entry, self.ram_entry, self.a_label, self.ram_label)

			disable(self.face2, self.f2, self.face3, self.f3,
					self.si_entry, self.ed_entry, self.pi_entry, self.raa_entry, self.h_entry, self.pi_entry2,
					self.si_label, self.ed_label, self.pi_label, self.raa_label, self.h_label, self.pi_label2)

		elif args[1:13] == ('alpha', 'color', 'edge_c', 'edge_w', 'grid', 'sides', 'edges', 'figcolor', 'rotation', 'rotmagt', 'rotmagp', 'save'):
			self.raa_label.config(text="Radius (Alt)")
			self.raa_entry.config(from_=1, to=50, resolution=1)
			self.pi_label.config(text=r"Multiple of " u'\u03C0' + " ("u'\u03C6'")")
			self.pi_entry.config(from_=1)
			self.ram_label.config(text="Radius (Main)")
			self.ram_entry.config(from_=1)

			shape_obj.shape(self.fig, alpha, color, edge_c, edge_w, grid, sides, edges, figcolor, rotation, rotmagt, rotmagp, save)

			activate(self.face, self.fck,
					 self.a_entry, self.si_entry, self.ed_entry,
					 self.a_label, self.si_label, self.ed_label)

			disable(self.face2, self.face3, self.f2, self.f3,
					self.pi_entry, self.raa_entry, self.h_entry, self.ram_entry, self.pi_entry2,
					self.pi_label, self.raa_label, self.h_label, self.ram_label, self.pi_label2)

		elif args[1:13] == ('alpha', 'color', 'edge_c', 'edge_w', 'grid', 'color2', 'color3', 'figcolor','rotation', 'rotmagt', 'rotmagp', 'save'):
			self.raa_label.config(text="Radius (Alt)")
			self.raa_entry.config(from_=1, to=50, resolution=1)
			self.pi_label.config(text=r"Multiple of " u'\u03C0' + " ("u'\u03C6'")")
			self.pi_entry.config(from_=1)
			self.ram_label.config(text="Radius (Main)")
			self.ram_entry.config(from_=1)
			shape_obj.shape(self.fig, alpha, color, edge_c, edge_w, grid, color2, color3, figcolor, rotation, rotmagt, rotmagp, save)

			activate(self.face, self.fck, self.face2, self.f2, self.face3, self.f3,
					 self.a_entry, self.a_label)

			disable(self.pi_entry, self.raa_entry, self.h_entry, self.ram_entry, self.si_entry, self.ed_entry,
					self.pi_entry2,
					self.pi_label, self.raa_label, self.h_label, self.ram_label, self.si_label, self.ed_label,
					self.pi_label2)

		elif args[1:12] == ('alpha', 'color', 'edge_c', 'edge_w', 'grid', 'radiusm', 'figcolor', 'rotation', 'rotmagt', 'rotmagp', 'save'):
			self.raa_label.config(text="Radius (Alt)")
			self.raa_entry.config(from_=1, to=50, resolution=1)
			self.pi_label.config(text=r"Multiple of " u'\u03C0' + " ("u'\u03C6'")")
			self.pi_entry.config(from_=1)
			self.ram_label.config(text="Radius (Main)")
			self.ram_entry.config(from_=1)
			shape_obj.shape(self.fig, alpha, color, edge_c, edge_w, grid, radiusm, figcolor, rotation, rotmagt, rotmagp, save)

			activate(self.face, self.fck,
					 self.ram_entry, self.a_entry, self.ram_label, self.a_label)

			disable(self.face2, self.face3, self.f2, self.f3,
					self.pi_entry, self.raa_entry, self.h_entry, self.si_entry, self.ed_entry, self.pi_entry2,
					self.pi_label, self.raa_label, self.h_label, self.si_label, self.ed_label, self.pi_label2)

		elif args[1:12] == ('alpha', 'color', 'edge_c', 'edge_w', 'grid', 'color2', 'figcolor', 'rotation', 'rotmagt', 'rotmagp', 'save'):
			self.raa_label.config(text="Radius (Alt)")
			self.raa_entry.config(from_=1, to=50, resolution=1)
			self.pi_label.config(text=r"Multiple of " u'\u03C0' + " ("u'\u03C6'")")
			self.pi_entry.config(from_=1)
			self.ram_label.config(text="Radius (Main)")
			self.ram_entry.config(from_=1)
			shape_obj.shape(self.fig, alpha, color, edge_c, edge_w, grid, color2, figcolor, rotation, rotmagt, rotmagp, save)

			activate(self.face, self.fck, self.face2, self.f2,
					 self.a_entry, self.a_label)

			disable(self.face3, self.f3,
					self.pi_entry, self.raa_entry, self.h_entry, self.si_entry, self.ed_entry, self.ram_entry,
					self.pi_entry2,
					self.pi_label, self.raa_label, self.h_label, self.si_label, self.ed_label, self.ram_label,
					self.pi_label2)

		elif args[1:8] == ('edge_c', 'edge_w', 'grid', 'slope', 'a', 'b', 'figcolor'):
			self.pi_label.config(text="Slope")
			self.pi_entry.config(from_=0)
			self.ram_label.config(text="Initial")
			self.ram_entry.config(from_=0)
			self.raa_label.config(text="Final")
			self.raa_entry.config(from_=0)
			shape_obj.shape(self.fig, edge_c, edge_w, grid, multi_pi, radiusm, radiusa, figcolor)

			activate(self.ram_entry, self.raa_entry, self.raa_label, self.ram_label, self.pi_entry, self.pi_label, )

			disable(self.face, self.face2, self.face3, self.fck, self.f2, self.f3,
					self.h_entry, self.a_entry, self.ed_entry,
					self.pi_entry2,
					self.h_label, self.a_label, self.ed_label,
					self.pi_label2)

		elif args[1:11] == ('alpha', 'color', 'edge_c', 'edge_w', 'grid', 'figcolor', 'rotation', 'rotmagt', 'rotmagp', 'save'):
			self.raa_label.config(text="Radius (Alt)")
			self.raa_entry.config(from_=1, to=50, resolution=1)
			self.pi_label.config(text=r"Multiple of " u'\u03C0' + " ("u'\u03C6'")")
			self.pi_entry.config(from_=1)
			self.ram_label.config(text="Radius (Main)")
			self.ram_entry.config(from_=1)
			shape_obj.shape(self.fig, alpha, color, edge_c, edge_w, grid, figcolor, rotation, rotmagt, rotmagp, save)

			activate(self.face, self.fck,
					 self.a_entry, self.a_label)

			disable(self.face2, self.face3, self.f2, self.f3,
					self.pi_entry, self.raa_entry, self.h_entry, self.si_entry, self.ed_entry, self.ram_entry,
					self.pi_entry2,
					self.pi_label, self.raa_label, self.h_label, self.si_label, self.ed_label, self.ram_label,
					self.pi_label2)

		elif args[1:7] == ('edge_c', 'edge_w', 'grid', 'radiusm', 'radiusa', 'figcolor'):
			self.raa_label.config(text="Radius (Alt)")
			self.raa_entry.config(from_=0, to=1, resolution=0.01)
			self.pi_label.config(text=r"Multiple of " u'\u03C0' + " ("u'\u03C6'")")
			self.pi_entry.config(from_=1)
			self.ram_label.config(text="Radius (Main)")
			self.ram_entry.config(from_=1)
			shape_obj.shape(self.fig, edge_c, edge_w, grid, radiusm, radiusa, figcolor)

			activate(self.ram_entry, self.raa_entry, self.raa_label, self.ram_label, )

			disable(self.face, self.face2, self.face3, self.fck, self.f2, self.f3,
					self.h_entry, self.a_entry, self.ed_entry,
					self.pi_entry2, self.si_entry, self.si_label,
					self.h_label, self.a_label, self.ed_label,
					self.pi_label2, self.pi_entry, self.pi_label)

		elif args[1:6] == ('edge_c', 'edge_w', 'grid', 'radiusm', 'figcolor'):
			self.raa_label.config(text="Radius (Alt)")
			self.raa_entry.config(from_=1, to=100, resolution=1)
			self.pi_label.config(text=r"Multiple of " u'\u03C0' + " ("u'\u03C6'")")
			self.pi_entry.config(from_=1)
			self.ram_label.config(text="Radius (Main)")
			self.ram_entry.config(from_=1)
			shape_obj.shape(self.fig, edge_c, edge_w, grid, radiusm, figcolor)

			activate(self.ram_entry, self.ram_label)

			disable(self.face, self.face2, self.face3, self.fck, self.f2, self.f3,
					self.h_entry, self.a_entry, self.ed_entry,
					self.pi_entry2, self.raa_entry, self.raa_label,
					self.h_label, self.a_label, self.ed_label,
					self.pi_label2, self.pi_entry, self.pi_label, self.si_entry, self.si_label)

		elif args[1:6] == ('edge_c', 'edge_w', 'grid', 'sides', 'figcolor'):
			self.raa_label.config(text="Radius (Alt)")
			self.raa_entry.config(from_=1, to=100, resolution=1)
			self.pi_label.config(text=r"Multiple of " u'\u03C0' + " ("u'\u03C6'")")
			self.pi_entry.config(from_=1)
			self.ram_label.config(text="Radius (Main)")
			self.ram_entry.config(from_=1)
			shape_obj.shape(self.fig, edge_c, edge_w, grid, sides, figcolor)

			activate(self.si_entry, self.si_label)

			disable(self.face, self.face2, self.face3, self.fck, self.f2, self.f3,
					self.raa_entry, self.h_entry, self.a_entry, self.ram_entry, self.ed_entry, self.pi_entry,
					self.pi_entry2,
					self.raa_label, self.h_label, self.a_label, self.ram_label, self.ed_label, self.pi_label,
					self.pi_label2)

		elif args[1:5] == ('edge_c', 'edge_w', 'grid', 'figcolor'):
			self.raa_label.config(text="Radius (Alt)")
			self.raa_entry.config(from_=1, to=100, resolution=1)
			self.pi_label.config(text=r"Multiple of " u'\u03C0' + " ("u'\u03C6'")")
			self.pi_entry.config(from_=1)
			self.ram_label.config(text="Radius (Main)")
			self.ram_entry.config(from_=1)
			shape_obj.shape(self.fig, edge_c, edge_w, grid, figcolor)

			disable(self.face, self.face2, self.face3, self.fck, self.f2, self.f3,
					self.pi_entry, self.raa_entry, self.h_entry, self.si_entry, self.ed_entry, self.a_entry,
					self.ram_entry, self.pi_entry2,
					self.pi_label, self.raa_label, self.h_label, self.si_label, self.ed_label, self.a_label,
					self.ram_label, self.pi_label2)

		#canvas.update()
		canvas.draw_idle()
		canvas.draw()

if __name__ == '__main__':
	root = tk.Tk()
	Geometry(root)

	root.title("GeoExpanse")
	root.geometry(str(root_width) + "x" + str(root_height))
	root.maxsize(str(root_width), str(root_height))
	root.minsize(str(500), str(root_height))

	def quit():
		global root
		root.quit()
		root.destroy()

	root.protocol("WM_DELETE_WINDOW", quit)
	root.update()
	root.update_idletasks()

	def quit(self):
		global root
		root.quit()
		root.destroy()

	root.bind("<Escape>", quit)

	icon = ImageTk.PhotoImage(file='icon.png')

	root.tk.call('wm', 'iconphoto', root._w, icon)
	root.mainloop()
