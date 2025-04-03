"""
2. NumPy Arrays
    - Array Creation: np.array(), np.zeros(), np.ones(), np.arange(), np.linspace()
    - Shape & Reshaping: .shape, .reshape(), .ravel(), .flatten()
    - Data Types: dtype, astype()
    - Indexing & Slicing: array[start:stop:step], fancy indexing, boolean masking

"""

import numpy as np

#---------------
# Array creation
#---------------

# Create a 1D array

arr1 = np.array([1, 2, 3, 4, 5])

# Access 1D array
print(arr1)

# Indexing

print(arr1[0])  # First element

print(arr1[4])  # Fifth element

# Slicing

print(arr1[1:3])  # Elements from second to third

print(arr1[:3])  # Elements from start to third

print(arr1[3:])  # Elements from third to end

# Create a 2D array

arr2 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# Access 2D array

print(arr2)

# Indexing

print(arr2[0][0])  # First element

print(arr2[2][2])  # Last element

print(arr2[1, :])  # Second row

print(arr2[:, 1])  # Second column

# Slicing

print(arr2[0, 1:3])  # Elements from second to third in the first row

print(arr2[1:, 1:])  # Elements from second to third in the second and third rows

# Create a 3D array

arr3 = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])

# Access 3D array

print(arr3)

print(arr3[0][0][0])  # First element

print(arr3[1][1][2])  # Last element

print(arr3[1, :, 1])  # Second column in the second row

print(arr3[:, 1, 2])  # Third element in the second column in all rows

print(arr3[1, 1, :])  # All elements in the second row and second column

# Slicing

print(arr3[0, 1:, 1:])  # Elements from second to third in the first row and second column

print(arr3[1:, 1:, 2:])  # Elements from second to third in the second and third rows and third column

zeros_arr = np.zeros((3, 4)) # 3 rows and 4 columns
print(zeros_arr)

ones_arr = np.ones((2, 3, 4)) # 2 3D arrays, each with 2 rows, 3 columns, and 4 elements

print(ones_arr)

arange_arr = np.arange(10) # 0 to 9

print(arange_arr)

linspace_arr = np.linspace(0, 1, 5) # 5 elements between 0 and 1

print(linspace_arr)

#----------------------
# Reshaping & Reshaping
#----------------------

arr = np.arange(10) 

print(arr)

reshaped_arr = arr.reshape(2, 5) # Reshape to 2 rows and 5 columns

print(reshaped_arr)

