# 📌 Project 3: Matrix Operations Tool
import numpy as np

# Example matrices
A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])

print("Matrix A:\n", A)
print("Matrix B:\n", B)

# Addition
print("\nA + B =\n", A + B)

# Subtraction
print("\nA - B =\n", A - B)

# Multiplication
print("\nA x B =\n", np.dot(A, B))

# Transpose
print("\nTranspose of A:\n", A.T)

# Determinant
print("\nDeterminant of A:", np.linalg.det(A))
print("Determinant of B:", np.linalg.det(B))
