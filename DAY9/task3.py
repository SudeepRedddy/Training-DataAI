import numpy as np

arr = np.arange(1, 25).reshape(2, 3, 4)

print("\nElements greater than 10:", arr[arr > 10])
print("Count of even numbers:", np.sum(arr % 2 == 0))
arr[arr < 10] = 0
print("Array after replacing values < 10 with 0:\n", arr)