import matplotlib.pyplot as plt
from matplotlib import *
from numpy import *
from matplotlib.animation import *

name = "Deltiod"
def r_(u):
#	r = (cos(pi/n))/(cos((m/n) * arcsin(cos((n/o) * u)))) # 1
	r = 1/(cos((m/n) *arcsin(cos((n/o)*u)))) #2
	return r

n = 1.5
m = 3
o = 2

u  = linspace(-o * pi, o *pi, 135) # 1
#u = linspace(-o * pi,o * pi, m**2 + o**2 + n +1) # 2



r = r_(u)

ax = plt.subplot(111, projection='polar')
#ax.patch.set_facecolor("black")
#ax.xaxis.set_tick_params(color="white", labelcolor="white")
#ax.yaxis.set_tick_params(color="white", labelcolor="white")

plt.axis('off')


delt = plt.plot(u, r, color="black", linewidth=1)

plt.show()

# 1) #2, n=1.5, m=3, o=2, # 1