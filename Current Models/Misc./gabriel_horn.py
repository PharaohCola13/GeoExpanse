# A Gabriel's Horn, brought to you by PharaohCola13

import sys
sys.path.insert(0,'../')
from parse import *

name = "Gabriel's-Horn"

if args.run:
    # Definition of x
    def x_(u, v):
        x = u
        return x

    # Definition of y
    def y_(u, v):
        y = (a * cos(v)) / u
        return y


    # Definition of z
    def z_(u, v):
        z = (a * sin(v)) /u
        return z

    a = args.radius # changes radius of the entire thing

    h = args.height

    # Value of the angles
    u = linspace(1, h, 25)
    v = linspace(0, 2 * pi, 25)

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
    ax.set_xlim(-4, 4)
    ax.set_ylim(-4, 4)
    ax.set_zlim(-4, 4)

    # Surface Plot
    horn = ax.plot_surface(x, y, z)

    horn.set_alpha(args.alpha)  # Transparency of figure
    horn.set_edgecolor('w')  # Edge color of the lines on the figure
    horn.set_linewidth(1)  # Line width of the edges
    horn.set_facecolor(args.color)  # General color of the figure

    if args.rotate:
# Definitions for animation
        def init():
            return horn,


        def animate(i):
# azimuth angle : 0 deg to 360 deg
# elev = i * n --> rotates object about the xy-plane with a magnitude of n
# azim = i * n --> rotates object around the z axis with a magnitude of n
# For top view elev = 90
# For side view elev = 0

            ax.view_init(elev=29, azim=i * 4)
            return horn,


# Animate
            ani = FuncAnimation(fig, animate, init_func=init,
                        frames=100, interval=20, blit=False, repeat=True)
        if args.save:
# Saving to Gabriel's-Horn.mp4

            Writer = writers['ffmpeg']
            writer = Writer(fps=15, bitrate=1800)

            ani.save('%s' % name, writer=writer)

plt.show()  # Shows Figure