import numpy as np
import sys 
import time
arr1= np.array([1, 2, 3, 4, 5])
print(arr1)

print(type(arr1))

arr2=np.array([[1,2,3,],[4,5,6,]])
print(arr2)

arr3=np.zeros((2,3))
print(arr3)

arr4=np.ones((2,3))
print(arr4)

print("Identity Matrix:")
arr5=np.identity(3)
print(arr5)

# arange(start, stop, jumpsize)

arr6=np.arange(5,16,2)
print(arr6)


# linspace(start, stop, difference between elements)
arr7=np.linspace(10,20,10)
print(arr7)

arr8=arr7.copy()
print(arr8)


print(arr1.shape)
print(arr2.shape)

arr9=np.array([[[1,2],[3,4]],[[5,6],[7,8]]])
print(arr9)
print(arr9.shape)  #gives the shape of the array
print(arr9.ndim)   #gives the number of dimensions of the array

print(arr1.size)  #gives the total number of elements in the array
print(arr2.size)  
print(arr9.size)

print(arr9.itemsize)  #gives the size of each element in bytes
print(arr8.itemsize)

print(arr8.dtype)  #gives the data type of the array
print(arr9.dtype)
print(arr9.astype(float))  #converts the data type of the array to float




# abhi tk above main ny kiya ha 
# np.array() - creates an array
# np.zeros() - creates an array filled with zeros
# np.ones() - creates an array filled with ones
# np.identity() - creates an identity matrix
# np.arange() - creates an array with a range of values
# np.linspace() - creates an array with evenly spaced values
# np.copy() - creates a copy of the array
# np.shape - gives the shape of the array
# np.ndim - gives the number of dimensions of the array
# np.size - gives the total number of elements in the array
# np.itemsize - gives the size of each element in bytes
# np.dtype - gives the data type of the array
# np.astype() - converts the data type of the array



# Now Python Lists VS Numpy Arrays
# Numpy arrays are more efficient than Python lists for numerical operations.
# Numpy arrays are more memory efficient than Python lists.
# Numpy arrays are more convenient to use for numerical operations than Python lists.

# Python List
lista=range(100)
print(lista)

# Numpy array 
arr11=np.arange(100)

# # Checking Size 
# print(sys.getsizeof(87)*len(lista))  # Size of Python list
# print(arr11.itemsize*arr11.size)  # Size of Numpy array


# # # Time Complexity
# # start=time.time()
# # x=range(10000000)
# # y=range(10000000, 20000000)

# # start1=time.time()
# # c=[(x,y) for x,y in zip(x,y)]
# # end1=time.time()

# # print("Time taken by Python List: ", end1-start1)


# # a=np.arange(10000000)
# # b=np.arange(10000000, 20000000)
# # start2=time.time()
# # c=a+b
# # end2=time.time()
# # print("Time taken by Numpy Array: ", end2-start2)


# now i have done
# numpy arrays and python lists
# numpy arrays are efficient fast and take less memory than python lists


# Now Slicing in Numpy Arrays

arr12=np.arange(24)
print(arr12)

arr13=np.arange(24).reshape(3,8)

print(arr13)

print(arr13[1,3]) 

print(arr13[-1])

# arr[start:end:step]

arr15=np.arange(24).reshape(6,4)
print(arr15)
# for 13,14
# print(arr15[3:5,2:4])

print(arr15[4:5,0:2])

# syntax yeh ha k arr[start(row ):end(row+1),start(column):end(column+1)]


for i in np.nditer(arr15):
    print(i)