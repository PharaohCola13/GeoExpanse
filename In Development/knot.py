# Some Knots, brought to you by PharaohCola13

import mpl_toolkits.mplot3d.axes3d as p3
import matplotlib.pyplot as plt
from matplotlib import cm
import numpy as np
from numpy import pi, linspace, cos, sin
from matplotlib.animation import FuncAnimation
from matplotlib.animation import writers

def x_(u,v):
    x = sin(v) + 2 * sin(2 * v)
    return x

def y_(u,v):
    y = cos(v) - 2 * cos(2 * v)
    return y

def z_(u,v):
    z = -sin(u)
    return z

u = linspace(0, 4 * pi, 100)
v = linspace(0, 2 * pi, 100)

u,v = np.meshgrid(u,v)

x = x_(u,v)
y = y_(u,v)
z = z_(u,v)

# Figure Properties
fig = plt.figure(figsize=(8,8))

ax = p3.Axes3D(fig)
ax.set_facecolor('black')

plt.axis('off')
plt.axis('equal')

# ax.set_xlim(-5,5)
# ax.set_ylim(-5,5)
ax.set_zlim(-5,5)

# Surface plot
k = ax.plot_surface(x, y, z, rstride=10, cstride=10, cmap='cool'
)

k.set_linewidth(0.0)
k.set_edgecolor('w')
k.set_alpha(0.5)

# Defintions for animations
def init():
   return k,

def animate(i):
    # azimuth angle : 0 deg to 360 deg
    # elev = i * n --> rotates object about the xy-plane with a magnitude of n
    # azim = i * n --> rotates object around the z axis with a magnitude of n
    # For top view elev = 90
    # For side view elev = 0

    ax.view_init(elev=50, azim= 2 * i)
    return k,

# Smooth transition elev = 50, frames = 180, interval = 1

# Animate
ani = FuncAnimation(fig, animate, init_func=init,
                     frames=180, interval=1, blit=False, repeat=True)

# Saving to Knot.mp4

# Writer = writers['ffmpeg']
# writer = Writer(fps=15, bitrate=1800)

# ani.save('Knot.mp4', writer=writer)

plt.show()
