# Distance formula script, brought to you by PharaohCola13

import numpy as np

option = int(input("(0) Distance between two points. (1) Use a distance to find another point in 2D.\n>> "))

if option == 0:
    X1  = float(input("What is the value of x for the first point?\n>> "))
    Y1  = float(input("What is the value of y for the first point?\n>> "))
    Z1  = float(input("What is the value of z for the first point?\n>> "))

    X2  = float(input("What is the value of x for the second point?\n>> "))
    Y2  = float(input("What is the value of y for the second point?\n>> "))
    Z2  = float(input("What is the value of z for the second point?\n>> "))

    s   = round(np.sqrt((X2-X1)**2 + (Y2-Y1)**2 + (Z2-Z1)**2),5)

    print("The distance between ({0}, {1}, {2}) and ({3}, {4}, {5}) is {6} units" .format(X1,Y1,Z1,X2,Y2,Z2,s))

elif option == 1:
    X1  = float(input("What is the value of x for the first point?\n>> "))
    Y1  = float(input("What is the value of y for the first point?\n>> "))

    s   = float(input("What is the horizontal distance necessary?\n>> "))

    X2 = X1 + s
    Y2 = Y1

    print("The new point is ({0},{1}).".format(X2,Y2))

# y-y1 = m(x-x1); m=0, dy=0