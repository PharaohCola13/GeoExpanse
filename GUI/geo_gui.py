import matplotlib

import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import mpl_toolkits.mplot3d.axes3d as p3
from matplotlib.animation import *
from numpy import *
from PIL import ImageTk
from PIL import Image
import sys
from time import sleep


try:
	matplotlib.use('tkagg')
except AttributeError:
	matplotlib.use('TKAgg')

try:
	# for Python2
	import Tkinter as tk
	# import tk.ttk as ttk
except ImportError:
	# for Python3
	import tkinter as tk
	# import tk.ttk as ttk

try:
	from tkColorChooser import askcolor
except ImportError:
	from tkinter.colorchooser import askcolor



sys.path.append('../In Development/')

sys.path.append('../Current Models/')
sys.path.append('../Current Models/Hyperbolic/')
sys.path.append('../Current Models/Misc./')
sys.path.append('../Current Models/Platonic Solids/')
sys.path.append('../Current Models/Surfaces/')
sys.path.append('../Current Models/Topological/')
sys.path.append('../Current Models/Two Space/')
sys.path.append('../Current Models/Archimedean/')

sys.path.append('../Scutoid Research/')

import prism, pyramid, sphere
import hyperbolic_octahedron, hyperbolic_paraboloid, one_sheet_hyperboloid
import three_dodecahedron, cressant, funnel, gabriel_horn, rose_spiral, shell, tesseract
import breather_surface, kuen_surface, steiner_surface, boys_surface, roman_surface, sine_surface, henneberg_surface
import cube, dodecahedron, icosahedron, octahedron
import cross_cap, klein, mobius, torus
import unk_surface, hecatostoeicostohedron, hyperbolic_cylinder, dini_surface, knot, neat, spiral, testing, penrose_triangle, vase, something_strange, enneper_surface
import line
import cuboctahedron, great_rombicosidodecahedron, snub_cube, truncated_cube



s = {	"Prism"					: prism,
		"Pyramid"				: pyramid,
		"Sphere"				: sphere,

		"Hyperbolic Octahedron"	: hyperbolic_octahedron,
		"Hyperbolic Paraboliod"	: hyperbolic_paraboloid,
		"One Sheet Hyperboliod"	: one_sheet_hyperboloid,

		"Three Dodecahedron"	: three_dodecahedron,
		"Cressant"				: cressant,
		"Funnel"				: funnel,
		"Gabriel's Horn"		: gabriel_horn,
		"Rose Spiral"			: rose_spiral,
		"Shell"					: shell,
		"Tesseract"				: tesseract,

		"Breather's Surface"	: breather_surface,
		"Kuen's Surface"		: kuen_surface,
		"Steiner's Surface"		: steiner_surface,
		"Boy's Surface"			: boys_surface,
		"Roman Surface"			: roman_surface,
		"Sine Surface"			: sine_surface,
		"Henneberg's Surface"	: henneberg_surface,

		"Cube"					: cube,
		"Dodecahedron"			: dodecahedron,
		"Icosahedron"			: icosahedron,
		"Octahedron"			: octahedron,

		"Cross Cap"				: cross_cap,
		"Klein Bottle"			: klein,
		"Mobius Strip"			: mobius,
		"Torus"					: torus,

		"Unk Surface"			: unk_surface,
		"Hecatostoeicostohedron": hecatostoeicostohedron,
		"Hyperbolic Cylinder"	: hyperbolic_cylinder,
		"Dini's Surface"		: dini_surface,
		"Knot"					: knot,
		"Neat"					: neat,
		"Spiral"				: spiral,
		"Testing"				: testing,
		"Penrose Triangle"		: penrose_triangle,
		"Vase"					: vase,
		"Something Strange"		: something_strange,
		"Enneper's Surface"		: enneper_surface,
		"Line"					: line,

		"Cuboctahedron"			: cuboctahedron,
		"Great Rombicosidodecahedron": great_rombicosidodecahedron,
		"Snub Cube"				: snub_cube,
		"Truncated Cube"		: truncated_cube,
 #		"Great Dodecahedron"	: 'great_dodecahedron',
 #		"Great Icosahedron"		: 'great_icosahedron'
 }

dim = "#303030" #Background
dimf = "#00C0FF" #Font Color
dimfa = dimf
dimt = dimf #Slider color

disa = "#d400ff"

bright = "potato"
brightf = "potato"

theme = "Dark"

#class Startup():
#	def __init__(self, master=None):
#		tk.Frame.__init__(self,master)

#	def task():
		#def bar():
		#	load = tk.Tk()
		#	load.title("Starting")

		#	progress = ttk.Progressbar(load, orient=tk.HORIZONTAL, length=200, mode='determinate')

		#	progress['value'] = 1
		#	load.update_idletasks()
		#	sleep(5)

		#	progress['value'] = 10
		#	load.update_idletasks()
		#	sleep(5)
		#	progress['value'] = 30

		#	load.update_idletasks()
		#	sleep(5)
		#	progress['value'] = 150

		#	progress.grid(row=0, column=0)

		#	load.mainloop()
		#	return bar()
		#return task()


class Geometry(tk.Frame):
	global theme, Polyhedra
	def __init__(self, master=None):
		tk.Frame.__init__(self,master)
		self.createWidgets()

	def createWidgets(self):
		img = ImageTk.PhotoImage(file='penrose_icon.png')
		self.fig = plt.figure(figsize=(5, 5))
		ax = p3.Axes3D(self.fig)
		ax.set_facecolor('black')
		plt.axis('off')
		canvas = FigureCanvasTkAgg(self.fig,root)
		canvas.get_tk_widget().grid(row=0,column=0, sticky='new')
		root.update_idletasks()
		canvas.draw()
		frame = tk.Frame(root, width=100, height=100)

		# Vars

		self.grid_axis 		= tk.StringVar()

		self.axis_limits 	= tk.StringVar()

		self.scroll			= tk.DoubleVar()

		self.shape_set 		= tk.StringVar()

		self.alpha 			= tk.StringVar()

		self.two_three 		= tk.StringVar()

		self.theme 			= theme

		self.rot 			= tk.StringVar()

		self.format_save 	= tk.StringVar()

		# Functions
		def axi():
			plt.axis(str(self.grid_axis.get()))
			plt.xlabel("X-Axis", color="white")
			plt.ylabel("Y-Axis", color="white")
			ax.set_zlabel("Z-Axis", color="white")
			plt.xticks(color="white")
			plt.yticks(color="white")

		def space():
			plt.figure(1)
			plt.gca()
			ax.set_facecolor('white')			
			plt.axis('on')

		def adjust():
			root.geometry("500x500+520+280")

		def FaceColor(self):
			color = ""
			self.c_entry = askcolor(title="Face Color", color=color)[1]
			self.fck.config(bg=self.c_entry)							
			return self.c_entry

		def FaceColor2(self):
			color = ""
			self.c_entry2 = askcolor(title="Face Color 2", color=color)[1]
			self.f2.config(bg=self.c_entry2)							
			return self.c_entry2

		def FaceColor3(self):
			color = ""
			self.c_entry3 = askcolor(title="Face Color 3", color=color)[1]
			self.f3.config(bg=self.c_entry3)								
			return self.c_entry3

		def EdgeColor(self):
			color = ""
			self.ec_entry = askcolor(title="Edge Color", color=color)[1]
			self.eck.config(bg=self.ec_entry)
			return self.ec_entry

		def popup_shape():
			top = tk.Toplevel(self)
			top.title("Shapes")
			top.config(background=dim)
			#top.geometry("750x750")
			pop = tk.Button(top, text="POP!", command=top.destroy)
			pop.grid(row=0, column=0, sticky='new')
			pop.config(bg=dim,fg=dimf, activebackground=dim, highlightbackground=dimf, activeforeground=dimfa)
			plotter = tk.Button(top, text="Plot",  command=lambda: self.plot(canvas,ax))
			plotter.grid(row=0, column=2, sticky="new")
			plotter.config(bg=dim,fg=dimf, activebackground=dim, highlightbackground=dimf, activeforeground=dimfa)
			top.tk.call('wm', 'iconphoto', top._w, img)

			if self.two_three.get() == "3d":

				#tk.Label(top, text="", font=('Helvetica', 16, 'bold'))
				prism = tk.Radiobutton(top, text="Prism",variable=self.shape_set, value="Prism")
				prism.grid(row=1, column=0, sticky="w")
				prism.config(bg=dim, fg=dimf, activebackground=dim, highlightthickness=0, activeforeground=dimfa,selectcolor=dim)

				pyram = tk.Radiobutton(top, text="Pyramid",variable=self.shape_set, value="Pyramid")
				pyram.grid(row=2, column=0, sticky="w")
				pyram.config(bg=dim, fg=dimf, activebackground=dim, highlightthickness=0, activeforeground=dimfa,selectcolor=dim)

				spher = tk.Radiobutton(top, text="Sphere",variable=self.shape_set, value="Sphere")
				spher.grid(row=3, column=0, sticky="w")
				spher.config(bg=dim, fg=dimf, activebackground=dim, highlightthickness=0, activeforeground=dimfa,selectcolor=dim)

				hy = tk.Label(top, text="--- Hyperbolic Objects ---", font=('Times', 12, 'bold'))
				hy.grid(row=4, column=0, sticky="nsew")
				hy.config(bg=dim, fg=dimf, activebackground=dim)

				hyoct = tk.Radiobutton(top, text="Hyperbolic Octahedron",variable=self.shape_set, value="Hyperbolic Octahedron")
				hyoct.grid(row=5, column=0 ,sticky="w")
				hyoct.config(bg=dim, fg=dimf, activebackground=dim, highlightthickness=0, activeforeground=dimfa,selectcolor=dim)
				
				#hyoct_hover = CreateToolTip(hyoct, ImageTk.PhotoImage(file="./Visual/Hyperbolic Octahedron.png"),"test")

				hypar = tk.Radiobutton(top, text="Hyperbolic Paraboliod",	variable=self.shape_set, value="Hyperbolic Paraboliod")
				hypar.grid(row=6, column=0, sticky="w")
				hypar.config(bg=dim, fg=dimf, activebackground=dim, highlightthickness=0, activeforeground=dimfa,selectcolor=dim)
				#hypar_hover = CreateToolTip(hypar, ImageTk.PhotoImage(file="./Visual/hypar.png"),"test")

				onesh = tk.Radiobutton(top, text="One Sheet Hyperboliod",	variable=self.shape_set, value="One Sheet Hyperboliod")
				onesh.grid(row=7, column=0, sticky="w")
				onesh.config(bg=dim, fg=dimf, activebackground=dim, highlightthickness=0, activeforeground=dimfa,selectcolor=dim)

				misc = tk.Label(top, text="--- Miscellaneous ---", font=('Times', 12, 'bold'))
				misc.grid(row=8, column=0, sticky='nsew')
				misc.config(bg=dim, fg=dimf, activebackground=dim)

				three = tk.Radiobutton(top, text="Three Dodecahedron",		variable=self.shape_set, value="Three Dodecahedron")
				three.grid(row=9,  column=0, sticky="w")
				three.config(bg=dim, fg=dimf, activebackground=dim, highlightthickness=0, activeforeground=dimfa,selectcolor=dim)

				cress = tk.Radiobutton(top, text="Cressant",				variable=self.shape_set, value="Cressant")
				cress.grid(row=10, column=0, sticky="w")
				cress.config(bg=dim, fg=dimf, activebackground=dim, highlightthickness=0, activeforeground=dimfa,selectcolor=dim)

				funne = tk.Radiobutton(top, text="Funnel",  				variable=self.shape_set, value="Funnel")
				funne.grid(row=11, column=0 ,sticky="w")
				funne.config(bg=dim, fg=dimf, activebackground=dim, highlightthickness=0, activeforeground=dimfa,selectcolor=dim)

				gabri = tk.Radiobutton(top, text="Gabriel's Horn",			variable=self.shape_set, value="Gabriel's Horn")
				gabri.grid(row=12, column=0, sticky="w")
				gabri.config(bg=dim, fg=dimf, activebackground=dim, highlightthickness=0, activeforeground=dimfa,selectcolor=dim)

				roses = tk.Radiobutton(top, text="Rose Spiral",				variable=self.shape_set, value="Rose Spiral")
				roses.grid(row=13, column=0, sticky="w")
				roses.config(bg=dim, fg=dimf, activebackground=dim, highlightthickness=0, activeforeground=dimfa,selectcolor=dim)

				shell = tk.Radiobutton(top, text="Shell", 					variable=self.shape_set, value="Shell")
				shell.grid(row=14, column=0, sticky="w")
				shell.config(bg=dim, fg=dimf, activebackground=dim, highlightthickness=0, activeforeground=dimfa,selectcolor=dim)

				tesse = tk.Radiobutton(top, text="Tesseract",				variable=self.shape_set, value="Tesseract")
				tesse.grid(row=15, column=0, sticky="w")
				tesse.config(bg=dim, fg=dimf, activebackground=dim, highlightthickness=0, activeforeground=dimfa,selectcolor=dim)

				surf = tk.Label(top, text="--- Surfaces ---", font=('Times', 12, 'bold'))
				surf.grid(row=1, column=2, sticky='new')
				surf.config(bg=dim, fg=dimf, activebackground=dim)

				breat = tk.Radiobutton(top, text="Breather's Surface",      variable=self.shape_set, value="Breather's Surface")
				breat.grid(row=2, column=2, sticky="w")
				breat.config(bg=dim, fg=dimf, activebackground=dim, highlightthickness=0, activeforeground=dimfa,selectcolor=dim)

				kuens =tk.Radiobutton(top, text="Kuen's Surface",          variable=self.shape_set, value="Kuen's Surface")
				kuens.grid(row=3, column=2, sticky="w")
				kuens.config(bg=dim, fg=dimf, activebackground=dim, highlightthickness=0, activeforeground=dimfa,selectcolor=dim)

				stein = tk.Radiobutton(top, text="Steiner's Surface",       variable=self.shape_set, value="Steiner's Surface")
				stein.grid(row=4, column=2, sticky="w")
				stein.config(bg=dim, fg=dimf, activebackground=dim, highlightthickness=0, activeforeground=dimfa,selectcolor=dim)

				boyss = tk.Radiobutton(top, text="Boy's Surface",           variable=self.shape_set, value="Boy's Surface")
				boyss.grid(row=5, column=2, sticky="w")
				boyss.config(bg=dim, fg=dimf, activebackground=dim, highlightthickness=0, activeforeground=dimfa,selectcolor=dim)

				roman = tk.Radiobutton(top, text="Roman Surface",           variable=self.shape_set, value="Roman Surface")
				roman.grid(row=6, column=2, sticky="w")
				roman.config(bg=dim, fg=dimf, activebackground=dim, highlightthickness=0, activeforeground=dimfa,selectcolor=dim)

				sines = tk.Radiobutton(top, text="Sine Surface",            variable=self.shape_set, value="Sine Surface")
				sines.grid(row=7, column=2, sticky="w")
				sines.config(bg=dim, fg=dimf, activebackground=dim, highlightthickness=0, activeforeground=dimfa,selectcolor=dim)

				henne = tk.Radiobutton(top, text="Henneberg's Surface",      variable=self.shape_set, value="Henneberg's Surface")
				henne.grid(row=7, column=2, sticky="w")
				henne.config(bg=dim, fg=dimf, activebackground=dim, highlightthickness=0, activeforeground=dimfa,selectcolor=dim)

				topo = tk.Label(top, text="--- Topological ---", font=('Times', 12, 'bold'))
				topo.grid(row=11, column=2, sticky='nsew')
				topo.config(bg=dim, fg=dimf, activebackground=dim)

				cross = tk.Radiobutton(top, text="Cross Cap",               variable=self.shape_set, value="Cross Cap")
				cross.grid(row=12, column=2, sticky="w")
				cross.config(bg=dim, fg=dimf, activebackground=dim, highlightthickness=0, activeforeground=dimfa,selectcolor=dim)

				klein = tk.Radiobutton(top, text="Klein Bottle",            variable=self.shape_set, value="Klein Bottle")
				klein.grid(row=13, column=2, sticky="w")
				klein.config(bg=dim, fg=dimf, activebackground=dim, highlightthickness=0, activeforeground=dimfa,selectcolor=dim)

				mobiu = tk.Radiobutton(top, text="Mobius Strip",            variable=self.shape_set, value="Mobius Strip")
				mobiu.grid(row=14, column=2 ,sticky="w")
				mobiu.config(bg=dim, fg=dimf, activebackground=dim, highlightthickness=0, activeforeground=dimfa,selectcolor=dim)

				torus = tk.Radiobutton(top, text="Torus",                   variable=self.shape_set, value="Torus")
				torus.grid(row=15, column=2, sticky="w")
				torus.config(bg=dim, fg=dimf, activebackground=dim, highlightthickness=0, activeforeground=dimfa,selectcolor=dim)

				dev = tk.Label(top, text="--- In Development ---", font=('Times', 12, 'bold'))
				dev.grid(row=1, column=4, sticky='nsew')
				dev.config(bg=dim, fg=dimf, activebackground=dim)

				unksu = tk.Radiobutton(top, text="Unk Surface",             variable=self.shape_set, value="Unk Surface")
				unksu.grid(row=2, column=4, sticky="w")
				unksu.config(bg=dim, fg=dimf, activebackground=dim, highlightthickness=0, activeforeground=dimfa,selectcolor=dim)

				polyh = tk.Radiobutton(top, text="Hecatostoeicostohedron",  variable=self.shape_set, value="Hecatostoeicostohedron")
				polyh.grid(row=3, column=4, sticky="w")
				polyh.config(bg=dim, fg=dimf, activebackground=dim, highlightthickness=0, activeforeground=dimfa,selectcolor=dim)

				hycyl = tk.Radiobutton(top, text="Hyperbolic Cylinder",     variable=self.shape_set, value="Hyperbolic Cylinder")
				hycyl.grid(row=4, column=4 ,sticky="w")
				hycyl.config(bg=dim, fg=dimf, activebackground=dim, highlightthickness=0, activeforeground=dimfa,selectcolor=dim)

				dinis = tk.Radiobutton(top, text="Dini's Surface",          variable=self.shape_set, value="Dini's Surface")
				dinis.grid(row=5, column=4, sticky="w")
				dinis.config(bg=dim, fg=dimf, activebackground=dim, highlightthickness=0, activeforeground=dimfa,selectcolor=dim)

				knot = tk.Radiobutton(top, text="Knot",                    variable=self.shape_set, value="Knot")
				knot.grid(row=6, column=4, sticky="w")
				knot.config(bg=dim, fg=dimf, activebackground=dim, highlightthickness=0, activeforeground=dimfa,selectcolor=dim)

				neat = tk.Radiobutton(top, text="Neat",                    variable=self.shape_set, value="Neat")
				neat.grid(row=7, column=4, sticky="w")
				neat.config(bg=dim, fg=dimf, activebackground=dim, highlightthickness=0, activeforeground=dimfa,selectcolor=dim)

				spira = tk.Radiobutton(top, text="Spiral",                  variable=self.shape_set, value="Spiral")
				spira.grid(row=8, column=4, sticky="w")
				spira.config(bg=dim, fg=dimf, activebackground=dim, highlightthickness=0, activeforeground=dimfa,selectcolor=dim)

				test = tk.Radiobutton(top, text="Testing",                 variable=self.shape_set, value="Testing")
				test.grid(row=9, column=4 ,sticky="w")
				test.config(bg=dim, fg=dimf, activebackground=dim, highlightthickness=0, activeforeground=dimfa,selectcolor=dim)

				vase = tk.Radiobutton(top, text="Vase",                    variable=self.shape_set, value="Vase")
				vase.grid(row=10, column=4, sticky="w")
				vase.config(bg=dim, fg=dimf, activebackground=dim, highlightthickness=0, activeforeground=dimfa,selectcolor=dim)

				somet = tk.Radiobutton(top, text="Something Strange",       variable=self.shape_set, value="Something Strange")
				somet.grid(row=11, column=4, sticky="w")
				somet.config(bg=dim, fg=dimf, activebackground=dim, highlightthickness=0, activeforeground=dimfa,selectcolor=dim)

				ennep = tk.Radiobutton(top, text="Enneper's Surface",       variable=self.shape_set, value="Enneper's Surface")
				ennep.grid(row=12, column=4, sticky="w")
				ennep.config(bg=dim, fg=dimf, activebackground=dim, highlightthickness=0, activeforeground=dimfa,selectcolor=dim)

				penro = tk.Radiobutton(top, text="Penrose Triangle",        variable=self.shape_set, value="Penrose Triangle")
				penro.grid(row=13,column=4,sticky="w")
				penro.config(bg=dim, fg=dimf, activebackground=dim, highlightthickness=0, activeforeground=dimfa,selectcolor=dim)

				arch = tk.Label(top, text="--- Archimedean Solids ---", font=('Times', 12, 'bold'))
				arch.grid(row=1, column=5, sticky='nsew')
				arch.config(bg=dim, fg=dimf, activebackground=dim)

				cuboc = tk.Radiobutton(top, text="Cuboctahedron",       variable=self.shape_set, value="Cuboctahedron")
				cuboc.grid(row=2, column=5, sticky="w")
				cuboc.config(bg=dim, fg=dimf, activebackground=dim, highlightthickness=0, activeforeground=dimfa,selectcolor=dim)

				grrom = tk.Radiobutton(top, text="Great\n Rombicosidodecahedron", variable=self.shape_set, value="Great Rombicosidodecahedron")
				grrom.grid(row=3, column=5, sticky="w")
				grrom.config(bg=dim, fg=dimf, activebackground=dim, highlightthickness=0, activeforeground=dimfa,selectcolor=dim)

				scube = tk.Radiobutton(top, text="Snub Cube", variable=self.shape_set, value="Snub Cube")
				scube.grid(row=4, column=5, sticky="w")
				scube.config(bg=dim, fg=dimf, activebackground=dim, highlightthickness=0, activeforeground=dimfa,selectcolor=dim)

				tcube = tk.Radiobutton(top, text="Truncated Cube", variable=self.shape_set, value="Truncated Cube")
				tcube.grid(row=5, column=5, sticky="w")
				tcube.config(bg=dim, fg=dimf, activebackground=dim, highlightthickness=0, activeforeground=dimfa,selectcolor=dim)

				plato = tk.Label(top, text="--- Platonic Solids ---", font=('Times', 12, 'bold'))
				plato.grid(row=6, column=5, sticky='nsew')
				plato.config(bg=dim, fg=dimf, activebackground=dim)

				cube = tk.Radiobutton(top, text="Cube",                    variable=self.shape_set, value="Cube")
				cube.grid(row=7, column=5, sticky="w")
				#cube_hover = CreateToolTip(cube, ImageTk.PhotoImage(file="./Visual/Cube.png"),"test")
				cube.config(bg=dim, fg=dimf, activebackground=dim, highlightthickness=0, activeforeground=dimfa,selectcolor=dim)

				dodec = tk.Radiobutton(top, text="Dodecahedron",            variable=self.shape_set, value="Dodecahedron")
				dodec.grid(row=8, column=5 ,sticky="w")
				#dodec_hover = CreateToolTip(dodec, ImageTk.PhotoImage(file="./Visual/Dodecahedron.png"),"test")
				dodec.config(bg=dim, fg=dimf, activebackground=dim, highlightthickness=0, activeforeground=dimfa,selectcolor=dim)

				icosa =tk.Radiobutton(top, text="Icosahedron",             variable=self.shape_set, value="Icosahedron")
				icosa.grid(row=9, column=5, sticky="w")
				#icosa_hover = CreateToolTip(icosa, ImageTk.PhotoImage(file="./Visual/icosa.png"),"test")
				icosa.config(bg=dim, fg=dimf, activebackground=dim, highlightthickness=0, activeforeground=dimfa,selectcolor=dim)

				octah = tk.Radiobutton(top, text="Octahedron",              variable=self.shape_set, value="Octahedron")
				octah.grid(row=10, column=5, sticky="w")
				octah.config(bg=dim, fg=dimf, activebackground=dim, highlightthickness=0, activeforeground=dimfa,selectcolor=dim)


				#grico = tk.Radiobutton(top, text="Great Icosahedron",        variable=self.shape_set, value="Great Icosahedron")
#				grico.grid(row=15,column=4,sticky="w")
#				grdod = tk.Radiobutton(top, text="Great Dodecahedron",        variable=self.shape_set, value="Great Dodecahedron")
#				grdod.grid(row=16,column=4,sticky="w")

				#tk.Radiobutton(top, text="Curves",       variable=self.shape_set, value="Curves")     .grid(row=13, column=4, sticky="w")
				self.shape_set.set("Penrose Triangle")

			elif self.two_three.get() == "2d":
				line = tk.Radiobutton(top, text="Line", variable=self.shape_set, value="Line")
				line.grid(row=1, column=0, sticky='w')
			# display = tk.Canvas(top, width=300, height=300)
			# display.grid(row=20, column=2, columnspan=4)
			#
			# img_dis = ImageTk.PhotoImage(Image.open("./Visual/{}.png".format(self.shape_set.get())))
			# display.create_image(5, 5, anchor=tk.NW, image=img_dis)
			#
			# top.update()
			# top.update_idletasks()
			# top.mainloop()

		def popup_save():
			top = tk.Toplevel(self)
			top.geometry("300x200")
			top.title("Save Figure")
			top.config(background=dim)
			pop = tk.Button(top, text="POP!", command=top.destroy)
			pop.grid(row=0, column=0)
			pop.config(bg=dim, 	fg=dimf, activebackground=dim, highlightbackground=dimf, activeforeground=dimfa)
			self.format_save	= tk.StringVar()
			def img():
				plt.savefig.format=self.format_save.get()

			png = tk.Radiobutton(top, text="png", variable=self.format_save, value="png", command=img, width=5)
			png.grid(row=1, column=0)
			png.config(bg=dim, 	fg=dimf, activebackground=dim, highlightthickness=0, activeforeground=dimfa, selectcolor=dim)

			jpg = tk.Radiobutton(top, text="jpg", variable=self.format_save, value="jpg", command=img, width=5)
			jpg.grid(row=1, column=1)
			jpg.config(bg=dim, 	fg=dimf, activebackground=dim, highlightthickness=0, activeforeground=dimfa, selectcolor=dim)

			mp4 = tk.Radiobutton(top, text="mp4", variable=self.format_save,    value="mp4", width=5)
			mp4.grid(row=2, column=0)
			mp4.config(bg=dim, 	fg=dimf, activebackground=dim, highlightthickness=0, activeforeground=dimfa, selectcolor=dim)

			save_img = tk.Button(top, text="save img", command=lambda: plt.savefig("{}.{}".format(self.shape_set.get(),self.format_save.get()), format=str(self.format_save.get())))
			save_img.grid(row=0, column=1)
			save_img.config(bg=dim,fg=dimf, activebackground=dim, highlightbackground=dimf, activeforeground=dimfa)

			save_vid = tk.Button(top, text="save video", command=lambda: self.plot(canvas,ax))
			save_vid.grid(row=0, column=2)
			save_vid.config(bg=dim, fg=dimf, activebackground=dim, highlightbackground=dimf, activeforeground=dimfa)

			self.format_save.set("png")
			#top.tk.call('wm', 'iconphoto', top._w, img)

		menu = tk.Menu(root)
		root.config(menu=menu)

		filemenu = tk.Menu(menu)
		menu.add_cascade(label="File", menu=filemenu)

		filemenu.add_command(label="Save", command=popup_save)
		filemenu.add_separator()
		filemenu.add_command(label="Quit", command=quit)

		menu.add_command(label="Figure", command=adjust)
		menu.add_command(label="Full", command=lambda: root.geometry("932x501"))

		# # Transparency
		self.a_label = tk.Label(root, text="Transparency")
		self.a_label.grid(row=0, column=1, sticky='nw', pady=110)
		self.a_entry = tk.Scale(root, from_=0, to=1, resolution=0.1, orient=tk.HORIZONTAL)
		self.a_entry.grid(row=0, column=2, sticky='nw', pady=90)
		self.a_entry.set(0.4)

		# # Height
		self.h_label = tk.Label(root, text="Height")
		self.h_label.grid(row=0, column=3, sticky='nw', pady=110, padx=10)
		self.h_entry = tk.Scale(root, from_=1, to=10, resolution=0.1, orient=tk.HORIZONTAL)
		self.h_entry.grid(row=0, column=4, sticky='nw', pady=90)
		self.h_entry.set(1)

		# Entry of the number of sides
		self.si_label = tk.Label(root, text="Number of Sides")
		self.si_label.grid(row=0, column=1, sticky='nw', pady=150)
		self.si_entry = tk.Scale(root, from_=1, to=100, resolution=1, orient=tk.HORIZONTAL)
		self.si_entry.grid(row=0, column=2, sticky='nw', pady=130)
		self.si_entry.set(20)

		# Entry of the number of edges
		self.ed_label = tk.Label(root, text="Number of Edges")
		self.ed_label.grid(row=0, column=1, sticky='nw', pady=190)
		self.ed_entry = tk.Scale(root, from_=1, to=100, resolution=1, orient=tk.HORIZONTAL)
		self.ed_entry.grid(row=0, column=2, sticky='nw', pady=170)
		self.ed_entry.set(2)

		# Multiple of Pi
		self.pi_label = tk.Label(root, text=r"Multiple of " u'\u03C0')
		self.pi_label.grid(row=0, column=1, sticky='nw', pady=230)
		self.pi_entry = tk.Scale(root, from_=1, to=100, resolution=1, orient=tk.HORIZONTAL)
		self.pi_entry.grid(row=0, column=2, sticky='nw', pady=210)
		self.pi_entry.set(2)

		# Edge Width
		self.ew_label = tk.Label(root, text="Edge Width")
		self.ew_label.grid(row=0, column=1, sticky='nw', pady=270)
		self.ew_entry = tk.Scale(root, from_=0, to=5, resolution=0.5, orient=tk.HORIZONTAL)
		self.ew_entry.grid(row=0, column=2, sticky='nw', pady=250)
		self.ew_entry.set(1)

		# Radius
		self.ram_label = tk.Label(root, text="Radius (Main)")
		self.ram_label.grid(row=0, column=3, sticky='nw', pady=150, padx=10)
		self.ram_entry = tk.Scale(root, from_=1, to=100, resolution=1, orient=tk.HORIZONTAL)
		self.ram_entry.grid(row=0, column=4, sticky='nw', pady=130)

		# Radius
		self.raa_label = tk.Label(root, text="Radius (Alt)")
		self.raa_label.grid(row=0, column=3, sticky='nw', pady=190, padx=10)
		self.raa_entry = tk.Scale(root, from_=1, to=100, resolution=1, orient=tk.HORIZONTAL)
		self.raa_entry.grid(row=0, column=4, sticky='nw', pady=170)

		# Edge Color
		self.edge = tk.Button(text="Edge Color", command=lambda: EdgeColor(self))
		self.edge.grid(row=0, column=1, sticky='new', pady=30, padx=0)

		self.eck = tk.Message(root, width=200000000, text=" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" ", borderwidth=5, 				relief=tk.GROOVE)
		self.eck.grid(row=0, column=1, sticky='new', pady=60)

		# Face Color
		self.face = tk.Button(text="Face Color", command=lambda: FaceColor(self))
		self.face.grid(row=0, column=2, sticky='new', pady=30, padx=0)

		self.fck = tk.Message(root, width=200000000, text=" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" ", borderwidth=5, 				relief=tk.GROOVE)
		self.fck.grid(row=0, column=2, sticky='new', pady=60, padx=0)

		# Edge Color
		self.face2 = tk.Button(text="Face Color 2", command=lambda: FaceColor2(self), state=tk.NORMAL)
		self.face2.grid(row=0, column=3, sticky='new', pady=30, padx=0)

		self.f2 = tk.Message(root, width=2000000, text=" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" ", borderwidth=5, 				relief=tk.GROOVE)
		self.f2.grid(row=0, column=3, sticky='new', pady=60, padx=0)

		# Face Color
		self.face3 = tk.Button(text="Face Color 3", command=lambda: FaceColor3(self), state=tk.NORMAL)
		self.face3.grid(row=0, column=4, sticky='new', pady=30, padx=0)

		self.f3 = tk.Message(root, width=2000000, text=" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" ", borderwidth=5, 				relief=tk.GROOVE)
		self.f3.grid(row=0, column=4, sticky='new', pady=60, padx=0)

		# Plotting
		self.plotting = tk.Button(root, text="Update", command=lambda: self.plot(canvas,ax), height=4)
		self.plotting.grid(row=0, column=1, columnspan=2,  sticky="new", pady=430)

		# Grid Functions (on/off)
		self.grid_on = tk.Radiobutton(root, text="Grid On", variable=self.grid_axis, value='on', command=axi)
		self.grid_on.grid(row=0, column=1, sticky='n')

		self.grid_off = tk.Radiobutton(root, text='Grid Off', variable=self.grid_axis, value='off', command=axi)
		self.grid_off.grid(row=0, column=2, sticky='n')
		self.grid_axis.set('off')

		# 2D or 3D
		self.two_space = tk.Radiobutton(root, text="2D", variable=self.two_three, value='2d', command=space)
		self.two_space.grid(row=0, column=2, sticky='nw', pady=350)

		self.three_space = tk.Radiobutton(root, text="3D", variable=self.two_three, value='3d', command=space)
		self.three_space.grid(row=0, column=2, sticky='nw', pady=380)
		self.two_three.set('3d')

		# Rotation 
		self.rot_on = tk.Radiobutton(root, text="Rot On", variable=self.rot, value='on')
		self.rot_on.grid(row=0, column=3, sticky='new')

		self.rot_off = tk.Radiobutton(root, text='Rot Off', variable=self.rot, value='off')
		self.rot_off.grid(row=0, column=4, sticky='new')

		# Shape Popup
		self.shapes = tk.Button(root, text="Shapes", command=popup_shape, height=4)
		self.shapes.grid(row=0, column=3, columnspan=2, sticky='new',pady=430)
		
		def dark(self):
				root.config(background=dim)
				# Scales
				self.a_entry.config(bg=dim,   fg=dimf, activebackground=dim, highlightthickness=0, troughcolor=dimt)
				self.h_entry.config(bg=dim,   fg=dimf, activebackground=dim, highlightthickness=0, troughcolor=dimt)
				self.si_entry.config(bg=dim,  fg=dimf, activebackground=dim, highlightthickness=0, troughcolor=dimt)
				self.ed_entry.config(bg=dim,  fg=dimf, activebackground=dim, highlightthickness=0, troughcolor=dimt)
				self.pi_entry.config(bg=dim,  fg=dimf, activebackground=dim, highlightthickness=0, troughcolor=dimt)
				self.ew_entry.config(bg=dim,  fg=dimf, activebackground=dim, highlightthickness=0, troughcolor=dimt)
				self.ram_entry.config(bg=dim, fg=dimf, activebackground=dim, highlightthickness=0, troughcolor=dimt)
				self.raa_entry.config(bg=dim, fg=dimf, activebackground=dim, highlightthickness=0, troughcolor=dimt)
				# Labels
				self.a_label.config(bg=dim,   fg=dimf, activebackground=dim)
				self.h_label.config(bg=dim,   fg=dimf, activebackground=dim)
				self.si_label.config(bg=dim,  fg=dimf, activebackground=dim)
				self.ed_label.config(bg=dim,  fg=dimf, activebackground=dim)
				self.pi_label.config(bg=dim,  fg=dimf, activebackground=dim)
				self.ew_label.config(bg=dim,  fg=dimf, activebackground=dim)
				self.ram_label.config(bg=dim, fg=dimf, activebackground=dim)
				self.raa_label.config(bg=dim, fg=dimf, activebackground=dim)
				# Radio Buttons
				self.grid_on.config(bg=dim, 	fg=dimf, activebackground=dim, highlightthickness=0, activeforeground=dimfa, selectcolor=dim)
				self.grid_off.config(bg=dim, 	fg=dimf, activebackground=dim, highlightthickness=0, activeforeground=dimfa, selectcolor=dim)
				self.two_space.config(bg=dim,	fg=dimf, activebackground=dim, highlightthickness=0, activeforeground=dimfa, selectcolor=dim)
				self.three_space.config(bg=dim, fg=dimf, activebackground=dim, highlightthickness=0, activeforeground=dimfa, selectcolor=dim)
				self.rot_on.config(bg=dim, 		fg=dimf, activebackground=dim, highlightthickness=0, activeforeground=dimfa, selectcolor=dim)
				self.rot_off.config(bg=dim, 	fg=dimf, activebackground=dim, highlightthickness=0, activeforeground=dimfa, selectcolor=dim)
				# Button				
				self.plotting.config(bg=dim, 	fg=dimf, activebackground=dim, highlightbackground=dimf, activeforeground=dimfa)
				self.face.config(bg=dim, 		fg=dimf, activebackground=dim, highlightbackground=dimf, activeforeground=dimfa)
				self.face2.config(bg=dim, 		fg=dimf, activebackground=dim, highlightbackground=dimf, activeforeground=dimfa)
				self.face3.config(bg=dim, 		fg=dimf, activebackground=dim, highlightbackground=dimf, activeforeground=dimfa)
				self.edge.config(bg=dim, 		fg=dimf, activebackground=dim, highlightbackground=dimf, activeforeground=dimfa)
				self.shapes.config(bg=dim, 		fg=dimf, activebackground=dim, highlightbackground=dimf, activeforeground=dimfa)
				# Menu				
				menu.config(bg=dim, 	fg=dimf, activebackground=dim, activeforeground=dimfa)
				filemenu.config(bg=dim, fg=dimf, activebackground=dim, activeforeground=dimfa)

#				prism.config(bg=dim, fg=dimf, activebackground=dim, highlightthickness=0, activeforeground=dimfa,
#					 selectcolor=dim)

		return dark(self)

	def plot(self, canvas, ax):
		try:
			edge_c = self.ec_entry
		except AttributeError:
			edge_c = "#f608ff"
			self.eck.config(bg=edge_c)
		try:
			color  = self.c_entry
		except AttributeError:
			color = "#00c4ff"
			self.fck.config(bg=color)
		try:
			color2  = self.c_entry2
		except AttributeError:
			color2 = "#000001"
			self.f2.config(bg=color2)
		try:
			color3  = self.c_entry3
		except AttributeError:
			color3 = "#000000"
			self.f3.config(bg=color3)
		
		alpha 		= self.a_entry.get()
		grid 		= self.grid_axis.get()
		edge_w 		= self.ew_entry.get()
		edges		= self.ed_entry.get()
		sides 		= self.si_entry.get()
		multi_pi	= self.pi_entry.get()
		radiusa		= self.raa_entry.get()
		radiusm		= self.ram_entry.get()
		rot 		= self.rot.get()
		save 		= self.format_save.get()
		height		= self.h_entry.get()


		name = self.shape_set.get()
		root.title("Geometric Modeling ({})".format(name))

		ax.clear()
		plt.cla()
		plt.clf()
		try: #Count: 14
			s[self.shape_set.get()].shape(self.fig, alpha, color, edge_c, edge_w, grid, sides, edges, multi_pi, radiusm, radiusa, color2, color3, height, rot, save)
		except KeyError:
			#name = testing.name
			root.title("Geometric Modeling (Testing)")
			testing.shape(self.fig, alpha, color, edge_c, edge_w, grid, sides, edges, multi_pi, radiusm, radiusa, color2, color3, height, rot, save)

			self.face2.config(state=tk.DISABLED, highlightbackground=disa)
			self.f2.config(bg=dim, fg=dim, relief=tk.RIDGE)
			self.face3.config(state=tk.DISABLED, highlightbackground=disa)
			self.f3.config(bg=dim, fg=dim, relief=tk.RIDGE)
			#self.ec_entry.config(color=edge_c)

			self.raa_entry.config(state=tk.DISABLED,bg=dim, fg=dim, activebackground=disa,  troughcolor=dim)
			self.raa_label.config(fg=disa)
			self.ram_entry.config(state=tk.DISABLED, bg=dim, fg=dim, activebackground=disa, troughcolor=dim)
			self.ram_label.config(fg=disa)
			self.h_entry.config(state=tk.DISABLED, bg=dim, fg=dim, activebackground=disa, troughcolor=dim)
			self.h_label.config(fg=disa)
			self.si_entry.config(state=tk.ACTIVE)
			self.si_label.config(fg=dimf)
			self.ed_entry.config(state=tk.ACTIVE)
			self.ed_label.config(fg=dimf)
			self.pi_entry.config(state=tk.ACTIVE)
			self.pi_label.config(fg=dimf)
		except TypeError:
			try: # Count: 12
				s[self.shape_set.get()].shape(self.fig, alpha, color, edge_c, edge_w, grid, sides, edges, multi_pi, radiusm, radiusa, height)

				self.face2.config(state=tk.DISABLED, highlightbackground=disa)
				self.f2.config(bg=dim, fg=dim, relief=tk.RIDGE)
				self.face3.config(state=tk.DISABLED, highlightbackground=disa)
				self.f3.config(bg=dim, fg=dim, relief=tk.RIDGE)

				self.si_entry.config(state=tk.ACTIVE, bg=dim, fg=dimf, activebackground=dim, troughcolor=dimt)
				self.si_label.config(fg=dimf)
				self.ed_entry.config(state=tk.ACTIVE, bg=dim, fg=dimf, activebackground=dim, troughcolor=dimt)
				self.ed_label.config(fg=dimf)
				self.pi_entry.config(state=tk.ACTIVE, bg=dim, fg=dimf, activebackground=dim, troughcolor=dimt)
				self.pi_label.config(fg=dimf)
				self.raa_entry.config(state=tk.ACTIVE, bg=dim, fg=dimf, activebackground=dim, troughcolor=dimt)
				self.raa_label.config(fg=dimf)
				self.ram_entry.config(state=tk.ACTIVE, bg=dim, fg=dimf, activebackground=dim, troughcolor=dimt)
				self.ram_label.config(fg=dimf)
				self.h_entry.config(state=tk.ACTIVE, bg=dim, fg=dimf, activebackground=dim, troughcolor=dimt)
				self.h_label.config(fg=dimf)
			except TypeError:
				try: # Count: 11
					s[self.shape_set.get()].shape(self.fig, alpha, color, edge_c, edge_w, grid, sides, edges, multi_pi, radiusm, height)

					self.face2.config(state=tk.DISABLED, highlightbackground=disa)
					self.f2.config(bg=dim, fg=dim, relief=tk.RIDGE)
					self.face3.config(state=tk.DISABLED, highlightbackground=disa)
					self.f3.config(bg=dim, fg=dim, relief=tk.RIDGE)

					self.si_entry.config(state=tk.ACTIVE, bg=dim, fg=dimf, activebackground=dim,  troughcolor=dimt)
					self.si_label.config(fg=dimf)
					self.ed_entry.config(state=tk.ACTIVE, bg=dim, fg=dimf, activebackground=dim, troughcolor=dimt)
					self.ed_label.config(fg=dimf)
					self.pi_entry.config(state=tk.ACTIVE, bg=dim, fg=dimf, activebackground=dim, troughcolor=dimt)
					self.pi_label.config(fg=dimf)
					self.ram_entry.config(state=tk.ACTIVE, bg=dim, fg=dimf, activebackground=dim, troughcolor=dimt)
					self.ram_label.config(fg=dimf)
					self.h_entry.config(state=tk.ACTIVE, bg=dim, fg=dimf, activebackground=dim, troughcolor=dimt)
					self.h_label.config(fg=dimf)
					self.raa_entry.config(state=tk.DISABLED,bg=dim, fg=dim, activebackground=dim, troughcolor=dim)
					self.raa_label.config(fg=disa)
				except TypeError:
					try: # Count: 10
						s[self.shape_set.get()].shape(self.fig, alpha, color, edge_c, edge_w, grid, sides, edges, multi_pi, radiusm)

						self.face2.config(state=tk.DISABLED, highlightbackground=disa)
						self.f2.config(bg=dim, fg=dim, relief=tk.RIDGE)
						self.face3.config(state=tk.DISABLED, highlightbackground=disa)
						self.f3.config(bg=dim, fg=dim, relief=tk.RIDGE)

						self.si_entry.config(state=tk.ACTIVE, bg=dim, fg=dimf, activebackground=dim, troughcolor=dimt)
						self.si_label.config(fg=dimf)
						self.ed_entry.config(state=tk.ACTIVE, bg=dim, fg=dimf, activebackground=dim, troughcolor=dimt)
						self.ed_label.config(fg=dimf)
						self.pi_entry.config(state=tk.ACTIVE, bg=dim, fg=dimf, activebackground=dim, troughcolor=dimt)
						self.pi_label.config(fg=dimf)
						self.ram_entry.config(state=tk.ACTIVE, bg=dim, fg=dimf, activebackground=dim, troughcolor=dimt)
						self.ram_label.config(fg=dimf)
						self.raa_entry.config(state=tk.DISABLED, bg=dim, fg=dim, activebackground=dim, troughcolor=dim)
						self.raa_label.config(fg=disa)
						self.h_entry.config(state=tk.DISABLED, bg=dim, fg=dim, activebackground=dim, troughcolor=dim)
						self.h_label.config(fg=disa)
					except TypeError:
						try: # Count: 9
							s[self.shape_set.get()].shape(self.fig, alpha, color, edge_c, edge_w, grid, sides, edges, multi_pi)

							self.face2.config(state=tk.DISABLED, highlightbackground=disa)
							self.f2.config(bg=dim, fg=dim, relief=tk.RIDGE)
							self.face3.config(state=tk.DISABLED, highlightbackground=disa)
							self.f3.config(bg=dim, fg=dim, relief=tk.RIDGE)

							self.si_entry.config(state=tk.ACTIVE, bg=dim, fg=dimf, activebackground=dim, troughcolor=dimt)
							self.si_label.config(fg=dimf)
							self.ed_entry.config(state=tk.ACTIVE, bg=dim, fg=dimf, activebackground=dim, troughcolor=dimt)
							self.ed_label.config(fg=dimf)
							self.pi_entry.config(state=tk.ACTIVE, bg=dim, fg=dimf, activebackground=dim, troughcolor=dimt)
							self.pi_label.config(fg=dimf)
							self.raa_entry.config(state=tk.DISABLED, bg=dim, fg=dim, activebackground=dim, troughcolor=dim)
							self.raa_label.config(fg=disa)
							self.h_entry.config(state=tk.DISABLED, bg=dim, fg=dim, activebackground=dim, troughcolor=dim)
							self.h_label.config(fg=disa)
							self.ram_entry.config(state=tk.DISABLED, bg=dim, fg=dim, activebackground=dim, troughcolor=dim)
							self.ram_label.config(fg=disa)
						except TypeError:
							try: # Count: 8
								s[self.shape_set.get()].shape(self.fig, alpha, color, edge_c, edge_w, grid, radiusm, color2)

								self.face3.config(state=tk.DISABLED, highlightbackground=disa)
								self.face2.config(state=tk.ACTIVE, highlightbackground=dimfa)
								self.f3.config(bg=dim, fg=dim, relief=tk.RIDGE)
								self.f2.config(relief=tk.GROOVE)

								self.pi_entry.config(state=tk.DISABLED, bg=dim, fg=dim, activebackground=dim, troughcolor=dim)
								self.pi_label.config(fg=disa)
								self.ram_entry.config(state=tk.ACTIVE, bg=dim, fg=dimf, activebackground=dim, troughcolor=dimt)
								self.ram_label.config(fg=dimf)
								self.raa_entry.config(state=tk.DISABLED, bg=dim, fg=dim, activebackground=dim, troughcolor=dim)
								self.raa_label.config(fg=disa)
								self.h_entry.config(state=tk.DISABLED, bg=dim, fg=dim, activebackground=dim, troughcolor=dim)
								self.h_label.config(fg=disa)
								self.si_entry.config(state=tk.DISABLED, bg=dim, fg=dim, activebackground=dim, troughcolor=dim)
								self.si_label.config(fg=disa)
								self.ed_entry.config(state=tk.DISABLED, bg=dim, fg=dim, activebackground=dim, troughcolor=dim)
								self.ed_label.config(fg=disa)
							except ValueError:
								try:
									s[self.shape_set.get()].shape(self.fig, alpha, color, edge_c, edge_w, grid, sides, edges)

									self.face2.config(state=tk.DISABLED, highlightbackground=disa)
									self.f2.config(bg=dim, fg=dim, relief=tk.RIDGE)
									self.face3.config(state=tk.DISABLED, highlightbackground=disa)
									self.f3.config(bg=dim, fg=dim, relief=tk.RIDGE)

									self.h_entry.config(state=tk.DISABLED, bg=dim, fg=dim, activebackground=dim, troughcolor=dim)
									self.h_label.config(fg=disa)
									self.ram_entry.config(state=tk.DISABLED, bg=dim, fg=dim, activebackground=dim, troughcolor=dim)
									self.ram_label.config(fg=disa)
									self.raa_entry.config(state=tk.DISABLED, bg=dim, fg=dim, activebackground=dim, troughcolor=dim)
									self.raa_label.config(fg=disa)
									self.si_entry.config(state=tk.ACTIVE, bg=dim, fg=dimf, activebackground=dim, troughcolor=dimt)
									self.si_label.config(fg=dimf)
									self.ed_entry.config(state=tk.ACTIVE, bg=dim, fg=dimf, activebackground=dim, troughcolor=dimt)
									self.ed_label.config(fg=dimf)
									self.pi_entry.config(state=tk.DISABLED, bg=dim, fg=dim, activebackground=dim, troughcolor=dim)
									self.pi_label.config(fg=disa)
								except TypeError:
									print("It's all good")
							except TypeError:
								try: # Count: 8
									s[self.shape_set.get()].shape(self.fig, alpha, color, edge_c, edge_w, grid, color2, color3)

									self.face2.config(state=tk.ACTIVE, highlightbackground=dimfa)
									self.face3.config(state=tk.ACTIVE, highlightbackground=dimfa)
									self.f2.config(relief=tk.GROOVE)
									self.f3.config(relief=tk.GROOVE)

									self.pi_entry.config(state=tk.DISABLED, bg=dim, fg=dim, activebackground=dim, highlightthickness=0, troughcolor=dim)
									self.pi_label.config(fg=disa)
									self.si_entry.config(state=tk.DISABLED, bg=dim, fg=dim, activebackground=dim, highlightthickness=0, troughcolor=dim)
									self.si_label.config(fg=disa)
									self.ed_entry.config(state=tk.DISABLED, bg=dim, fg=dim, activebackground=dim, highlightthickness=0, troughcolor=dim)
									self.ed_label.config(fg=disa)
									self.h_entry.config(state=tk.DISABLED, bg=dim, fg=dim, activebackground=dim, highlightthickness=0, troughcolor=dim)
									self.h_label.config(fg=disa)
									self.ram_entry.config(state=tk.DISABLED, bg=dim, fg=dim, activebackground=dim, highlightthickness=0, troughcolor=dim)
									self.ram_label.config(fg=disa)
									self.raa_entry.config(state=tk.DISABLED, bg=dim, fg=dim, activebackground=dim, troughcolor=dim)
									self.raa_label.config(fg=disa)
								except TypeError:
										try: # Count:7
											s[self.shape_set.get()].shape(self.fig, alpha, color, edge_c, edge_w, grid, radiusm)

											self.face2.config(state=tk.DISABLED, highlightbackground=disa)
											self.f2.config(bg=dim, fg=dim, relief=tk.RIDGE)
											self.face3.config(state=tk.DISABLED, highlightbackground=disa)
											self.f3.config(bg=dim, fg=dim, relief=tk.RIDGE)

											self.h_entry.config(state=tk.DISABLED, bg=dim, fg=dim, activebackground=dim, troughcolor=dim)
											self.h_label.config(fg=disa)
											self.raa_entry.config(state=tk.DISABLED, bg=dim, fg=dim, activebackground=dim, troughcolor=dim)
											self.raa_label.config(fg=disa)
											self.ram_entry.config(state=tk.ACTIVE, bg=dim, fg=dimf, activebackground=dim, troughcolor=dimt)
											self.ram_label.config(fg=dimf)
											self.pi_entry.config(state=tk.DISABLED, bg=dim, fg=dim, activebackgroun=dim, troughcolor=dim)
											self.pi_label.config(fg=disa)
											self.si_entry.config(state=tk.DISABLED,bg=dim, fg=dim, activebackground=dim, troughcolor=dim)
											self.si_label.config(fg=disa)
											self.ed_entry.config(state=tk.DISABLED, bg=dim, fg=dim, activebackground=dim, troughcolor=dim)
											self.ed_label.config(fg=disa)
										except TypeError:
											try: #Count: 7
												s[self.shape_set.get()].shape(self.fig, alpha, color, edge_c, edge_w, grid, color2)
												self.face3.config(state=tk.DISABLED, highlightbackground=disa)
												self.face2.config(state=tk.ACTIVE, highlightbackground=dimfa)
												self.f2.config(relief=tk.GROOVE)
												self.f3.config(bg=dim, fg=dim, relief=tk.RIDGE)

												self.h_entry.config(state=tk.DISABLED, bg=dim, fg=dim, activebackground=dim, troughcolor=dim)
												self.h_label.config(fg=disa)
												self.raa_entry.config(state=tk.DISABLED, bg=dim, fg=dim, activebackground=dim, troughcolor=dim)
												self.raa_label.config(fg=disa)
												self.ram_entry.config(state=tk.DISABLED, bg=dim, fg=dim, activebackground=dim, troughcolor=dim)
												self.ram_label.config(fg=disa)
												self.pi_entry.config(state=tk.DISABLED, bg=dim, fg=dim, activebackground=dim, troughcolor=dim)
												self.pi_label.config(fg=disa)
												self.si_entry.config(state=tk.DISABLED, bg=dim, fg=dim, activebackground=dim, troughcolor=dim)
												self.si_label.config(fg=disa)
												self.ed_entry.config(state=tk.DISABLED, bg=dim, fg=dim, activebackground=dim, troughcolor=dim)
												self.ed_label.config(fg=disa)
											except TypeError:
												try: #Count: 6
													s[self.shape_set.get()].shape(self.fig, alpha, color, edge_c, edge_w, grid)
													self.face2.config(state=tk.DISABLED, highlightbackground=disa)
													self.f2.config(bg=dim, fg=dim, relief=tk.RIDGE)
													self.face3.config(state=tk.DISABLED, highlightbackground=disa)
													self.f3.config(bg=dim, fg=dim, relief=tk.RIDGE)

													self.ram_entry.config(state=tk.DISABLED, bg=dim, fg=dim, activebackground=dim, troughcolor=dim)
													self.ram_label.config(fg=disa)
													self.h_entry.config(state=tk.DISABLED, bg=dim, fg=dim, activebackground=dim, troughcolor=dim)
													self.h_label.config(fg=disa)
													self.raa_entry.config(state=tk.DISABLED, bg=dim, fg=dim, activebackground=dim, troughcolor=dim)
													self.raa_label.config(fg=disa)
													self.pi_entry.config(state=tk.DISABLED, bg=dim, fg=dim, activebackground=dim, troughcolor=dim)
													self.pi_label.config(fg=disa)
													self.si_entry.config(state=tk.DISABLED, bg=dim, fg=dim, activebackground=dim, troughcolor=dim)
													self.si_label.config(fg=disa)
													self.ed_entry.config(state=tk.DISABLED, bg=dim, fg=dim, activebackground=dim, troughcolor=dim)
													self.ed_label.config(fg=disa)
												except NameError:
													print("FUCKING SHIT")
													#pass
		canvas.draw()

if __name__ == '__main__':
	root = tk.Tk()
	
	root.title("Geometric Models")
	root.geometry("932x501")
	img = ImageTk.PhotoImage(file='penrose_icon.png')

	root.tk.call('wm', 'iconphoto', root._w, img)
	root.protocol("WM_DELETE_WINDOW", quit)
	root.update()
	root.update_idletasks()

	def quit():
		global root
		root.quit()
		root.destroy()

	
	def quit_alt():
		global root_alt
		root_alt.quit()
		root_alt.destroy()


	geo = Geometry(master=root)
	geo.mainloop()
