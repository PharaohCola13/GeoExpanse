# A Family of curve, brought to you by PharaohCola13

import mpl_toolkits.mplot3d.axes3d as p3
import matplotlib.pyplot as plt
from matplotlib import *
from numpy import *
from mpl_toolkits.mplot3d.art3d import *
from matplotlib.animation import *

name = "Curves"

X = linspace(0, 2 * pi, 50)
Y = linspace(0, 2 * pi, 50)
x,y = meshgrid(X,Y)
#print(Y)
Z = x**2 + y**2 - 2*x - 2*y
# Figure Properties
fig = plt.figure(figsize=(8,8))

ax = p3.Axes3D(fig)
ax.set_facecolor('black') # Figure background turns black

#plt.plot([0, 0], 'r-', lw=3)

# Axis Properties
plt.axis("on") # Turns off the axis grid
# Axis Limits

# Surface Plot
curves = ax.plot_surface(x,y, Z)

curves.set_alpha(1) # Transparency of figure#
curves.set_edgecolor("blue") # Edge color of the lines on the figure
curves.set_linewidth(0.5) # Line width of the edges
curves.set_facecolor("deepskyblue") # General color of the figure

	#plt.draw()
plt.show()

# Saving to curve.mp4


	# if c > a:
	#	name = 'Ring-curve'
	# elif c == a:
	#	name = 'Horn-curve'
	#elif c < a:
	#	name = 'Spindle-curve'
	
