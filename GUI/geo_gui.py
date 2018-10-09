import matplotlib

matplotlib.use('TkAgg')
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
import interesting, hecatostoeicostohedron, hyperbolic_cylinder, dini_surface, knot, neat, spiral, testing, \
    penrose_triangle, vase, something_strange, enneper_surface
import line
import cuboctahedron, great_rombicosidodecahedron, snub_cube, truncated_cube

s = {"Prism"				: prism,
         "Pyramid"				: pyramid,
         "Sphere"				: sphere,

         "Hyperbolic Octahedon"	: hyperbolic_octahedron,
         "Hyperbolic Parabolod"	: hyperbolic_paraboloid,
         "One Sheet Hyperbolod"	: one_sheet_hyperboloid,

         "Three Dodecahedon"	: three_dodecahedron,
         "Cressant"				: cressant,
         "Funnel"				: funnel,
         "Gabriel's Hn"		: gabriel_horn,
         "Rose Spi"			: rose_spiral,
         "Shell"					: shell,
         "Tesseract"				: tesseract,

         "Breather's Surfce"	: breather_surface,
         "Kuen's Surfe"		: kuen_surface,
         "Steiner's Surfe"		: steiner_surface,
         "Boy's Surf"			: boys_surface,
         "Roman Surf"			: roman_surface,
         "Sine Surf"			: sine_surface,
         "Henneberg's Surfce"	: henneberg_surface,

         "Cube"					: cube,
         "Dodecahed"			: dodecahedron,
         "Icosahed"			: icosahedron,
         "Octahed"			: octahedron,

         "Cross Cap"				: cross_cap,
         "Klein Bot"			: klein,
         "Mobius St"			: mobius,
         "Torus"					: torus,

         "Unk Surf"			: interesting,
         "Hecatostoeicostohedron": hecatostoeicostohedron,
         "Hyperbolic Cyliner"	: hyperbolic_cylinder,
         "Dini's Surfe"		: dini_surface,
         "Knot"					: knot,
         "Neat"					: neat,
         "Spiral"				: spiral,
         "Testing"				: testing,
         "Penrose Triane"		: penrose_triangle,
         "Vase"					: vase,
         "Something Strae"		: something_strange,
         "Enneper's Surfe"		: enneper_surface,
         "Line"					: line,

         "Cuboctahed"			: cuboctahedron,
         "Great Rombicosidodecahedron": great_rombicosidodecahedron,
         "Snub Cube"				: snub_cube,
         "Truncated Ce"		: truncated_cube,
         #		"Great Dodecahedron"	: 'great_dodecahedron',
         #		"Great Icosahedron"		: 'great_icosahedron'

}


dim = "#303030"  #   ackground
dimf = "#00C0FF"  #   ont Color

disa = "#d400ff" #   isabled Text

c


ss Geometry(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self,mas ter)
        self.createWidgets()

    def createWidgets(self):
        global icon
        self.fig = plt.figure(figsize=(5, 5))
        ax = p3.Axes3D(self.fig)
        ax.set_facecolor('black')
        plt.axis('off')
        canvas = FigureCanvasTkAgg(self.fig,roo t)
        canvas.get_tk_widget().grid(row=0,col umn=0, sticky='new')
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
            self.c_entry = askcolor(title="Face Color")[1]
            self.fck.config(bg=self.c_entry)
            return self.c_entry

        def FaceColor2(self):
            self.c_entry2 = askcolor(title="Face Color 2")[1]
            self.f2.config(bg=self.c_entry2)
            return self.c_entry2

        def FaceColor3(self):
            self.c_entry3 = askcolor(title="Face Color 3")[1]
            self.f3.config(bg=self.c_entry3)
            return self.c_entry3

        def EdgeColor(self):
            self.ec_entry = askcolor(title="Edge Color")[1]
            self.eck.config(bg=self.ec_entry)
            return self.ec_entry

        def popup_shape():
            top = tk.Toplevel(self)
            top.title("Shapes")
            top.config(background=dim)
            top.tk.call('wm', 'iconphoto', top._w, icon)

            pop = tk.Button(top, text="POP!", command=top.destroy)
            pop.grid(row=0, column=0, sticky='new')
            pop.config(bg=dim,f g=dimf, activebackground=dim, highlightbackground=dimf, activeforeground=dimf)

            plotter = tk.Button(top, text="Plot", command=lambda: self.plot(canvas,a x))
            plotter.grid(row=0, column=2, sticky="new")
            plotter.config(bg=dim,f g=dimf, activebackground=dim, highlightbackground=dimf, activeforeground=dimf)

            if self.two_three.get() == "3d":
                prism = tk.Radiobutton(top, text="Prism",v ariable=self.shape_set, value="Prism")
                prism.grid(row=1, column=0, sticky="w")

                pyram = tk.Radiobutton(top, text="Pyramid",v ariable=self.shape_set, value="Pyramid")
                pyram.grid(row=2, column=0, sticky="w")

                spher = tk.Radiobutton(top, text="Sphere",v ariable=self.shape_set, value="Sphere")
                spher.grid(row=3, column=0, sticky="w")

                ##
                hy = tk.Label(top, text="--- Hyperbolic Objects ---", font=('Times', 12, 'bold'))
                hy.grid(row=4, column=0, sticky="nsew")
                hy.config(bg=dim, fg=dimf, activebackground=dim)

                hyoct = tk.Radiobutton(top, text="Hyperbolic Octahedron", variable=self.shape_set,
                                       value="Hyperbolic Octahedron")
                hyoct.grid(row=5, column=0 , sticky="w")

                hypar = tk.Radiobutton(top, text="Hyperbolic Paraboliod", variable=self.shape_set,
                                       value="Hyperbolic Paraboliod")
                hypar.grid(row=6, column=0, sticky="w")

                onesh = tk.Radiobutton(top, text="One Sheet Hyperboliod", variable=self.shape_set,
                                       value="One Sheet Hyperboliod")
                onesh.grid(row=7, column=0, sticky="w")

                ##
                misc = tk.Label(top, text="--- Miscellaneous ---", font=('Times', 12, 'bold'))
                misc.grid(row=8, column=0, sticky='nsew')
                misc.config(bg=dim, fg=dimf, activebackground=dim)

                three = tk.Radiobutton(top, text="Three Dodecahedron", variable=self.shape_set,
                                       value="Three Dodecahedron")
                three.grid(row=9, column=0, sticky="w")

                cress = tk.Radiobutton(top, text="Cressant", variable=self.shape_set, value="Cressant")
                cress.grid(row=10, column=0, sticky="w")

                funne = tk.Radiobutton(top, text="Funnel", variable=self.shape_set, value="Funnel")
                funne.grid(row=11, column=0, sticky="w")

                gabri = tk.Radiobutton(top, text="Gabriel's Horn", variable=self.shape_set, value="Gabriel's Horn")
                gabri.grid(row=12, column=0, sticky="w")

                roses = tk.Radiobutton(top, text="Rose Spiral", variable=self.shape_set, value="Rose Spiral")
                roses.grid(row=13, column=0, sticky="w")

                shell = tk.Radiobutton(top, text="Shell", variable=self.shape_set, value="Shell")
                shell.grid(row=14, column=0, sticky="w")

                tesse = tk.Radiobutton(top, text="Tesseract", variable=self.shape_set, value="Tesseract")
                tesse.grid(row=15, column=0, sticky="w")

                ##
                surf = tk.Label(top, text="--- Surfaces ---", font=('Times', 12, 'bold'))
                surf.grid(row=1, column=2, sticky='new')
                surf.config(bg=dim, fg=dimf, activebackground=dim)

                breat = tk.Radiobutton(top, text="Breather's Surface", variable=self.shape_set,
                                       value="Breather's Surface")
                breat.grid(row=2, column=2, sticky="w")

                kuens = tk.Radiobutton(top, text="Kuen's Surface", variable=self.shape_set, value="Kuen's Surface")
                kuens.grid(row=3, column=2, sticky="w")

                stein = tk.Radiobutton(top, text="Steiner's Surface", variable=self.shape_set,
                                       value="Steiner's Surface")
                stein.grid(row=4, column=2, sticky="w")

                boyss = tk.Radiobutton(top, text="Boy's Surface", variable=self.shape_set, value="Boy's Surface")
                boyss.grid(row=5, column=2, sticky="w")

                roman = tk.Radiobutton(top, text="Roman Surface", variable=self.shape_set, value="Roman Surface")
                roman.grid(row=6, column=2, sticky="w")

                sines = tk.Radiobutton(top, text="Sine Surface", variable=self.shape_set, value="Sine Surface")
                sines.grid(row=7, column=2, sticky="w")

                henne = tk.Radiobutton(top, text="Henneberg's Surface", variable=self.shape_set,
                                       value="Henneberg's Surface")
                henne.grid(row=7, column=2, sticky="w")

                ##
                topo = tk.Label(top, text="--- Topological ---", font=('Times', 12, 'bold'))
                topo.grid(row=11, column=2, sticky='nsew')
                topo.config(bg=dim, fg=dimf, activebackground=dim)

                cross = tk.Radiobutton(top, text="Cross Cap", variable=self.shape_set, value="Cross Cap")
                cross.grid(row=12, column=2, sticky="w")

                klein = tk.Radiobutton(top, text="Klein Bottle", variable=self.shape_set, value="Klein Bottle")
                klein.grid(row=13, column=2, sticky="w")

                mobiu = tk.Radiobutton(top, text="Mobius Strip", variable=self.shape_set, value="Mobius Strip")
                mobiu.grid(row=14, column=2, sticky="w")

                torus = tk.Radiobutton(top, text="Torus", variable=self.shape_set, value="Torus")
                torus.grid(row=15, column=2, sticky="w")

                ##
                dev = tk.Label(top, text="--- In Development ---", font=('Times', 12, 'bold'))
                dev.grid(row=1, column=4, sticky='nsew')
                dev.config(bg=dim, fg=dimf, activebackground=dim)

                unksu = tk.Radiobutton(top, text="Unk Surface", variable=self.shape_set, value="Unk Surface")
                unksu.grid(row=2, column=4, sticky="w")

                polyh = tk.Radiobutton(top, text="Hecatostoeicostohedron", variable=self.shape_set,
                                       value="Hecatostoeicostohedron")
                polyh.grid(row=3, column=4, sticky="w")

                hycyl = tk.Radiobutton(top, text="Hyperbolic Cylinder", variable=self.shape_set,
                                       value="Hyperbolic Cylinder")
                hycyl.grid(row=4, column=4, sticky="w")

                dinis = tk.Radiobutton(top, text="Dini's Surface", variable=self.shape_set, value="Dini's Surface")
                dinis.grid(row=5, column=4, sticky="w")

                knot = tk.Radiobutton(top, text="Knot", variable=self.shape_set, value="Knot")
                knot.grid(row=6, column=4, sticky="w")

                neat = tk.Radiobutton(top, text="Neat", variable=self.shape_set, value="Neat")
                neat.grid(row=7, column=4, sticky="w")

                spira = tk.Radiobutton(top, text="Spiral", variable=self.shape_set, value="Spiral")
                spira.grid(row=8, column=4, sticky="w")

                test = tk.Radiobutton(top, text="Testing", variable=self.shape_set, value="Testing")
                test.grid(row=9, column=4, sticky="w")

                vase = tk.Radiobutton(top, text="Vase", variable=self.shape_set, value="Vase")
                vase.grid(row=10, column=4, sticky="w")

                somet = tk.Radiobutton(top, text="Something Strange", variable=self.shape_set,
                                       value="Something Strange")
                somet.grid(row=11, column=4, sticky="w")

                ennep = tk.Radiobutton(top, text="Enneper's Surface", variable=self.shape_set,
                                       value="Enneper's Surface")
                ennep.grid(row=12, column=4, sticky="w")

                penro = tk.Radiobutton(top, text="Penrose Triangle", variable=self.shape_set, value="Penrose Triangle")
                penro.grid(row=13, column=4, sticky="w")

                ##
                arch = tk.Label(top, text="--- Archimedean Solids ---", font=('Times', 12, 'bold'))
                arch.grid(row=1, column=5, sticky='nsew')
                arch.config(bg=dim, fg=dimf, activebackground=dim)

                cuboc = tk.Radiobutton(top, text="Cuboctahedron", variable=self.shape_set, value="Cuboctahedron")
                cuboc.grid(row=2, column=5, sticky="w")

                grrom = tk.Radiobutton(top, text="Great\n Rombicosidodecahedron", variable=self.shape_set,
                                       value="Great Rombicosidodecahedron")
                grrom.grid(row=3, column=5, sticky="w")

                scube = tk.Radiobutton(top, text="Snub Cube", variable=self.shape_set, value="Snub Cube")
                scube.grid(row=4, column=5, sticky="w")

                tcube = tk.Radiobutton(top, text="Truncated Cube", variable=self.shape_set, value="Truncated Cube")
                tcube.grid(row=5, column=5, sticky="w")

                ##
                plato = tk.Label(top, text="--- Platonic Solids ---", font=('Times', 12, 'bold'))
                plato.grid(row=6, column=5, sticky='nsew')
                plato.config(bg=dim, fg=dimf, activebackground=dim)

                cube = tk.Radiobutton(top, text="Cube", variable=self.shape_set, value="Cube")
                cube.grid(row=7, column=5, sticky="w")

                dodec = tk.Radiobutton(top, text="Dodecahedron", variable=self.shape_set, value="Dodecahedron")
                dodec.grid(row=8, column=5, sticky="w")
                icosa = tk.Radiobutton(top, text="Icosahedron", variable=self.shape_set, value="Icosahedron")
                icosa.grid(row=9, column=5, sticky="w")

                octah = tk.Radiobutton(top, text="Octahedron", variable=self.shape_set, value="Octahedron")
                octah.grid(row=10, column=5, sticky="w")

                # grico = tk.Radiobutton(top, text="Great Icosahedron",        variable=self.shape_set, value="Great Icosahedron")
                #				grico.grid(row=15,column=4,sticky="w")
                #				grdod = tk.Radiobutton(top, text="Great Dodecahedron",        variable=self.shape_set, value="Great Dodecahedron")
                #				grdod.grid(row=16,column=4,sticky="w")
                # cube_hover = CreateToolTip(cube, ImageTk.PhotoImage(file="./Visual/Cube.png"),"test")

                def shape_config():
                    fam = [prism, pyram, spher]
                    hyp = [hyoct, hypar, onesh]
                    mis = [three, cress, funne, gabri, roses, shell, tesse]
                    sur = [breat, kuens, stein, boyss, roman, sines, henne]
                    top = [cross, klein, mobiu, torus]
                    dev = [unksu, polyh, hycyl, dinis, knot, neat, spira, test, vase, somet, ennep, penro]
                    arc = [cuboc, grrom, scube, tcube]
                    pla = [cube, dodec, icosa, octah]
                    sh_all = fam + hyp + mis + sur + top + dev + arc + pla
                    for m in sh_all:
                        m.config(bg=dim, fg=dimf, activebackground=dim, highlightthickness=0, activeforeground=dimf,
                                 selectcolor=dim)

                return shape_config()
                # shape_config()

                self.shape_set.set("Penrose Triangle")

            elif self.two_three.get() == "2d":
                line = tk.Radiobutton(top, text="Line", variable=self.shape_set, value="Line")
                line.grid(row=1, column=0, sticky='w')

        def popup_save():
            top = tk.Toplevel(self)
            top.geometry("300x200")
            top.title("Save Figure")
            top.tk.call('wm', 'iconphoto', top._w, icon)
            top.config(background=dim)

            pop = tk.Button(top, text="POP!", command=top.destroy)
            pop.grid(row=0, column=0)
            pop.config(bg=dim, fg=dimf, activebackground=dim, highlightbackground=dimf, activeforeground=dimf)

            self.format_save = tk.StringVar()

            def img():
                plt.savefig.format = self.format_save.get()

            # def save_mp4():
            #	plt.axis("off")
            #	ax.set_facecolor('black')
            #	ax.grid(False)
            #	ax.axis('off')
            #	ax.set_xticks([])
            #	ax.set_yticks([])
            #	ax.set_zticks([])

            #	plt.axis('off')
            #	plt.axis('equal')

            #	def init():
            #		return testing.test,

            #	def animate(i):
            #		ax.view_init(elev=i, azim=i)
            #		return testing.test,

            # Animate
            #	ani = FuncAnimation(self.fig, animate, init_func=init, interval=1, frames=500, repeat=True)

            #	Writer = writers['ffmpeg']
            #	writer = Writer(fps=15, bitrate=1800)
            #	ani.save('Testers.mp4',writer=writer)

            #	plt.ion()
            #	plt.show()
            #	sleep(0)
            #	plt.close()

            png = tk.Radiobutton(top, text="png", variable=self.format_save, value="png", command=img, width=5)
            png.grid(row=1, column=0)
            png.config(bg=dim, fg=dimf, activebackground=dim, highlightthickness=0, activeforeground=dimf,
                       selectcolor=dim)

            jpg = tk.Radiobutton(top, text="jpg", variable=self.format_save, value="jpg", command=img, width=5)
            jpg.grid(row=1, column=1)
            jpg.config(bg=dim, fg=dimf, activebackground=dim, highlightthickness=0, activeforeground=dimf,
                       selectcolor=dim)

            # mp4 = tk.Radiobutton(top, text="mp4", variable=self.format_save,    value="mp4", width=5)
            # mp4.grid(row=2, column=0)
            # mp4.config(bg=dim, 	fg=dimf, activebackground=dim, highlightthickness=0, activeforeground=dimf, selectcolor=dim)

            save_img = tk.Button(top, text="save img",
                                 command=lambda: plt.savefig("{}.png".format(s[self.shape_set.get()])))
            # plt.savefig("{}.{}".format(self.shape_set.get(),self.format_save.get()), format=str(self.format_save.get())))
            save_img.grid(row=0, column=1)
            save_img.config(bg=dim, fg=dimf, activebackground=dim, highlightbackground=dimf, activeforeground=dimf)

            # save_vid = tk.Button(top, text="save video", command=lambda: save_mp4())
            # save_vid.grid(row=0, column=2)
            # save_vid.config(bg=dim, fg=dimf, activebackground=dim, highlightbackground=dimf, activeforeground=dimf)

            self.format_save.set("png")

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

        self.eck = tk.Message(root, width=200000000,
                              text=" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" ", borderwidth=5,
                              relief=tk.GROOVE)
        self.eck.grid(row=0, column=1, sticky='new', pady=60)

        # Face Color
        self.face = tk.Button(text="Face Color", command=lambda: FaceColor(self))
        self.face.grid(row=0, column=2, sticky='new', pady=30, padx=0)

        self.fck = tk.Message(root, width=200000000,
                              text=" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" ", borderwidth=5,
                              relief=tk.GROOVE)
        self.fck.grid(row=0, column=2, sticky='new', pady=60, padx=0)

        # Edge Color
        self.face2 = tk.Button(text="Face Color 2", command=lambda: FaceColor2(self), state=tk.NORMAL)
        self.face2.grid(row=0, column=3, sticky='new', pady=30, padx=0)

        self.f2 = tk.Message(root, width=2000000, text=" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" ",
                             borderwidth=5, relief=tk.GROOVE)
        self.f2.grid(row=0, column=3, sticky='new', pady=60, padx=0)

        # Face Color
        self.face3 = tk.Button(text="Face Color 3", command=lambda: FaceColor3(self), state=tk.NORMAL)
        self.face3.grid(row=0, column=4, sticky='new', pady=30, padx=0)

        self.f3 = tk.Message(root, width=2000000, text=" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" ",
                             borderwidth=5, relief=tk.GROOVE)
        self.f3.grid(row=0, column=4, sticky='new', pady=60, padx=0)

        # Plotting
        self.plotting = tk.Button(root, text="Update", command=lambda: self.plot(canvas, ax), height=4)
        self.plotting.grid(row=0, column=1, columnspan=2, sticky="new", pady=430)

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
        self.shapes.grid(row=0, column=3, columnspan=2, sticky='new', pady=430)

        def dark(self):
            scales = [self.a_entry, self.h_entry, self.si_entry, self.ed_entry, self.pi_entry, self.ew_entry,
                      self.ram_entry, self.raa_entry]
            labels = [self.a_label, self.h_label, self.si_label, self.ed_label, self.pi_label, self.ew_label,
                      self.ram_label, self.raa_label]
            radio = [self.grid_on, self.grid_off, self.two_space, self.three_space, self.rot_on, self.rot_off]
            button = [self.plotting, self.face, self.face2, self.face3, self.edge, self.shapes]
            menus = [menu, filemenu]

            root.config(background=dim)
            # Scales
            for m in scales:
                m.config(bg=dim, fg=dimf, activebackground=dim, highlightthickness=0, troughcolor=dimf)
            for n in labels:
                n.config(bg=dim, fg=dimf, activebackground=dim)
            for o in radio:
                o.config(bg=dim, fg=dimf, activebackground=dim, highlightthickness=0, activeforeground=dimf,
                         selectcolor=dim)
            for p in button:
                p.config(bg=dim, fg=dimf, activebackground=dim, highlightbackground=dimf, activeforeground=dimf)
            for q in menus:
                q.config(bg=dim, fg=dimf, activebackground=dim, activeforeground=dimf)

        return dark(self)

    def plot(self, canvas, ax):
        try:
            edge_c = self.ec_entry
        except AttributeError:
            edge_c = "#f608ff"
            self.eck.config(bg=edge_c)
        try:
            color = self.c_entry
        except AttributeError:
            color = "#00c4ff"
            self.fck.config(bg=color)
        try:
            color2 = self.c_entry2
        except AttributeError:
            color2 = "#000001"
            self.f2.config(bg=color2)
        try:
            color3 = self.c_entry3
        except AttributeError:
            color3 = "#000000"
            self.f3.config(bg=color3)

        alpha = self.a_entry.get()
        grid = self.grid_axis.get()
        edge_w = self.ew_entry.get()
        edges = self.ed_entry.get()
        sides = self.si_entry.get()
        multi_pi = self.pi_entry.get()
        radiusa = self.raa_entry.get()
        radiusm = self.ram_entry.get()
        rot = self.rot.get()
        save = self.format_save.get()
        height = self.h_entry.get()

        name = self.shape_set.get()
        root.title("Geometric Modeling ({})".format(name))

        ax.clear()
        plt.cla()
        plt.clf()

        try:  # Count: 14
            s[self.shape_set.get()].shape(self.fig, alpha, color, edge_c, edge_w, grid, sides, edges, multi_pi, radiusm,
                                          radiusa, color2, color3, height, rot, save)
        except KeyError:
            name = interesting.name
            root.title("Geometric Modeling ({})".format(name))
            testing.shape(self.fig, alpha, color, edge_c, edge_w, grid, sides, edges, multi_pi, rot, save)

            active = [self.si_entry, self.ed_entry, self.pi_entry]
            active_label = [self.si_label, self.ed_label, self.pi_label]
            disable = [self.ram_entry, self.raa_entry, self.h_entry]
            disable_label = [self.ram_label, self.raa_label, self.h_label]
            color = [self.face2, self.face3]
            color_label = [self.f2, self.f3]

            for m in disable:
                m.config(state=tk.DISABLED, bg=dim, fg=dim, activebackground=dim, troughcolor=dim)
                for n in disable_label:
                    n.config(fg=disa)
                    for o in color:
                        o.config(state=tk.DISABLED, highlightbackground=disa)
                        for p in color_label:
                            p.config(bg=dim, fg=dim, relief=tk.RIDGE)
            for m in active:
                m.config(state=tk.ACTIVE, bg=dim, fg=dimf, activebackground=dim, troughcolor=dimf)
                for n in active_label:
                    n.config(fg=dimf)
        except TypeError:
            try:  # Count: 12
                s[self.shape_set.get()].shape(self.fig, alpha, color, edge_c, edge_w, grid, sides, edges, multi_pi,
                                              radiusm, radiusa, height)

                active = [self.si_entry, self.ed_entry, self.pi_entry, self.raa_entry, self.ram_entry, self.h_entry]
                active_label = [self.si_label, self.ed_label, self.pi_label, self.raa_label, self.ram_label,
                                self.h_label]
                color = [self.face2, self.face3]
                color_label = [self.f2, self.f3]

                for n in color:
                    n.config(state=tk.DISABLED, highlightbackground=disa)
                    for m in color_label:
                        m.config(bg=dim, fg=dim, relief=tk.RIDGE)

                for n in active:
                    n.config(state=tk.ACTIVE, bg=dim, fg=dimf, activebackground=dim, troughcolor=dimf)
                    for m in active_label:
                        m.config(fg=dimf)

            except TypeError:
                try:  # Count: 11
                    s[self.shape_set.get()].shape(self.fig, alpha, color, edge_c, edge_w, grid, sides, edges, multi_pi,
                                                  radiusm, height)
                    active = [self.si_entry, self.ed_entry, self.pi_entry, self.ram_entry, self.h_entry]
                    active_label = [self.si_label, self.ed_label, self.pi_label, self.ram_label, self.h_label]
                    disable = [self.raa_entry]
                    disable_label = [self.raa_label]
                    color = [self.face2, self.face3]
                    color_label = [self.f2, self.f3]

                    for m in disable:
                        m.config(state=tk.DISABLED, bg=dim, fg=dim, activebackground=dim, troughcolor=dim)
                        for n in disable_label:
                            n.config(fg=disa)
                            for o in color:
                                o.config(state=tk.DISABLED, highlightbackground=disa)
                                for p in color_label:
                                    p.config(bg=dim, fg=dim, relief=tk.RIDGE)

                    for m in active:
                        m.config(state=tk.ACTIVE, bg=dim, fg=dimf, activebackground=dim, troughcolor=dimf)
                        for n in active_label:
                            n.config(fg=dimf)

                except TypeError:
                    try:  # Count: 10
                        s[self.shape_set.get()].shape(self.fig, alpha, color, edge_c, edge_w, grid, sides, edges,
                                                      multi_pi, radiusm)
                        active = [self.si_entry, self.ed_entry, self.pi_entry, self.ram_entry]
                        active_label = [self.si_label, self.ed_label, self.pi_label, self.ram_label]
                        disable = [self.raa_entry, self.h_entry]
                        disable_label = [self.raa_label, self.h_label]
                        color = [self.face2, self.face3]
                        color_label = [self.f2, self.f3]

                        for m in disable:
                            m.config(state=tk.DISABLED, bg=dim, fg=dim, activebackground=dim, troughcolor=dim)
                            for n in disable_label:
                                n.config(fg=disa)
                                for o in color:
                                    o.config(state=tk.DISABLED, highlightbackground=disa)
                                    for p in color_label:
                                        p.config(bg=dim, fg=dim, relief=tk.RIDGE)

                        for m in active:
                            m.config(state=tk.ACTIVE, bg=dim, fg=dimf, activebackground=dim, troughcolor=dimf)
                            for n in active_label:
                                n.config(fg=dimf)

                    except TypeError:
                        try:  # Count: 9
                            s[self.shape_set.get()].shape(self.fig, alpha, color, edge_c, edge_w, grid, sides, edges,
                                                          multi_pi)
                            active = [self.si_entry, self.ed_entry, self.pi_entry]
                            active_label = [self.si_label, self.ed_label, self.pi_label]
                            disable = [self.raa_entry, self.h_entry, self.ram_entry]
                            disable_label = [self.raa_label, self.h_label, self.ram_label]
                            color = [self.face2, self.face3]
                            color_label = [self.f2, self.f3]

                            for m in disable:
                                m.config(state=tk.DISABLED, bg=dim, fg=dim, activebackground=dim, troughcolor=dim)
                                for n in disable_label:
                                    n.config(fg=disa)
                                    for o in color:
                                        o.config(state=tk.DISABLED, highlightbackground=disa)
                                        for p in color_label:
                                            p.config(bg=dim, fg=dim, relief=tk.RIDGE)

                            for m in active:
                                m.config(state=tk.ACTIVE, bg=dim, fg=dimf, activebackground=dim, troughcolor=dimf)
                                for n in active_label:
                                    n.config(fg=dimf)

                        except TypeError:
                            try:  # Count: 8
                                s[self.shape_set.get()].shape(self.fig, alpha, color, edge_c, edge_w, grid, radiusm,
                                                              color2)
                                active = [self.ram_entry]
                                active_label = [self.ram_label]
                                disable = [self.si_entry, self.ed_entry, self.pi_entry, self.raa_entry, self.h_entry]
                                disable_label = [self.si_label, self.ed_label, self.pi_label, self.raa_label,
                                                 self.h_label]
                                color = [self.face2, self.face3]
                                color_label = [self.f2, self.f3]

                                for m in disable:
                                    m.config(state=tk.DISABLED, bg=dim, fg=dim, activebackground=dim, troughcolor=dim)
                                    for n in disable_label:
                                        n.config(fg=disa)
                                        for o in color:
                                            self.face3.config(state=tk.DISABLED, highlightbackground=disa)
                                            for p in color_label:
                                                self.f3.config(bg=dim, fg=dim, relief=tk.RIDGE)

                                for m in active:
                                    m.config(state=tk.ACTIVE, bg=dim, fg=dimf, activebackground=dim, troughcolor=dimf)
                                    for n in active_label:
                                        n.config(fg=dimf)
                                        for o in color:
                                            self.face2.config(state=tk.ACTIVE, highlightbackground=dimf)
                                            for p in color_label:
                                                self.f2.config(relief=tk.GROOVE)

                            except ValueError:
                                s[self.shape_set.get()].shape(self.fig, alpha, color, edge_c, edge_w, grid, sides,
                                                              edges)
                                active = [self.si_entry, self.ed_entry]
                                active_label = [self.si_label, self.ed_label]
                                disable = [self.pi_entry, self.raa_entry, self.h_entry, self.ram_entry]
                                disable_label = [self.pi_label, self.raa_label, self.h_label, self.ram_label]
                                color = [self.face2, self.face3]
                                color_label = [self.f2, self.f3]

                                for m in disable:
                                    m.config(state=tk.DISABLED, bg=dim, fg=dim, activebackground=dim, troughcolor=dim)
                                    for n in disable_label:
                                        n.config(fg=disa)
                                        for o in color:
                                            o.config(state=tk.DISABLED, highlightbackground=disa)
                                            for p in color_label:
                                                p.config(bg=dim, fg=dim, relief=tk.RIDGE)

                                for m in active:
                                    m.config(state=tk.ACTIVE, bg=dim, fg=dimf, activebackground=dim, troughcolor=dimf)
                                    for n in active_label:
                                        n.config(fg=dimf)

                            except TypeError:
                                try:  # Count: 8
                                    s[self.shape_set.get()].shape(self.fig, alpha, color, edge_c, edge_w, grid, color2,
                                                                  color3)
                                    disable = [self.pi_entry, self.raa_entry, self.h_entry, self.ram_entry,
                                               self.si_entry, self.ed_entry]
                                    disable_label = [self.pi_label, self.raa_label, self.h_label, self.ram_label,
                                                     self.si_label, self.ed_label]
                                    color = [self.face2, self.face3]
                                    color_label = [self.f2, self.f3]

                                    for m in disable:
                                        m.config(state=tk.DISABLED, bg=dim, fg=dim, activebackground=dim,
                                                 troughcolor=dim)
                                        for n in disable_label:
                                            n.config(fg=disa)
                                            for o in color:
                                                o.config(state=tk.ACTIVE, highlightbackground=dimf)
                                                for p in color_label:
                                                    p.config(relief=tk.GROOVE)

                                except TypeError:
                                    try:  # Count:7
                                        s[self.shape_set.get()].shape(self.fig, alpha, color, edge_c, edge_w, grid,
                                                                      radiusm)
                                        active = [self.ram_entry]
                                        active_label = [self.ram_label]
                                        disable = [self.pi_entry, self.raa_entry, self.h_entry, self.si_entry,
                                                   self.ed_entry]
                                        disable_label = [self.pi_label, self.raa_label, self.h_label, self.si_label,
                                                         self.ed_label]
                                        color = [self.face2, self.face3]
                                        color_label = [self.f2, self.f3]

                                        for m in disable:
                                            m.config(state=tk.DISABLED, bg=dim, fg=dim, activebackground=dim,
                                                     troughcolor=dim)
                                            for n in disable_label:
                                                n.config(fg=disa)
                                                for o in color:
                                                    o.config(state=tk.DISABLED, highlightbackground=disa)
                                                    for p in color_label:
                                                        p.config(bg=dim, fg=dim, relief=tk.RIDGE)

                                        for m in active:
                                            m.config(state=tk.ACTIVE, bg=dim, fg=dimf, activebackground=dim,
                                                     troughcolor=dimf)
                                            for n in active_label:
                                                n.config(fg=dimf)

                                    except TypeError:
                                        try:  # Count: 7
                                            s[self.shape_set.get()].shape(self.fig, alpha, color, edge_c, edge_w, grid,
                                                                          color2)
                                            disable = [self.pi_entry, self.raa_entry, self.h_entry, self.si_entry,
                                                       self.ed_entry, self.ram_entry]
                                            disable_label = [self.pi_label, self.raa_label, self.h_label, self.si_label,
                                                             self.ed_label, self.ram_label]
                                            color = [self.face2, self.face3]
                                            color_label = [self.f2, self.f3]

                                            for m in disable:
                                                m.config(state=tk.DISABLED, bg=dim, fg=dim, activebackground=dim,
                                                         troughcolor=dim)
                                                for n in disable_label:
                                                    n.config(fg=disa)
                                                    for o in color:
                                                        self.face3.config(state=tk.DISABLED, highlightbackground=disa)
                                                        for p in color_label:
                                                            self.f3.config(bg=dim, fg=dim, relief=tk.RIDGE)

                                            for o in color:
                                                self.face2.config(state=tk.ACTIVE, highlightbackground=dimf)
                                                for p in color_label:
                                                    self.f2.config(relief=tk.GROOVE)

                                        except TypeError:
                                            try:  # Count: 6
                                                s[self.shape_set.get()].shape(self.fig, alpha, color, edge_c, edge_w,
                                                                              grid)
                                                disable = [self.pi_entry, self.raa_entry, self.h_entry, self.si_entry,
                                                           self.ed_entry, self.ram_entry]
                                                disable_label = [self.pi_label, self.raa_label, self.h_label,
                                                                 self.si_label, self.ed_label, self.ram_label]
                                                color = [self.face2, self.face3]
                                                color_label = [self.f2, self.f3]

                                                for m in disable:
                                                    m.config(state=tk.DISABLED, bg=dim, fg=dim, activebackground=dim,
                                                             troughcolor=dim)
                                                    for n in disable_label:
                                                        n.config(fg=disa)
                                                        for o in color:
                                                            o.config(state=tk.DISABLED, highlightbackground=disa)
                                                            for p in color_label:
                                                                p.config(bg=dim, fg=dim, relief=tk.RIDGE)

                                            except NameError:
                                                print("FUCKING SHIT")
        canvas.draw()


if __name__ == '__main__':
    root = tk.Tk()

    root.title("Geometric Models")
    root.geometry("932x501")
    icon = ImageTk.PhotoImage(file='penrose_icon.png')

    root.tk.call('wm', 'iconphoto', root._w, icon)
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