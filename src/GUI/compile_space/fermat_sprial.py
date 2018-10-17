import matplotlib.pyplot as plt
from matplotlib import *
from numpy import *
from matplotlib.animation import *

name = "Fermat Spiral"

def r_(u):
	r = (a**m * u)
	return r

def r2_(u):
	r2 = 1/((a**-m) * u)
	return r2

m = 2
a = 6
u = linspace(0.001, 2 * pi,1000)
r = r_(u)
r2 = r2_(u)

plt.subplot(111, projection='polar')
plt.plot(u, r**(1/m))
plt.show()
