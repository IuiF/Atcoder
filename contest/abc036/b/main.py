import numpy as np


n = int(input())
a = [list(input()) for _ in range(n)]
a = np.array(a)
a = np.rot90(a, k=3)

for i in a:
    print(*i, sep="")
