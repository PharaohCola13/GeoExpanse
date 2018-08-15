# A Pyramid, brought to you by PharaohCola13

import mpl_toolkits.mplot3d.axes3d as p3
import matplotlib.pyplot as plt
from matplotlib import cm
import numpy as np
from numpy import pi, linspace, cos, sin, inf, log10
from mpl_toolkits.mplot3d.art3d import Poly3DCollection, Line3DCollection
from matplotlib.animation import FuncAnimation
from matplotlib.animation import writers

def x_(u,v):
    x = ((h - u) / h) * r * cos(v)
    return x

def y_(u,v):
    y = ((h - u)/h) * r * sin(v)
    return y

def z_(u,v):
    z = u
    return z
# Number of sides on the base
s = 3

# Height
h = 1

# Radius
r = 1

u = linspace(0, h, 10)
v = linspace(0, 2 * pi, s+1)

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
pyramid = ax.plot_surface(x,y,z, cmap='rainbow')

pyramid.set_alpha(0.5)
pyramid.set_edgecolor('w')
pyramid.set_linewidth(0)

# Definitions for animation
def init():
    return pyramid,

def animate(i):
    # azimuth angle : 0 deg to 360 deg
    # elev = i * n --> rotates object about the xy-plane with a magnitude of n
    # azim = i * n --> rotates object around the z axis with a magnitude of n
    # For top view elev = 90
    # For side view elev = 0

    ax.view_init(elev=i, azim=i*4)
    return pyramid,

# Animate
ani = FuncAnimation(fig, animate, init_func=init,
                    frames=100, interval=20, blit=False, repeat=True)
# Saving to Pyramid.mp4

#Writer = writers['ffmpeg']
#writer = Writer(fps=15, bitrate=1800)

#ani.save('Pyramid.mp4', writer=writer)


plt.show()
