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

# np.isin
#With the help of numpy.isin() method, we can see that one array having values are checked 
# in a different numpy array having different elements with different sizes.
print(arr1)
item = [12,34,5,36,66,89,32]
print(f"isin values : {arr1[np.isin(arr1,item)]}")

#np.flip
#The numpy.flip() 
#function reverses the order of array elements along the specified axis, preserving the shape of the array.

print(arr1)
print(f"flip value : {np.flip(arr1)}")
print(b)
print(f"flip in 2D : {np.flip(b)}")

print(arr)
print(f"put value : {np.put(arr,[0,1],[110,530])}")
print(arr)

# np.delete
# The numpy.delete() function returns a new array with the deletion of sub-arrays along with the mentioned axis.
print(arr)
print(f"delete function : {np.delete(arr,[0,3,4,5,1])}")

'''
Set functions
np.union1d
np.intersect1d
np.setdiff1d
np.setxor1d
np.in1d
'''
m = np.array([1,2,3,4,5])
n = np.array([3,4,5,6,7])

print(f"union : {np.union1d(m,n)}")
print(f"intersection : {np.intersect1d(m,n)}")
print(f"setdifference : {np.setdiff1d(m,n)}")
print(f"setxor1d : {np.setxor1d(m,n)}")
print(f"in1d : {m[np.in1d(m,2)]} ")