import numpy as np

# Creating an original array (base is None)
original_array = np.array([1, 2, 3, 4, 5])
print("Original array base:", original_array.base)  # Output: None

# Creating a view by slicing
view_array = original_array[1:4]
print("View array base:", view_array.base)  # Output: [1 2 3 4 5]

# creating a copy
copy_array = original_array.copy()
print("Copy array base:", copy_array.base) #output: None

# Changing the view affects the original
view_array[0] = 100
print("Original array after view change:", original_array) #output: [  1 100   3   4   5]

print("view array:", view_array) #output: [100   3   4]

print("copy array:", copy_array) #output: [1 2 3 4 5]