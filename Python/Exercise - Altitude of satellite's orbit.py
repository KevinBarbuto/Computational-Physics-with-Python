# Objective: Write a program that takes a user input for the period of
# a satellite's orbit, and then outputs the necessary altitude of the
# satellite. The satellite's name is "Thrash".

G = 6.67e-11 # Newton's gravitational constant
M = 5.97e24 # mass of the earth
R = 6371e3 # radius of the earth
pi = 3.1415926535 # pi, rounded

T = float(input("Enter the period of the satellite's orbit, in seconds: "))
h = G*M*T**2 / 4*pi**2 - R # satellite's altitude

print("The satellite must be ", h, "meters from the earth's surface.")
