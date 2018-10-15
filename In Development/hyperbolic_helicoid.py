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
def x_(u,v):
	x = (sinh(v) * cos(t * u))/(1 + cosh(u) * cosh(v))
	return x

# Definition of y
def y_(u,v):
	y = (sinh(v) * sin(t * u))/(1 + cosh(u) * cosh(v))
	return y

# Definition of z
def z_(u,v):
	z = (cosh(v) * sinh(u))/(1 + cosh(u) * cosh(v))
	return z

# Value of the angles
t = 3
u = linspace(-2 * pi, 2 * pi, 50)
v = linspace(-2 * pi, 2 * pi, 50)

u, v = np.meshgrid(u, v)

# Symbolic representation
x = x_(u,v)
y = y_(u,v)
z = z_(u,v)

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