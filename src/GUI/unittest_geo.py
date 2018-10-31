import geo_gui
from geo_gui import s
import geo_windows
import matplotlib
import matplotlib.pyplot as plt
import unittest
import atexit
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import warnings
import mpl_toolkits.mplot3d.axes3d as p3
import sys

try:
	import tkinter as tk
	from tkinter.colorchooser import askcolor
except ImportError:
	import Tkinter as tk
	from tkColorChooser import askcolor

##
sys.path.append('../In Development/')

sys.path.append('../Current Models/')
sys.path.append('../Current Models/Hyperbolic/')
sys.path.append('../Current Models/Misc./')
sys.path.append('../Current Models/Platonic Solids/')
sys.path.append('../Current Models/Surfaces/')
sys.path.append('../Current Models/Topological/')
sys.path.append('../Current Models/Two Space/')
sys.path.append('../Current Models/Archimedean/')

import prism, pyramid, sphere
import hyperbolic_octahedron, hyperbolic_paraboloid, one_sheet_hyperboloid, hyperbolic_helicoid, hyperbolic_cylinder
import three_dodecahedron, crescent, funnel, gabriel_horn, rose_spiral, shell, tesseract, spiral, seashell, steinbach_screw
import breather_surface, kuen_surface, steiner_surface, boys_surface, roman_surface, sine_surface, henneberg_surface, unk_surface, dini_surface, enneper_surface, corkscrew_surface, shoe_surface
import cube, dodecahedron, icosahedron, octahedron
import cross_cap, klein, mobius, torus
import neat, testing, vase, something_strange, great_dodecahedron
import cuboctahedron, great_rombicosidodecahedron, snub_cube, truncated_cube, disdyakis_triacontahedron, great_icosahedron
import deltoid, log_spiral, parabola, penrose_square, penrose_circle, line, penrose_triangle, polygon, ellipse

gen1 	= [prism, sphere]
gen2 	= [pyramid, funnel, gabriel_horn, dini_surface]
arc1	= [cuboctahedron, snub_cube, truncated_cube, tesseract]
arc2 	= [disdyakis_triacontahedron, cube, dodecahedron, icosahedron, octahedron, mobius]
arc3	= [great_rombicosidodecahedron, three_dodecahedron]
hyp1 	= [hyperbolic_helicoid, hyperbolic_octahedron, hyperbolic_paraboloid, one_sheet_hyperboloid,
		   crescent, rose_spiral, seashell, shell, spiral, steinbach_screw, breather_surface,
		   corkscrew_surface, kuen_surface, shoe_surface]
hyp2 	= [hyperbolic_cylinder]
mis1	= [boys_surface, enneper_surface, henneberg_surface, roman_surface, steiner_surface,
		   unk_surface, cross_cap, klein]
sur1	= [sine_surface, torus]

two1	= [ellipse]
two2	= [log_spiral, parabola, deltoid]
two3	= [line]
two4	= [penrose_circle, penrose_square, penrose_triangle]

fig = plt.figure(figsize=(8, 8), facecolor="black", edgecolor="white")
class TestObject(unittest.TestCase):
	def test_general(self):
		geo_gui.Geometry(tk.Tk())

class TestShapes(unittest.TestCase):
	def test_shape3d(self):
		def general(*args):
			for m in range(len(gen1)):
				gen1[m].shape(*args, 10, 10, 2, 1, 1, 1)
			for m in range(len(gen2)):
				gen2[m].shape(*args, 10, 10, 2, 1, 1)
			for m in range(len(arc1)):
				arc1[m].shape(*args, 'gold')
			for m in range(len(arc2)):
				arc2[m].shape(*args)
			for m in range(len(arc3)):
				arc3[m].shape(*args, 'gold', 'red')
			for m in range(len(hyp1)):
				hyp1[m].shape(*args, 10, 10)
			for m in range(len(hyp2)):
				hyp2[m].shape(*args, 10, 10, 1, 1)
			for m in range(len(mis1)):
				mis1[m].shape(*args, 10, 10, 2)
			for m in range(len(sur1)):
				sur1[m].shape(*args, 10, 10, 2, 1)
		return general(fig, 0.5, 'deepskyblue', 'white', 1, 'off')
	def test_shape2d(self):
		def twospace(*args):
			for m in range(len(two1)):
				two1[m].shape(*args, 1, 1)
			for m in range(len(two2)):
				two2[m].shape(*args, 1)
			for m in range(len(two3)):
				two3[m].shape(*args, 1, 1, 1)
			for m in range(len(two4)):
				two4[m].shape(*args)
		return twospace(fig, 'white', 1, 'off')

if __name__ == "__main__":

	unittest.main(verbosity=0)
