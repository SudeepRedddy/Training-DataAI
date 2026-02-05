import numpy as np

arr = np.arange(1, 25).reshape(2, 3, 4)
print("Array:\n", arr)
print("Shape:", arr.shape)

print("\nFirst layer:\n", arr[0])
print("Last layer:\n", arr[-1])
print("Element at layer=1, row=2, column=3:", arr[1, 2, 3])
print("First row of all layers:\n", arr[:, 0, :])
print("Last row of all layers:\n", arr[:, -1, :])

print("\nElements greater than 10:", arr[arr > 10])
print("Count of even numbers:", np.sum(arr % 2 == 0))
arr[arr < 10] = 0
print("Array after replacing values < 10 with 0:\n", arr)

