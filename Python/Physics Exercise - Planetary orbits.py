# Objective: Calculate various properties of an elliptical (solar) orbit, given
# the speed and distance from the sun at the orbit's parihelion.

from math import sqrt,pi

M = 1.9891e30 # Mass of the sun, in kg
G = 6.6738e-11 # Newton's gravitational constant, in m^3 kg^-1 s^-2

l1 = float(input("Enter the shortest distance to the sun (m): "))
v1 = float(input("Enter the planet's speed at that distance (m/s): "))

# Find v2 as the smaller root of a quadratic equation comprised of a,b,c

a = 1
b = -2*G*M/(v1*l1)
c = -v1**2 + 2*G*M/l1

root1 = (-b + sqrt(b**2 - 4*a*c)) / (2*a) # Find quadratic roots
root2 = (-b - sqrt(b**2 - 4*a*c)) / (2*a)
v2 = min(root1,root2) # v2 is the smaller of the two roots

print("\nThe velocity at the aphelion is: {:.4e} m/s".format(v2))

# Find l2, the furthest distance from the sun

l2 = l1*v1/v2

print("The farthest distance from the sun is: {:.4e} m".format(l2))

# Find the orbital period

SemMajA = 0.5 * (l1 + l2) # Semi-major axis
SemMinA = sqrt(l1 * l2) # Semi-major axis

T = 2*pi*SemMajA*SemMinA / (l1 * v1)

print("The orbital period is: {:.4e} s".format(T))

# Find the orbital eccentricity

e = (l2 - l1) / (l2 + l1)

print("The orbital eccentricity is: {:.4e}".format(e))
