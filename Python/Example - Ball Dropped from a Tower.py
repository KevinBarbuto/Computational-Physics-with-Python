# Example problem taken from a physics-based programming class I took years ago.

# OBJECTIVE: Write a program that gives the height of a ball from the ground
# that has been dropped from a tower of variable height, after a variable
# period of time. Air resistance is not considered.

g = 9.81 # m/s^2; acceleration due to gravity
h = float(input("Enter the height of the tower: "))
t = float(input("Enter the time interval: "))
s = 0.5*g*t**2 # kinematics formula for the ball's travel distance
print("The current height of the ball is ", h-s, "meters.")

# Negative answers indicate that the ball would have hit the ground
# prior to the time interval entered by the user.

# Possible ideas for future alterations / expansions of the program:
# - Find the exact point in time that the ball would hit the ground, based
#   on the tower height entered by the user. Maybe even take it a step
#   further and make the program return an error if the user enters a time
#   interval that would continue after the ball hits the ground.
