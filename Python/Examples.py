# Various NumPy array arithmetic tests

from numpy import array

a = array([1,2,3,4],int)
b = array([2,4,6,8],int)

print(b/a +1) # [2, 2, 2, 2] + 1
print(b / (a+1)) # [1, 4/3, 3/2, 8/5]
print(1/a) # [1, 0.5, 0.3333, 0.25 ]
