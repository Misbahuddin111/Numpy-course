# sort array
import numpy as np
arr1 = np.random.randint(1,100,17)
print(np.sort(arr1))

# 2D array sort 
b = np.random.randint(1,100,24).reshape(6,4)
print(b)
print(np.sort(b))
print(np.sort(b,axis=0)) # 0 => coloumns 1=> row


# append in 1D array
print(np.append(arr1,55))

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

arr = np.arange(1,25)
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


# np.argmin
print(f"argmin value: {np.argmin(arr)}")

#np.cumsum
#numpy.cumsum() function is used when we want to compute the cumulative sum of array elements over a given axis.
print(b)
print(f"cumsum value : {np.cumsum(b, axis=0)}")

## np.cumprod
print(f"cumprod : {np.cumprod(arr)}")

#np.percentile
#numpy.percentile()function used to compute the nth percentile of the given data (array elements) along the specified axis.
print(arr)
print(f"persentile value : {np.percentile(arr,50)}")

#np.histogram
# Numpy has a built-in numpy.histogram() function which represents the frequency of data distribution in the graphical form.
print(arr1)
print(f"histogram value : {np.histogram(arr1,bins=[0,50,100])}")

