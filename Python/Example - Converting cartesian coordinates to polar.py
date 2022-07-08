# Objective: Take any set of cartesian coordinates and convert it into
# polar coordinates.

from math import sqrt,atan2,pi,degrees

x = float(input("Enter the x coordinate: "))
y = float(input("Enter the y coordinate: "))

r = sqrt(x**2 + y**2) # Find the radial coordinate
rad = atan2(y, x) # Find the angular coordinate, in radians.
deg = rad * (180/pi) # Convert radians into degrees

print("Cartesian coordinates: r =", r, ", θ =", deg)

# Note: The atan2 function is necessary for finding θ, because the
# normal atan(y/x) can't distinguish between -y/x and y/-x, which is
# essential for determining the correct angle.
