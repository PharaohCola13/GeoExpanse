import matplotlib.pyplot as plt
from matplotlib import *
from numpy import *
from matplotlib.animation import *

name = "Polygons"
def r_(u):
	r = 1/(cos((m/n) *arcsin(sin((n/o)*u+p))))
	return r

n = 5
m = 2
o = 2
p = 0.79


u = linspace(-2 * pi,2 * pi, o**2 * m**2 * n + 1)

r = r_(u)

ax = plt.subplot(111, projection='polar')
#ax.patch.set_facecolor("black")
#ax.xaxis.set_tick_params(color="white", labelcolor="white")
#ax.yaxis.set_tick_params(color="white", labelcolor="white")

plt.axis('off')


delt = plt.plot(u, r, color="black", linewidth=1)

plt.show()