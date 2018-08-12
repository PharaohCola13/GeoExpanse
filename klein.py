# A Klein Bottle, brought to you by PharaohCola13

import mpl_toolkits.mplot3d.axes3d as p3
import matplotlib.pyplot as plt
from matplotlib import cm
import numpy as np
from numpy import pi, linspace, cos, sin
from matplotlib.animation import FuncAnimation
from matplotlib.animation import writers


# Klein Bottle x,y,z Components
def x_(u, v):
    x = -2 + 2 * cos(v) - cos(u)
    x[v < 3 * pi] = -2 + (2 + cos(u[v < 3 * pi])) * cos(v[v < 3 * pi])
    x[v < 2 * pi] = cos(u[v < 2 * pi]) * (2.5 - 1.5 * cos(v[v < 2 * pi]))

    return x


def y_(u, v):
    y = sin(u)
    y[v < 2 * pi] = sin(u[v < 2 * pi]) * (2.5 - 1.5 * cos(v[v < 2 * pi]))

    return y


def z_(u, v):
    z = -3 * v + 12 * pi
    z[v < 3 * pi] = (2 + cos(u[v < 3 * pi])) * sin(v[v < 3 * pi]) + 3 * pi
    z[v < 2 * pi] = 3 * v[v < 2 * pi] - 3 * pi
    z[v < pi] = -2.5 * sin(v[v < pi])

    return z


u = linspace(0, 2 * pi, 10)
v = linspace(0, 4 * pi, 38)

u, v = np.meshgrid(u, v)

x = x_(u, v)
y = y_(u, v)
z = z_(u, v)

# Figure Properties
fig = plt.figure(figsize=(8,8))

ax = p3.Axes3D(fig)
ax.set_facecolor('black')

plt.axis("off")
plt.axis('equal')

# Surface Plot
ln = ax.plot_surface(x, y, z, rstride=1, cstride=1, cmap='rainbow',
                     antialiased=False)

ln.set_linewidth(0.0)
ln.set_edgecolor('w')
ln.set_alpha(0.5)

# Axis Limits
ax.set_xlim(-5, 5)
ax.set_ylim(-5, 5)
ax.set_zlim(0,10)

# Definitions for animations

def init():
    return ln,

def animate(i):
    # azimuth angle : 0 deg to 360 deg
    # elev = i * n --> rotates object about the xy-plane with a magnitude of n
    # azim = i * n --> rotates object around the z axis with a magnitude of n
    # For top view elev = 90
    # For side view elev = 0

    ax.view_init(elev=90, azim=i*10)
    return ln,

# Smooth tranisition azim=i*10, frames=36, interval=1

# Animate
ani = FuncAnimation(fig, animate, init_func=init,
                    frames=36, interval=1, blit=False, repeat=True)

# Saving to klein.mp4

#Writer = writers['ffmpeg']
#writer = Writer(fps=15, bitrate=1800)

#ani.save('klein_rainbow.mp4', writer=writer)

plt.show()