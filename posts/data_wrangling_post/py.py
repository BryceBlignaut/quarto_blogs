import numpy as np

# creating an array with 5 evenly spaced numbers between 0 and 1
arr1 = np.linspace(0, 1, 5)
print(arr1)

# creating an array with 10 evenly spaced numbers between 1 and 10
arr2 = np.linspace(1, 10,10)
print(arr2)

# functions and expressions can be apply across the entire array
# in this example we added 5 to each value in the array
print(arr2 +5)