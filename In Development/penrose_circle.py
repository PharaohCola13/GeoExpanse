import matplotlib.pyplot as plt
from matplotlib import *
from numpy import *
from matplotlib.animation import *
from matplotlib.patches import Arc

cd
name = "Penrose Circle"

circle  = plt.Circle((0,0), sqrt(0.75), fill=False)
circle1 = plt.Circle((0,0), 2, fill=False)

ellipse = Arc(xy=(0.23,0), width=3.28, height=3.976, fill=False, theta1=180, theta2=270)
ellipse1 = Arc(xy=(-0.27, 0), width=2.279, height=2.4449, fill=False, theta1=0, theta2=180)

ellipse2 = Arc(xy=(-0.23,0), width=3.28, height=3.976, fill=False, theta1=0, theta2=90)
ellipse3 = Arc(xy=(0.27, 0), width=2.279, height=2.4449, fill=False, theta1=180, theta2=360)
fig = plt.figure(figsize=(6,6))

ax = plt.subplot(111)

ax.set_xlim(-2.5, 2.5)
ax.set_ylim(-2.5, 2.5)
ax.set_aspect("equal")

ax.add_artist(circle)
ax.add_artist(circle1)
ax.add_artist(ellipse)
ax.add_artist(ellipse1)
ax.add_artist(ellipse2)
ax.add_artist(ellipse3)

plt.show()