import mpl_toolkits.mplot3d.axes3d as p3
import matplotlib.pyplot as plt
from matplotlib import cm
import numpy as np
from numpy import pi, linspace, cos, sin, inf, log10
from mpl_toolkits.mplot3d.art3d import Poly3DCollection, Line3DCollection
from matplotlib.animation import FuncAnimation
from matplotlib.animation import writers

def x_(u,v):
	x = r * cos(v)
	return x

def y_(u,v):
	y = r * sin(v)
	return y

def z_(u,v):
	z = u
	return z

# Height
h = 1
# Radius
r = 0.5
# Number of edges on the base
s = 7

u = linspace(0, h, 100)
v = linspace(0, 2 * pi, s + 1)


u, v = np.meshgrid(u, v)

x = x_(u,v)
y = y_(u,v)
z = z_(u,v)

# Figure Properties
fig = plt.figure(figsize=(8,8))

ax = p3.Axes3D(fig)
ax.set_facecolor('black')

plt.axis('off')
plt.axis('equal')

# Surface Plot
prism = ax.plot_surface(x,y,z, cmap='rainbow')

prism.set_alpha(0.5)
prism.set_edgecolor('w')
prism.set_linewidth(0)

# Definitions for animation
def init():
    return prism,

def animate(i):
    # azimuth angle : 0 deg to 360 deg
    # elev = i * n --> rotates object about the xy-plane with a magnitude of n
    # azim = i * n --> rotates object around the z axis with a magnitude of n
    # For top view elev = 90
    # For side view elev = 0

    ax.view_init(elev=i, azim=i*4)
    return prism,

# Animate
#ani = FuncAnimation(fig, animate, init_func=init,
#                    frames=100, interval=20, blit=False, repeat=True)
# Saving to Prism.mp4

#Writer = writers['ffmpeg']
#writer = Writer(fps=15, bitrate=1800)

#ani.save('Prism.mp4', writer=writer)


plt.show()
