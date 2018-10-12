import matplotlib.pyplot as plt
from matplotlib import *
from numpy import *
from matplotlib.animation import *

name = "Log Spiral"

def r_(u):
	r = exp(a *u)
	return r

a = 0.1
u = linspace(-5 *pi, pi,1000)
r = r_(u)

plt.subplot(111, projection='polar')
plt.plot(u, r)

#plt.show()
