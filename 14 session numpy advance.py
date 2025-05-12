# numpy vs python list
# speed of both

# advance indexing
# fency indexing
import numpy as np
a = np.arange(24).reshape(6,4)
print(a)
print(a[[0,2,3,]]) # for rows 
print(a[:,[0,2,3]]) # for columns 

# boolean indexing 
aa = np.random.randint(1,100,18).reshape(3,6)
print(aa)
print(aa[aa>50])
print(aa[aa % 2 == 0])


arr1 = np.array([[1, 2, 3], [4, 5, 6]])  # Shape: (2, 3)
arr2 = np.array([10, 20, 30])            # Shape: (3,)
result = arr1 + arr2                     # arr2 is broadcast to (2, 3)
print(result)
# Output:
# [[11 22 33]
#  [14 25 36]]

""" Explanation:

arr1 shape: (2, 3)
arr2 shape: (3,) (padded to (1, 3) and stretched to (2, 3))
Result shape: (2, 3)
arr2 is repeated for each row of arr1: [10, 20, 30] is added to both rows """

