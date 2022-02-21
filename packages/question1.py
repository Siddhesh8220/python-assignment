# 1] Import any 1 python
# built-in package and use 1 module and 3 functions within it.

import pandas as pd
import numpy as np

s = pd.Series(np.random.randn(4))
print(s)
print("\n")

arr = np.array([1, 2, 3, 4, 5])
print(arr)
print("\n")

newarr = np.array_split(arr, 3)
print(newarr)
print("\n")
