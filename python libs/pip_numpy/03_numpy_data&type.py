import numpy as np

arr = np.array([1,2,3,4,5] , dtype = 'i4')
print(arr)
print(arr.dtype)


#change data type
arr2 = np.array([1.2,3.4,5.6])
newarr = arr2.astype('i')
print(newarr)
print(newarr.dtype)

#change into boolean
arrr = np.array([1 ,2 , 0])
newarr2 = arrr.astype(bool)
print(newarr2)
print(newarr2.dtype)