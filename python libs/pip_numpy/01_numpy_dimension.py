import numpy as np
arr0 = np.array(98)
arr1 = np.array([1,2,3])#1 dimension
arr2 = np.array([[1,2,3] , [4,5,6]])
arr3 = np.array([[[1,2,3], [4,5,6]] , [[7,8,9] , [12,34,65]]])
arr4 = np.array([1,2,3,4] , ndmin=4)
 #we can define array of n number 
print(arr0 ," dimensions the arrays have", arr0.ndim, "\n")
print(arr1 ," dimensions the arrays have", arr1.ndim, "\n")
print(arr2 ," dimensions the arrays have", arr2.ndim, "\n")
print(arr3 ," dimensions the arrays have", arr3.ndim, "\n")
print(arr4 ," dimensions the arrays have", arr4.ndim, "\n")
