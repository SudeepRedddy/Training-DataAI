import numpy as np

arr = np.arange(1, 25).reshape(2, 3, 4)

print("\nFirst layer:\n", arr[0])
print("Last layer:\n", arr[-1])
print("Element at layer=1, row=2, column=3:", arr[1, 2, 3])
print("First row of all layers:\n", arr[:, 0, :])
print("Last row of all layers:\n", arr[:, -1, :])