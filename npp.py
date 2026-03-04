import numpy as np
# Slicing
arr = np.array([10, 20, 30, 40, 50])
print("First:", arr[0])
print("Last:", arr[-1])
print("Slice [1:3]:", arr[1:3])

#reshape
arr = np.arange(12)
print("Original:", arr)
matrix = arr.reshape(3, 4)
print("Reshaped to 3x4:\n", matrix)
print("Flattened:", matrix.flatten())

#filtering
scores = np.array([45, 78, 23, 90, 56, 88, 34, 67])
print("All scores:", scores)
print("Scores above 60:", scores[scores > 60])
print("Count above 60:", np.sum(scores > 60))
