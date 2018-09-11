# A One Sheet Hyperboloid, brought to you by PharaohCola13

import sys
sys.path.insert(0,'../')
from parse import *

name = "One-Sheet-Hyperboloid"

if args.run:
# Definition of x
    def x_(u, v):
        x = (cosh(u) * cos(v))
        return x

# Definition of y
    def y_(u, v):
        y = (cosh(u) * sin(v))
        return y


# Definition of z
    def z_(u, v):
        z = sinh(u)
        return z

# Value of the angles
    u = linspace(-2, 2, 25)
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
    ax.set_xlim(-3, 3)
    ax.set_ylim(-3, 3)
    ax.set_zlim(-3, 3)

# Surface Plot
    one_hyper = ax.plot_surface(x, y, z)

    one_hyper.set_alpha(args.alpha)  # Transparency of figure
    one_hyper.set_edgecolor('w')  # Edge color of the lines on the figure
    one_hyper.set_linewidth(0.5)  # Line width of the edges
    one_hyper.set_facecolor(args.color)  # General color of the figure

    if args.rotate:
# Definitions for animation
        def init():
            return one_hyper,


        def animate(i):
# azimuth angle : 0 deg to 360 deg
# elev = i * n --> rotates object about the xy-plane with a magnitude of n
# azim = i * n --> rotates object around the z axis with a magnitude of n
# For top view elev = 90
# For side view elev = 0

            ax.view_init(elev=-90, azim=i * 4)
            return one_hyper,


# Animate
            ani = FuncAnimation(fig, animate, init_func=init,
                      frames=100, interval=20, blit=False, repeat=True)

        if args.save:
# Saving to One-Sheet-Hyperboloid.mp4

            Writer = writers['ffmpeg']
            writer = Writer(fps=15, bitrate=1800)

            ani.save('One-Sheet-Hyperboloid.mp4', writer=writer)

plt.show()  # Shows Figure
