# Objective: Find the time it takes for a spaceship to reach its destination,
# both classically and relativistically.

from math import sqrt

x = float(input("Enter the distance in light years for the ship to travel: "))
v = float(input("Enter the ship's speed, as a fraction of the speed of light: "))

t0 = x/v # Compute the time in classical mechanics

print("\nIn the earth's reference frame, the trip will take {:.2f}".format(t0), "years.")

t = t0 * sqrt(1 - v**2)# Compute time in relativistic mechanics

print("In the ship's reference frame, the trip will take {:.2f}".format(t), "years.")
