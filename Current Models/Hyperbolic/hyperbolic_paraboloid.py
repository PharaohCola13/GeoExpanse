# A Hyperbolic Paraboliod, brought to you by PharaohCola13

import sys
sys.path.insert(0,'./parse.py')
from  parse import *

if args.run:
    # Definition of x
    def x_(u, v):
        x = u
        return x


    # Definition of y
    def y_(u, v):
        y = v
        return y


    # Definition of z
    def z_(u, v):
        z = u * v
        return z

    # Value of the angles
    u = linspace(-pi/2, pi/2, 25)
    v = linspace(-pi/2, pi/2, 25)

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
    ax.set_xlim(-2, 2)
    ax.set_ylim(-2, 2)
    ax.set_zlim(-2, 2)

    # Surface Plot
    hyper_para = ax.plot_surface(x, y, z)

    hyper_para.set_alpha(args.alpha)  # Transparency of figure
    hyper_para.set_edgecolor('w')  # Edge color of the lines on the figure
    hyper_para.set_linewidth(1)  # Line width of the edges
    hyper_para.set_facecolor(args.color)  # General color of the figure

    if args.rotate:
# Definitions for animation
        def init():
            return hyper_para,


    def animate(i):
# azimuth angle : 0 deg to 360 deg
# elev = i * n --> rotates object about the xy-plane with a magnitude of n
# azim = i * n --> rotates object around the z axis with a magnitude of n
# For top view elev = 90
# For side view elev = 0

        ax.view_init(elev=29, azim=i * 4)
        return hyper_para,


# Animate
        ani = FuncAnimation(fig, animate, init_func=init,
                        frames=100, interval=20, blit=False, repeat=True)

        if args.save:
# Saving to Hyperbolic_Paraboliod.mp4

            Writer = writers['ffmpeg']
            writer = Writer(fps=15, bitrate=1800)

            ani.save('Hyperbolic_Paraboliod.mp4', writer=writer)

plt.show()  # Shows Figure
