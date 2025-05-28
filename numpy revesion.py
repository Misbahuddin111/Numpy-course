import numpy as np
list1 = [1,2,4,5]
print(np.array(list1))
# 2D array
list2 = [[1,2,3],[4,5,6]]
print(np.array(list2))

# arange type
list3 = np.arange(21).reshape(3,7)
print(list3)

# reshape type  reshpe create rows and coloumns 

list3 = np.arange(21).reshape(3,7)
print(list3)
# np.ones(), np.zeros() and np.random()
one = np.ones((3,3))
print(one)
zeros = np.zeros((2,4))
print(zeros)

randoms = np.random.random((2,3))
print(randoms)


# arrays attributes
arr1 = np.array([10, 20, 30, 40])
print(np.ndim(arr1))
print(np.shape(arr1))
print(np.size(arr1))
print(arr1.dtype)
print(arr1.itemsize)

# in 2D arrays

arr2 = np.array([[1, 2, 3], [4, 5, 6]])
print("dimensions", np.ndim(arr2))
print(np.shape(arr2))
print(np.size(arr2))
print(arr2.dtype)
print(arr2.itemsize)

# numpy operatons 
a1 = np.arange(12).reshape(3,4)
a2 = np.arange(12,24).reshape(3,4)
print( a1 * 2)
print(a1)
print(a2)
# print( f"sum , { a1 + a2}")
print(f"multiplications {a1 * a2}")

# numpy functions 
a1 = np.arange(1,16).reshape(3,5)
print(a1)
print(np.max(a1 , axis=1))
print(a1)
print(np.min(a1, axis=1))

# shape in numpy
arraay = np.array([[1,3], [2,4],[5,6],[7,8]])
print(arraay)
print(arraay.shape)

arr = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
print("Array:\n", arr)
print("Shape:", arr.shape)

# numpy tricks 

a = np.random.randint(1,100,24).reshape(6,4)
print(a)
print(np.sort(a,axis=0)) # by default its axis is row (1)

# Key Concept: Concatenating arrays
# Concatenate: np.concatenate() combines arrays along a specified axis (e.g., horizontal)
c = np.arange(6).reshape(2, 3)
d = np.arange(6, 12).reshape(2, 3)
print("\nArray c:\n", c)
print("Array d:\n", d)
print("Concatenated array (axis=1):\n", np.concatenate((c, d), axis=1))  # Horizontal stacking

e = np.array([1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6])
print(np.unique(e))


arr = np.arange(1, 25)
print("\nOriginal array:", arr)
print("Original shape:", arr.shape)
print("Shape after expand_dims:", np.expand_dims(arr, axis=1).shape)  # Add column dimension

# Key Concept: Conditional indexing and replacement
# Where: np.where() finds indices or replaces values based on a condition
print("\nIndices where arr > 19:", np.where(arr > 19))  # Indices of values > 19
print("Indices where arr is even:", np.where(arr % 2 == 0))  # Indices of even numbers
print("Replace arr > 6 with 0:", np.where(arr > 6, 0, arr))  # Replace >6 with 0
print("Replace even numbers with 0:", np.where(arr % 2 == 0, 0, arr))  # Replace evens with 0

print("\nIndex of maximum value:", np.argmax(arr))
print(f"Index of minimum value: {np.argmin(arr)}")