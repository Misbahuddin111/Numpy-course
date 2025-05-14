# sort array
import numpy as np
arr = np.random.randint(1,100,17)
print(np.sort(arr))

# 2D array sort 
b = np.random.randint(1,100,24).reshape(6,4)
print(b)
print(np.sort(b))
print(np.sort(b,axis=0)) # 0 => coloumns 1=> row


# append in 1D array
print(np.append(arr,55))

# 2d array append
print(np.append(b,np.ones((b.shape[0],1)),axis=1))

# concatenate
# code
c = np.arange(6).reshape(2,3)
d = np.arange(6,12).reshape(2,3)

print(c)
print(d)
print(np.concatenate((c,d),axis=1))

# unique
# With the help of np.unique() method,
#  we can get the unique values from an array given as parameter in np.unique() method.
e = np.array([1,1,2,2,3,3,4,4,5,5,6,6])
print(np.unique(e))

#np.expand_dims
 # With the help of Numpy.expand_dims() method, we can get the expanded dimensions of an array

arr = np.arange(25)
print(arr)
print(arr.shape)
print(np.expand_dims(arr,axis=1).shape)

#np.where
#The numpy.where() function returns the indices of elements in an input array where the given condition is satisfied.
print(np.where(arr>19))
print(np.where(arr% 2==0))
# np.where(conditions, true,false)
print(np.where(arr>6,0,arr))
print(np.where(arr%2 == 0,0,arr))

#np.argmax
#The numpy.argmax() function returns indices of the max element of the array in a particular axis.
print(np.argmax(arr))

