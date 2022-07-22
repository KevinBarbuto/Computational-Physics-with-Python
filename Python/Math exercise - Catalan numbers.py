# Objective: Print the Catalan sequence of numbers, up to a ceiling.

n = 0 # List position
C = 1 # Starting number

ceiling = int(input("Enter the max Catalan number: "))

while C <= ceiling:
    print(int(C))
    C = ( (4*n + 2)/(n + 2) ) * C # Calculates the next number
    n += 1
    
