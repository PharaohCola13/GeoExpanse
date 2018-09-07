# Breather's Surface, brought to you by PharaohCola13

import mpl_toolkits.mplot3d.axes3d as p3
import matplotlib.pyplot as plt

from mpl_toolkits.mplot3d.art3d import *
from matplotlib.animation import *
from matplotlib import *
from numpy import *

name = "Breather's-Surface"

option = int(input('Run? (0) Yes, (1) No\n>> '))

while option == 0:
# Definition of x
    def x_(u, v):
        x = (-u + (2. * w * cosh(b*u) * sinh(b*u) / (b * ((w * cosh(b * u))**2 + (b * sin(w * v))**2))))
        return x

# Definition of y
    def y_(u, v):
        y = (2. * w * cosh(b * u) * (-1 * (w * cos(v) * cos(w * v)) - sin(v) * sin(w * v)) / (b * ((w * cosh(b * u))**2 + (b * sin(w * v))**2)))
        return y


# Definition of z
    def z_(u, v):
        z = (2. * w * cosh(b * u) * (-(w * sin(v) * cos(w * v)) + cos(v) * sin(w * v))) / (b * ((w * cosh(b * u))**2 + (b * sin(w * v))**2))
        return z

    b = 0.4
    r = 1. - b**2
    w = sqrt(r)
# Value of the angles
    u = linspace(-13.2,  13.2, 75)
    v = linspace(-37.4, 37.4, 75)

    u, v = meshgrid(u, v)

# Symbolic representation
    x = x_(u, v)
    y = y_(u, v)
    z = z_(u, v)

# Figure Properties
    fig = plt.figure(figsize=(8, 8))

    ax = p3.Axes3D(fig)
    ax.set_facecolor('black')  # Figure background turns black

# Axis Properties
    plt.axis('off')  # Turns off the axis grid
    plt.axis('equal')

# Axis Limits
    ax.set_xlim(-10, 10)
    ax.set_ylim(-10, 10)
    ax.set_zlim(-10, 10)

# Surface Plot
    color = str(raw_input('What color is the figure?\n>> '))
    alpha = float(input('How transparent is the figure? (0 to 1)\n>> '))

    breath_surf = ax.plot_surface(x, y, z)

    breath_surf.set_alpha(alpha)  # Transparency of figure
    breath_surf.set_edgecolor('w')  # Edge color of the lines on the figure
    breath_surf.set_linewidth(0.5)  # Line width of the edges
    breath_surf.set_facecolor(color)  # General color of the figure

    rotate = int(input('Rotate the figure? (0) Yes, (1) No.\n>> '))
    if rotate == 0:
# Definitions for animation
        def init():
            return breath_surf,


        def animate(i):
# azimuth angle : 0 deg to 360 deg
# elev = i * n --> rotates object about the xy-plane with a magnitude of n
# azim = i * n --> rotates object around the z axis with a magnitude of n
# For top view elev = 90
# For side view elev = 0

            ax.view_init(elev=i*4, azim=i * 4)
            return breath_surf,


# Animate
        ani = FuncAnimation(fig, animate, init_func=init,
                           frames=100, interval=20, blit=False, repeat=True)

        save = int(input('Save the animation? (0) Yes, (1) No.\n>> '))
        if save == 0:
# Saving to Breather's-Surface.mp4

            Writer = writers['ffmpeg']
            writer = Writer(fps=15, bitrate=1800)

            ani.save('../Samples/%s.mp4' % name, writer=writer)
            plt.show() # Shows Figure

        elif save == 1:
            plt.show() # Shows Figure

    elif rotate == 1:
        plt.show()  # Shows Figure
    option = int(input('Run again? (0) Yes, (1) No\n>> '))
