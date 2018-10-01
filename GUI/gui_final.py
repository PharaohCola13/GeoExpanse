import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg#, NavigationToolbar2TkAgg
import mpl_toolkits.mplot3d.axes3d as p3
from matplotlib.animation import *
from numpy import *
import Tkinter as tk  # python 2.7
from PIL import ImageTk
import sys
from tkColorChooser import askcolor

sys.path.insert(0, '../In Development/')

sys.path.insert(0, '../Current Models/')
sys.path.insert(0, '../Current Models/Hyperbolic')
sys.path.insert(0, '../Current Models/Misc.')
sys.path.insert(0, '../Current Models/Platonic Solids')
sys.path.insert(0, '../Current Models/Surfaces')
sys.path.insert(0, '../Current Models/Topological')
sys.path.insert(0, '../Current Models/Two Space')


sys.path.insert(0, '../Scutoid Research/')

## Current Models
import prism
import pyramid
import sphere
#
# # Hyperbolic
import hyperbolic_octahedron
import hyperbolic_paraboloid
import one_sheet_hyperboloid
#
# # Misc.
import three_dodecahedron
import cressant
import funnel
import gabriel_horn
import rose_spiral
import shell
import tesseract
#
# # Surfaces
import boys_surface
import breather_surface
import kuen_surface
import steiner_surface
import roman_surface
import sine_surface
import henneberg_surface
#
# # Platonic Surfaces
import cube
import dodecahedron
import icosahedron
import octahedron
#
# # Topological
import cross_cap
import klein
import mobius
import torus

# # Two Space
import line
#
# # ## In Development
import interesting
import polyhedron
import hyperbolic_cylinder
import dini_surface
import knot
import neat
import spiral
import penrose_triangle
import testing
import vase
import something_strange
import enneper_surface

s = {"Prism":prism,
	"Pyramid":pyramid,
	 "Sphere":sphere,
	 "Hyperbolic Octahedron":hyperbolic_octahedron,
	 "Hyperbolic Paraboliod":hyperbolic_paraboloid,
	 "One Sheet Hyperboliod":one_sheet_hyperboloid,
	 "Three Dodecahedron": three_dodecahedron,
	 "Cressant":cressant,
	 "Funnel":funnel,
	 "Gabriel's Horn": gabriel_horn,
	 "Rose Spiral": rose_spiral,
	 "Shell":shell,
	 "Tesseract":tesseract,
	 "Breather's Surface":breather_surface,
	 "Kuen's Surface":kuen_surface,
	 "Steiner's Surface":steiner_surface,
	 "Boy's Surface":boys_surface,
	 "Roman Surface":roman_surface,
	 "Sine Surface":sine_surface,
	 "Henneberg's Surface":henneberg_surface,
	 "Cube": cube,
	 "Dodecahedron":dodecahedron,
	 "Icosahedron":icosahedron,
	 "Octahedron":octahedron,
	 "Cross Cap":cross_cap,
	 "Klein Bottle":klein,
	 "Mobius Strip":mobius,
	 "Torus":torus,
	 "Unk Surface":interesting,
	 "120 Polyhedron": polyhedron,
	 "Hyperbolic Cylinder":hyperbolic_cylinder,
	 "Dini's Surface":dini_surface,
	 "Knot":knot,
	 "Neat":neat,
	 "Spiral":spiral,
	 "Testing":testing,
	 "Penrose Triangle":penrose_triangle,
	 "Vase":vase,
	 "Something Strange":something_strange,
	 "Enneper's Surface":enneper_surface,
	 #"Curves":curves
	 "Line":line
	 }

#theme = "Dark"

dim = "#303030"
dimf = "#00C0FF"
dimfa = dimf
dimt = dimf

bright = "potato"
brightf = "potato"

class themes(tk.Frame):
	def __init__(self, master=None):
		tk.Frame.__init__(self,master)
		self.createWidgets()

	def createWidgets(self):
		img = ImageTk.PhotoImage(file='penrose_icon.png')
		#canvas = FigureCanvasTkAgg(self.fig,root_alt)
		#canvas.get_tk_widget().grid(row=0,column=0, sticky='new')
	
		#frame = tk.Frame(root_alt, width=100, height=100)
		theme = tk.StringVar()

		pop = tk.Button(root_alt, text="POP!", command=root_alt.destroy)
		pop.grid(row=0, column=0, sticky='new')

		tk.Radiobutton(root_alt, text="Dark", variable=theme.get(), value="Dark").grid(row=1, column=0, sticky="w")
		tk.Radiobutton(root_alt, text="Light", variable=theme.get(), value="Light").grid(row=2, column=0, sticky="w")
		tk.Radiobutton(root_alt, text="Normal", variable=theme.get(), value="Normal").grid(row=3, column=0, sticky="w")

		theme.set("Dark")

		#top.tk.call('wm', 'iconphoto', top._w, img)
		#theme = "Dark"
	#return theme

theme = "Dark"

class Geometry(tk.Frame):
	global theme
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

		self.grid_axis = tk.StringVar()

		self.axis_limits = tk.StringVar()

		self.scroll		= tk.DoubleVar()

		self.shape_set = tk.StringVar()

		self.alpha = tk.StringVar()

		self.two_three = tk.StringVar()

		self.theme = theme

	# Save Variables

		# Functions
		def axi():
			plt.axis(str(self.grid_axis.get()))
			plt.xlabel("X-Axis", color="white")
			plt.ylabel("Y-Axis", color="white")
			ax.set_zlabel("Z-Axis", color="white")
			plt.xticks(color="white")
			plt.yticks(color="white")
		   # plt.plot([0,0], 'r-',lw=3)

		#def lim(i):
		##    plt.xlim((-1 * i, i))
		 #   plt.ylim((-1 * i, i))
		def space():
			plt.figure(1)
			plt.gca()
			ax.set_facecolor('white')			
			plt.axis('on')
		def adjust():
			root.geometry("500x500+520+280")

		def scro(i):
			ax.view_init(elev=self.scroll.get(), azim=self.scroll.get())

		def FaceColor(self):
			self.c_entry = askcolor(title="Face Color", color="#e4e4e4")[1]
			
			self.fck.config(bg=self.c_entry)
			return self.c_entry

		def EdgeColor(self):
			self.ec_entry = askcolor(color="#ffd900", title="Edge Color")[1]
			self.eck.config(bg=self.ec_entry)
			return self.ec_entry



		def popup_shape():
			top = tk.Toplevel(self)
			top.title("Shapes")
			pop = tk.Button(top, text="POP!", command=top.destroy)
			pop.grid(row=0, column=0, sticky='new')
			plot = tk.Button(top, text="Plot",  command=lambda: self.test(canvas,ax))
			plot.grid(row=0, column=2, sticky="new")

			top.tk.call('wm', 'iconphoto', top._w, img)
			if self.two_three.get() == "3d":

				#tk.Label(top, text="", font=('Helvetica', 16, 'bold'))
				top.prism = tk.Radiobutton(top, text="Prism",variable=self.shape_set, value="Prism")
				top.prism.grid(row=1, column=0, sticky="w")
				pyram = tk.Radiobutton(top, text="Pyramid",variable=self.shape_set, value="Pyramid")
				pyram.grid(row=2, column=0, sticky="w")
				spher = tk.Radiobutton(top, text="Sphere",variable=self.shape_set, value="Sphere")
				spher.grid(row=3, column=0, sticky="w")

				hy = tk.Label(top, text="--- Hyperbolic Objects ---", font=('Times', 12, 'bold'))
				hy.grid(row=4, column=0, sticky="nsew")
				hyoct = tk.Radiobutton(top, text="Hyperbolic Octahedron",variable=self.shape_set, value="Hyperbolic Octahedron")
				hyoct.grid(row=5, column=0 ,sticky="w")
				hypar = tk.Radiobutton(top, text="Hyperbolic Paraboliod",	variable=self.shape_set, value="Hyperbolic Paraboliod")
				hypar.grid(row=6, column=0, sticky="w")
				onesh = tk.Radiobutton(top, text="One Sheet Hyperboliod",	variable=self.shape_set, value="One Sheet Hyperboliod")
				onesh.grid(row=7, column=0, sticky="w")

				misc = tk.Label(top, text="--- Miscellaneous ---", font=('Times', 12, 'bold'))
				misc.grid(row=8, column=0, sticky='nsew')
				three = tk.Radiobutton(top, text="Three Dodecahedron",		variable=self.shape_set, value="Three Dodecahedron")
				three.grid(row=9,  column=0, sticky="w")
				cress = tk.Radiobutton(top, text="Cressant",				variable=self.shape_set, value="Cressant")
				cress.grid(row=10, column=0, sticky="w")
				funne = tk.Radiobutton(top, text="Funnel",  				variable=self.shape_set, value="Funnel")
				funne.grid(row=11, column=0 ,sticky="w")
				gabri = tk.Radiobutton(top, text="Gabriel's Horn",			variable=self.shape_set, value="Gabriel's Horn")
				gabri.grid(row=12, column=0, sticky="w")
				roses = tk.Radiobutton(top, text="Rose Spiral",				variable=self.shape_set, value="Rose Spiral")
				roses.grid(row=13, column=0, sticky="w")
				shell = tk.Radiobutton(top, text="Shell", 					variable=self.shape_set, value="Shell")
				shell.grid(row=14, column=0, sticky="w")
				tesse = tk.Radiobutton(top, text="Tesseract",				variable=self.shape_set, value="Tesseract")
				tesse.grid(row=15, column=0, sticky="w")

				surf = tk.Label(top, text="--- Surfaces ---", font=('Times', 12, 'bold'))
				surf.grid(row=1, column=2, sticky='new')
				breat = tk.Radiobutton(top, text="Breather's Surface",      variable=self.shape_set, value="Breather's Surface")
				breat.grid(row=2, column=2, sticky="w")
				kuens =tk.Radiobutton(top, text="Kuen's Surface",          variable=self.shape_set, value="Kuen's Surface")
				kuens.grid(row=3, column=2, sticky="w")
				stein = tk.Radiobutton(top, text="Steiner's Surface",       variable=self.shape_set, value="Steiner's Surface")
				stein.grid(row=4, column=2, sticky="w")
				boyss = tk.Radiobutton(top, text="Boy's Surface",           variable=self.shape_set, value="Boy's Surface")
				boyss.grid(row=5, column=2, sticky="w")

				plato = tk.Label(top, text="--- Platonic Solids ---", font=('Times', 12, 'bold'))
				plato.grid(row=6, column=2, sticky='nsew')
				cube = tk.Radiobutton(top, text="Cube",                    variable=self.shape_set, value="Cube")
				cube.grid(row=7, column=2, sticky="w")
				dodec = tk.Radiobutton(top, text="Dodecahedron",            variable=self.shape_set, value="Dodecahedron")
				dodec.grid(row=8, column=2 ,sticky="w")
				icosa =tk.Radiobutton(top, text="Icosahedron",             variable=self.shape_set, value="Icosahedron")
				icosa.grid(row=9, column=2, sticky="w")
				octah = tk.Radiobutton(top, text="Octahedron",              variable=self.shape_set, value="Octahedron")
				octah.grid(row=10, column=2, sticky="w")

				topo = tk.Label(top, text="--- Topological ---", font=('Times', 12, 'bold'))
				topo.grid(row=11, column=2, sticky='nsew')
				cross = tk.Radiobutton(top, text="Cross Cap",               variable=self.shape_set, value="Cross Cap")
				cross.grid(row=12, column=2, sticky="w")
				klein = tk.Radiobutton(top, text="Klein Bottle",            variable=self.shape_set, value="Klein Bottle")
				klein.grid(row=13, column=2, sticky="w")
				mobiu = tk.Radiobutton(top, text="Mobius Strip",            variable=self.shape_set, value="Mobius Strip")
				mobiu.grid(row=14, column=2 ,sticky="w")
				torus = tk.Radiobutton(top, text="Torus",                   variable=self.shape_set, value="Torus")
				torus.grid(row=15, column=2, sticky="w")

				dev = tk.Label(top, text="--- In Development ---", font=('Times', 12, 'bold'))
				dev.grid(row=1, column=4, sticky='nsew')
				unksu = tk.Radiobutton(top, text="Unk Surface",             variable=self.shape_set, value="Unk Surface")
				unksu.grid(row=2, column=4, sticky="w")
				polyh = tk.Radiobutton(top, text="120-Polyhedron",          variable=self.shape_set, value="120 Polyhedron")
				polyh.grid(row=3, column=4, sticky="w")
				hycyl = tk.Radiobutton(top, text="Hyperbolic Cylinder",     variable=self.shape_set, value="Hyperbolic Cylinder")
				hycyl.grid(row=4, column=4 ,sticky="w")
				dinis = tk.Radiobutton(top, text="Dini's Surface",          variable=self.shape_set, value="Dini's Surface")
				dinis.grid(row=5, column=4, sticky="w")
				knot = tk.Radiobutton(top, text="Knot",                    variable=self.shape_set, value="Knot")
				knot.grid(row=6, column=4, sticky="w")
				neat = tk.Radiobutton(top, text="Neat",                    variable=self.shape_set, value="Neat")
				neat.grid(row=7, column=4, sticky="w")
				spira = tk.Radiobutton(top, text="Spiral",                  variable=self.shape_set, value="Spiral")
				spira.grid(row=8, column=4, sticky="w")
				test = tk.Radiobutton(top, text="Testing",                 variable=self.shape_set, value="Testing")
				test.grid(row=9, column=4 ,sticky="w")
				vase = tk.Radiobutton(top, text="Vase",                    variable=self.shape_set, value="Vase")
				vase.grid(row=10, column=4, sticky="w")
				somet = tk.Radiobutton(top, text="Something Strange",       variable=self.shape_set, value="Something Strange")
				somet.grid(row=11, column=4, sticky="w")
				ennep = tk.Radiobutton(top, text="Enneper's Surface",       variable=self.shape_set, value="Enneper's Surface")
				ennep.grid(row=12, column=4, sticky="w")
				penro = tk.Radiobutton(top, text="Penrose Triangle",        variable=self.shape_set, value="Penrose Triangle")
				penro.grid(row=13,column=4,sticky="w")

				#tk.Radiobutton(top, text="Curves",       variable=self.shape_set, value="Curves")     .grid(row=13, column=4, sticky="w")
				self.shape_set.set("Penrose Triangle")

			elif self.two_three.get() == "2d":
				line = tk.Radiobutton(top, text="Line", variable=self.shape_set, value="Line")
				line.grid(row=1, column=0, sticky='w')
			return prism


		def popup_save():
			top = tk.Toplevel(self)
			top.geometry("200x200")
			top.title("Save Figure")
			pop = tk.Button(top, text="POP!", command=top.destroy)
			pop.grid(row=0, column=0)
			self.format_save	= tk.StringVar()
			def img():
				plt.savefig.format=self.format_save.get()
			def vid():
				Writer = writers['ffmpeg']
				writer = Writer(fps=15, bitrate=1800)
				# # Defintions for animations
				def init():
					return s[self.shape_set.get()],
				def animate(i):
					# # azimuth angle : 0 deg to 360 deg
					# # elev = i * n --> rotates object about the xy-plane with a magnitude of n
					# # azim = i * n --> rotates object around the z axis with a magnitude of n
					# # For top view elev = 90
					# # For side view elev = 0
					return s[self.shape_set.get()],

			tk.Radiobutton(top, text="png", variable=self.format_save, value="png", command=img, width=5).grid(row=1, column=0)
			tk.Radiobutton(top, text="jpg", variable=self.format_save, value="jpg", command=img, width=5).grid(row=1, column=1)
			tk.Radiobutton(top, text="mp4", command=vid, width=5).grid(row=2, column=0)
			tk.Button(top, text="save img", command=lambda: plt.savefig("{}.{}".format(self.shape_set.get(),self.format_save.get()), format=str(self.format_save.get()))).grid(row=0, column=1)
			tk.Button(top, text="save video", command=lambda: FuncAnimation(self.fig, vid.animate, init_func=vid.init,
							interval=1, frames=500, blit=False, repeat=True).save('{}.mp4'.format(self.shape_set.get()), writer=writer)).grid(row=0, column=2)

			top.tk.call('wm', 'iconphoto', top._w, img)

		menu = tk.Menu(root)
		root.config(menu=menu)

		filemenu = tk.Menu(menu)
		menu.add_cascade(label="File", menu=filemenu)

		filemenu.add_command(label="Save", command=popup_save)
		#filemenu.add_command(label="Theme", command=popup_theme)
		filemenu.add_separator()
		filemenu.add_command(label="Quit", command=quit)

		#if root.geometry("720x780"):
		menu.add_command(label="Figure", command=adjust)
		menu.add_command(label="All", command=lambda: root.geometry("714x501"))
	  #elif root.geometry("500x500"):
	#		menu.add_command(label="Figure", command=adjust, state=tk.DIABLED)
#			menu.add_command(label="All", command=lambda: root.geometry("720x780"), state=tk.ACTIVE)

		# Rotational functions
		#self.elev_label  = tk.Label(root, text="XY-rotation")
		#self.elev_label.grid(row=0, column=0, sticky='new', pady=510)
		#self.scroll_elev = tk.Scale(root, from_=-50, to=50, width=40, orient=tk.HORIZONTAL, variable=self.scroll,
		#							command=scro)
		#self.scroll_elev.grid(row=0, column=0, sticky="nsew", pady=530)

		#self.azim_label = tk.Label(root, text="Z-rotation")
		#self.azim_label.grid(row=0, column=0, sticky="new", pady=610, )
		#self.scroll_azim = tk.Scale(root, from_=-50, to=50, width=40, orient=tk.HORIZONTAL, variable=self.scroll,
		#							command=scro)
		#self.scroll_azim.grid(row=0, column=0, sticky="nsew", pady=630)

		# Transparency
		self.a_label = tk.Label(root, text="Transparency")
		self.a_label.grid(row=0, column=1, sticky='nw', pady=110)
		self.a_entry = tk.Scale(root, from_=0, to=1, resolution=0.1, orient=tk.HORIZONTAL)
		self.a_entry.grid(row=0, column=2, sticky='nw', pady=90)
		self.a_entry.set(0.4)

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
		self.ed_entry.set(20)

		self.pi_label = tk.Label(root, text=r"Multiple of \pi")
		self.pi_label.grid(row=0, column=1, sticky='nw', pady=230)
		self.pi_entry = tk.Scale(root, from_=1, to=100, resolution=1, orient=tk.HORIZONTAL)
		self.pi_entry.grid(row=0, column=2, sticky='nw', pady=210)

		# Edge Width
		self.ew_label = tk.Label(root, text="Edge Width")
		self.ew_label.grid(row=0, column=1, sticky='nw', pady=270)
		self.ew_entry = tk.Scale(root, from_=0, to=5, resolution=0.5, orient=tk.HORIZONTAL)
		self.ew_entry.grid(row=0, column=2, sticky='nw', pady=250)
		self.ew_entry.set(1)

		# Radius
		self.ra_label = tk.Label(root, text="Radius")
		self.ra_label.grid(row=0, column=1, sticky='nw', pady=310)
		self.ra_entry = tk.Scale(root, from_=1, to=100, resolution=1, orient=tk.HORIZONTAL)
		self.ra_entry.grid(row=0, column=2, sticky='nw', pady=290)

		# Face Color
		self.face = tk.Button(text="Face\n Color", command=lambda: FaceColor(self), height=3, width=3)
		self.face.grid(row=0, column=1, sticky='ne', pady=30, padx=4)

		self.fck = tk.Checkbutton(root, state=tk.DISABLED, height=3, width=3)
		self.fck.grid(row=0, column=1, sticky='nw', pady=30)

		# Edge Color
		self.edge = tk.Button(text="Edge\n Color", command=lambda: EdgeColor(self), height=3, width=3)
		self.edge.grid(row=0, column=2, sticky='nw', pady=30)

		self.eck = tk.Checkbutton(root, state=tk.DISABLED, height=3, width=3)
		self.eck.grid(row=0, column=2, sticky='ne', pady=30)




		# Ploting plot
		self.plot_plot = tk.Button(root, text="Render Plot", command=lambda: self.plot
		(canvas,ax), height=4)
		self.plot_plot.grid(row=0, column=1, sticky="new", pady=350)

		# Ploting test
		self.plot_test = tk.Button(root, text="Update", command=lambda: self.test
		(canvas,ax), height=4)
		self.plot_test.grid(row=0, column=1,  sticky="new", pady=430)


		# Changing axis limits
#		tk.Label(root, text="Axis Limits").grid(row=0, column=0, sticky="new", pady=710)#
#		self.axis_zoom = tk.Scale(root, from_=1, to=100, width=40, orient=tk.HORIZONTAL)
#		self.axis_zoom.grid(row=0, column=0, sticky="nsew", pady=730)

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

		self.shapes = tk.Button(root, text="Shapes", command=popup_shape, height=4)
		self.shapes.grid(row=0, column=2, sticky='new',pady=430)

		def dark(self):		
				#self.tk.Frame.config(bg=dim, fg=dim, activebackground=dim)
				root.config(background=dim)
				self.a_entry.config(bg=dim, fg=dimf, activebackground=dim, highlightthickness=0, troughcolor=dimt)
				self.si_entry.config(bg=dim, fg=dimf, activebackground=dim, highlightthickness=0, troughcolor=dimt)
				self.ed_entry.config(bg=dim, fg=dimf, activebackground=dim, highlightthickness=0,troughcolor=dimt)
				self.pi_entry.config(bg=dim, fg=dimf, activebackground=dim, highlightthickness=0, troughcolor=dimt)
				self.ew_entry.config(bg=dim, fg=dimf, activebackground=dim, highlightthickness=0, troughcolor=dimt)
				self.ra_entry.config(bg=dim, fg=dimf, activebackground=dim, highlightthickness=0,troughcolor=dimt)
				self.shapes.config(bg=dim, fg=dimf, activebackground=dim, highlightbackground=dimf, activeforeground=dimfa)
				#self.elev_label.config(bg=dim, fg=dimf, activebackground=dim)
				#self.azim_label.config(bg=dim, fg=dimf, activebackground=dim)
				self.a_label.config(bg=dim, fg=dimf, activebackground=dim)
				self.si_label.config(bg=dim, fg=dimf, activebackground=dim)
				self.ed_label.config(bg=dim, fg=dimf, activebackground=dim)
				self.pi_label.config(bg=dim, fg=dimf, activebackground=dim)
				self.ew_label.config(bg=dim, fg=dimf, activebackground=dim)
				self.ra_label.config(bg=dim, fg=dimf, activebackground=dim)
				self.grid_on.config(bg=dim, fg=dimf, activebackground=dim, highlightthickness=0,activeforeground=dimfa, selectcolor=dim)
				self.grid_off.config(bg=dim, fg=dimf, activebackground=dim, highlightthickness=0, activeforeground=dimfa, selectcolor=dim)
				self.two_space.config(bg=dim, fg=dimf, activebackground=dim, highlightthickness=0,activeforeground=dimfa, selectcolor=dim)
				self.three_space.config(bg=dim, fg=dimf, activebackground=dim, highlightthickness=0,activeforeground=dimfa, selectcolor=dim)
				self.plot_test.config(bg=dim, fg=dimf, activebackground=dim, highlightbackground=dimf, activeforeground=dimfa)
				self.plot_plot.config(bg=dim, fg=dimf, activebackground=dim, highlightbackground=dimf, activeforeground=dimfa)
				#self.scroll_azim.config(bg=dim, fg=dimf, activebackground=dim, highlightthickness=0, troughcolor=dimt)
				#self.scroll_elev.config(bg=dim, fg=dimf, activebackground=dim, highlightthickness=0, troughcolor=dimt)
				self.face.config(bg=dim, fg=dimf, activebackground=dim, highlightbackground=dimf, activeforeground=dimfa)
				self.edge.config(bg=dim, fg=dimf, activebackground=dim, highlightbackground=dimf,activeforeground=dimfa)
				menu.config(bg=dim, fg=dimf, activebackground=dim,activeforeground=dimfa)
				filemenu.config(bg=dim, fg=dimf, activebackground=dim,activeforeground=dimfa)
				#pop.config(bg=dim, fg=dim, activebackground=dim)
				#popup_shape(prism).config(bg=dim, fg=dimf, activebackground=dim, highlightthickness=0,activeforeground=dimfa, selectcolor=dim)

		def light(self):
				tk.Button.config(bg="white", fg="white", activebackground="white")
		if theme == "Dark":
				dark(self)

		elif theme == "Light":
				tk.Button(top, text="Apply", command=lambda: light(self)).grid(row=0, column=1, sticky="new")

		elif theme == "Normal":
				tk.Button(top, text="Apply", command=lambda: default(self)).grid(row=0, column=1, sticky="new")



	def plot(self,canvas, ax):
		ax.clear()
		name = self.shape_set.get()

		root.title("Geometric Models ({})".format(name))

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


		plt.axis(self.grid_axis.get())

		s[self.shape_set.get()] = ax.plot_surface(x, y, z)

		s[self.shape_set.get()].set_alpha(self.a_entry.get())
		s[self.shape_set.get()].set_edgecolor(self.ec_entry)
		s[self.shape_set.get()].set_linewidth(self.ew_entry.get())
		s[self.shape_set.get()].set_facecolor(self.c_entry)

		#def init():
		#	return s[self.shape_set.get()],

		#def animate(i):
		#	return s[self.shape_set.get()]

		# Animate
		#ani = FuncAnimation(self.fig, animate, init_func=init,
		#					interval=1, frames=500, blit=False, repeat=True)
		canvas.draw()

	def test(self, canvas, ax):
		edge_c 		= self.ec_entry
		color 		= self.c_entry
		#rot_azim 	= self.scroll_azim.get()
		#rot_elev 	= self.scroll_elev.get()
		alpha 		= self.a_entry.get()
		grid 		= self.grid_axis.get()
		edge_w 		= self.ew_entry.get()
		#zoom 		= self.axis_zoom.get()
		#slope 		= self.slope.get()
		edges		= self.ed_entry.get()
		sides 		= self.si_entry.get()
		multi_pi	= self.pi_entry.get()
		radius		= self.ra_entry.get()
		
		name = self.shape_set.get()
		root.title("Geometric Modeling ({})".format(name))

		ax.clear()
		plt.cla()
		plt.clf()	

		#ax.set_xlim(self.axis_limits.get(),self.axis_limits.get())
		#ax.set_ylim(self.axis_limits.get(),self.axis_limits.get())
		#ax.set_zlim(-50,50)

		s[self.shape_set.get()].shape(self.fig, alpha, color, edge_c, edge_w, grid, sides,
				   edges, multi_pi, radius)		

		canvas.draw()



if __name__ == '__main__':
	root = tk.Tk()
	root_alt = tk.Tk()
	
	root.title("Geometric Models")
	root_alt.title("Theme")

	#theme = themes.self.theme
	root.geometry("714x501")
	root_alt.geometry("200x200")
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


	#root_alt.tk.call('wm', 'iconphoto', root_alt._w, img)
	root_alt.protocol("WM_DELETE_WINDOW", quit_alt)
	root_alt.update()
	root_alt.update_idletasks()

	them = themes(master=root_alt)

	geo = Geometry(master=root)

	#geo.createWidgets()
	them.mainloop()
	geo.mainloop()
