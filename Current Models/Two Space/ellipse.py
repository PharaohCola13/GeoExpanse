import matplotlib.pyplot as plt
from matplotlib import *
from numpy import *
from matplotlib.animation import *

name = "Ellipse"

def x_(t):
	x = a * cos(t)
	return x

def y_(t):
	y = b * sin(t)
	return y


a = 1
b = 1
t = linspace(-pi,pi, 100)
x = x_(t)
y = y_(t)

plt.subplot(111)
plt.plot(x, y)
plt.show()
