import matplotlib.pyplot as plt
from matplotlib import *
from numpy import *
from matplotlib.animation import *

name = "Fermat Spiral"

def r_(u):
	r = sin(a*u)**2 + cos(b*u)**2
	return r

a = 2
b = 10

u = linspace(0, 10 * pi,1000)

r = r_(u)

ax = plt.subplot(111, projection='polar')
ax.xaxis.set_tick_params(color="black", labelcolor="white")
ax.yaxis.set_tick_params(color="black", labelcolor="white")

plt.axis("off")

plt.plot(u, r, color="blue", linewidth=1)

plt.show()