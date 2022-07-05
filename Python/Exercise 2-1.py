# Objective: Write a program that will calculate the time required
# for a ball to hit the ground when dropped from a tower of variable height.

g = 9.81 # m/s^2; acceleration due to gravity
h = float(input("Enter the height of the tower: ")) # m; height of the tower
t = (2*h/g)**(1/2)
print(t)
