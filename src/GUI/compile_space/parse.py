import mpl_toolkits.mplot3d.axes3d as p3
import matplotlib.pyplot as plt
from matplotlib import *
from fractions import *

from numpy import *
from mpl_toolkits.mplot3d.art3d import *
from matplotlib.animation import *

import argparse
import sys

parser = argparse.ArgumentParser()
parser.add_argument("-Y", "--run", help="Runs program", action="store_true")
parser.add_argument("-c", "--color", help="Defines Color", action="store")
parser.add_argument("-a", "--alpha", help="Defines Transparency", action="store", type=float)
parser.add_argument("-r", "--rotate", help="Rotates Figure", action="store_true")
parser.add_argument("-s", "--save", help="Saves Figure as mp4", action="store_true")

args = parser.parse_args(args=None if sys.argv[1:] else ['--help'])

print(args)