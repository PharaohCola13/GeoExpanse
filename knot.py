# Some Knots, brought to you by PharaohCola13

import mpl_toolkits.mplot3d.axes3d as p3
import matplotlib.pyplot as plt
from matplotlib import cm
import numpy as np
from numpy import pi, linspace, cos, sin
from matplotlib.animation import FuncAnimation
from matplotlib.animation import writers

def x_(t):
    x = sin(t) + 2*sin(2*t)
    return x
def y_(t):
    y = cos(t) - 2*cos(2*t)
    return y
def z_(t)
    z = -sin(3*t)
    return z

# Figure Properties
fig = plt.figure(figsize=(8,8))

ax = p3.Axes3D(fig)
ax.set_facecolor('black')

plt.axis('off')
plt.axis('equal')


# Surface plot
k = ax.plot_trisurf(x, y, z, cmap='rainbow'
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

    ax.view_init(elev=50, azim= 4 * i)
    return k,

# Animate
ani = FuncAnimation(fig, animate, init_func=init,
                    frames=100, interval=20, blit=False, repeat=True)

# Saving to mobius.mp4

# Writer = writers['ffmpeg']
# writer = Writer(fps=15, bitrate=1800)

# ani.save('mobius.mp4', writer=writer)


plt.show()