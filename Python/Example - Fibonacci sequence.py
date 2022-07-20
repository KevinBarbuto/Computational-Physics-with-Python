# Objective: Calculate every number in the Fibonacci sequence up to an
# arbitrary ending point (let's say, for all numbers under 1,000).

f1,f2 = 1,1 # Declare starting variables

ceiling = int(input("Enter the maximum value of the Fibonnaci sequence: "))

while f1 <= ceiling:
    print(f1) # Prints the current number in the sequence

    f1,f2 = f2,f1+f2 # Determine next two numbers in the sequence
