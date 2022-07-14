# Objective: Find the transmission and reflection probabilities for a particle
# reaching a quantum potential step.

from math import sqrt

# Constants and parameters
m = float(input("Enter the particle's mass in kg: "))
E = float(input("Enter the particle's energy in eV: "))
V = float(input("Enter the energy of the potential step in eV: "))
hbar = 6.582e-16 # Reduced Planck constant in eV*s

# Wavevectors
k1 = sqrt(2*m*E)/hbar
k2 = sqrt( 2*m*(E-V) )/hbar

# Probabilities
T = 4*k1*k2 / (k1+k2)**2 # Find transmission probability
R = ( (k1-k2) / (k1+k2) )**2 # Find reflection probability

print("\nThe transmission probability is {:.5f}".format(T))
print("\nThe reflection probability is {:.5f}".format(R))

# Note: Work can be checked by adding T and R together; this should equal 1.

total = T + R
print("\nThe total probability is {:.5f}".format(total))
