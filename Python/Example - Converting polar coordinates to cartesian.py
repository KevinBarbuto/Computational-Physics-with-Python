# Objective: Write a program that can convert polar coordinates into cartesian.

from math import sin,cos,pi # import functions from math library

print("Enter the polar coordinates for the point.")
r = float(input("Enter the radial coordinate: "))
d = float(input("Enter the angular coordinate, in degrees: "))

theta = d * (pi/180) # convert from degrees into radians

x = r*cos(theta) # convert into cartesian coordinates
y = r*sin(theta)

print("Cartesian coordinates: x =", x, " y =", y)
