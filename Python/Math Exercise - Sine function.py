# Objective: Plot a simple graph of the sin(x) function.

from matplotlib.pyplot import plot,show
from numpy import linspace,sin

x = linspace(0,10,100)
y = sin(x)
plot(x,y)
show()
