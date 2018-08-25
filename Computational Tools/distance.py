# Distance formula script, brought to you by PharaohCola13

import numpy as np

X1 = float(input("What is the first x value?\n>> "))
Y1 = float(input("What is the first y value?\n>> "))
Z1 = float(input("What is the first z value?\n>> "))

X2 = float(input("What is the second x value?\n>> "))
Y2 = float(input("What is the second y value?\n>> "))
Z2 = float(input("What is the second z value?\n>> "))

s = round(np.sqrt((X2-X1)**2 + (Y2-Y1)**2 + (Z2-Z1)**2),5)

print(s)