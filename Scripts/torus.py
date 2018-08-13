# A Torus, brought to you by PharaohCola13

import mpl_toolkits.mplot3d.axes3d as p3
import matplotlib.pyplot as plt
from matplotlib import cm
import numpy as np
from numpy import pi, linspace, cos, sin
from matplotlib.animation import FuncAnimation
from matplotlib.animation import writers

def x_(u, v):
    x = 2 * ((c + a * cos(u)) * cos(v))
    return x

def y_(u, v):
    y = 2 * ((c + a *cos(u)) * sin(v))
    return y

# look at what happens when you switch out sin(u) with sin(v)

def z_(u, v):
    z = 2 * (a * sin(u))
    return z

n = 100

# c > a produces a ring torus
# c = a produces a horn tours
# c < a produces a spindle torus

c, a = 2, 1

u = linspace(0, 2 * pi, n)
v = linspace(0, 2 * pi, n)

u, v = np.meshgrid(u,v)

x = x_(u, v)
y = y_(u, v)
z = z_(u, v)

# Figure Properties
fig = plt.figure(figsize=(8, 8))

ax = p3.Axes3D(fig)
ax.set_facecolor('black')

plt.axis('off')
plt.axis('equal')

ax.set_xlim(-5, 5)
ax.set_ylim(-5, 5)
ax.set_zlim(-5, 5)

# Surface Plot
t = ax.plot_surface(x, y, z, rstride=5, cstride=5, cmap='rainbow')

t.set_edgecolor('w')
t.set_linewidth(0.1)
t.set_alpha(0.5)

# Defintions for animations
def init():
    return t,

def animate(i):
    # azimuth angle : 0 deg to 360 deg
    # elev = i * n --> rotates object about the xy-plane with a magnitude of n
    # azim = i * n --> rotates object around the z axis with a magnitude of n
    # For top view elev = 90
    # For side view elev = 0

    ax.view_init(elev=50, azim= 4 * i)
    return t,


# Animate
ani = FuncAnimation(fig, animate, init_func=init,
                    frames=36, interval=1, blit=False, repeat=True)

# Saving to torus.mp4

#Writer = writers['ffmpeg']
#writer = Writer(fps=15, bitrate=1800)

#ani.save('torus.mp4', writer=writer)

plt.show()
