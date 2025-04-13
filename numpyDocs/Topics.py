"""
1. Basics of NumPy
    - What is NumPy?
    - Why Use NumPy?
    - Installation: pip install numpy
    - Importing NumPy: import numpy as np
    
2. NumPy Arrays
    - Array Creation: np.array(), np.zeros(), np.ones(), np.arange(), np.linspace()
    - Shape & Reshaping: .shape, .reshape(), .ravel(), .flatten()
    - Data Types: dtype, astype()
    - Indexing & Slicing: array[start:stop:step], fancy indexing, boolean masking

3. Mathematical Operations
    - Basic Arithmetic: +, -, *, /, **, %
    - Broadcasting: Element-wise operations on different-sized arrays
    - Aggregations: np.sum(), np.mean(), np.std(), np.min(), np.max(), np.argmin(), np.argmax()
    - Element-wise functions: np.exp(), np.log(), np.sqrt(), np.abs(), np.sin(), np.cos(), np.tan()

4. Linear Algebra
    - Matrix Multiplication: np.dot(), @ operator
    - Transpose: array.T
    - Determinant: np.linalg.det()
    - Inverse: np.linalg.inv()
    - Eigenvalues & Eigenvectors: np.linalg.eig()
    - Singular Value Decomposition (SVD): np.linalg.svd()

5. Random Module
    - Random Numbers: np.random.rand(), np.random.randn(), np.random.randint()
    - Shuffling & Permutations: np.random.shuffle(), np.random.permutation()
    - Seeding: np.random.seed() (for reproducibility)

6. Statistical Functions
    - Descriptive Statistics: np.mean(), np.median(), np.var(), np.std()
    - Percentile & Quantiles: np.percentile(), np.quantile()
    - Correlation & Covariance: np.corrcoef(), np.cov()

7. Broadcasting & Vectorization
    - Efficient computation using broadcasting instead of loops
    - Vectorized operations using ufuncs

8. Performance Optimization
    - Using np.vectorize() for fast operations
    - Memory-efficient arrays: np.float32, np.int16
    - Avoiding Python loops using NumPy vectorization

9. Working with Files
    - Reading & Writing: np.loadtxt(), np.savetxt(), np.genfromtxt(), np.save(), np.load()

10. Integration with AI Libraries
    - Converting NumPy arrays to TensorFlow/PyTorch tensors
    - Efficient data manipulation for machine learning models

-np.where
"""
