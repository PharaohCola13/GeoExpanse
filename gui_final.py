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
import sys

sys.path.insert(0, './In Development/')

sys.path.insert(0, './Current Models/')
sys.path.insert(0, './Current Models/Hyperbolic')
sys.path.insert(0, './Current Models/Misc.')
sys.path.insert(0, './Current Models/Platonic Solids')
sys.path.insert(0, './Current Models/Surfaces')
sys.path.insert(0, './Current Models/Topological')

sys.path.insert(0, './Scutoid Research/')

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
     "Enneper's Surface":enneper_surface
     }


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

        self.axis_limits = tk.StringVar()

        self.scroll		= tk.IntVar()

        self.shape_set = tk.StringVar()

        # Save Variables

        # Functions

        def axi():
            plt.axis(str(self.grid_axis.get()))

        def scro(i):
            ax.view_init(elev=self.scroll.get(), azim=self.scroll.get())

        def quit():
            global root
            root.quit()
            root.destroy()

        def popup_shape():
            top = tk.Toplevel(self)
            #top.geometry("200x200")
            top.title("Shapes")

            tk.Button(top, text="POP!", command=top.destroy).grid(row=0, column=0, sticky='new')

            #tk.Label(top, text="", font=('Helvetica', 16, 'bold'))
            tk.Radiobutton(top, text="Prism",                   variable=self.shape_set, value="Prism")                 .grid(row=1, column=0, sticky="w")
            tk.Radiobutton(top, text="Pyramid",                 variable=self.shape_set, value="Pyramid")               .grid(row=2, column=0, sticky="w")
            tk.Radiobutton(top, text="Sphere",                  variable=self.shape_set, value="Sphere")                .grid(row=3, column=0, sticky="w")

            tk.Label(top, text="--- Hyperbolic Objects ---", font=('Helvetica', 12, 'bold')).grid(row=4, column=0, sticky="nsew")
            tk.Radiobutton(top, text="Hyperbolic Octahedron",   variable=self.shape_set, value="Hyperbolic Octahedron") .grid(row=5, column=0 ,sticky="w")
            tk.Radiobutton(top, text="Hyperbolic Paraboliod",   variable=self.shape_set, value="Hyperbolic Paraboliod") .grid(row=6, column=0, sticky="w")
            tk.Radiobutton(top, text="One Sheet Hyperboliod",   variable=self.shape_set, value="One Sheet Hyperboliod") .grid(row=7, column=0, sticky="w")

            tk.Label(top, text="--- Misc. ---", font=('Helvetica', 12, 'bold')).grid(row=8, column=0, sticky='nsew')
            tk.Radiobutton(top, text="Three Dodecahedron",      variable=self.shape_set, value="Three Dodecahedron")    .grid(row=9, column=0, sticky="w")
            tk.Radiobutton(top, text="Cressant",                variable=self.shape_set, value="Cressant")              .grid(row=10, column=0, sticky="w")
            tk.Radiobutton(top, text="Funnel",                  variable=self.shape_set, value="Funnel")                .grid(row=11, column=0 ,sticky="w")
            tk.Radiobutton(top, text="Gabriel's Horn",          variable=self.shape_set, value="Gabriel's Horn")        .grid(row=12, column=0, sticky="w")
            tk.Radiobutton(top, text="Rose Spiral",             variable=self.shape_set, value="Rose Spiral")           .grid(row=13, column=0, sticky="w")
            tk.Radiobutton(top, text="Shell",                   variable=self.shape_set, value="Shell")                 .grid(row=14, column=0, sticky="w")
            tk.Radiobutton(top, text="Tesseract",               variable=self.shape_set, value="Tesseract")             .grid(row=15, column=0, sticky="w")

            tk.Label(top, text="--- Surfaces ---", font=('Helvetica', 12, 'bold')).grid(row=1, column=2, sticky='new')
            tk.Radiobutton(top, text="Breather's Surface",      variable=self.shape_set, value="Breather's Surface")    .grid(row=2, column=2, sticky="w")
            tk.Radiobutton(top, text="Kuen's Surface",          variable=self.shape_set, value="Kuen's Surface")        .grid(row=3, column=2, sticky="w")
            tk.Radiobutton(top, text="Steiner's Surface",       variable=self.shape_set, value="Steiner's Surface")     .grid(row=4, column=2, sticky="w")
            tk.Radiobutton(top, text="Boy's Surface",           variable=self.shape_set, value="Boy's Surface")         .grid(row=5, column=2, sticky="w")

           # tk.Separator(master, orient=VERTICAL).grid(column=1, row=0, rowspan=20, sticky='ns')

            tk.Label(top, text="--- Platonic Solids ---", font=('Helvetica', 12, 'bold')).grid(row=6, column=2, sticky='nsew')
            tk.Radiobutton(top, text="Cube",                    variable=self.shape_set, value="Cube")                  .grid(row=7, column=2, sticky="w")
            tk.Radiobutton(top, text="Dodecahedron",            variable=self.shape_set, value="Dodecahedron")          .grid(row=8, column=2 ,sticky="w")
            tk.Radiobutton(top, text="Icosahedron",             variable=self.shape_set, value="Icosahedron")           .grid(row=9, column=2, sticky="w")
            tk.Radiobutton(top, text="Octahedron",              variable=self.shape_set, value="Octahedron")            .grid(row=10, column=2, sticky="w")

            tk.Label(top, text="--- Topological ---", font=('Helvetica', 12, 'bold')).grid(row=11, column=2, sticky='nsew')
            tk.Radiobutton(top, text="Cross Cap",               variable=self.shape_set, value="Cross Cap")             .grid(row=12, column=2, sticky="w")
            tk.Radiobutton(top, text="Klein Bottle",            variable=self.shape_set, value="Klein Bottle")          .grid(row=13, column=2, sticky="w")
            tk.Radiobutton(top, text="Mobius Strip",            variable=self.shape_set, value="Mobius Strip")          .grid(row=14, column=2 ,sticky="w")
            tk.Radiobutton(top, text="Torus",                   variable=self.shape_set, value="Torus")                 .grid(row=15, column=2, sticky="w")

            tk.Label(top, text="--- In Development ---", font=('Helvetica', 12, 'bold')).grid(row=1, column=4, sticky='nsew')
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

            tk.Button(top, text="Plot",  command=lambda: self.test(canvas,ax)).grid(row=0, column=2, sticky="new")

            img = ImageTk.PhotoImage(file='penrose_icon.png')
            top.tk.call('wm', 'iconphoto', top._w, img)

        def popup_save():
            top = tk.Toplevel(self)
            top.geometry("200x100")
            top.title("Save Figure")
            tk.Button(top, text="POP!", command=top.destroy).grid(row=0, column=0)
            #Writer = writers['ffmpeg']
            #writer = Writer(fps=15, bitrate=1800)
            #ani.save('%s.mp4' % name, writer=writer)
            self.format_save	= tk.StringVar()
            def img():
                plt.savefig.format=self.format_save.get()

            tk.Radiobutton(top, text="png", variable=self.format_save, value="png", command=img, width=5).grid(row=1, column=0)
            tk.Radiobutton(top, text="jpg", variable=self.format_save, value="jpg", command=img, width=5).grid(row=1, column=1)
            tk.Button(top, text="save", command=lambda: plt.savefig("{}.{}".format(self.shape_set.get(),self.format_save.get()), format=str(self.format_save.get()))).grid(row=0, column=1)
            #self.format_save.set("png")
            img = ImageTk.PhotoImage(file='penrose_icon.png')
            top.tk.call('wm', 'iconphoto', top._w, img)

        # Save window
        tk.Button(root, text="Save", command=popup_save).grid(row=0, column=1, columnspan=2, pady=656, sticky='new')

        # Shape
        tk.Button(root, text="Shapes", command=popup_shape).grid(row=0, column=1, columnspan=2, sticky='new', pady=470)

        # Ploting plot
        tk.Button(root, text="Render Plot", command=lambda: self.plot
        (canvas,ax), height=4).grid(row=0, column=1, sticky="new", pady=500)

        # Ploting test
        tk.Button(root, text="Update", command=lambda: self.test
        (canvas,ax), height=4).grid(row=0, column=1,  sticky="new", pady=584)

        # Quit button
        tk.Button(root, text="Quit", command=quit, height=10).grid(row=0, column=2, rowspan=1, sticky='new', pady=500)

        # Rotational functions
        tk.Label(root, text="XY-rotation").grid(row=0, column=0, sticky='new', pady=510)
        self.scroll_elev = tk.Scale(root, from_=-50, to=50, width=40, orient=tk.HORIZONTAL, variable=self.scroll, command=scro)
        self.scroll_elev.grid(row=0, column=0, sticky="nsew", pady=530)

        tk.Label(root, text="Z-rotation").grid(row=0, column=0, sticky="new", pady=610, )
        self.scroll_azim = tk.Scale(root, from_=-50, to=50, width=40, orient=tk.HORIZONTAL, variable=self.scroll, command=scro)
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
        self.c_entry.insert(13, 'deepskyblue')
        # c_entry.insert(13, colorset)
        self.c_entry.grid(row=0, column=1, sticky='n', pady=50)
        self.c_entry.select_set(12)

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
        self.ec_entry.insert(13, 'deepskyblue')
        self.ec_entry.grid(row=0, column=2, sticky='nw', pady=50)
        self.ec_entry.select_set(11)

        self.ec_scroll = tk.Scrollbar(root, orient=tk.VERTICAL, width=15)
        self.ec_scroll.grid(row=0, column=2, sticky='ne', pady=52)
        self.ec_scroll.config(command=self.ec_entry.yview)

        self.ec_entry.configure(yscrollcommand=self.ec_scroll.set)


    def plot(self,canvas, ax):
        ax.clear()
        name = "Unk Surface"

        root.title("Geometric Models ({})".format(name))

        #edge_c 		= self.ec_entry.get(self.ec_entry.curselection()[0])
        #color 			= self.c_entry.get(self.c_entry.curselection()[0])
        #rot_azim 		= self.scroll_azim.get()
        #rot_elev 		= self.scroll_elev.get()
        #alpha 			= self.a_entry.get()
        #grid 			= self.grid_axis.get()
        #edge_w 		= self.ew_entry.get()
        #zoom 			= self.axis_zoom.get()
        #edges			= self.ed_entry.get()
        #sides 			= self.si_entry.get()
        #multi_pi		= self.pi_entry.get()
        #zoom 			= self.axis_zoom.get()

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

        interest = ax.plot_surface(x, y, z)

        interest.set_alpha(self.a_entry.get())
        interest.set_edgecolor(self.ec_entry.get(self.ec_entry.curselection()[0]))
        interest.set_linewidth(self.ew_entry.get())
        interest.set_facecolor(self.c_entry.get(self.c_entry.curselection()[0]))

        def init():
            return interest,

        def animate(i):
            return interest

        # Animate
        ani = FuncAnimation(self.fig, animate, init_func=init,
                            interval=1, frames=500, blit=False, repeat=True)
        canvas.draw()

    def test(self, canvas, ax):
        name = self.shape_set.get()
        root.title("Geometric Modeling ({})".format(name))
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


        ax.set_xlim(-50,50)
        ax.set_ylim(-50,50)
        ax.set_zlim(-50,50)

        s[self.shape_set.get()].shape(self.fig, alpha, color, edge_c, edge_w, grid, sides,
               edges, multi_pi, radius)

    # # Defintions for animations
    #     def init():
    #         return torus
    #
    #     def animate(i):
    # # azimuth angle : 0 deg to 360 deg
    # # elev = i * n --> rotates object about the xy-plane with a magnitude of n
    # # azim = i * n --> rotates object around the z axis with a magnitude of n
    # # For top view elev = 90
    # # For side view elev = 0
    #         ax.view_init(self.scroll.get())
    #         return torus


    # Animate
    #     FuncAnimation(self.fig, animate, init_func=init,
    #                        frames=36, interval=1, blit=False, repeat=True)
        canvas.draw()

img = ImageTk.PhotoImage(file='penrose_icon.png')
root.tk.call('wm', 'iconphoto', root._w, img)

root.update()
root.update_idletasks()

geo = Geometry(master=root)
geo.mainloop()
