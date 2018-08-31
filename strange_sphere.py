# Something Strange, brought to you by PharaohCola13

import mpl_toolkits.mplot3d.axes3d as p3
import matplotlib.pyplot as plt
from matplotlib import cm
import numpy as np
from numpy import pi, linspace, cos, sin, tan, log1p
from mpl_toolkits.mplot3d.art3d import Poly3DCollection, Line3DCollection
from matplotlib.animation import FuncAnimation
from matplotlib.animation import writers

# x: t*s*cos(u) * cos(v)
# y: t*s*cos(u) * sin(v)
# z: t * s * sin(v)

def x_(u,v):
	x = t*s*cos(u) * cos(v)
	return x

def y_(u,v):
	y = t * s * cos(u) * sin(v)
	return y

def z_(u,v):
    z = t * s* sin(v)
    return z

s = 10
t = linspace(0, pi, 20)

u = linspace(0, 2 * pi, 20)
v = linspace(0, 2 * pi, 20)

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

ax.set_xlim(-50,50)
ax.set_ylim(-50,50)
ax.set_zlim(-50,50)

# Surface Plot
strange = ax.plot_surface(x, y, z)

strange.set_alpha(1)
strange.set_edgecolor('w')
strange.set_linewidth(0.5)
strange.set_facecolor('deepskyblue')

# Definitions for animation
def init():
	return strange,

def animate(i):
    # azimuth angle : 0 deg to 360 deg
    # elev = i * n --> rotates object about the xy-plane with a magnitude of n
    # azim = i * n --> rotates object around the z axis with a magnitude of n
    # For top view elev = 90
    # For side view elev = 0
	ax.view_init(elev=0, azim=i*4)
	return strange,

# Animate
ani = FuncAnimation(fig, animate, init_func=init,
                    frames=90, interval=1, blit=False, repeat=True)

# Saving to Something_Strange.mp4

Writer = writers['ffmpeg']
writer = Writer(fps=15, bitrate=1800)

ani.save('Something_Strange.mp4', writer=writer)

plt.show()
