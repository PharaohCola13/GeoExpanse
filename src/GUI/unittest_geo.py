import geo_gui
import geo_linux
import geo_windows
from geo_gui import s as s_dev
from geo_linux import s as s_linu
from geo_windows import s as s_wind
import matplotlib
import matplotlib.pyplot as plt
import unittest
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

root = tk.Tk()
root_width = 920
root_height = 530	
root.geometry(str(root_width) + "x" + str(root_height))
root.maxsize(str(root_width), str(root_height))
root.minsize(str(500), str(root_height))

fig = plt.figure(figsize=(8, 8), facecolor="black", edgecolor="white")
canvas = FigureCanvasTkAgg(fig ,root)
ax = p3.Axes3D(fig)

app_dev = geo_gui.Geometry(root)
#app_lin = geo_linux.Geometry(root)
#app_win = geo_windows.Geometry(root)

class Superfical(unittest.TestCase):
	def test_widget(self):
		try:	
			app_dev.createWidgets(root)
			print("\033[32m" + "Superfical Test: Passed")
			print("\033[0m")
		except:
			print("\033[91m" + "Superfical Test: Failed")
			print("\033[0m")

class TestObject(unittest.TestCase):
	def test_shape(self):
		passed = []
		failed = []
		if not sys.warnoptions:
			warnings.simplefilter("ignore")
		print("---" * 3 + " Individual Shape Test: Start " + "---" * 3)
		for k,v in sorted(s_dev.iteritems()):	
			try:		
				app_dev.plot(canvas, ax, s_dev[k])
				print("\033[32m{0:30}: ".ljust(20).format(k) + "\033[32m Cleared")
				passed.append(k)
				#print("\033[0m")
			except TypeError:
				print("\033[91m{0:30}: ".ljust(10).format(k) + "\033[91m Failed")
				failed.append(k)
		net = len(passed) - 1
		tot = len(passed) + len(failed) - 1
		#print("{} out of {} Models Have Passed ".format(net, tot))
		print("\033[0m" + "--" * 5 + " Individual Shape Test: End " + "--" * 5)
		print("Model Count: {}".format(tot))
		print("{:f}% Pass".format(float(net)/tot * 100.))
		print("\033[0m")


if __name__ == "__main__":
	unittest.main(verbosity=0)
