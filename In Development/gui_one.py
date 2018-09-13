import tkinter as Tkinter
from tkinter.ttk import Style
import matplotlib
from matplotlib import *

matplotlib.use('TkAgg')
import mpl_toolkits.mplot3d.axes3d as p3
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import *
from matplotlib.animation import *
from numpy import *

root = Tkinter.Tk()

# greeting = Tkinter.Label(text='Hello')
# greeting.pack(side='top')

Tkinter.Frame(root)

top_frame = Tkinter.Frame(root).grid(row=0, pady=15)
right_frame = Tkinter.Frame(root).grid(column=2, padx=10)

side = Tkinter.StringVar()
# side.set('50')

color = Tkinter.StringVar()
# color.set('gold')

alpha = Tkinter.StringVar()


def sel():
    selection = plt.axis(str(grid_axis.get()))

grid_axis = Tkinter.StringVar()

c_entry_label = Tkinter.Label(root, text="Face Color").grid(row=1, column=3)
c_entry = Tkinter.Listbox(root, exportselection=0, width=10)
c_entry.insert(1, 'gold')
c_entry.insert(2, 'teal')
c_entry.insert(3, 'white')
c_entry.insert(4, 'red')
c_entry.insert(5, 'blue')
c_entry.insert(6, 'fuchsia')
c_entry.insert(7, 'green')
c_entry.insert(8, 'lime')
c_entry.insert(9, 'paleturquoise')
c_entry.insert(10, 'orange')
c_entry.insert(11, 'lightgray')
c_entry.insert(12, 'black')
c_entry.insert(13, 'coral')
c_entry.insert(14, 'deepskyblue')

c_entry.grid(row=2, column=3)

Tkinter.Label(right_frame, text="Edge Color").grid(row=1, column=2)
ec_entry = Tkinter.Listbox(right_frame, exportselection=0, width=10)
ec_entry.insert(1, 'gold')
ec_entry.insert(2, 'teal')
ec_entry.insert(3, 'white')
ec_entry.insert(4, 'red')
ec_entry.insert(5, 'blue')
ec_entry.insert(6, 'fuchsia')
ec_entry.insert(7, 'green')
ec_entry.insert(8, 'lime')
ec_entry.insert(9, 'paleturquoise')
ec_entry.insert(10, 'orange')
ec_entry.insert(11, 'lightgray')
ec_entry.insert(12, 'black')
ec_entry.insert(13, 'coral')
ec_entry.insert(14, 'deepskyblue')
ec_entry.grid(row=2, column=2)

a_entry_label = Tkinter.Label(top_frame, text="Transparency").grid(row=0, column=0)
a_entry = Tkinter.Spinbox(root, from_=0, to=1, increment=0.1, textvariable=alpha, width=3)
a_entry.grid(row=0, column=1)

Tkinter.Label(root, text="XY-rotation").grid(row=1, column=1, pady=10)
scroll_elev = Tkinter.Scale(root, from_=-50, to=50, width=40)
scroll_elev.grid(row=2, column=1, sticky="nsew")

Tkinter.Label(root, text="Z-rotation").grid(row=1, column=0, pady=10)
scroll_azim = Tkinter.Scale(root, from_=-50, to=50, width=40)
scroll_azim.grid(row=2, column=0, sticky="nsew")

grid_on = Tkinter.Radiobutton(root, text="On", variable=grid_axis, value='on', command=sel)
grid_on.grid(row=0, column=3)

grid_off = Tkinter.Radiobutton(root, text='Off', variable=grid_axis, value='off', command=sel)
grid_off.grid(row=0, column=2)

# Figure Properties
fig = plt.figure(figsize=(10, 10))

ax = p3.Axes3D(fig)
ax.set_facecolor('black')  # Figure background turns black

# Axis Properties
# plt.axis(grid_axis.get()) # Turns off the axis grid
plt.axis('equal')


def make_plot(event=None):
    global fig, ax, scroll_elev, scroll_azim, alpha, color, edge_color

    # si = int(side.get())
    c = c_entry.get(c_entry.curselection()[0])
    edge_color = ec_entry.get(ec_entry.curselection()[0])
    a = float(alpha.get())
    def x_(u, v):
        x = cos(u) * sin(v)
        return x
    def y_(u, v):
        y = sin(u) * sin(v)
        return y
    def z_(u, v):
        z = cos(v) + log1p(tan(2 + v) ** 2)
        return z
    u = linspace(0.001, 2 * pi, 25)
    v = linspace(0, 2 * pi, 25)
    u, v = meshgrid(u, v)
    x = x_(u, v)
    y = y_(u, v)
    z = z_(u, v)
    # Surface Plot
    interest = ax.plot_surface(x, y, z)
    interest.set_alpha(a)
    interest.set_edgecolor(edge_color)
    interest.set_linewidth(0.5)
    interest.set_facecolor(c)
    # Definitions for animation
    def init():
        return interest,
    #
    def animate(i):
        #     # azimuth angle : 0 deg to 360 deg
        #     # elev = i * n --> rotates object about the xy-plane with a magnitude of n
        #     # azim = i * n --> rotates object around the z axis with a magnitude of n
        #     # For top view elev = 90
        #     # For side view elev = 0
        #
        ax.view_init(elev=scroll_elev.get() * 10, azim=scroll_azim.get() * 10)
        return interest,

    # Animate
    ani = FuncAnimation(fig, animate, init_func=init,
                        frames=100, interval=1, repeat=True)

    plt.show()

MakePlot = Tkinter.Button(root, command=make_plot, text="Render")
MakePlot.grid(row=10, column=1)

root.mainloop()

while True:
    root.update_idletasks()
    root.update()