import numpy as np

# Key Concept: Sorting arrays in ascending order
# Sort 1D array: np.sort() arranges elements of a 1D array in ascending order
arr1 = np.random.randint(1, 100, 17)
print("Original 1D array:", arr1)
print("Sorted 1D array:", np.sort(arr1))

# Key Concept: Sorting 2D arrays along rows or columns
# Sort 2D array: np.sort() sorts rows (axis=1) or columns (axis=0) of a 2D array
b = np.random.randint(1, 100, 24).reshape(6, 4)
print("\nOriginal 2D array:\n", b)
print("Sorted 2D array (by rows):\n", np.sort(b))  # Default axis=1
print("Sorted 2D array (by columns):\n", np.sort(b, axis=0))

# Key Concept: Appending elements to arrays
# Append: np.append() adds elements to 1D or 2D arrays, ensuring shape compatibility
print("\n1D array after appending 55:", np.append(arr1, 55))  # Add single value
print("2D array after appending column of ones:\n", np.append(b, np.ones((b.shape[0], 1)), axis=1))  # Add column

# Key Concept: Concatenating arrays
# Concatenate: np.concatenate() combines arrays along a specified axis (e.g., horizontal)
c = np.arange(6).reshape(2, 3)
d = np.arange(6, 12).reshape(2, 3)
print("\nArray c:\n", c)
print("Array d:\n", d)
print("Concatenated array (axis=1):\n", np.concatenate((c, d), axis=1))  # Horizontal stacking

# Key Concept: Extracting unique elements
# Unique: np.unique() returns sorted unique elements, removing duplicates
e = np.array([1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6])
print("\nArray with duplicates:", e)
print("Unique values:", np.unique(e))

# Key Concept: Expanding array dimensions
# Expand dims: np.expand_dims() adds a new axis, changing array shape (e.g., 1D to 2D)
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

# Key Concept: Finding indices of max/min values
# Argmax/Argmin: np.argmax() and np.argmin() return indices of max and min values
print("\nIndex of maximum value:", np.argmax(arr))
print(f"Index of minimum value: {np.argmin(arr)}")

# Key Concept: Cumulative sum of elements
# Cumsum: np.cumsum() computes cumulative sum along a specified axis
print("\nOriginal 2D array:\n", b)
print(f"Cumulative sum along columns (axis=0):\n", np.cumsum(b, axis=0))

# Key Concept: Cumulative product of elements
# Cumprod: np.cumprod() computes cumulative product of array elements
print(f"\nCumulative product of 1D array:", np.cumprod(arr))

# Key Concept: Calculating percentiles
# Percentile: np.percentile() computes the nth percentile (e.g., median at 50%)
print("\nOriginal array:", arr)
print(f"50th percentile (median): {np.percentile(arr, 50)}")

# Key Concept: Frequency distribution in bins
# Histogram: np.histogram() counts frequencies of data in specified bins
print("\nOriginal 1D array:", arr1)
print(f"Histogram (bins [0,50,100]):", np.histogram(arr1, bins=[0, 50, 100]))

# Key Concept: Checking element presence
# Isin: np.isin() checks if array elements are in a given list, returning a mask
print("\nOriginal 1D array:", arr1)
item = [12, 34, 5, 36, 66, 89, 32]
print(f"Elements of arr1 in item list:", arr1[np.isin(arr1, item)])

# Key Concept: Reversing array elements
# Flip: np.flip() reverses element order along specified or all axes
print("\nOriginal 1D array:", arr1)
print(f"Flipped 1D array:", np.flip(arr1))
print("Original 2D array:\n", b)
print(f"Flipped 2D array (all axes):\n", np.flip(b))

# Key Concept: Modifying specific indices
# Put: np.put() replaces values at specified indices (in-place modification)
print("\nOriginal array:", arr)
np.put(arr, [0, 1], [110, 530])  # Replace indices 0 and 1
print("Array after np.put:", arr)

# Key Concept: Deleting elements
# Delete: np.delete() removes elements at specified indices, returning new array
print("\nOriginal array:", arr)
print(f"Array after deleting indices [0,3,4,5,1]:", np.delete(arr, [0, 3, 4, 5, 1]))

# Key Concept: Set operations on arrays
# Set operations: Perform union, intersection, difference, XOR, and membership tests
m = np.array([1, 2, 3, 4, 5])
n = np.array([3, 4, 5, 6, 7])
print(f"\nUnion of m and n:", np.union1d(m, n))  # Unique elements from both
print(f"Intersection of m and n:", np.intersect1d(m, n))  # Common elements
print(f"Set difference (m - n):", np.setdiff1d(m, n))  # Elements in m, not n
print(f"Set XOR of m and n:", np.setxor1d(m, n))  # Elements in one, not both
print(f"Elements of m equal to 2:", m[np.in1d(m, 2)])  # Check if 2 is in m