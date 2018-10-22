import geo_gui
import geo_windows
import unittest
import atexit

try:
	import tkinter as tk
	from tkinter.colorchooser import askcolor
except ImportError:
	import Tkinter as tk
	from tkColorChooser import askcolor

class TestObject(unittest.TestCase):

	def test_general(self):
		a = geo_gui.Geometry(root)
		b = a.createWidgets(root)


if __name__ == "__main__":
	root = tk.Tk()
	geo_gui.Geometry(root)


	#root.quit()
	#root.destroy()

	unittest.main(verbosity=2)
