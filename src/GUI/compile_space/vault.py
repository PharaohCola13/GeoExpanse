# A Pair of Cressants, brought to you by PharaohCola13

import mpl_toolkits.mplot3d.axes3d as p3
import matplotlib.pyplot as plt
from matplotlib import *
from numpy import *
from mpl_toolkits.mplot3d.art3d import *
from matplotlib.animation import *

name = "Steinbach Screw"

#def shape(fig, alpha, color, edge_c, edge_w, grid, sides, edges):

# Definition of x
def x_(r,z):
	x = sqrt(r**2 - z**2)
	return x

# Definition of y
def y_(r,z):
	y = -u * sqrt(r**2 - z**2)
	return y

# Definition of z
def z_(r,z):
	z = z
	return z

r = 1
z = 1
# Value of the angles
u = linspace(4, 10, 10)
v = linspace(0, 6.25, 10)

u, v = np.meshgrid(u, v)

# Symbolic representation
z = z_(u,v)
x = x_(u,v)
y = y_(u,v)


# Figure Properties
fig = plt.figure(figsize=(8,8))
ax = p3.Axes3D(fig)
ax.set_facecolor('black') # Figure background turns black

# Axis Properties
plt.axis("off") # Turns off the axis grid
plt.axis('equal')

# Surface Plot
cressant = ax.plot_surface(x, y, z)

cressant.set_alpha(1) # Transparency of figure
cressant.set_edgecolor("white") # Edge color of the lines on the figure
cressant.set_linewidth(1) # Line width of the edges
cressant.set_facecolor("deepskyblue") # General color of the figure

plt.show()