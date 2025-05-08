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
