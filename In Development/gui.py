import tkinter as Tkinter
from tkinter.ttk import Style
import matplotlib
from matplotlib import *

matplotlib.use('TkAgg')
#matplotlib.use("gtk3cairo")
import mpl_toolkits.mplot3d.axes3d as p3
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import *
from matplotlib.animation import *
from numpy import *
from polyhedron import shape

root = Tkinter.Tk()

# greeting = Tkinter.Label(text='Hello')
# greeting.pack(side='top')

Tkinter.Frame(root)

root.title("Geometric Models")

top_frame = Tkinter.Frame(root).grid(row=0, pady=15)
right_frame = Tkinter.Frame(root).grid(column=2, padx=10)

alpha = Tkinter.StringVar()
alpha.set(0.3)

def sel():
    selection = plt.axis(str(grid_axis.get()))

grid_axis = Tkinter.StringVar()
grid_axis.set('off')

scrollbar_c = Tkinter.Scrollbar(root)
scrollbar_c.grid(rows=3, column=5)
c_entry_label = Tkinter.Label(root, text="Face Color").grid(row=1, column=4)
c_entry = Tkinter.Listbox(root, width=15, yscrollcommand=scrollbar_c.set,)
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

c_entry.grid(row=2, column=4)
scrollbar_c.config(command=c_entry.yview)

scrollbar_ec = Tkinter.Scrollbar(root)
scrollbar_ec.grid(row=2, column=3)

Tkinter.Label(right_frame, text="Edge Color").grid(row=1, column=2)
ec_entry = Tkinter.Listbox(right_frame, exportselection=0, width=15, yscrollcommand=scrollbar_ec.set)
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
ec_entry.grid(row=2, column=2, sticky="ns")

scrollbar_ec.config(command=ec_entry.yview)

grid_on = Tkinter.Radiobutton(root, text="On", variable=grid_axis, value='on', command=sel)
grid_on.grid(row=0, column=3)

grid_off = Tkinter.Radiobutton(root, text='Off', variable=grid_axis, value='off', command=sel)
grid_off.grid(row=0, column=2)

a_entry_label = Tkinter.Label(top_frame, text="Transparency").grid(row=0, column=0)
a_entry = Tkinter.Entry(root, textvariable = alpha, width=3)
a_entry.grid(row=0, column=1)

#si_entry_label = Tkinter.Label(root, text="Sides").grid(row=1, column=6)
#si_entry = Tkinter.Scale(root, from_=0, to=100, width=10)
#si_entry.grid(row=1, column=7)

ew_entry_label = Tkinter.Label(root, text="Edge Width").grid(row=1, column=7)
ew_entry       = Tkinter.Scale(root, from_=0, to=10, width=10)
ew_entry.grid(row=2, column=7)

#h_entry_label = Tkinter.Label(root, text="Height").grid(row=2, column=6)
#h_entry = Tkinter.Entry(root, textvariable=height, width=3)
#h_entry.grid(row=2, column=7)


def rot(i):
    selection = ax.view_init(elev=int(scroll_elev) * i, azim=int(scroll_azim) * i)


Tkinter.Label(root, text="XY-rotation").grid(row=1, column=1, pady=10)
scroll_elev = Tkinter.Scale(root, from_=-50, to=50, width=40, command=rot)
scroll_elev.grid(row=2, column=1, sticky="nsew")

Tkinter.Label(root, text="Z-rotation").grid(row=1, column=0, pady=10)
scroll_azim = Tkinter.Scale(root, from_=-50, to=50, width=40, command=rot)
scroll_azim.grid(row=2, column=0, sticky="nsew")


# Figure Properties
fig = plt.figure(figsize=(10, 10))

ax = p3.Axes3D(fig)
ax.set_facecolor('black')  # Figure background turns black

ax.set_xlim(-5, 5)
ax.set_ylim(-5, 5)
ax.set_zlim(-5, 5)

def make_shape():
    shape(c_entry.get(c_entry.curselection()[0]),
           ec_entry.get(ec_entry.curselection()[0]),
           ew_entry.get(),
           a_entry.get(),
           #scroll_elev.get(),
           #scroll_azim.get(),
          )

MakePlot = Tkinter.Button(root, command=make_shape, text="Render")
MakePlot.grid(row=10, columns=3, sticky="nsew")

root.mainloop()

while True:
	root.update_idletasks()
	root.update()