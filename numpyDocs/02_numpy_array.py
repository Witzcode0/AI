"""
2. NumPy Arrays
    Array Creation:
    np.array(), np.zeros(), np.ones(), np.arange(), np.linspace()

    Shape & Reshaping:
    .shape, .reshape(), .ravel(), .flatten()

    Data Types:
    dtype, astype()

    Indexing & Slicing:
    array[start:stop:step], fancy indexing, boolean masking

    Boolean Indexing:
    arr > value, arr == value, arr[arr > value]

    np.where():
    np.where(condition, value_if_true, value_if_false)
    ➤ Used to return values or positions based on a condition.

    Fancy Indexing:
    Selecting elements using a list/array of indices
    ➤ Example: arr[[1, 3, 4]]

    np.argwhere():
    Returns the indices where a condition is True
    ➤ Example: np.argwhere(arr > 10)
"""

import numpy as np

# ---------------
# Array Creation:
# ---------------
# np.array() creates a NumPy array from a list or tuple.
arr = np.array([1, 2, 3, 4, 5])

# np.zeros()
# Purpose: Creates a new NumPy array filled with zeros.
# Syntax: np.zeros(shape, dtype=float)
result = np.zeros([3, 2])  # 3x2 array of zeros with default float type
# print(result)

result = np.zeros([3, 2], dtype=int)  # 3x2 array of zeros with int type
# print(result)

# np.ones()
# Purpose: Creates a new NumPy array filled with ones.
# Syntax: np.ones(shape, dtype=float, order='C')
result = np.ones([3, 4], dtype=int)  # 3x4 array of ones with int type
# print(result)

# np.arange()
# Purpose: Creates a NumPy array with evenly spaced values within a given interval using a step size.
# Syntax: np.arange([start,] stop, [step,], dtype=None)
result = np.arange(1, 10, 2)  # Array from 1 to 9 with a step size of 2
# print(result)

result = np.arange(1, 10, 2, dtype=float)  # Same array but with float type
# print(result)

# np.linspace()
# Purpose: Generates a sequence of evenly spaced numbers over a specified interval.
# Syntax: np.linspace(start, stop, num=50, endpoint=True, retstep=False, dtype=None)
result = np.linspace(10, 20, 5)  # 5 equally spaced numbers between 10 and 20
# print(result)

result = np.linspace(10, 20, 5, endpoint=False)  # Same but excluding the endpoint
# print(result)

arr, step = np.linspace(10, 20, 5, endpoint=False, retstep=True)  # Get step size along with array
# print(arr)
# print(step)

# ------------------
# Shape & Reshaping:
# ------------------

# .shape
# Returns the shape (dimensions) of the array as a tuple.
arr = np.array([[1, 2, 3], [4, 5, 6]])  # 2x3 array
# print(arr.shape)

# .reshape(new_shape)
# Changes the shape of an array without changing the data.
result = arr.reshape(3, 2)  # Reshaped to 3x2
# print(result)

arr = np.arange(12)  # 1D array with 12 elements
result = arr.reshape(2, 6)  # Reshape to 2x6
# print(result)

# .ravel()
# Flattens a multi-dimensional array to 1D (returns a view if possible).
reshape_arr = arr.reshape(3, 2, 2)  # 3x2x2 array
ravel_arr = reshape_arr.ravel()  # Flatten it to 1D
# print(ravel_arr)

# .flatten()
# Also flattens a multi-dimensional array to 1D, but returns a copy.
# print(arr.flatten())  # Output: [1 2 3 4]

# ---------------------------
# Data Types: dtype, astype()
# ---------------------------

# .dtype
# Returns the data type of the elements in the array.
arr = np.array(['apple', 10, '10.5'])
# print(arr.dtype)  # Output: <U21 (unicode string)

# .astype()
# Casts the array to a new type and creates a copy with the specified dtype.
arr = np.array([1.1, 2.2, 3.3, 4.4])
arr_int = arr.astype(int)  # Convert to integer
# print(arr_int)

arr = np.array([1, 2, 3, 4])
arr_float = arr.astype(float)  # Convert to float
# print(arr_float)

# --------------------------
# Indexing & Slicing:
# --------------------------

# Indexing: Accessing a single value
# print(arr[0])  # First element
# print(arr[-1])  # Last element

# Slicing: Accessing a subarray
# print(arr[1:3])  # Elements from second to third
# print(arr[:3])  # Elements from start to third
# print(arr[3:])  # Elements from third to end

arr = np.array([[1, 2], [3, 4]])  # 2x2 array

# Accessing elements using indexing and slicing
# print(arr[0])  # First row
# print(arr[0][0])  # First element of first row
# print(arr[1:])  # Second row to the end
# print(arr[:, 1])  # All rows, second column
# print(arr[1:, 1:])  # Second row to end, second column to end

# ---------------------------
# Boolean Indexing:
# ---------------------------

# Boolean indexing allows selecting elements based on a condition.
arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
# print(arr)
# print(arr > 5)  # Condition to check values greater than 5

# Apply boolean mask to filter values greater than 5
# print(arr[arr > 5])  # Output: [6 7 8 9]

# --------------------------
# np.where()
# --------------------------
# np.where() is used to return elements based on a condition.
set_val_arr = np.where(arr > 5, 'High', 'Low')  # Assign 'High' if greater than 5, else 'Low'
# print(set_val_arr)

# Example: Set values based on a condition
set_val_array = np.where(arr > 5, arr, -1)  # Set -1 where condition is False
# print(set_val_array)

# --------------------------
# Fancy Indexing:
# --------------------------

# Fancy indexing allows selecting elements using a list/array of indices.
arr = np.array([1, 2, 3, 4, 5])
index = [1, 3, 4]
# print(arr[index])  # Output: [2 4 5]

# ---------------------------
# np.argwhere()
# ---------------------------
# np.argwhere() returns the indices of elements that satisfy a given condition.
arr = np.array([10, 25, 30, 5])
index = np.argwhere(arr > 20)  # Indices where values are greater than 20
# print(index)  # Output: [[1] [2]]

arr = np.array([[10, 34, 56, 28, 24], [56, 79, 90, 12, 15], [29, 63, 82, 29, 75]])
index = np.argwhere(arr >= 50)  # Indices where values are greater than or equal to 50
# print(index)  # Output: [[0 2] [1 0] [1 1] [1 2] [2 1] [2 2] [2 4]]


