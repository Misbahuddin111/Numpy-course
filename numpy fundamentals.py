import numpy as np
# 1D array
list1 = [1,2,3,4]
array1 = np.array(list1)
print(array1)
# 2D array
list2 = [[3,4,5,6,],[4,6,8,1]]
array2 = np.array(list2)
print(array2)
# arange type
range2 = np.arange(1,10)
print(range2)

# reshape type  reshpe create rows and coloumns 
print(range2.reshape(3,3))

# np.ones(), np.zeros() and np.random()

one = np.ones((3,3))
print(one)

zero = np.zeros((4,3))
print(zero)

random1 = np.random.random((3,2))
print(random1)

# linespace ()
print(np.linspace(1,10,4))

# identity
print(np.identity(4))

# arrays attributes 

import numpy as np

# Example 1: 1D Array
# Creating a 1D array with integers
arr1 = np.array([10, 20, 30, 40])

print("1D Array Example:")
print("Array:", arr1)
# ndim: Returns the number of dimensions (axes) of the array
print("ndim:", arr1.ndim, "# Number of dimensions")
# shape: Returns a tuple showing the size of the array along each dimension
print("shape:", arr1.shape, "# Tuple of dimensions (rows, columns, etc.)")
# size: Returns the total number of elements in the array
print("size:", arr1.size, "# Total number of elements")
# dtype: Returns the data type of the array's elements
print("dtype:", arr1.dtype, "# Data type of elements")
# itemsize: Returns the size (in bytes) of each element
print("itemsize:", arr1.itemsize, "# Size of each element in bytes")

# Example 2: 2D Array
# Creating a 2D array with integers
arr2 = np.array([[1, 2, 3], [4, 5, 6]])

print("\n2D Array Example:")
print("Array:\n", arr2)
# ndim: Shows that this is a 2D array (has rows and columns)
print("ndim:", arr2.ndim, "# Number of dimensions")
# shape: Returns (rows, columns) for a 2D array
print("shape:", arr2.shape, "# Tuple of (rows, columns)")
# size: Total elements = rows * columns
print("size:", arr2.size, "# Total number of elements")
# dtype: Data type of elements (int64 by default, system-dependent)
print("dtype:", arr2.dtype, "# Data type of elements")
# itemsize: Size of each element in bytes (int64 = 8 bytes)
print("itemsize:", arr2.itemsize, "# Size of each element in bytes")

# Example 3: Array with Specific Data Type (float32)
# Creating a 1D array with float32 data type
arr3 = np.array([1.1, 2.2, 3.3], dtype=np.float32)

print("\nFloat32 Array Example:")
print("Array:", arr3)
# ndim: Still a 1D array, regardless of data type
print("ndim:", arr3.ndim, "# Number of dimensions")
# shape: Tuple showing number of elements in the 1D array
print("shape:", arr3.shape, "# Tuple of dimensions")
# size: Total number of elements in the array
print("size:", arr3.size, "# Total number of elements")
# dtype: Explicitly set to float32
print("dtype:", arr3.dtype, "# Data type of elements")
# itemsize: Size of float32 is 4 bytes
print("itemsize:", arr3.itemsize, "# Size of each element in bytes")
