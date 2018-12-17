import matplotlib.pyplot as plt
from matplotlib import *
from numpy import *
from matplotlib.animation import *

name = "Fermat Spiral"

def r_(u):
	r = sin(a*u)**2 + cos(b*u)**2 + tan(c*u)
	return r

a = 1
b = 1
c = 1

u = linspace(0, 2 * pi,100)

r = r_(u)

ax = plt.subplot(111, projection='polar')
ax.xaxis.set_tick_params(color="black", labelcolor="white")
ax.yaxis.set_tick_params(color="black", labelcolor="white")

plt.axis("off")

ax.set_xlim(-6, 6)
ax.set_ylim(-90, 90)
plt.plot(u, r, color="blue", linewidth=1)

plt.show()