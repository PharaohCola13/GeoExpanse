import mpl_toolkits.mplot3d.axes3d as p3
import matplotlib.pyplot as plt
from matplotlib import cm
import numpy as np
from numpy import pi, linspace, cos, sin
from matplotlib.animation import FuncAnimation
from matplotlib.animation import writers


def x_(u,v):
    x = cos(u) * sin(2 * v)
#    x[u < 2 * pi] = cos(u[u < 2*pi]) * sin(2 * v[u < 2 * pi])
    return x

def y_(u,v):
    y = sin(u) * sin(2 * v)
#    y[u < 2 * pi] = sin(u[u < 2 * pi]) * sin(2 * v[u < 2 * pi])
    return y

def z_(u,v):
    z = (cos(v) * cos(v)) - ((cos(u) * cos(u)) * sin(v) * sin(v))
    return z

u = linspace(0, 2 * pi, 28)
v = linspace(0, pi/2, 28)

u, v = np.meshgrid(u, v)

x = x_(u, v)
y = y_(u, v)
z = -z_(u, v)

fig = plt.figure(figsize=(8,8))

ax = p3.Axes3D(fig)
ax.set_facecolor('black')

plt.axis('off')
plt.axis('equal')

cc = ax.plot_surface(x,y,z, rstride=1, cstride=1)

cc.set_alpha(0.5)

def init():
    return cc,

def animate(i):
    # azimuth angle : 0 deg to 360 deg
    # elev = i * n --> rotates object about the xy-plane with a magnitude of n
    # azim = i * n --> rotates object around the z axis with a magnitude of n
    ax.view_init(elev=0, azim=i*4)
    return cc,

# Animate
ani = FuncAnimation(fig, animate, init_func=init,
                    frames=100, interval=20, blit=False, repeat=True)
# Saving to Cross-Cap.mp4

Writer = writers['ffmpeg']
writer = Writer(fps=15, bitrate=1800)

ani.save('Cross-Cap.mp4', writer=writer)

plt.show()

