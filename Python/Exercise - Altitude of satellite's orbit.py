# Objective: Write a program that takes a user input for the period of
# a satellite's orbit, and then outputs the necessary altitude of the
# satellite. The satellite's name is "Thrash".

G = 6.67e-11 # Newton's gravitational constant
M = 5.97e24 # mass of the earth
R = 6371e3 # radius of the earth
pi = 3.1415926535 # pi, rounded

T = float(input("Enter the period of the satellite's orbit, in seconds: "))
h = (G*M*T**2 / (4*pi**2) )**(1/3) - R # satellite's altitude

print("The satellite must be ", h, "meters from the earth's surface.")

# The derivation for the formula used can be seen in "satellite altitude derivation.jpg".

# If the program returns a negative output (i.e. in the case of a 45-minute
# orbit), then this implies that Thrash would have to be below the earth's
# surface. Therefore, the orbit is impossible.

# For a satellite orbiting the earth once a day (24 hour period), the required
# altitude is about 35855910.18 meters. For a sidereal day's orbit
# (23.93 hours), the necessary altitude is about 35773762.33 meters.
# That's a difference of about 82147.85 meters.
