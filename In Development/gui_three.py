import matplotlib
matplotlib.use('TkAgg')
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
import mpl_toolkits.mplot3d.axes3d as p3
from numpy import *
from matplotlib.figure import Figure
import Tkinter as tk  # python 2.7
import ttk            # python 2.7
import sys

class Geometry(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self,master)
        self.createWidgets()

    def createWidgets(self):
        fig=plt.figure(figsize=(8,8))
        ax = p3.Axes3D(fig)
	ax.set_facecolor('black')
	plt.axis('off')
        canvas=FigureCanvasTkAgg(fig,master=root)
        canvas.get_tk_widget().grid(row=0,column=1)
        canvas.draw()

        self.plotbutton=tk.Button(master=root, text="Render", command=lambda: self.plot(canvas,ax))
        self.plotbutton.grid(row=0,column=0)


    def plot(self,canvas,ax):
       
		ax.clear()         # clear axes from previous plot
		
		for i in range(3):
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

			interest = ax.plot_surface(x, y, z)

			interest.set_alpha(0.2)
			interest.set_edgecolor('gold')
			interest.set_linewidth(0.5)
			interest.set_facecolor('white')

			def animate(i):
		#     # azimuth angle : 0 deg to 360 deg
		#     # elev = i * n --> rotates object about the xy-plane with a magnitude of n
		#     # azim = i * n --> rotates object around the z axis with a magnitude of n
		#     # For top view elev = 90
		#     # For side view elev = 0
		#
				ax.view_init(elev=scroll_elev.get() * i, azim=scroll_azim.get() * i)
				return interest,

       # for i in range(3):
        #    theta = np.random.uniform(0,360,10)
         #   r = np.random.uniform(0,1,10)
          #  ax.plot(theta,r,linestyle="None",marker='o', color=c[i])
		canvas.draw()

root=tk.Tk()
geo=Geometry(master=root)
geo.mainloop()
