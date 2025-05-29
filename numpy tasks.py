# Question: Create a 3x3 NumPy array filled with random integers between 1 and 10 (inclusive). 
# Ensure the random seed is set to 42 for reproducibility.

#Task: Write code to generate and print this array.

import numpy as np
arr1 = np.arange(1,10).reshape(3,3)
print(arr1)

#3. Array Operations
#Question: Create two 1D NumPy arrays of length 5 with random integers between 1 and 20. 
# Compute the element-wise sum, difference, and product of these arrays.

#Task: Write code to generate the arrays and print the results of the three operations.

arr3 = np.random.randint(1,20,5)
arr2 =np.random.randint(1,20,5)
print(arr1)
print(arr2)
print(arr3 + arr2)
add1 = np.add(arr2 , arr3)
print(add1)
subtract1 = np.subtract(arr3,arr2)
print(subtract1)

#Question: Create two 2x3 and 3x2 matrices with random integers between 1 and 5. 
# Perform matrix multiplication and print the resulting matrix.

#Task: Write code to generate the matrices, perform the multiplication, and display the result.

a1 = np.random.randint(1,6 ,size=(3,2))
a2 = np.random.randint(1,6,size=(2,3))
print(a1,a2)
multiply = np.dot(a1,a2)
print(f"multiply\n: {multiply}")


#5. Array Filtering
#Question: Create a 1D NumPy array of 10 random integers between 1 and 100. 
# Find all elements greater than 50 and replace them with 0.

#Task: Write code to generate the array, apply the condition, and print the modified array

array_fil = np.random.randint(1,100,10)
print(np.where(array_fil>50,0,array_fil))

#6. Array Reshaping
#Question: Create a 1D NumPy array with numbers from 1 to 12. Reshape it into a 3x4 array,
#  then transpose it to a 4x3 array.

#Task: Write code to create, reshape, transpose, and print both arrays.
arra1 = np.arange(12)
print(arra1)
reshape = arra1.reshape(3,4)
print(reshape)
print(reshape.transpose())

#7. Statistical Operations

#Question: Create a 5x5 NumPy array with random floats between 0 and 1.
#  Compute the mean, standard deviation, and sum of each row.

#Task: Write code to generate the array and print the mean, standard deviation, and sum for each row.

float_array = np.random.uniform(0,1,size=(5,5))
print(float_array)
mean = np.mean(float_array)
sum = np.sum(float_array)
std = np.std(float_array)
print(std)
print(mean)
print(sum)