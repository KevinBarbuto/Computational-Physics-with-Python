# Takes the average of a set of values. This file requires the use of an
# additional file, "values.txt", which consists of a list of numerical values.

from numpy import loadtxt

values = loadtxt("values.txt", float)
mean = sum(values) / len(values)
print(mean)
