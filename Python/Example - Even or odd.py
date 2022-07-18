# Objective: Take an integer input and determine whether it is odd or even.

n = int(input("Enter an integer: "))

if n%2 == 0:
    print("\nThe number is even.")
else:
    print("\nThe number is odd.")

print("\nNow, enter one odd integer and one even, in either order.")

a = int(input("First integer: "))
b = int(input("Second integer: "))

while (a+b)%2 == 0:
    print("Now now, don't be silly. One even, one odd. Try again sweetie.")
    
    a = int(input("\nFirst integer: "))
    b = int(input("Second integer: "))

print("\nGood job. Your numbers were", a, "and", b,".")
