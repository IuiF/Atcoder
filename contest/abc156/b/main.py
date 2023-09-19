import numpy as np

n, k = map(int, input().split())
print(len(np.base_repr(n, k)))
