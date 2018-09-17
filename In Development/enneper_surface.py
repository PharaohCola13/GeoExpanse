# Enneper Surface, brought to you by PharaohCola13

import mpl_toolkits.mplot3d.axes3d as p3
import matplotlib.pyplot as plt
from matplotlib import *
from numpy import *
from mpl_toolkits.mplot3d.art3d import *
from matplotlib.animation import *

def name():
    name = "Enneper Surface"

#def shape(fig, alpha, color, edge_c, edge_w,  grid, sides, edges, rot_azim, rot_elev):
def x_(u,v):
    x = u - (u**3/3) + (u * v**2)
    return x

def y_(u,v):
    y = v - (v**3/3) + (v * u**2)
    return y

def z_(u,v):
    z = u**2 - v**2
    return z

u = linspace(-pi,pi, 100)
v = linspace(-pi,pi, 100)

u, v = meshgrid(u, v)

x = x_(u,v)
y = y_(u,v)
z = z_(u,v)

# Figure Properties
fig = plt.figure(figsize=(8,8))

ax = p3.Axes3D(fig)
ax.set_facecolor('black')

plt.axis('off')
#plt.axis('equal')

# Surface Plot
interest = ax.plot_surface(x, y, z)


interest.set_alpha(0.4)
interest.set_edgecolor('gold')
interest.set_linewidth(0.5)
interest.set_facecolor('white')

def init():
    return interest,

def animate(i):
    #     # azimuth angle : 0 deg to 360 deg
    #     # elev = i * n --> rotates object about the xy-plane with a magnitude of n
    #     # azim = i * n --> rotates object around the z axis with a magnitude of n
    #     # For top view elev = 90
    #     # For side view elev = 0
    #
    ax.view_init(elev=4* i, azim=4* i)
    return

# Animate
#ani = FuncAnimation(fig, animate, init_func=init,
 #                   frames=100, interval=1, blit=False, repeat=True)
ax.format_coord = lambda x, y: ""
plt.show()