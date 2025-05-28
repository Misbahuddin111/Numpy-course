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