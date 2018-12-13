import mpl_toolkits.mplot3d.axes3d as p3
import matplotlib.pyplot as plt

from mpl_toolkits.mplot3d.art3d import *
from matplotlib.animation import *
from matplotlib import *
from numpy import *

name = "Hyperbolic Tetrahedron"


def x_(u, v):
	x = ((2 * cos(u) + 2 * cos(u)**2 - 1)  * (1 - v)**2)
	return x


def y_(u, v):
	y = (2*sin(u) - 2*sin(u)*cos(u)) * (1 - v)**2
	return y


# Definition of z
def z_(u, v):
	z = v
	return z

u = linspace(-pi, pi, 30)
v = linspace(0,1, 10)

u, v = np.meshgrid(u, v)

x = x_(u, v)
y = y_(u, v)
z = z_(u, v)

# Figure Properties
fig = plt.figure(figsize=(8,8))
ax = p3.Axes3D(fig)
ax.set_facecolor("black")

plt.axis("off")

# Axis Limits
ax.set_zlim(0,1)


# Surface plot
N = ax.plot_surface(x, y, z, rstride=1, cstride=1)

N.set_linewidth(0.5)
N.set_edgecolor("gold")
N.set_alpha(0.5)
N.set_facecolor("white")

plt.show()