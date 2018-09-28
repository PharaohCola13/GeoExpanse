import matplotlib
import matplotlib.axes as axis
matplotlib.use('TkAgg')
import numpy as np
import matplotlib.pyplot as plt
from tkColorChooser import askcolor
#from tkinter.colorchooser import *
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg#, NavigationToolbar2TkAgg
import mpl_toolkits.mplot3d.axes3d as p3
from matplotlib.animation import *
from numpy import *
from matplotlib.figure import Figure
import Tkinter as tk  # python 2.7
import PIL
from PIL import ImageTk
import sys



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
import testing
import vase
import something_strange
import enneper_surface
import curves

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
     "Interesting":interesting,
     "120 Polyhedron": polyhedron,
     "Hyperbolic Cylinder":hyperbolic_cylinder,
     "Dini's Surface":dini_surface,
     "Knot":knot,
     "Neat":neat,
     "Spiral":spiral,
     "Testing":testing,
     "Vase":vase,
     "Something Strange":something_strange,
     "Enneper's Surface":enneper_surface,
	 #"Curves":curves
	 "Line":line
     }


root = tk.Tk()

root.title("Geometric Models")

root.geometry("720x780")

img = ImageTk.PhotoImage(file='penrose_icon.png')

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
		frame = tk.Frame(root, width=100, height=100)

        # Vars

		self.grid_axis = tk.StringVar()

		self.axis_limits = tk.StringVar()

		self.scroll		= tk.DoubleVar()

		self.shape_set = tk.StringVar()

		self.alpha = tk.StringVar()

		self.theme = tk.StringVar()

		self.two_three = tk.StringVar()

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
			

		def scro(i):
			ax.view_init(elev=self.scroll.get(), azim=self.scroll.get())

		def quit():
			global root
			root.quit()
			root.destroy()

		def FaceColor(self):
			self.c_entry = askcolor(title="Face Color", color="#e4e4e4")[1]
			
			self.face.config(bg=self.c_entry, fg="black", activeforeground="black")
			return self.c_entry

		def EdgeColor():
			self.ec_entry = askcolor(color="#ffd900", title="Edge Color")[1]
			self.edge.config(bg=self.ec_entry,fg="black", activeforeground="black")
			return self.ec_entry

		def popup_theme():
			top = tk.Toplevel(self)
			top.title("Themes")
			dim = "#303030"
			dimf = "#00C0FF"
			dimfa = dimf
			dimt = dimf
			bright = "potato"
			brightf = "potato"
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
				self.elev_label.config(bg=dim, fg=dimf, activebackground=dim)
				self.azim_label.config(bg=dim, fg=dimf, activebackground=dim)
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
				self.scroll_azim.config(bg=dim, fg=dimf, activebackground=dim, highlightthickness=0, troughcolor=dimt)
				self.scroll_elev.config(bg=dim, fg=dimf, activebackground=dim, highlightthickness=0, troughcolor=dimt)
				self.face.config(bg=dim, fg=dimf, activebackground=dim, highlightbackground=dimf, activeforeground=dimfa)
				self.edge.config(bg=dim, fg=dimf, activebackground=dim, highlightbackground=dimf,activeforeground=dimfa)
				menu.config(bg=dim, fg=dimf, activebackground=dim,activeforeground=dimfa)
				filemenu.config(bg=dim, fg=dimf, activebackground=dim,activeforeground=dimfa)

				pop.config(bg=dim, fg=dim, activebackground=dim)
			def light(self):
				tk.Button.config(bg="white", fg="white", activebackground="white")

			pop = tk.Button(top, text="POP!", command=top.destroy)
			pop.grid(row=0, column=0, sticky='new')

			tk.Radiobutton(top, text="Dark", variable=self.theme.get(), value="Dark").grid(row=1, column=0, sticky="w")
			tk.Radiobutton(top, text="Light", variable=self.theme.get(), value="Light").grid(row=2, column=0, sticky="w")
			tk.Radiobutton(top, text="Normal", variable=self.theme.get(), value="Normal").grid(row=3, column=0, sticky="w")

			tk.Button(top, text="Apply", command=lambda: dark(self)).grid(row=0, column=1, sticky="new")

			top.tk.call('wm', 'iconphoto', top._w, img)


		def popup_shape():
			top = tk.Toplevel(self)
	        #top.geometry("200x200"
			top.title("Shapes")
			pop = tk.Button(top, text="POP!", command=top.destroy)
			pop.grid(row=0, column=0, sticky='new')
			plot = tk.Button(top, text="Plot",  command=lambda: self.test(canvas,ax))
			plot.grid(row=0, column=2, sticky="new")

			top.tk.call('wm', 'iconphoto', top._w, img)
			if self.two_three.get() == "3d":

				#tk.Label(top, text="", font=('Helvetica', 16, 'bold'))
				tk.Radiobutton(top, text="Prism",variable=self.shape_set, value="Prism")					.grid(row=1, column=0, sticky="w")
				tk.Radiobutton(top, text="Pyramid",variable=self.shape_set, value="Pyramid")               .grid(row=2, column=0, sticky="w")
				tk.Radiobutton(top, text="Sphere",variable=self.shape_set, value="Sphere")                .grid(row=3, column=0, sticky="w")

				tk.Label(top, text="--- Hyperbolic Objects ---", font=('Times', 12, 'bold')).grid(row=4, column=0, sticky="nsew")
				tk.Radiobutton(top, text="Hyperbolic Octahedron",variable=self.shape_set, value="Hyperbolic Octahedron") .grid(row=5, column=0 ,sticky="w")
				tk.Radiobutton(top, text="Hyperbolic Paraboliod",	variable=self.shape_set, value="Hyperbolic Paraboliod") .grid(row=6, column=0, sticky="w")
				tk.Radiobutton(top, text="One Sheet Hyperboliod",	variable=self.shape_set, value="One Sheet Hyperboliod") .grid(row=7, column=0, sticky="w")

				tk.Label(top, text="--- Miscellaneous ---", font=('Times', 12, 'bold')).grid(row=8, column=0, sticky='nsew')
				tk.Radiobutton(top, text="Three Dodecahedron",		variable=self.shape_set, value="Three Dodecahedron")    .grid(row=9,  column=0, sticky="w")
				tk.Radiobutton(top, text="Cressant",				variable=self.shape_set, value="Cressant")              .grid(row=10, column=0, sticky="w")
				tk.Radiobutton(top, text="Funnel",  				variable=self.shape_set, value="Funnel")                .grid(row=11, column=0 ,sticky="w")
				tk.Radiobutton(top, text="Gabriel's Horn",			variable=self.shape_set, value="Gabriel's Horn")        .grid(row=12, column=0, sticky="w")
				tk.Radiobutton(top, text="Rose Spiral",				variable=self.shape_set, value="Rose Spiral")           .grid(row=13, column=0, sticky="w")
				tk.Radiobutton(top, text="Shell", 					variable=self.shape_set, value="Shell")                 .grid(row=14, column=0, sticky="w")
				tk.Radiobutton(top, text="Tesseract",				variable=self.shape_set, value="Tesseract")             .grid(row=15, column=0, sticky="w")

				tk.Label(top, text="--- Surfaces ---", font=('Times', 12, 'bold')).grid(row=1, column=2, sticky='new')
				tk.Radiobutton(top, text="Breather's Surface",      variable=self.shape_set, value="Breather's Surface")    .grid(row=2, column=2, sticky="w")
				tk.Radiobutton(top, text="Kuen's Surface",          variable=self.shape_set, value="Kuen's Surface")        .grid(row=3, column=2, sticky="w")
				tk.Radiobutton(top, text="Steiner's Surface",       variable=self.shape_set, value="Steiner's Surface")     .grid(row=4, column=2, sticky="w")
				tk.Radiobutton(top, text="Boy's Surface",           variable=self.shape_set, value="Boy's Surface")         .grid(row=5, column=2, sticky="w")

				tk.Label(top, text="--- Platonic Solids ---", font=('Times', 12, 'bold')).grid(row=6, column=2, sticky='nsew')
				tk.Radiobutton(top, text="Cube",                    variable=self.shape_set, value="Cube")                  .grid(row=7, column=2, sticky="w")
				tk.Radiobutton(top, text="Dodecahedron",            variable=self.shape_set, value="Dodecahedron")          .grid(row=8, column=2 ,sticky="w")
				tk.Radiobutton(top, text="Icosahedron",             variable=self.shape_set, value="Icosahedron")           .grid(row=9, column=2, sticky="w")
				tk.Radiobutton(top, text="Octahedron",              variable=self.shape_set, value="Octahedron")            .grid(row=10, column=2, sticky="w")

				tk.Label(top, text="--- Topological ---", font=('Times', 12, 'bold')).grid(row=11, column=2, sticky='nsew')
				tk.Radiobutton(top, text="Cross Cap",               variable=self.shape_set, value="Cross Cap")             .grid(row=12, column=2, sticky="w")
				tk.Radiobutton(top, text="Klein Bottle",            variable=self.shape_set, value="Klein Bottle")          .grid(row=13, column=2, sticky="w")
				tk.Radiobutton(top, text="Mobius Strip",            variable=self.shape_set, value="Mobius Strip")          .grid(row=14, column=2 ,sticky="w")
				tk.Radiobutton(top, text="Torus",                   variable=self.shape_set, value="Torus")                 .grid(row=15, column=2, sticky="w")

				tk.Label(top, text="--- In Development ---", font=('Times', 12, 'bold')).grid(row=1, column=4, sticky='nsew')
				tk.Radiobutton(top, text="Interesting",             variable=self.shape_set, value="Interesting")           .grid(row=2, column=4, sticky="w")
				tk.Radiobutton(top, text="120-Polyhedron",          variable=self.shape_set, value="120 Polyhedron")        .grid(row=3, column=4, sticky="w")
				tk.Radiobutton(top, text="Hyperbolic Cylinder",     variable=self.shape_set, value="Hyperbolic Cylinder")   .grid(row=4, column=4 ,sticky="w")
				tk.Radiobutton(top, text="Dini's Surface",          variable=self.shape_set, value="Dini's Surface")        .grid(row=5, column=4, sticky="w")
				tk.Radiobutton(top, text="Knot",                    variable=self.shape_set, value="Knot")                  .grid(row=6, column=4, sticky="w")
				tk.Radiobutton(top, text="Neat",                    variable=self.shape_set, value="Neat")                  .grid(row=7, column=4, sticky="w")
				tk.Radiobutton(top, text="Spiral",                  variable=self.shape_set, value="Spiral")                .grid(row=8, column=4, sticky="w")
				tk.Radiobutton(top, text="Testing",                 variable=self.shape_set, value="Testing")               .grid(row=9, column=4 ,sticky="w")
				tk.Radiobutton(top, text="Vase",                    variable=self.shape_set, value="Vase")                  .grid(row=10, column=4, sticky="w")
				tk.Radiobutton(top, text="Something Strange",       variable=self.shape_set, value="Something Strange")     .grid(row=11, column=4, sticky="w")
				tk.Radiobutton(top, text="Enneper's Surface",       variable=self.shape_set, value="Enneper's Surface")     .grid(row=12, column=4, sticky="w")
				#tk.Radiobutton(top, text="Curves",       variable=self.shape_set, value="Curves")     .grid(row=13, column=4, sticky="w")
				self.shape_set.set("Prism")

			elif self.two_three.get() == "2d":
				tk.Radiobutton(top, text="Line", variable=self.shape_set, value="Line").grid(row=1, column=0, sticky='w')


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
		filemenu.add_command(label="Theme", command=popup_theme)
		filemenu.add_separator()
		filemenu.add_command(label="Quit", command=quit)

		self.shapes = tk.Button(root, text="Shapes", command=popup_shape, height=4)
		self.shapes.grid(row=0, column=2, sticky='new',pady=584)

		# Rotational functions
		self.elev_label  = tk.Label(root, text="XY-rotation")
		self.elev_label.grid(row=0, column=0, sticky='new', pady=510)
		self.scroll_elev = tk.Scale(root, from_=-50, to=50, width=40, orient=tk.HORIZONTAL, variable=self.scroll,
							        command=scro)
		self.scroll_elev.grid(row=0, column=0, sticky="nsew", pady=530)

		self.azim_label = tk.Label(root, text="Z-rotation")
		self.azim_label.grid(row=0, column=0, sticky="new", pady=610, )
		self.scroll_azim = tk.Scale(root, from_=-50, to=50, width=40, orient=tk.HORIZONTAL, variable=self.scroll,
							        command=scro)
		self.scroll_azim.grid(row=0, column=0, sticky="nsew", pady=630)

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

		self.pi_label = tk.Label(root, text=r"Multiple of \pi)
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
		self.face = tk.Button(text="Face Color", command=lambda: FaceColor(self), height=2)
		self.face.grid(row=0, column=1, sticky='new', pady=30)

		# Edge Color
		self.edge = tk.Button(text="Edge Color", command=EdgeColor, height=2)
		self.edge.grid(row=0, column=2, sticky='new', pady=30)




		# Ploting plot
		self.plot_plot = tk.Button(root, text="Render Plot", command=lambda: self.plot
		(canvas,ax), height=4)
		self.plot_plot.grid(row=0, column=1, sticky="new", pady=500)

		# Ploting test
		self.plot_test = tk.Button(root, text="Update", command=lambda: self.test
		(canvas,ax), height=4)
		self.plot_test.grid(row=0, column=1,  sticky="new", pady=584)


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
		self.two_space.grid(row=0, column=2, sticky='nw', pady=500)

		self.three_space = tk.Radiobutton(root, text="3D", variable=self.two_three, value='3d', command=space)
		self.three_space.grid(row=0, column=2, sticky='nw', pady=525)
		self.two_three.set('3d')

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
        s[self.shape_set.get()].set_edgecolor(self.ec_entry.get(self.ec_entry.curselection()[0]))
        s[self.shape_set.get()].set_linewidth(self.ew_entry.get())
        s[self.shape_set.get()].set_facecolor(self.c_entry.get(self.c_entry.curselection()[0]))

        def init():
            return s[self.shape_set.get()],

        def animate(i):
            return s[self.shape_set.get()]

        # Animate
        ani = FuncAnimation(self.fig, animate, init_func=init,
                            interval=1, frames=500, blit=False, repeat=True)
        canvas.draw()

    def test(self, canvas, ax):
		edge_c 		= self.ec_entry
		color 		= self.c_entry
		rot_azim 	= self.scroll_azim.get()
		rot_elev 	= self.scroll_elev.get()
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

root.tk.call('wm', 'iconphoto', root._w, img)

root.protocol("WM_DELETE_WINDOW", quit)
root.update()
root.update_idletasks()

geo = Geometry(master=root)
geo.mainloop()
