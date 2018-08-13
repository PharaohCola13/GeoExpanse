# A Mobius Band, brought to you by PharaohCola13

# triangulate in the underlying parametrization
from matplotlib.tri import Triangulation
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
import mpl_toolkits.mplot3d.axes3d as p3
from matplotlib.animation import FuncAnimation
from matplotlib.animation import writers
from matplotlib import cm

# Mobius Band components
theta = np.linspace(0, 2 * np.pi, 30)

w = np.linspace(-0.25, 0.25, 8)
w, theta = np.meshgrid(w, theta)

phi = 0.5 * theta

# radius in x-y plane
r = 1 + w * np.cos(phi)

x = np.ravel(r * np.cos(theta))
y = np.ravel(r * np.sin(theta))
z = np.ravel(w * np.sin(phi))

tri = Triangulation(np.ravel(w), np.ravel(theta))

# Figure Properties
fig = plt.figure(figsize=(8,8))

ax = p3.Axes3D(fig)
ax.set_facecolor('black')

plt.axis('off')
plt.axis('equal')

# Axis Limits
ax.set_xlim(-1, 1)
ax.set_ylim(-1, 1)
ax.set_zlim(-1, 1)


# Mobius Band
mb = ax.plot_trisurf(x, y, z, triangles=tri.triangles, cmap='rainbow'
)

mb.set_linewidth(0.0)
mb.set_edgecolor('w')
mb.set_alpha(0.5)

# Defintions for animations
def init():
    return mb,

def animate(i):
    # azimuth angle : 0 deg to 360 deg
    # elev = i * n --> rotates object about the xy-plane with a magnitude of n
    # azim = i * n --> rotates object around the z axis with a magnitude of n
    # For top view elev = 90
    # For side view elev = 0

    ax.view_init(elev=50, azim= 4 * i)
    return mb,

# Animate
ani = FuncAnimation(fig, animate, init_func=init,
                    frames=100, interval=20, blit=False, repeat=True)

# Saving to mobius.mp4

# Writer = writers['ffmpeg']
# writer = Writer(fps=15, bitrate=1800)

# ani.save('mobius.mp4', writer=writer)


plt.show()
