# A Pair of Cressants, brought to you by PharaohCola13

import mpl_toolkits.mplot3d.axes3d as p3
import matplotlib.pyplot as plt
from matplotlib import *
from numpy import *
from mpl_toolkits.mplot3d.art3d import *
from matplotlib.animation import *

name = "Hyperbolic Helicoid"

#def shape(fig, alpha, color, edge_c, edge_w, grid, sides, edges):

# Definition of x
def x_(z):
	x = 0.5 * sqrt(2) * z + 0.125 * sqrt(6) * sqrt(5 - (4 * sqrt(6) * z * (1 + sqrt(6)*z)))
	return x

# Definition of y
def y_(z):
	y = 0.5 * sqrt(6) * z + 0.125 * sqrt(2) * sqrt(5 - (4*sqrt(6) *z *(1 + sqrt(6)*z)))
	return y


# Value of the angles

#z = linspace(sqrt(6)/12, (6 - sqrt(6))/12, 50)
z = linspace(-sqrt(6), sqrt(6), 50)
z = meshgrid(z)

# Symbolic representation
x = x_(z)
y = y_(z)

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