# A Hyperbolic Tetrahedron, Brought to you by PharaohCola13
import mpl_toolkits.mplot3d.axes3d as p3
import matplotlib.pyplot as plt

from mpl_toolkits.mplot3d.art3d import *
from matplotlib.animation import *
from matplotlib import *
from numpy import *

name = "Hyperbolic Tetrahedron"


def x_(u, v):
	x = ((2 * cos(u) + 2 * cos(u) ** 2 -1))
	return x


def y_(u, v):
	y = (2 * sin(u) - 2 * sin(u) * cos(u))
	return y


# Definition of z
def z_(u, v):
	z = 0
	return z


# Value of the angles
u = linspace(-pi, pi, 30)
v = linspace(0, 1, 30)

u, v = meshgrid(u, v)

x = x_(u, v)
y = y_(u, v)
z = z_(u, v)

# Figure Properties
fig = plt.figure(figsize=(8,8))
ax = p3.Axes3D(fig)
ax.set_facecolor("black")

plt.axis("off")

# Surface plot
hy_tetra = ax.plot_surface(x, y, z)

hy_tetra.set_linewidth(1)
hy_tetra.set_edgecolor("gold")
hy_tetra.set_alpha(0.5)
hy_tetra.set_facecolor("fuchsia")

plt.show()