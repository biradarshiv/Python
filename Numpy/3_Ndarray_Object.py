"""
The most important object defined in NumPy is an N-dimensional array type called ndarray.
It describes the collection of items of the same type.
Items in the collection can be accessed using a zero-based index.

numpy.array(object, dtype = None, copy = True, order = None, subok = False, ndmin = 0)

"""

import numpy as np

a = np.array([1,2,3])
print(a)

print("# Specify the minimum number of dimensions")
a = np.array([1, 2, 3,4,5], ndmin = 2)
print(a)
a = np.array([1, 2, 3,4,5], ndmin = 3)
print(a)

a = np.array([1, 2, 3], dtype = complex)
print(a)

print("# EOF")

