import numpy as np

H, W = map(int, input().split())
A = list(list(input()) for _ in range(H))
B = list(list(input()) for _ in range(H))
A_arr = np.array(A)
B_arr = np.array(B)

for _ in range(H):
    A_arr = np.roll(A_arr, 1, axis=0)
    for _ in range(W):
        if np.array_equal(A_arr, B_arr):
            print("Yes")
            exit()
        A_arr = np.roll(A_arr, 1, axis=1)

print("No")
