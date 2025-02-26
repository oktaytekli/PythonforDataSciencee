import numpy as np

v = np.array([1,2,3,4,5])

## KLASİK DÖNGÜ İLE ##

ab = []
for i in v:
    if i <3:
        print(i)

for i in v:
    if i < 3:
        ab.append(i)

## NUMPY İLE ##
v < 3
print(v[ v < 3])
print(v[ v > 3])
print(v[ v != 3])
print(v[ v == 3])
print(v[ v >= 3])
