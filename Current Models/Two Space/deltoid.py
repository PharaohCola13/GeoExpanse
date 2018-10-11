import matplotlib.pyplot as plt
from matplotlib import *
from numpy import *
from matplotlib.animation import *

name = "Deltiod"

def x_(t):
	x = 2 * a *cos(t) *(1 + cos(t)) - a
	return x
def y_(t):
	y = 2 * a *sin(t) *(1 - cos(t))
	return y

a = 1
t = linspace(0, 2 *pi, 100)
# y = meshgrid(y)

x = x_(t)
y = y_(t)
fig = plt.figure(figsize=(8,8))
plt.axis("on")
plt.axis('equal')

line = plt.plot(x, y)

plt.show()

# line.set_edgecolor(edge_c) # Edge color of the lines on the figure
# line.set_linewidth(edge_w) # Line width of the edges
