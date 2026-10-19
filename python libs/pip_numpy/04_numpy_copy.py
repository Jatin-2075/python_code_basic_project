import numpy as np
arr = np.array([1,2,3,4,5])
x = arr.copy() # this func is copy
arr[0] = 476
print(arr)
print(x)
# this func only woek for x now lets see view func

arr2 = np.array([1, 2, 3, 4, 5])
v = arr2.view()
v[0] = 31

print(arr2)
print(v)