
import numpy as np

# Advantages of Numpy
# 1 Allows several Mathematical Operation
# 2 Faster operations

# Numpy
# Contains multidimensional array data strucutres
# Contains a large library of functions that operate efficiently on these data structures

a = np.array([[1,2,3],
             [4,5,6]])
print(a.shape)


# Why use Numpy?
# Contains multidimensional array data structure
# Improve speed, reduce memory consumption, and offer a high level syntax for performing a variety of common processing task

# Restrictions
# 1. All elements of the array must be of the same type of data.
# 2. Once created, the total size of the array can't change.
# 3. The shape must be rectangualr

# Initialization
a = np.array([1,2,3,4,5,6])
print(a)
# Access elements of an array
print(a[0])

#Array is mutable
a[0] = 10
print(a)

# Slice notation can be used for indexing
print(a[:3])


# Higher dimensional array

a = np.array([[1,2,3], [4,5,6], [7,8,9]])
print(a)
print(a.shape)

# In numpy, a dimension of an array is sometimes referred to as an "axis".

print(a[1,2])

# Array attributes

# n dim
print(a.ndim)

# shape
print(a.shape)

print(len(a.shape))

# size
print(a.size)

# Array are typically homogeneous
print(a.dtype)

# Create a basic array

print(np.zeros(2))
print(np.ones(2))
print(np.empty(2))

print(np.arange(4))
print(np.arange(2,9,2))

print(np.linspace(0, 10, num = 5))

# Specifying your data type
x = np.ones(2, dtype=np.int64)
print(x)
print(type(x))

# Adding, removing and sorting elements

arr = np.array([2, 1, 5, 3, 7, 4, 6, 8])
print(np.sort(arr))

a = np.array([1, 2, 3, 4])
b = np.array([5, 6, 7, 8])

np.concatenate((a, b))


# Shape and Size of an array

array_example = np.array([[[0, 1, 2, 3],
                           [4, 5, 6, 7]],

                          [[0, 1, 2, 3],
                           [4, 5, 6, 7]],

                          [[0 ,1 ,2, 3],
                           [4, 5, 6, 7]]])

# To find the number of dimensions of the array
print(array_example.ndim)

# To find the total numbers of elements in the array
print(array_example.size)

# To find the shape of the array
print(array_example.shape)


# Re-shapping of an array
a = np.arange(6)
print(a)

b = a.reshape(3, 2)
print(b)

# Conversion of 1D array into a 2D array

a = np.array([1, 2, 3, 4, 5, 6])
print(a.shape)
a2 = a[np.newaxis, :]
print(a2.shape)

b = np.expand_dims(a, axis = 1)
print(b.shape)


# Indexing and Slicing
data = np.array([1, 2, 3])
print(data[1])
print(data[0:2])

# Create and array from existing data

a = np.arange(10)
print(a)

arr1 = a[3:8]
print(arr1)

a1 = np.array([[1, 1], [2, 2]])
a2 = np.array([[3, 3], [4, 4]])

print(np.vstack((a1, a2)))


print(np.hstack((a1, a2)))

x = np.arange(1, 25).reshape(2, 12)
print(x)

print(np.hsplit(x, 3))

a = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
b1 = a[0, :]
print(b1)

b1[0] = 99
print(b1)
print(a)

b2= a.copy()

# Basic array operation

data = np.array([1, 2])
ones = np.ones(2, dtype=np.int_)
print(data + ones)

a = np.array([1, 2, 3, 4])
print(a.sum())

# Broadcasting
data = np.array([1.0, 2.0])
print(data * 1.6)

# More useful array operations
a = np.array([[0.45053314, 0.17296777, 0.34376245, 0.5510652],
              [0.54627315, 0.05093587, 0.40067661, 0.55645993],
              [0.12697628, 0.82485143, 0.26590556, 0.56917101]])

print(a.sum())
print(a.min())
print(a.min(axis = 0))

# Creating Matrices
data = np.array([[1, 2], [3, 4], [5, 6]])
print(data)

# Generating random numbers
print(np.random.random(3))


# Transposing and reshpaing a matrix

arr = np.arange(6).reshape((2, 3))
print(arr)
print(arr.transpose())


# Reverse an array
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])
reversed_arr = np.flip(arr)
print('Reversed Array: ', reversed_arr)

# Reversing a 2D array

arr_2d = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
reversed_arr = np.flip(arr_2d)
print(reversed_arr)


# Reshapping and Flattening Multidimensional array

x = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
print(x.flatten())

a1 = x.flatten()
a1[0] = 99
print(x)  # Original array
print(a1)  # New array

a2 = x.ravel()
a2[0] = 98
print(x)  # Original array
print(a2)  # New array

# Working with mathematical formula
# Mean square error
# error = (1/n) * np.sum(np.square(predictions - labels))

# Save and Load NumPy objects

a = np.array([1, 2, 3, 4, 5, 6])

np.save('filename', a)
b = np.load('filename.npy')
print(b)

csv_arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])

np.savetxt('new_file_csv', csv_arr)

print(np.loadtxt('new_file_csv'))

# Importing and exporting a CSV
import pandas as pd


a = np.array([[-2.58289208,  0.43014843, -1.24082018, 1.59572603],
              [ 0.99027828, 1.17150989,  0.94125714, -0.14692469],
              [ 0.76989341,  0.81299683, -0.95068423, 0.11769564],
              [ 0.20484034,  0.34784527,  1.96979195, 0.51992837]])

df = pd.DataFrame(a)
print(df)

df.to_csv('pd.csv')

data = pd.read_csv('pd.csv')


# Plotting Arrays with Matplotlib

a = np.array([2, 1, 5, 7, 4, 6, 8, 14, 10, 9, 18, 20, 22])

import matplotlib.pyplot as plt

plt.plot(a)
plt.show()

x = np.linspace(0, 5, 20)
y = np.linspace(0, 10, 20)
plt.plot(x, y, 'purple')
plt.plot(x, y, 'o')
plt.show()

fig = plt.figure()
ax = fig.add_subplot(projection='3d')
X = np.arange(-5, 5, 0.15)
Y = np.arange(-5, 5, 0.15)
X, Y = np.meshgrid(X, Y)
R = np.sqrt(X**2 + Y**2)
Z = np.sin(R)

ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap='viridis')
plt.show()

